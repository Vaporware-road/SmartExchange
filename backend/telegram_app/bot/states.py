"""FSM states mirroring BotSession.State for aiogram handlers."""

from __future__ import annotations

from aiogram.fsm.state import State, StatesGroup

from telegram_app.models import BotSession


class CustomerStates(StatesGroup):
    START = State()
    MAIN_MENU = State()
    PROFILE = State()
    EXCHANGE_SOURCE = State()
    EXCHANGE_TARGET = State()
    EXCHANGE_AMOUNT = State()
    EXCHANGE_PRICE = State()
    EXCHANGE_TTL = State()
    EXCHANGE_SUMMARY = State()
    ALERT_MENU = State()
    ALERT_SOURCE = State()
    ALERT_TARGET = State()
    ALERT_PRICE = State()
    ALERT_SUMMARY = State()


def state_from_session_value(value: str) -> State | None:
    """Map BotSession.State string to aiogram State."""
    if value not in BotSession.State.values:
        return None
    return getattr(CustomerStates, value, None)
