import logging

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task(name="bot_gateway.refresh_live_rates_cache")
def refresh_live_rates_cache_task(source: str = "celery_beat") -> None:
    """Warm every desk's rates cache.

    The cache is partitioned per account, so a single refresh under the task's
    default (unscoped) context would fill a namespace no request ever reads.
    One pass per account keeps each desk's first bot reply off the database.
    """
    from accounts.models import Account
    from accounts.scoping import act_as_account
    from bot_gateway.services.rates_cache import refresh_live_rates_cache

    for account_id in Account.objects.values_list("pk", flat=True):
        try:
            with act_as_account(account_id):
                refresh_live_rates_cache(source)
        except Exception:
            logger.exception(
                "bot_gateway periodic cache refresh failed (account=%s)", account_id
            )
