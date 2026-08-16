"""Django-backed aiogram FSM storage using BotSession rows."""

from __future__ import annotations

from typing import Any, Mapping

from aiogram.fsm.state import State
from aiogram.fsm.storage.base import BaseStorage, StateType, StorageKey
from asgiref.sync import sync_to_async

from telegram_app.models import BotSession, TelegramBot


class DjangoBotSessionStorage(BaseStorage):
    """
    Persist aiogram FSM state/data on BotSession.state + BotSession.context.

    ``bot`` is the Django TelegramBot row (not aiogram Bot).
    """

    def __init__(self, django_bot: TelegramBot):
        self.django_bot = django_bot

    def _session(self, key: StorageKey) -> BotSession:
        session, _ = BotSession.objects.get_or_create(
            telegram_user_id=int(key.chat_id),
            bot=self.django_bot,
            defaults={"state": BotSession.State.START, "context": {}},
        )
        return session

    async def set_state(self, key: StorageKey, state: StateType = None) -> None:
        def _set():
            session = self._session(key)
            if state is None:
                session.state = BotSession.State.START
            elif isinstance(state, State):
                # state.state is like "CustomerStates:MAIN_MENU"
                name = state.state.split(":")[-1] if state.state else BotSession.State.START
                session.state = name if name in BotSession.State.values else BotSession.State.START
            else:
                raw = str(state)
                name = raw.split(":")[-1]
                session.state = name if name in BotSession.State.values else BotSession.State.START
            session.save(update_fields=["state", "updated_at", "last_activity"])

        await sync_to_async(_set)()

    async def get_state(self, key: StorageKey) -> str | None:
        def _get():
            session = self._session(key)
            return f"CustomerStates:{session.state}"

        return await sync_to_async(_get)()

    async def set_data(self, key: StorageKey, data: Mapping[str, Any]) -> None:
        def _set():
            session = self._session(key)
            session.context = dict(data)
            session.save(update_fields=["context", "updated_at", "last_activity"])

        await sync_to_async(_set)()

    async def get_data(self, key: StorageKey) -> dict[str, Any]:
        def _get():
            session = self._session(key)
            return dict(session.context or {})

        return await sync_to_async(_get)()

    async def close(self) -> None:
        return None
