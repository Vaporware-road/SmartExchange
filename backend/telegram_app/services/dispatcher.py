"""Outbound broadcast + inbound customer-bot entry (aiogram)."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import List

from telegram_app.bot.factory import feed_customer_update
from telegram_app.models import DefaultMessageSettings, TelegramBot
from telegram_app.services.customer_ops import upsert_customer_profile
from telegram_app.services.telegram_client import TelegramService

logger = logging.getLogger(__name__)

# Re-export for older imports / tests.
__all__ = [
    "broadcast_rendered_template",
    "process_update_payload",
    "upsert_customer_profile",
    "customer_bot_webhook_url",
    "sync_webhooks_from_site_settings",
    "DispatchResult",
]


@dataclass
class DispatchResult:
    bot: str
    channel: str
    success: bool
    detail: str
    fallback_used: bool = False


def _prepare_caption(settings: DefaultMessageSettings, template_name: str) -> str:
    caption = (settings.default_caption or "").strip()
    if caption:
        return caption
    return f"🔔 {template_name}"


def broadcast_rendered_template(
    template,
    image_path: str,
    image_url: str | None = None,
) -> List[dict]:
    """
    Broadcast a rendered template image to all active channels for bots with active settings.
    """
    results: List[DispatchResult] = []

    active_settings = (
        DefaultMessageSettings.objects.select_related("bot")
        .prefetch_related("bot__channels")
        .filter(active=True, bot__is_active=True)
    )

    for settings in active_settings:
        bot = settings.bot
        channels = bot.channels.filter(is_active=True)
        if not channels.exists():
            logger.info(
                "No active channels found for bot '%s'; skipping broadcast.",
                bot,
            )
            continue

        caption = _prepare_caption(settings, template.name)
        buttons = settings.default_buttons or []

        try:
            client = TelegramService(bot.get_plain_token())
        except Exception as exc:  # pragma: no cover - defensive
            logger.exception("Failed to initialize Telegram client for bot '%s': %s", bot, exc)
            continue

        for channel in channels:
            success = False
            detail = ""
            fallback_used = False

            try:
                success, detail = client.send_photo(
                    chat_id=channel.chat_id,
                    photo=image_path,
                    caption=caption,
                    buttons=buttons,
                )
                if not success:
                    fallback_used = True
                    success, detail, _ = client.send_message(
                        chat_id=channel.chat_id,
                        text=caption,
                        buttons=buttons,
                    )
            except Exception as exc:  # pragma: no cover - defensive
                logger.exception(
                    "Failed to send rendered template to '%s' via bot '%s': %s",
                    channel.chat_id,
                    bot,
                    exc,
                )
                success = False
                detail = str(exc)

            results.append(
                DispatchResult(
                    bot=str(bot),
                    channel=channel.chat_id,
                    success=success,
                    detail=detail,
                    fallback_used=fallback_used,
                )
            )

    return [
        {
            "bot": result.bot,
            "channel": result.channel,
            "success": result.success,
            "message": result.detail,
            "fallback_used": result.fallback_used,
            "image_url": image_url,
        }
        for result in results
    ]


def process_update_payload(bot: TelegramBot, update_dict: dict) -> None:
    """
    Single entry for webhook and polling: feed update into aiogram Dispatcher.
    Never raises to the caller.
    """
    try:
        feed_customer_update(bot, update_dict)
    except Exception:
        logger.exception(
            "process_update_payload failed bot_id=%s update_id=%s",
            bot.pk,
            update_dict.get("update_id"),
        )


def customer_bot_webhook_url(base_url: str, bot_id: int) -> str:
    base = (base_url or "").rstrip("/")
    return f"{base}/api/telegram/webhook/{bot_id}/"


def sync_webhooks_from_site_settings() -> list[dict]:
    """
    If SiteSettings.telegram_webhook_base_url is an https URL, setWebhook for each
    active bot. Returns per-bot result dicts.
    """
    from setting.models import SiteSettings

    try:
        settings_obj = SiteSettings.load()
    except Exception:
        logger.exception("sync_webhooks_from_site_settings: cannot load SiteSettings")
        return []

    base = (getattr(settings_obj, "telegram_webhook_base_url", None) or "").strip()
    if not base:
        logger.info("telegram_webhook_base_url empty; skipping setWebhook")
        return []
    if not base.lower().startswith("https://"):
        logger.warning(
            "telegram_webhook_base_url must be https; got %r — skipping setWebhook",
            base,
        )
        return [{"ok": False, "detail": "base URL must be https"}]

    results = []
    for bot in TelegramBot.objects.filter(is_active=True):
        url = customer_bot_webhook_url(base, bot.pk)
        try:
            client = TelegramService(bot.get_plain_token())
            ok, detail = client.set_webhook(url)
        except Exception as exc:
            ok, detail = False, str(exc)
        results.append({"bot_id": bot.pk, "url": url, "ok": ok, "detail": detail})
        logger.info("setWebhook bot_id=%s ok=%s detail=%s", bot.pk, ok, detail)
    return results
