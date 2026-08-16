""" /start handler. """

from __future__ import annotations

from aiogram import Bot, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from telegram_app.bot.handlers.reply import run_conversation
from telegram_app.models import TelegramBot


def create_router() -> Router:
    router = Router(name="start")

    @router.message(CommandStart())
    async def on_start(
        message: Message,
        bot: Bot,
        django_bot: TelegramBot,
        event_update=None,
    ) -> None:
        if not message.from_user:
            return
        update_id = getattr(event_update, "update_id", None)
        await run_conversation(
            bot=bot,
            django_bot=django_bot,
            user_id=message.from_user.id,
            text=message.text,
            callback_data=None,
            message_id=message.message_id,
            update_id=update_id,
            message=message,
            chat_id=message.chat.id,
        )

    return router
