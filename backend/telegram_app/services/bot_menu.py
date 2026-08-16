"""Register Telegram Menu button + bot commands for customer bots."""

from __future__ import annotations

import logging

from aiogram import Bot
from aiogram.types import BotCommand, MenuButtonCommands
from asgiref.sync import async_to_sync

logger = logging.getLogger(__name__)

CUSTOMER_BOT_COMMANDS = [
    BotCommand(command="start", description="Open welcome / menu help"),
    BotCommand(command="profile", description="Customer profile"),
    BotCommand(command="exchange", description="Registering for exchange"),
    BotCommand(command="notifications", description="Notification System"),
]

_MENU_CONFIGURED: set[int] = set()


async def ensure_customer_bot_menu_async(bot: Bot, *, django_bot_id: int) -> None:
    """Idempotent setMyCommands + MenuButtonCommands for a bot process lifetime."""
    if django_bot_id in _MENU_CONFIGURED:
        return
    try:
        await bot.set_my_commands(CUSTOMER_BOT_COMMANDS)
        await bot.set_chat_menu_button(menu_button=MenuButtonCommands())
        _MENU_CONFIGURED.add(django_bot_id)
        logger.info("customer bot menu configured bot_id=%s", django_bot_id)
    except Exception:
        logger.exception("ensure_customer_bot_menu failed bot_id=%s", django_bot_id)


def ensure_customer_bot_menu(bot: Bot, *, django_bot_id: int) -> None:
    async_to_sync(ensure_customer_bot_menu_async)(bot, django_bot_id=django_bot_id)


def clear_menu_configured_cache() -> None:
    """Test helper."""
    _MENU_CONFIGURED.clear()
