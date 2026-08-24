"""Time-of-day auto-posting scheduler for AutoPostConfig records.

Celery beat runs ``telegram_app.auto_post_due_configs`` every minute; that task
calls :func:`run_due_auto_posts`, which:

1. finds enabled configs whose ``time_of_day`` matches the current time in the
   config's own IANA timezone and that have not already run today,
2. for each, dispatches the existing price-publisher task (category or special
   price) and waits for the bounded result,
3. on success persists a ``Finalization`` / ``SpecialPriceFinalization`` so
   auto-posts show up in analytics and the publish-task duplicate guards keep
   working across manual and automatic posts.

The publish tasks themselves are idempotent: an unchanged price snapshot that
was already posted to the same channel is skipped, so a config whose prices
have not moved since the last finalization does not spam the channel.
"""

from __future__ import annotations

import logging
from datetime import time as dt_time
from typing import Optional
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from django.conf import settings
from django.db import transaction
from django.utils import timezone

from change_price.models import PriceHistory
from price_publisher.tasks import publish_category_prices_task, publish_special_price_task
from special_price.models import SpecialPriceHistory

from ..models import AutoPostConfig

logger = logging.getLogger(__name__)

# How long to wait for a publish task result before giving up (same as finalize).
def _publish_timeout() -> int:
    return max(1, int(getattr(settings, "FINALIZE_TASK_WAIT_TIMEOUT", 75)))


def _config_timezone(config: AutoPostConfig) -> ZoneInfo:
    try:
        return ZoneInfo(config.timezone or "")
    except (ZoneInfoNotFoundError, ValueError):
        try:
            return ZoneInfo(settings.TIME_ZONE)
        except (ZoneInfoNotFoundError, ValueError):
            return ZoneInfo("UTC")


def _ran_today(config: AutoPostConfig, local_now) -> bool:
    if not config.last_run_at:
        return False
    try:
        last_local = config.last_run_at.astimezone(_config_timezone(config))
    except (ValueError, OverflowError):
        return False
    return last_local.date() == local_now.date()


def due_configs(now=None) -> list[AutoPostConfig]:
    """Enabled, active configs whose scheduled time matches ``now`` and that
    have not already run today (in their configured timezone)."""
    now = now or timezone.now()
    qs = (
        AutoPostConfig.objects.select_related(
            "channel", "channel__bot", "category", "special_price_type"
        )
        .filter(enabled=True, channel__is_active=True, channel__bot__is_active=True)
        .order_by("id")
    )
    due = []
    for config in qs:
        tz = _config_timezone(config)
        local_now = now.astimezone(tz)
        if (local_now.hour, local_now.minute) != (
            config.time_of_day.hour,
            config.time_of_day.minute,
        ):
            continue
        if _ran_today(config, local_now):
            continue
        due.append(config)
    return due


def _category_latest_ids(category_id: int) -> list[int]:
    """Latest PriceHistory id per price type in the category (mirrors finalize)."""
    from category.models import PriceType
    from change_price.prefetch_helpers import prefetch_price_histories_latest

    ids = []
    price_types = PriceType.objects.filter(category_id=category_id).prefetch_related(
        prefetch_price_histories_latest()
    )
    for price_type in price_types:
        latest = price_type.price_histories.first()
        if latest is not None:
            ids.append(latest.id)
    return ids


def _special_latest_id(special_price_type_id: int) -> Optional[int]:
    latest = SpecialPriceHistory.objects.filter(
        special_price_type_id=special_price_type_id
    ).first()
    return latest.id if latest is not None else None


def dispatch_config(config: AutoPostConfig) -> dict:
    """Publish one config's current prices and persist the finalization.

    Returns a summary dict with ``config_id``, ``target``, ``dispatched``,
    ``message_sent``, and ``detail``.
    """
    base = {
        "config_id": config.id,
        "channel_id": config.channel_id,
        "dispatched": False,
        "message_sent": False,
        "detail": "",
    }
    notes = (config.notes or "").strip() or None

    if config.special_price_type_id:
        history_id = _special_latest_id(config.special_price_type_id)
        if history_id is None:
            base["detail"] = "no special price history"
            return base
        try:
            async_result = publish_special_price_task.apply_async(
                kwargs={
                    "special_price_history_id": history_id,
                    "channel_id": config.channel_id,
                    "notes": notes,
                }
            )
            publication = _wait_result(async_result)
        except Exception as exc:  # noqa: BLE001 - report, do not kill beat
            logger.exception("auto_post special dispatch failed config_id=%s", config.id)
            base["detail"] = f"dispatch error: {exc}"
            return base
        base["target"] = "special"
        base["history_id"] = history_id
        base["message_sent"] = bool(publication.get("success"))
        base["detail"] = publication.get("response", "") or ""
        _record_special_finalization(config, history_id, publication)
        _mark_run(config)
        base["dispatched"] = True
        return base

    # Category target.
    history_ids = _category_latest_ids(config.category_id)
    if not history_ids:
        base["detail"] = "no prices for category"
        return base
    try:
        async_result = publish_category_prices_task.apply_async(
            kwargs={
                "category_id": config.category_id,
                "channel_id": config.channel_id,
                "notes": notes,
                "price_history_ids": history_ids,
            }
        )
        publication = _wait_result(async_result)
    except Exception as exc:  # noqa: BLE001
        logger.exception("auto_post category dispatch failed config_id=%s", config.id)
        base["detail"] = f"dispatch error: {exc}"
        return base
    base["target"] = "category"
    base["history_ids"] = history_ids
    base["message_sent"] = bool(publication.get("success"))
    base["detail"] = publication.get("response", "") or ""
    _record_category_finalization(config, history_ids, publication)
    _mark_run(config)
    base["dispatched"] = True
    return base


def _wait_result(async_result) -> dict:
    """Bounded wait mirroring finalize's publication wait."""
    from celery.exceptions import TimeoutError as CeleryTimeoutError

    try:
        payload = async_result.get(timeout=_publish_timeout())
        if isinstance(payload, dict):
            return payload
        return {
            "success": False,
            "response": f"Invalid task response: {type(payload).__name__}",
        }
    except CeleryTimeoutError:
        return {"success": False, "response": "Publish task timed out"}
    except Exception as exc:  # noqa: BLE001
        logger.exception("auto_post: publish task failed")
        return {"success": False, "response": f"Publish task error: {exc}"}


def _record_category_finalization(
    config: AutoPostConfig, history_ids: list[int], publication: dict
) -> None:
    from finalize.models import Finalization, FinalizedPriceHistory

    message_sent = bool(publication.get("success"))
    with transaction.atomic():
        finalization = Finalization.objects.create(
            category_id=config.category_id,
            channel=config.channel if message_sent else None,
            finalized_by=None,  # scheduled, no acting user
            message_sent=message_sent,
            image_caption=publication.get("caption") if message_sent else None,
            telegram_response=publication.get("response", "") or None,
            notes=(config.notes or "").strip() or None,
        )
        histories = PriceHistory.objects.filter(id__in=history_ids).only("id")
        FinalizedPriceHistory.objects.bulk_create(
            [
                FinalizedPriceHistory(finalization=finalization, price_history=history)
                for history in histories
            ]
        )


def _record_special_finalization(
    config: AutoPostConfig, history_id: int, publication: dict
) -> None:
    from finalize.models import SpecialPriceFinalization

    message_sent = bool(publication.get("success"))
    with transaction.atomic():
        SpecialPriceFinalization.objects.create(
            special_price_history_id=history_id,
            channel=config.channel if message_sent else None,
            finalized_by=None,
            message_sent=message_sent,
            image_caption=publication.get("caption") if message_sent else None,
            telegram_response=publication.get("response", "") or None,
            notes=(config.notes or "").strip() or None,
        )


def _mark_run(config: AutoPostConfig) -> None:
    AutoPostConfig.objects.filter(pk=config.pk).update(last_run_at=timezone.now())
    config.last_run_at = timezone.now()


def run_due_auto_posts(now=None) -> dict:
    """Dispatch every due auto-post config. Returns a summary dict."""
    configs = due_configs(now)
    results = []
    for config in configs:
        logger.info("auto_post dispatching config_id=%s channel_id=%s", config.id, config.channel_id)
        results.append(dispatch_config(config))
    summary = {
        "checked": AutoPostConfig.objects.filter(enabled=True).count(),
        "dispatched": sum(1 for r in results if r.get("dispatched")),
        "published": sum(1 for r in results if r.get("message_sent")),
        "results": results,
    }
    return summary
