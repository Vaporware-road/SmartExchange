"""Shared reply delivery for customer bot handlers."""

from __future__ import annotations

import logging

from aiogram import Bot
from aiogram.exceptions import TelegramAPIError
from aiogram.types import CallbackQuery, Message
from asgiref.sync import sync_to_async

from telegram_app.bot.keyboards import as_reply_markup
from telegram_app.models import TelegramBot
from telegram_app.services.conversation import ConversationEngine
from telegram_app.services.locks import acquire_processing_lock

logger = logging.getLogger(__name__)

LAST_PROCESSED_UPDATE_ID_KEY = "last_processed_update_id"


async def deliver_engine_reply(
    *,
    bot: Bot,
    chat_id: int,
    response: dict,
) -> None:
    """Send on the *current* aiogram event loop (never via a cached sync Bot)."""
    text_out = (response.get("text") or "").strip()
    if not text_out:
        return

    markup = as_reply_markup(
        response.get("buttons"),
        remove_keyboard=bool(response.get("remove_keyboard")),
    )
    try:
        await bot.send_message(
            chat_id=chat_id,
            text=text_out,
            parse_mode=None,
            reply_markup=markup,
        )
    except TelegramAPIError as exc:
        logger.error(
            "send_message failed chat_id=%s detail=%s",
            chat_id,
            exc,
        )
    except Exception:
        logger.exception("send_message failed chat_id=%s", chat_id)


async def run_conversation(
    *,
    bot: Bot,
    django_bot: TelegramBot,
    user_id: int,
    text: str | None,
    callback_data: str | None,
    message_id: int | None,
    update_id: int | None,
    callback: CallbackQuery | None = None,
    message: Message | None = None,
    chat_id: int,
) -> None:
    if not await sync_to_async(acquire_processing_lock)(django_bot.pk, update_id):
        if callback:
            try:
                await callback.answer("Please wait…")
            except Exception:
                pass
        return

    if callback:
        try:
            await callback.answer()
        except Exception:
            logger.debug("callback.answer failed", exc_info=True)

    engine = ConversationEngine(django_bot)

    def _process():
        session = engine.get_or_create_session(user_id)
        if update_id is not None:
            last = (session.context or {}).get(LAST_PROCESSED_UPDATE_ID_KEY)
            if last is not None and int(update_id) <= int(last):
                return None
        response = engine.process_update(
            session,
            text=text,
            callback_data=callback_data,
            message_id=message_id,
        )
        if update_id is not None:
            ctx = dict(session.context or {})
            ctx[LAST_PROCESSED_UPDATE_ID_KEY] = int(update_id)
            session.context = ctx
            session.save(update_fields=["context", "updated_at"])
        return response

    response = await sync_to_async(_process)()
    if response is None:
        return

    await deliver_engine_reply(bot=bot, chat_id=chat_id, response=response)
