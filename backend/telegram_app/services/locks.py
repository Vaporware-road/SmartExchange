"""Shared cache locks for customer-bot update processing."""

from __future__ import annotations

from django.core.cache import cache

PROCESSING_LOCK_PREFIX = "tg_cust_lock_"
USER_LOCK_PREFIX = "tg_cust_user_lock_"
PROCESSING_LOCK_TIMEOUT = 120
USER_LOCK_TIMEOUT = 30


def acquire_processing_lock(bot_id: int, update_id: int | None) -> bool:
    if update_id is None:
        return True
    key = f"{PROCESSING_LOCK_PREFIX}{bot_id}_{update_id}"
    return cache.add(key, 1, timeout=PROCESSING_LOCK_TIMEOUT)


def acquire_user_lock(bot_id: int, user_id: int) -> bool:
    key = f"{USER_LOCK_PREFIX}{bot_id}_{user_id}"
    return cache.add(key, 1, timeout=USER_LOCK_TIMEOUT)


def release_user_lock(bot_id: int, user_id: int) -> None:
    cache.delete(f"{USER_LOCK_PREFIX}{bot_id}_{user_id}")
