"""
Re-engagement audience resolution, one-shot send, and periodic campaign runner.
"""

from __future__ import annotations

from datetime import timedelta

from django.utils import timezone

from ..models import (
    BotSession,
    CampaignDeliveryLog,
    CustomerProfile,
    ReengageCampaign,
    ReengageOffer,
    TelegramBot,
)
from .staff_access import staff_telegram_id_set
from .telegram_client import TelegramService

REENGAGE_BATCH_CAP = 100
INACTIVE_DAYS = 30


def inactive_cutoff(now=None):
    return (now or timezone.now()) - timedelta(days=INACTIVE_DAYS)


def _exclude_staff(user_ids) -> list[int]:
    staff_ids = staff_telegram_id_set()
    seen: set[int] = set()
    out: list[int] = []
    for raw in user_ids:
        try:
            uid = int(raw)
        except (TypeError, ValueError):
            continue
        if uid in seen:
            continue
        if str(uid) in staff_ids:
            continue
        seen.add(uid)
        out.append(uid)
    return out


def resolve_audience_user_ids(bot: TelegramBot, audience: str) -> list[int]:
    sessions = BotSession.objects.filter(bot=bot)
    cutoff = inactive_cutoff()

    if audience == "inactive":
        ids = sessions.filter(last_activity__lt=cutoff).values_list(
            "telegram_user_id", flat=True
        )
        return _exclude_staff(ids)

    tagged_ids = set(
        CustomerProfile.objects.filter(tag=audience).values_list(
            "telegram_user_id", flat=True
        )
    )
    ids = sessions.filter(telegram_user_id__in=tagged_ids).values_list(
        "telegram_user_id", flat=True
    )
    return _exclude_staff(ids)


def send_to_audience(
    bot: TelegramBot,
    audience: str,
    message: str,
    *,
    batch_cap: int = REENGAGE_BATCH_CAP,
) -> dict:
    """Send a one-shot DM batch to an audience. Returns sent/failed/skipped counts."""
    all_ids = resolve_audience_user_ids(bot, audience)
    total_matching = len(all_ids)
    target_user_ids = all_ids[:batch_cap]
    skipped = max(0, total_matching - len(target_user_ids))

    token = bot.get_plain_token()
    if not token:
        return {
            "sent": 0,
            "failed": 0,
            "skipped": skipped,
            "audience": audience,
            "bot_id": bot.id,
            "batch_cap": batch_cap,
            "error": "no_token",
        }

    try:
        client = TelegramService(token)
    except Exception as exc:
        return {
            "sent": 0,
            "failed": 0,
            "skipped": skipped,
            "audience": audience,
            "bot_id": bot.id,
            "batch_cap": batch_cap,
            "error": str(exc),
        }

    sent = 0
    failed = 0
    last_error = ""
    for uid in target_user_ids:
        ok, err, _mid = client.send_message(
            chat_id=uid, text=message, parse_mode=None
        )
        if ok:
            sent += 1
        else:
            failed += 1
            last_error = str(err or "")

    result = {
        "sent": sent,
        "failed": failed,
        "skipped": skipped,
        "audience": audience,
        "bot_id": bot.id,
        "batch_cap": batch_cap,
    }
    if last_error:
        result["last_error"] = last_error
    return result


def schedule_next_run(campaign: ReengageCampaign, *, from_time=None) -> None:
    base = from_time or timezone.now()
    if campaign.schedule == ReengageCampaign.Schedule.DAILY:
        delta = timedelta(days=1)
    elif campaign.schedule == ReengageCampaign.Schedule.WEEKLY:
        delta = timedelta(weeks=1)
    else:
        delta = timedelta(days=30)
    campaign.next_run_at = base + delta
    campaign.save(update_fields=["next_run_at", "updated_at"])


def run_due_campaigns(*, now=None) -> dict:
    """Run all active campaigns whose next_run_at <= now."""
    now = now or timezone.now()
    due = ReengageCampaign.objects.filter(is_active=True, next_run_at__lte=now)
    summary = {"campaigns_run": 0, "total_sent": 0, "total_failed": 0}

    for campaign in due.select_related("bot"):
        result = send_to_audience(
            campaign.bot,
            campaign.audience,
            campaign.message,
        )
        CampaignDeliveryLog.objects.create(
            bot=campaign.bot,
            campaign=campaign,
            sent=result.get("sent", 0),
            failed=result.get("failed", 0),
            skipped=result.get("skipped", 0),
        )
        schedule_next_run(campaign, from_time=now)
        summary["campaigns_run"] += 1
        summary["total_sent"] += result.get("sent", 0)
        summary["total_failed"] += result.get("failed", 0)

    return summary


def send_offer(offer: ReengageOffer) -> dict:
    """Send an offer template to its audience and log delivery."""
    text = f"{offer.title}\n\n{offer.body}"
    result = send_to_audience(offer.bot, offer.audience, text)
    CampaignDeliveryLog.objects.create(
        bot=offer.bot,
        offer=offer,
        sent=result.get("sent", 0),
        failed=result.get("failed", 0),
        skipped=result.get("skipped", 0),
    )
    return result
