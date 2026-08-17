"""Shared exchange-request status and TTL hold operations."""

from __future__ import annotations

from ..models import ExchangeRequest, TelegramBot

DEFAULT_HOLD_TTL_MINUTES = 5


def hold_increment_minutes(bot: TelegramBot | None) -> int:
    ttl = getattr(bot, "default_exchange_ttl_minutes", None) if bot else None
    try:
        value = int(ttl) if ttl is not None else DEFAULT_HOLD_TTL_MINUTES
    except (TypeError, ValueError):
        value = DEFAULT_HOLD_TTL_MINUTES
    return value if value >= 1 else DEFAULT_HOLD_TTL_MINUTES


def set_request_status(req: ExchangeRequest, status: str) -> ExchangeRequest:
    allowed = set(ExchangeRequest.Status.values)
    if status not in allowed:
        raise ValueError(f"Invalid status: {status}")
    req.status = status
    req.save(update_fields=["status", "updated_at"])
    return req


def hold_request(req: ExchangeRequest) -> int:
    increment = hold_increment_minutes(req.bot)
    req.ttl_minutes = int(req.ttl_minutes or 0) + increment
    req.save(update_fields=["ttl_minutes", "updated_at"])
    return req.ttl_minutes
