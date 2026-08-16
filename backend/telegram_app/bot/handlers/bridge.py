"""Catch-all bridge: typed replies, currency catalog callbacks, remaining updates."""

from __future__ import annotations

from aiogram import Bot, Router
from aiogram.types import CallbackQuery, Message

from telegram_app.bot.handlers.reply import run_conversation
from telegram_app.models import TelegramBot


def create_router() -> Router:
    router = Router(name="bridge")

    @router.message()
    async def on_message(
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

    @router.callback_query()
    async def on_callback(
        callback: CallbackQuery,
        bot: Bot,
        django_bot: TelegramBot,
        event_update=None,
    ) -> None:
        if not callback.from_user or not callback.message:
            return
        update_id = getattr(event_update, "update_id", None)
        await run_conversation(
            bot=bot,
            django_bot=django_bot,
            user_id=callback.from_user.id,
            text=None,
            callback_data=callback.data,
            message_id=callback.message.message_id,
            update_id=update_id,
            callback=callback,
            chat_id=callback.message.chat.id,
        )

    return router
