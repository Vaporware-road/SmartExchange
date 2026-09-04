from __future__ import annotations

import logging
import time
from typing import Any, Optional

from django.conf import settings
from django.core.cache import cache
from django.utils import timezone

from category.models import Category
from telegram_app.models import TelegramBot
from telegram_app.services.telegram_client import TelegramService

from bot_gateway.adapters.base import InboundMessage, OutboundReply
from bot_gateway.models import (
    BotCustomer,
    BotInteractionLog,
    Direction,
    Platform,
    TriggerType,
    WhatsAppConfig,
)
from bot_gateway.services.auth_tokens import build_webapp_url, issue_customer_token
from bot_gateway.services.formatter import build_reply_text
from bot_gateway.services.triggers import match_trigger
from bot_gateway.services.whatsapp_client import send_text_message

logger = logging.getLogger(__name__)


def _rate_limit_key(platform: str, sender_id: str) -> str:
    return f"bot_gateway:ratelimit:{platform}:{sender_id}"


def acquire_dedup_lock(platform: str, update_id: str) -> bool:
    if not update_id:
        return True
    key = f"bot_gateway:dedup:{platform}:{update_id}"
    return cache.add(key, 1, timeout=300)


def is_rate_limited(platform: str, sender_id: str) -> bool:
    limit = int(getattr(settings, "BOT_GATEWAY_RATE_LIMIT", 20))
    window = int(getattr(settings, "BOT_GATEWAY_RATE_WINDOW", 60))
    key = _rate_limit_key(platform, sender_id)
    count = cache.get(key, 0) + 1
    cache.set(key, count, window)
    return count > limit


def upsert_customer(msg: InboundMessage) -> BotCustomer:
    if msg.platform == Platform.TELEGRAM:
        customer, _ = BotCustomer.objects.get_or_create(
            platform=Platform.TELEGRAM,
            telegram_chat_id=int(msg.sender_id),
            defaults={
                "display_name": msg.display_name,
                "username": msg.username,
            },
        )
    else:
        customer, _ = BotCustomer.objects.get_or_create(
            platform=Platform.WHATSAPP,
            whatsapp_phone=msg.sender_id,
            defaults={"display_name": msg.display_name},
        )
    customer.display_name = msg.display_name or customer.display_name
    customer.username = msg.username or customer.username
    customer.last_seen_at = timezone.now()
    customer.save(
        update_fields=["display_name", "username", "last_seen_at"]
    )
    return customer


def _resolve_category(
    matched: Optional[Category],
    default_category: Optional[Category],
) -> Optional[Category]:
    if matched:
        return matched
    if default_category:
        return default_category
    return Category.objects.order_by("name").first()


def _build_order_button(
    customer: BotCustomer,
    *,
    bot_id: Optional[int],
    button_text: str,
    auth_extra: Optional[dict] = None,
) -> tuple[str, list]:
    token = issue_customer_token(customer, bot_id=bot_id, extra=auth_extra)
    webapp_url = build_webapp_url(token)
    buttons = [[{"text": button_text, "web_app": {"url": webapp_url}}]]
    return webapp_url, buttons


def process_inbound_telegram(bot: TelegramBot, msg: InboundMessage) -> None:
    started = time.monotonic()
    if not acquire_dedup_lock(msg.platform, msg.update_id):
        return

    customer = upsert_customer(msg)
    rate_limited = is_rate_limited(msg.platform, msg.sender_id)
    trigger_type, matched_cat = match_trigger(msg.text)

    if rate_limited:
        BotInteractionLog.objects.create(
            customer=customer,
            platform=msg.platform,
            direction=Direction.INBOUND,
            message_text=msg.text[:2000],
            trigger_type=trigger_type,
            was_rate_limited=True,
            update_id=msg.update_id,
        )
        return

    if trigger_type == TriggerType.OTHER:
        BotInteractionLog.objects.create(
            customer=customer,
            platform=msg.platform,
            direction=Direction.INBOUND,
            message_text=msg.text[:2000],
            trigger_type=trigger_type,
            update_id=msg.update_id,
        )
        return

    category = _resolve_category(matched_cat, bot.default_category)
    reply_text = build_reply_text(category, trigger_type)
    button_text = bot.order_button_text or "🛒 ثبت سفارش سریع"
    webapp_url, buttons = _build_order_button(
        customer, bot_id=bot.pk, button_text=button_text
    )

    service = TelegramService(bot.token)
    ok, err = service.send_message(
        msg.chat_id,
        reply_text,
        parse_mode="HTML",
        buttons=buttons,
    )
    elapsed_ms = int((time.monotonic() - started) * 1000)
    BotInteractionLog.objects.create(
        customer=customer,
        platform=msg.platform,
        direction=Direction.INBOUND,
        message_text=msg.text[:2000],
        trigger_type=trigger_type,
        response_ms=elapsed_ms,
        update_id=msg.update_id,
    )
    BotInteractionLog.objects.create(
        customer=customer,
        platform=msg.platform,
        direction=Direction.OUTBOUND,
        message_text=reply_text[:2000] if ok else f"ERROR: {err}"[:2000],
        trigger_type=trigger_type,
        response_ms=elapsed_ms,
        update_id=msg.update_id,
    )
    if not ok:
        logger.warning("Telegram reply failed bot=%s: %s", bot.pk, err)


def process_inbound_whatsapp(
    msg: InboundMessage,
    config: Optional[WhatsAppConfig] = None,
) -> None:
    from bot_gateway.services.whatsapp_client import get_active_config

    cfg = config or get_active_config()
    if not cfg:
        return

    started = time.monotonic()
    if not acquire_dedup_lock(msg.platform, msg.update_id):
        return

    customer = upsert_customer(msg)
    rate_limited = is_rate_limited(msg.platform, msg.sender_id)
    trigger_type, matched_cat = match_trigger(msg.text)

    if rate_limited:
        BotInteractionLog.objects.create(
            customer=customer,
            platform=msg.platform,
            direction=Direction.INBOUND,
            message_text=msg.text[:2000],
            trigger_type=trigger_type,
            was_rate_limited=True,
            update_id=msg.update_id,
        )
        return

    if trigger_type == TriggerType.OTHER:
        BotInteractionLog.objects.create(
            customer=customer,
            platform=msg.platform,
            direction=Direction.INBOUND,
            message_text=msg.text[:2000],
            trigger_type=trigger_type,
            update_id=msg.update_id,
        )
        return

    category = _resolve_category(matched_cat, cfg.default_category)
    reply_text = build_reply_text(category, trigger_type)
    button_text = cfg.order_button_text or "🛒 ثبت سفارش سریع"
    webapp_url, _ = _build_order_button(customer, bot_id=None, button_text=button_text)

    ok, err = send_text_message(
        msg.sender_id,
        reply_text,
        config=cfg,
        cta_url=webapp_url,
        cta_text=button_text,
    )
    elapsed_ms = int((time.monotonic() - started) * 1000)
    BotInteractionLog.objects.create(
        customer=customer,
        platform=msg.platform,
        direction=Direction.INBOUND,
        message_text=msg.text[:2000],
        trigger_type=trigger_type,
        response_ms=elapsed_ms,
        update_id=msg.update_id,
    )
    BotInteractionLog.objects.create(
        customer=customer,
        platform=msg.platform,
        direction=Direction.OUTBOUND,
        message_text=reply_text[:2000] if ok else f"ERROR: {err}"[:2000],
        trigger_type=trigger_type,
        response_ms=elapsed_ms,
        update_id=msg.update_id,
    )
    if not ok:
        logger.warning("WhatsApp reply failed: %s", err)
