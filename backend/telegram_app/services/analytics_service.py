"""
Shared analytics for Telegram admin dashboard (web hub + in-bot admin).

Reads persisted snapshots when available; falls back to live ORM aggregation.
"""

from __future__ import annotations

from collections import Counter
from datetime import date, datetime, timedelta
from typing import Any

from django.db.models import Avg, Count
from django.db.models.functions import ExtractHour, TruncDate
from django.utils import timezone

from finalize.models import Finalization, SpecialPriceFinalization

from ..models import (
    BotCustomerGrowthSnapshot,
    BotDailyUsageSnapshot,
    BotSession,
    ChannelMemberSnapshot,
    CustomerProfile,
    ExchangeRequest,
    PriceAlert,
    ReengageCampaign,
    TelegramBot,
    TelegramChannel,
)
from .customer_tags import display_name, telegram_display_name, telegram_username

INACTIVE_DAYS = 30
DAILY_USAGE_DAYS = 30
EXCHANGE_LIST_LIMIT = 50
ALERT_LIST_LIMIT = 50
EVENT_FEED_LIMIT = 30
MEMBER_PERIOD_MONTHS = {
    1: "Last month",
    3: "Last 3 months",
    9: "Last 9 months",
    12: "Last year",
}


def _session_user_ids(bot: TelegramBot):
    return BotSession.objects.filter(bot=bot).values_list("telegram_user_id", flat=True)


def customers_for_bot(bot: TelegramBot):
    return CustomerProfile.objects.filter(
        telegram_user_id__in=_session_user_ids(bot)
    )


def inactive_cutoff(now=None):
    return (now or timezone.now()) - timedelta(days=INACTIVE_DAYS)


def period_start(months: int, now=None) -> datetime:
    return (now or timezone.now()) - timedelta(days=30 * months)


def backfill_daily_usage(bot: TelegramBot, *, days: int = DAILY_USAGE_DAYS) -> None:
    """Populate BotDailyUsageSnapshot from BotSession for recent days."""
    now = timezone.now()
    since = now - timedelta(days=days)
    sessions = BotSession.objects.filter(bot=bot, last_activity__gte=since)
    rows = (
        sessions.annotate(day=TruncDate("last_activity"))
        .values("day")
        .annotate(users=Count("telegram_user_id", distinct=True))
    )
    for row in rows:
        day = row["day"]
        if not day:
            continue
        BotDailyUsageSnapshot.objects.update_or_create(
            bot=bot,
            date=day,
            defaults={"active_users": row["users"]},
        )


def backfill_customer_growth(bot: TelegramBot, *, days: int = DAILY_USAGE_DAYS) -> None:
    """Populate BotCustomerGrowthSnapshot from BotSession.created_at."""
    now = timezone.now()
    since = now - timedelta(days=days)
    rows = (
        BotSession.objects.filter(bot=bot, created_at__gte=since)
        .annotate(day=TruncDate("created_at"))
        .values("day")
        .annotate(new_users=Count("telegram_user_id", distinct=True))
    )
    for row in rows:
        day = row["day"]
        if not day:
            continue
        BotCustomerGrowthSnapshot.objects.update_or_create(
            bot=bot,
            date=day,
            defaults={"new_customers": row["new_users"]},
        )


def daily_usage_rows(bot: TelegramBot) -> list[dict[str, Any]]:
    now = timezone.now()
    since_date = (now - timedelta(days=DAILY_USAGE_DAYS)).date()
    snaps = BotDailyUsageSnapshot.objects.filter(
        bot=bot, date__gte=since_date
    ).order_by("date")
    if snaps.exists():
        return [
            {"date": s.date.isoformat(), "users": s.active_users} for s in snaps
        ]

    backfill_daily_usage(bot)
    snaps = BotDailyUsageSnapshot.objects.filter(
        bot=bot, date__gte=since_date
    ).order_by("date")
    if snaps.exists():
        return [
            {"date": s.date.isoformat(), "users": s.active_users} for s in snaps
        ]

    daily_since = now - timedelta(days=DAILY_USAGE_DAYS)
    sessions = BotSession.objects.filter(bot=bot)
    daily_rows = (
        sessions.filter(last_activity__gte=daily_since)
        .annotate(day=TruncDate("last_activity"))
        .values("day")
        .annotate(users=Count("telegram_user_id", distinct=True))
        .order_by("day")
    )
    return [
        {"date": row["day"].isoformat() if row["day"] else None, "users": row["users"]}
        for row in daily_rows
    ]


def most_requested_currencies(bot: TelegramBot, *, limit: int = 10) -> list[dict]:
    currency_counter: Counter = Counter()
    for er in ExchangeRequest.objects.filter(bot=bot).values(
        "source_currency", "target_currency"
    ):
        src = er.get("source_currency")
        tgt = er.get("target_currency")
        if src:
            currency_counter[src] += 1
        if tgt:
            currency_counter[tgt] += 1
    return [
        {"currency": code, "count": count}
        for code, count in currency_counter.most_common(limit)
    ]


def exchange_status_counts(bot: TelegramBot, *, now=None) -> dict[str, int]:
    exchanges = ExchangeRequest.objects.filter(bot=bot)
    status_counts = {
        row["status"]: row["c"]
        for row in exchanges.values("status").annotate(c=Count("id"))
    }
    for key in ExchangeRequest.Status.values:
        status_counts.setdefault(key, 0)
    status_counts["_running"] = sum(
        1 for er in exchanges.iterator() if er.is_running(now=now or timezone.now())
    )
    return status_counts


def new_members_dual(bot: TelegramBot, months: int, *, now=None) -> dict[str, Any]:
    """Channel subscriber delta + bot DM user growth for a period."""
    now = now or timezone.now()
    since = period_start(months, now)
    since_date = since.date()

    customers = customers_for_bot(bot)
    bot_dm_new = customers.filter(created_at__gte=since).count()

    growth_snaps = BotCustomerGrowthSnapshot.objects.filter(
        bot=bot, date__gte=since_date
    )
    if growth_snaps.exists():
        bot_dm_new = sum(s.new_customers for s in growth_snaps)
    else:
        bot_dm_from_sessions = (
            BotSession.objects.filter(bot=bot, created_at__gte=since)
            .values("telegram_user_id")
            .distinct()
            .count()
        )
        if bot_dm_from_sessions:
            bot_dm_new = bot_dm_from_sessions

    channel_growth = 0
    channel_details: list[dict] = []
    channels = TelegramChannel.objects.filter(bot=bot, is_active=True)
    for ch in channels:
        if not ch.bot_admin_verified:
            continue
        latest = ch.last_member_count
        if latest is None:
            snap = (
                ChannelMemberSnapshot.objects.filter(channel=ch, bot_is_admin=True)
                .order_by("-sampled_at")
                .first()
            )
            if snap:
                latest = snap.member_count
        if latest is None:
            continue

        start_snap = (
            ChannelMemberSnapshot.objects.filter(
                channel=ch,
                bot_is_admin=True,
                sampled_at__lte=since,
            )
            .order_by("-sampled_at")
            .first()
        )
        start_count = start_snap.member_count if start_snap else latest
        delta = max(0, latest - start_count)
        channel_growth += delta
        channel_details.append(
            {
                "channel_id": ch.id,
                "channel_name": ch.name,
                "current_members": latest,
                "growth": delta,
            }
        )

    return {
        "months": months,
        "label": MEMBER_PERIOD_MONTHS.get(months, f"{months} months"),
        "channel_growth": channel_growth,
        "bot_dm_growth": bot_dm_new,
        "channels": channel_details,
    }


def all_member_windows(bot: TelegramBot) -> dict[str, int]:
    result = {}
    for months in (1, 3, 9, 12):
        dual = new_members_dual(bot, months)
        result[str(months)] = dual["channel_growth"] + dual["bot_dm_growth"]
    return result


def customer_analysis(bot: TelegramBot, *, now=None) -> dict[str, Any]:
    now = now or timezone.now()
    cutoff = inactive_cutoff(now)
    sessions = BotSession.objects.filter(bot=bot)
    exchanges = ExchangeRequest.objects.filter(bot=bot)
    customers = customers_for_bot(bot)

    active_sessions = sessions.filter(last_activity__gte=cutoff)
    inactive_count = sessions.filter(last_activity__lt=cutoff).count()
    returned_count = active_sessions.filter(created_at__lt=cutoff).count()

    peak_rows = (
        exchanges.annotate(hour=ExtractHour("created_at"))
        .values("hour")
        .annotate(c=Count("id"))
        .order_by("hour")
    )
    hour_hist = [0] * 24
    for row in peak_rows:
        hour = row["hour"]
        if hour is None or hour < 0 or hour > 23:
            continue
        hour_hist[hour] = row["c"]

    vip_ids = list(
        customers.filter(tag=CustomerProfile.Tag.VIP).values_list("id", flat=True)
    )
    global_ids = list(
        customers.filter(tag=CustomerProfile.Tag.GLOBAL).values_list("id", flat=True)
    )
    vip_avg = (
        ExchangeRequest.objects.filter(bot=bot, customer_id__in=vip_ids)
        .values("customer_id")
        .annotate(c=Count("id"))
        .aggregate(avg=Avg("c"))["avg"]
        or 0
    )
    global_avg = (
        ExchangeRequest.objects.filter(bot=bot, customer_id__in=global_ids)
        .values("customer_id")
        .annotate(c=Count("id"))
        .aggregate(avg=Avg("c"))["avg"]
        or 0
    )
    ratio = None
    if global_avg and float(global_avg) > 0:
        ratio = round(float(vip_avg) / float(global_avg), 3)

    return {
        "returned": returned_count,
        "inactive": inactive_count,
        "inactive_days": INACTIVE_DAYS,
        "peak_hours": [{"hour": h, "count": hour_hist[h]} for h in range(24)],
        "vip_vs_ordinary_request_ratio": ratio,
        "vip_avg_requests": round(float(vip_avg), 3) if vip_avg else 0,
        "ordinary_avg_requests": round(float(global_avg), 3) if global_avg else 0,
    }


def channel_member_summary(bot: TelegramBot) -> list[dict[str, Any]]:
    channels = TelegramChannel.objects.filter(bot=bot, is_active=True)
    result = []
    for ch in channels:
        snap = (
            ChannelMemberSnapshot.objects.filter(channel=ch)
            .order_by("-sampled_at")
            .first()
        )
        publish_count = Finalization.objects.filter(
            channel=ch, message_sent=True
        ).count()
        publish_count += SpecialPriceFinalization.objects.filter(
            channel=ch, message_sent=True
        ).count()
        result.append(
            {
                "channel_id": ch.id,
                "name": ch.name,
                "chat_id": ch.chat_id,
                "member_count": ch.last_member_count or (snap.member_count if snap else None),
                "bot_admin_verified": ch.bot_admin_verified,
                "last_sampled_at": (
                    ch.last_member_sampled_at.isoformat()
                    if ch.last_member_sampled_at
                    else (snap.sampled_at.isoformat() if snap else None)
                ),
                "publish_activity_total": publish_count,
            }
        )
    return result


def format_analytics_dashboard_summary(bot: TelegramBot) -> str:
    usage = daily_usage_rows(bot)
    total_30d = sum(row["users"] for row in usage)
    today_str = timezone.now().date().isoformat()
    today_users = next(
        (row["users"] for row in usage if row["date"] == today_str), 0
    )
    currencies = most_requested_currencies(bot, limit=5)
    currency_lines = (
        "\n".join(f"  {r['currency']}: {r['count']}" for r in currencies)
        or "  (none yet)"
    )
    channels = channel_member_summary(bot)
    channel_lines = (
        "\n".join(
            f"  {c['name']}: {c['member_count'] or '?'} members"
            for c in channels
        )
        or "  (no channels configured)"
    )
    return (
        f"📈 Analytics — {bot.name}\n\n"
        f"📅 Daily bot usage (30d):\n"
        f"  🔥 Total active user-days: {total_30d}\n"
        f"  ☀️ Today: {today_users} users\n\n"
        f"📣 Channel members (latest):\n{channel_lines}\n\n"
        f"ℹ️ Note: Channel post view counts are not available via Bot API.\n\n"
        f"💱 Top currencies:\n{currency_lines}"
    )


def format_customer_analysis(bot: TelegramBot) -> str:
    data = customer_analysis(bot)
    peak = data["peak_hours"]
    top_hour = max(peak, key=lambda r: r["count"]) if peak else {"hour": 0, "count": 0}
    ratio = data["vip_vs_ordinary_request_ratio"]
    ratio_text = f"{ratio}x" if ratio is not None else "N/A"
    return (
        f"👥 Customer Analysis — {bot.name}\n\n"
        f"🔄 Returned users (active again after {INACTIVE_DAYS}d idle): "
        f"{data['returned']}\n"
        f"😴 Inactive users (no activity in {INACTIVE_DAYS}d): {data['inactive']}\n\n"
        f"⏰ Peak exchange hour: {top_hour['hour']:02d}:00 "
        f"({top_hour['count']} requests)\n\n"
        f"⭐ VIP users submit ~{ratio_text} more exchange requests than "
        f"ordinary users on average.\n"
        f"  💎 VIP avg: {data['vip_avg_requests']}\n"
        f"  🌐 Global avg: {data['ordinary_avg_requests']}"
    )


def format_exchange_requests(bot: TelegramBot, *, kind: str) -> str:
    counts = exchange_status_counts(bot)
    if kind == "successful":
        n = counts.get(ExchangeRequest.Status.SUCCESSFUL, 0)
        label = "Successful"
    else:
        n = counts.get(ExchangeRequest.Status.NEW, 0)
        label = "New"
    return f"💱 Exchange Requests — {label}\n\n📊 Count: {n}"


def format_new_members(bot: TelegramBot, months: int) -> str:
    dual = new_members_dual(bot, months)
    return (
        f"👋 New members — {dual['label']}\n\n"
        f"📣 Channel subscribers gained: {dual['channel_growth']}\n"
        f"💬 New bot DM users: {dual['bot_dm_growth']}\n"
        f"✨ Combined: {dual['channel_growth'] + dual['bot_dm_growth']}"
    )


def _exchange_event_row(req: ExchangeRequest, event_type: str) -> dict:
    customer = req.customer
    if customer:
        name = telegram_display_name(customer) or display_name(customer)
        username = telegram_username(customer)
    else:
        name = ""
        username = ""
    return {
        "id": req.id,
        "event_type": event_type,
        "request_id": req.id,
        "customer_telegram_user_id": customer.telegram_user_id if customer else None,
        "customer_name": name,
        "customer_username": username,
        "source_currency": req.source_currency,
        "target_currency": req.target_currency,
        "amount": str(req.amount),
        "status": req.status,
        "occurred_at": req.updated_at.isoformat(),
    }


def _campaign_event_row(campaign: ReengageCampaign) -> dict:
    return {
        "id": f"campaign-{campaign.id}",
        "event_type": "campaign_created",
        "campaign_id": campaign.id,
        "audience": campaign.audience,
        "schedule": campaign.schedule,
        "is_active": campaign.is_active,
        "occurred_at": campaign.created_at.isoformat(),
    }


def build_event_feed(bot: TelegramBot, *, limit: int = EVENT_FEED_LIMIT) -> list[dict]:
    """Build a merged event feed of recent exchange request events + new campaigns."""
    # Recent exchange requests (new/updated) — ordered by most recent activity
    recent_exchanges = (
        ExchangeRequest.objects.filter(bot=bot)
        .select_related("customer")
        .order_by("-updated_at")[:limit]
    )

    events = []
    for req in recent_exchanges:
        # Classify: if created_at and updated_at are within 5 seconds → new submission
        age = abs((req.updated_at - req.created_at).total_seconds())
        event_type = "request_created" if age < 5 else f"request_{req.status}"
        events.append((_exchange_event_row(req, event_type), req.updated_at))

    # Recent campaigns created
    recent_campaigns = (
        ReengageCampaign.objects.filter(bot=bot)
        .order_by("-created_at")[:10]
    )
    for campaign in recent_campaigns:
        events.append((_campaign_event_row(campaign), campaign.created_at))

    # Merge by occurred_at descending
    events.sort(key=lambda x: x[1], reverse=True)
    return [e[0] for e in events[:limit]]


def build_dashboard_payload(
    bot: TelegramBot,
    *,
    exchange_serializer,
    alert_serializer,
    channel_serializer,
    bot_summary: dict,
) -> dict[str, Any]:
    """Full dashboard dict for web API (replaces inline logic in admin_api)."""
    now = timezone.now()
    customers = customers_for_bot(bot)
    customer_ids = list(customers.values_list("id", flat=True))
    exchanges = ExchangeRequest.objects.filter(bot=bot).select_related("customer")
    alerts_qs = (
        PriceAlert.objects.filter(customer_id__in=customer_ids)
        .select_related("customer")
        .order_by("-created_at")
    )
    channels = (
        TelegramChannel.objects.filter(bot=bot)
        .select_related("bot")
        .order_by("-created_at")
    )

    tag_counts = {
        "global": customers.filter(tag=CustomerProfile.Tag.GLOBAL).count(),
        "vip": customers.filter(tag=CustomerProfile.Tag.VIP).count(),
        "special": customers.filter(tag=CustomerProfile.Tag.SPECIAL).count(),
        "total": customers.count(),
    }

    status_counts = exchange_status_counts(bot, now=now)
    running = status_counts.pop("_running", 0)

    member_windows = {}
    member_windows_detail = {}
    for months in (1, 3, 9, 12):
        dual = new_members_dual(bot, months, now=now)
        member_windows[str(months)] = dual["channel_growth"] + dual["bot_dm_growth"]
        member_windows_detail[str(months)] = dual

    analysis = customer_analysis(bot, now=now)

    return {
        "bot": bot_summary,
        "customers_status": {
            "by_tag": tag_counts,
            "definitions": {"inactive_days": INACTIVE_DAYS},
        },
        "notifications": {
            "events": build_event_feed(bot),
            "unread_count": ExchangeRequest.objects.filter(
                bot=bot, status=ExchangeRequest.Status.NEW
            ).count(),
        },
        "reports": {
            "running": running,
            "new": status_counts.get(ExchangeRequest.Status.NEW, 0),
            "pending": status_counts.get(ExchangeRequest.Status.NEW, 0),
            "successful": status_counts.get(ExchangeRequest.Status.SUCCESSFUL, 0),
            "cancelled": status_counts.get(ExchangeRequest.Status.CANCELLED, 0),
        },
        "publish": {
            "channels": channel_serializer(channels, many=True).data,
            "pointers": {
                "messenger": "hub:publish/messenger",
                "finalize": "/finalize",
                "studio": "/categories",
            },
        },
        "analytics": {
            "daily_usage": daily_usage_rows(bot),
            "channel_members": channel_member_summary(bot),
            "channel_views": {
                "available": False,
                "stub": True,
                "detail": "Channel post views are not available via the Bot API.",
            },
        },
        "exchange_requests": {
            "items": exchange_serializer(
                exchanges.order_by("-created_at")[:EXCHANGE_LIST_LIMIT], many=True
            ).data,
            "most_requested_currencies": most_requested_currencies(bot),
            "new_members": member_windows,
            "new_members_detail": member_windows_detail,
            "successful_status": ExchangeRequest.Status.SUCCESSFUL,
        },
        "customer_analysis": analysis,
    }


def build_profile_analytics_summary(bot: TelegramBot) -> dict[str, Any]:
    """Condensed analytics for programmer user profile (no large item lists)."""
    analysis = customer_analysis(bot)
    status_counts = exchange_status_counts(bot)
    return {
        "daily_usage": daily_usage_rows(bot)[-7:],
        "channel_members": channel_member_summary(bot),
        "most_requested_currencies": most_requested_currencies(bot, limit=5),
        "new_members": {
            str(m): new_members_dual(bot, m)
            for m in (1, 3, 9, 12)
        },
        "exchange_status": {
            "new": status_counts.get(ExchangeRequest.Status.NEW, 0),
            "pending": status_counts.get(ExchangeRequest.Status.NEW, 0),
            "successful": status_counts.get(ExchangeRequest.Status.SUCCESSFUL, 0),
            "cancelled": status_counts.get(ExchangeRequest.Status.CANCELLED, 0),
        },
        "customer_analysis": analysis,
    }


def snapshot_daily_usage_for_bot(bot: TelegramBot, *, target_date: date | None = None) -> int:
    """Snapshot active users for one day (default yesterday). Returns count."""
    if target_date is None:
        target_date = (timezone.now() - timedelta(days=1)).date()
    start = timezone.make_aware(datetime.combine(target_date, datetime.min.time()))
    end = start + timedelta(days=1)
    count = (
        BotSession.objects.filter(
            bot=bot,
            last_activity__gte=start,
            last_activity__lt=end,
        )
        .values("telegram_user_id")
        .distinct()
        .count()
    )
    BotDailyUsageSnapshot.objects.update_or_create(
        bot=bot,
        date=target_date,
        defaults={"active_users": count},
    )
    return count


def snapshot_customer_growth_for_bot(bot: TelegramBot, *, target_date: date | None = None) -> int:
    if target_date is None:
        target_date = (timezone.now() - timedelta(days=1)).date()
    start = timezone.make_aware(datetime.combine(target_date, datetime.min.time()))
    end = start + timedelta(days=1)
    count = (
        BotSession.objects.filter(
            bot=bot,
            created_at__gte=start,
            created_at__lt=end,
        )
        .values("telegram_user_id")
        .distinct()
        .count()
    )
    BotCustomerGrowthSnapshot.objects.update_or_create(
        bot=bot,
        date=target_date,
        defaults={"new_customers": count},
    )
    return count


def snapshot_channel_members_for_bot(bot: TelegramBot) -> dict:
    """Sample member counts for all active channels. Requires bot admin in channel."""
    from .telegram_client import TelegramService

    token = bot.get_plain_token()
    if not token:
        return {"sampled": 0, "skipped": 0, "error": "no_token"}

    try:
        client = TelegramService(token)
    except Exception as exc:
        return {"sampled": 0, "skipped": 0, "error": str(exc)}

    ok, me_info, _err = client.get_me()
    if not ok or not me_info:
        return {"sampled": 0, "skipped": 0, "error": "get_me_failed"}

    bot_user_id = me_info["id"]
    sampled = 0
    skipped = 0
    channels = TelegramChannel.objects.filter(bot=bot, is_active=True)

    for ch in channels:
        ok_m, member_info, _ = client.get_chat_member(ch.chat_id, bot_user_id)
        is_admin = False
        if ok_m and member_info:
            status = (member_info.get("status") or "").lower()
            is_admin = status in ("administrator", "creator")

        if not is_admin:
            ch.bot_admin_verified = False
            ch.save(update_fields=["bot_admin_verified", "updated_at"])
            skipped += 1
            ChannelMemberSnapshot.objects.create(
                channel=ch,
                member_count=0,
                bot_is_admin=False,
            )
            continue

        ok_c, count, _ = client.get_chat_member_count(ch.chat_id)
        if not ok_c or count is None:
            skipped += 1
            continue

        now = timezone.now()
        ChannelMemberSnapshot.objects.create(
            channel=ch,
            member_count=count,
            bot_is_admin=True,
        )
        ch.last_member_count = count
        ch.last_member_sampled_at = now
        ch.bot_admin_verified = True
        ch.save(
            update_fields=[
                "last_member_count",
                "last_member_sampled_at",
                "bot_admin_verified",
                "updated_at",
            ]
        )
        sampled += 1

    return {"sampled": sampled, "skipped": skipped}
