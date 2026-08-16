"""
Resolve board prices for customer PriceAlerts and fire DMs when thresholds hit.

Uses latest ``PriceHistory`` for an active ``PriceType`` matching source/target
ISO codes. Does not invent FX when no board pair exists.
"""

from __future__ import annotations

import logging
from datetime import timedelta
from decimal import Decimal

from django.utils import timezone

from category.models import PriceType
from change_price.models import PriceHistory
from ..models import PriceAlert, TelegramBot
from .telegram_client import TelegramService

logger = logging.getLogger(__name__)

DEFAULT_COOLDOWN = timedelta(hours=1)


def resolve_board_price(source_currency: str, target_currency: str) -> Decimal | None:
    """Latest board price for the pair, or None if no matching PriceType/history."""
    src = (source_currency or "").strip().upper()
    tgt = (target_currency or "").strip().upper()
    if not src or not tgt:
        return None

    price_types = PriceType.objects.filter(
        is_active=True,
        source_currency__code__iexact=src,
        target_currency__code__iexact=tgt,
    )
    if not price_types.exists():
        return None

    history = (
        PriceHistory.objects.filter(price_type__in=price_types)
        .order_by("-created_at")
        .first()
    )
    if history is None:
        return None
    return history.price


def alert_should_fire(alert: PriceAlert, current: Decimal) -> bool:
    if alert.direction == PriceAlert.Direction.INCREASE:
        return current >= alert.target_price
    if alert.direction == PriceAlert.Direction.DECREASE:
        return current <= alert.target_price
    return False


def alert_in_cooldown(alert: PriceAlert, *, now=None, cooldown: timedelta = DEFAULT_COOLDOWN) -> bool:
    if alert.last_triggered_at is None:
        return False
    now = now or timezone.now()
    return alert.last_triggered_at + cooldown > now


def _pick_send_bot() -> TelegramBot | None:
    return TelegramBot.objects.filter(is_active=True).order_by("id").first()


def _dm_customer(alert: PriceAlert, current: Decimal, bot: TelegramBot) -> bool:
    chat_id = alert.customer.telegram_user_id
    text = (
        f"Price alert ({alert.direction})\n"
        f"{alert.source_currency}/{alert.target_currency}\n"
        f"Target: {alert.target_price}\n"
        f"Current: {current}"
    )
    try:
        client = TelegramService(bot.get_plain_token())
        ok, detail, _ = client.send_message(chat_id=chat_id, text=text, parse_mode=None)
    except Exception:
        logger.exception("alert_checker: DM failed alert_id=%s", alert.pk)
        return False
    if not ok:
        logger.warning("alert_checker: DM failed alert_id=%s detail=%s", alert.pk, detail)
    return ok


def check_price_alerts(*, cooldown: timedelta = DEFAULT_COOLDOWN) -> dict:
    """
    Scan active alerts once. Returns counters for observability/tests.
    """
    now = timezone.now()
    bot = _pick_send_bot()
    stats = {
        "checked": 0,
        "skipped_no_price": 0,
        "skipped_cooldown": 0,
        "skipped_threshold": 0,
        "triggered": 0,
        "dm_failed": 0,
        "no_bot": 0,
    }
    if bot is None:
        stats["no_bot"] = 1
        logger.warning("alert_checker: no active TelegramBot; skipping DMs")

    alerts = (
        PriceAlert.objects.filter(is_active=True)
        .select_related("customer")
        .order_by("id")
    )
    for alert in alerts:
        stats["checked"] += 1
        current = resolve_board_price(alert.source_currency, alert.target_currency)
        if current is None:
            stats["skipped_no_price"] += 1
            logger.info(
                "alert_checker: no board price for %s/%s alert_id=%s",
                alert.source_currency,
                alert.target_currency,
                alert.pk,
            )
            continue
        if alert_in_cooldown(alert, now=now, cooldown=cooldown):
            stats["skipped_cooldown"] += 1
            continue
        if not alert_should_fire(alert, current):
            stats["skipped_threshold"] += 1
            continue
        if bot is None:
            stats["dm_failed"] += 1
            continue
        if _dm_customer(alert, current, bot):
            alert.last_triggered_at = now
            alert.save(update_fields=["last_triggered_at", "updated_at"])
            stats["triggered"] += 1
        else:
            stats["dm_failed"] += 1

    return stats
