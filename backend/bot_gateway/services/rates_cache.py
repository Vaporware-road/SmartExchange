"""
Redis-backed live rates cache for high-traffic bot replies.
"""
from __future__ import annotations

import logging

from django.conf import settings
from django.core.cache import cache

from core.prices_snapshot import build_prices_public_snapshot

logger = logging.getLogger(__name__)

CACHE_KEY = "bot_gateway:live_rates:v1"
CAPTIONS_KEY = "bot_gateway:formatted_captions:v1"


def _cache_ttl() -> int:
    return int(getattr(settings, "BOT_GATEWAY_RATES_CACHE_TTL", 15))


def refresh_live_rates_cache(source: str) -> dict:
    """Rebuild snapshot and pre-formatted captions, store in Redis."""
    from bot_gateway.services.formatter import build_all_formatted_captions

    snapshot = build_prices_public_snapshot()
    ttl = _cache_ttl()
    cache.set(CACHE_KEY, snapshot, ttl)
    try:
        captions = build_all_formatted_captions()
        cache.set(CAPTIONS_KEY, captions, ttl)
    except Exception:
        logger.exception("bot_gateway: caption cache build failed (source=%s)", source)
    logger.debug("bot_gateway: rates cache refreshed (source=%s, ttl=%s)", source, ttl)
    return snapshot


def get_cached_live_rates() -> dict:
    """Return cached snapshot; fallback to DB rebuild on miss."""
    data = cache.get(CACHE_KEY)
    if data is not None:
        return data
    return refresh_live_rates_cache("cache_miss")


def get_cached_caption(category_id: int) -> str:
    """Return pre-formatted caption for a category id."""
    captions = cache.get(CAPTIONS_KEY)
    if captions is None:
        refresh_live_rates_cache("caption_miss")
        captions = cache.get(CAPTIONS_KEY) or {}
    return (captions or {}).get(str(category_id)) or (captions or {}).get(category_id) or ""
