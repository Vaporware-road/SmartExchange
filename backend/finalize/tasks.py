import logging

from celery import shared_task

from finalize.services import ExternalAPIService
from change_price.models import PriceHistory
from special_price.models import SpecialPriceHistory

logger = logging.getLogger(__name__)


def _rebuild_price_items(price_history_ids: list[int]):
    histories = (
        PriceHistory.objects.filter(id__in=price_history_ids)
        .select_related("price_type", "price_type__source_currency", "price_type__target_currency")
        .order_by("id")
    )
    return [(history.price_type, history) for history in histories]


def _rebuild_special_price_items(special_price_history_ids: list[int]):
    histories = (
        SpecialPriceHistory.objects.filter(id__in=special_price_history_ids)
        .select_related(
            "special_price_type",
            "special_price_type__source_currency",
            "special_price_type__target_currency",
        )
        .order_by("id")
    )
    return [(history.special_price_type, history) for history in histories]


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    max_retries=3,
    retry_backoff=True,
    retry_jitter=True,
)
def send_finalized_prices_task(self, *, price_history_ids: list[int]):
    price_items = _rebuild_price_items(price_history_ids)
    if not price_items:
        logger.info("send_finalized_prices_task skipped: no price items")
        return {"sent": [], "failed": [], "skipped": ["empty_items"]}
    return ExternalAPIService.send_finalized_prices(price_items)


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    max_retries=3,
    retry_backoff=True,
    retry_jitter=True,
)
def send_finalized_special_prices_task(self, *, special_price_history_ids: list[int]):
    special_price_items = _rebuild_special_price_items(special_price_history_ids)
    if not special_price_items:
        logger.info("send_finalized_special_prices_task skipped: no special price items")
        return {"sent": [], "failed": [], "skipped": ["empty_items"]}
    return ExternalAPIService.send_finalized_special_prices(special_price_items)
