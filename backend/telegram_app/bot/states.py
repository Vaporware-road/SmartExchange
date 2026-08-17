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
    ADMIN_MENU = State()
    ADMIN_REQUEST_LIST = State()
    ADMIN_REQUEST_DETAIL = State()
    ADMIN_CHANGE_STATE = State()
    ADMIN_SET_TAG = State()
    ADMIN_ANALYTICS = State()
    ADMIN_ANALYTICS_EXCHANGE = State()
    ADMIN_ANALYTICS_MEMBERS = State()
    ADMIN_REENGAGE = State()
    ADMIN_REENGAGE_AUDIENCE = State()
    ADMIN_REENGAGE_COMPOSE = State()
    ADMIN_REENGAGE_SCHEDULE = State()
    ADMIN_OFFER_CREATE = State()


def state_from_session_value(value: str) -> State | None:
    """Map BotSession.State string to aiogram State."""
    if value not in BotSession.State.values:
        return None
    return getattr(CustomerStates, value, None)
