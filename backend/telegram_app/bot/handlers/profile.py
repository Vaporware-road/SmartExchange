"""Profile submenu callbacks."""

from __future__ import annotations

from aiogram import Bot, F, Router
from aiogram.types import CallbackQuery

from telegram_app.bot.handlers.reply import run_conversation
from telegram_app.models import TelegramBot
from telegram_app.services.conversation import (
    CB_PROFILE_BACK,
    CB_PROFILE_HISTORY,
    CB_PROFILE_ID,
    CB_PROFILE_MOST,
    CB_PROFILE_RUNNING,
)

_PROFILE_CBS = {
    CB_PROFILE_HISTORY,
    CB_PROFILE_MOST,
    CB_PROFILE_ID,
    CB_PROFILE_BACK,
    CB_PROFILE_RUNNING,
}


def create_router() -> Router:
    router = Router(name="profile")

    @router.callback_query(F.data.in_(_PROFILE_CBS))
    async def on_profile(
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
