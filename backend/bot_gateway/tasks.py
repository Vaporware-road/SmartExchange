import logging

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task(name="bot_gateway.refresh_live_rates_cache")
def refresh_live_rates_cache_task(source: str = "celery_beat") -> None:
    from bot_gateway.services.rates_cache import refresh_live_rates_cache

    try:
        refresh_live_rates_cache(source)
    except Exception:
        logger.exception("bot_gateway periodic cache refresh failed")
