"""Exchange registration flow callbacks."""

from __future__ import annotations

from aiogram import Bot, F, Router
from aiogram.types import CallbackQuery

from telegram_app.bot.handlers.reply import run_conversation
from telegram_app.models import TelegramBot


def create_router() -> Router:
    router = Router(name="exchange")

    @router.callback_query(F.data.startswith("exch:"))
    async def on_exchange(
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
