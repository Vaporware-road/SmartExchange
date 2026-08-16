"""aiogram middlewares for customer bots."""

from __future__ import annotations

from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message, TelegramObject
from asgiref.sync import sync_to_async
from django.core.cache import cache

from telegram_app.services.customer_ops import upsert_customer_profile
from telegram_app.services.locks import USER_LOCK_PREFIX, USER_LOCK_TIMEOUT

UpdateHandler = Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]]


class CustomerProfileMiddleware(BaseMiddleware):
    """Upsert CustomerProfile from the update's from_user."""

    async def __call__(
        self,
        handler: UpdateHandler,
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        user = None
        if isinstance(event, Message):
            user = event.from_user
        elif isinstance(event, CallbackQuery):
            user = event.from_user
        if user is not None:
            payload = {
                "message": {
                    "from": {
                        "id": user.id,
                        "username": user.username or "",
                        "first_name": user.first_name or "",
                        "last_name": user.last_name or "",
                        "language_code": user.language_code or "",
                    }
                }
            }
            await sync_to_async(upsert_customer_profile)(payload)
        return await handler(event, data)


class UserLockMiddleware(BaseMiddleware):
    """Drop overlapping updates for the same telegram user (multi-click guard)."""

    async def __call__(
        self,
        handler: UpdateHandler,
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        django_bot = data.get("django_bot")
        user = None
        if isinstance(event, Message):
            user = event.from_user
        elif isinstance(event, CallbackQuery):
            user = event.from_user
        if not django_bot or user is None:
            return await handler(event, data)

        key = f"{USER_LOCK_PREFIX}{django_bot.pk}_{user.id}"
        acquired = await sync_to_async(cache.add)(key, 1, timeout=USER_LOCK_TIMEOUT)
        if not acquired:
            if isinstance(event, CallbackQuery):
                try:
                    await event.answer("Please wait…")
                except Exception:
                    pass
            return None
        try:
            return await handler(event, data)
        finally:
            await sync_to_async(cache.delete)(key)
