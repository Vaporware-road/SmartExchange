"""Build aiogram Bot + Dispatcher bound to a Django TelegramBot row."""

from __future__ import annotations

import copy
import logging
from typing import Any, Tuple

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Update
from asgiref.sync import async_to_sync

from telegram_app.bot.handlers import build_root_router
from telegram_app.bot.middlewares import CustomerProfileMiddleware, UserLockMiddleware
from telegram_app.bot.storage import DjangoBotSessionStorage
from telegram_app.models import TelegramBot
from telegram_app.services.bot_menu import ensure_customer_bot_menu_async

logger = logging.getLogger(__name__)

# Cache dispatchers per Django bot pk for the process lifetime.
_DISPATCHERS: dict[int, Tuple[Bot, Dispatcher]] = {}


def _normalize_user(user: dict[str, Any] | None) -> dict[str, Any] | None:
    if not user:
        return user
    out = dict(user)
    out.setdefault("is_bot", False)
    out.setdefault("first_name", "")
    return out


def _normalize_chat(chat: dict[str, Any] | None) -> dict[str, Any] | None:
    if not chat:
        return chat
    out = dict(chat)
    out.setdefault("type", "private")
    return out


def _normalize_message(message: dict[str, Any] | None) -> dict[str, Any] | None:
    if not message:
        return message
    out = dict(message)
    out.setdefault("date", 0)
    if "chat" in out:
        out["chat"] = _normalize_chat(out["chat"])
    if "from" in out:
        out["from"] = _normalize_user(out["from"])
    return out


def normalize_update_dict(update_dict: dict) -> dict:
    """Fill required Telegram fields so pydantic Update validation succeeds."""
    data = copy.deepcopy(update_dict)
    if "message" in data:
        data["message"] = _normalize_message(data["message"])
    if "edited_message" in data:
        data["edited_message"] = _normalize_message(data["edited_message"])
    if "callback_query" in data:
        cq = dict(data["callback_query"])
        if "from" in cq:
            cq["from"] = _normalize_user(cq["from"])
        if "message" in cq:
            cq["message"] = _normalize_message(cq["message"])
        cq.setdefault("chat_instance", "0")
        data["callback_query"] = cq
    return data


def build_bot_and_dispatcher(django_bot: TelegramBot) -> Tuple[Bot, Dispatcher]:
    token = django_bot.get_plain_token()
    bot = Bot(
        token=token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    storage = DjangoBotSessionStorage(django_bot)
    dp = Dispatcher(storage=storage)
    dp["django_bot"] = django_bot

    root = build_root_router()
    root.message.middleware(UserLockMiddleware())
    root.callback_query.middleware(UserLockMiddleware())
    root.message.middleware(CustomerProfileMiddleware())
    root.callback_query.middleware(CustomerProfileMiddleware())
    dp.include_router(root)
    return bot, dp


def get_bot_and_dispatcher(django_bot: TelegramBot) -> Tuple[Bot, Dispatcher]:
    cached = _DISPATCHERS.get(django_bot.pk)
    if cached is not None:
        bot, dp = cached
        dp["django_bot"] = django_bot
        return bot, dp
    bot, dp = build_bot_and_dispatcher(django_bot)
    _DISPATCHERS[django_bot.pk] = (bot, dp)
    return bot, dp


async def feed_customer_update_async(django_bot: TelegramBot, update_dict: dict) -> None:
    bot, dp = get_bot_and_dispatcher(django_bot)
    await ensure_customer_bot_menu_async(bot, django_bot_id=django_bot.pk)
    try:
        update = Update.model_validate(normalize_update_dict(update_dict))
    except Exception:
        logger.exception(
            "Invalid Telegram update bot_id=%s update_id=%s",
            django_bot.pk,
            update_dict.get("update_id"),
        )
        return
    await dp.feed_update(bot, update)


def feed_customer_update(django_bot: TelegramBot, update_dict: dict) -> None:
    """Sync entry used by Django webhook views (thread-safe with Django ORM)."""
    async_to_sync(feed_customer_update_async)(django_bot, update_dict)


async def close_cached_bots() -> None:
    from telegram_app.services.bot_menu import clear_menu_configured_cache

    for bot, _dp in _DISPATCHERS.values():
        try:
            await bot.session.close()
        except Exception:
            logger.debug("bot session close failed", exc_info=True)
    _DISPATCHERS.clear()
    clear_menu_configured_cache()
