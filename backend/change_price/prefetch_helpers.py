"""
Prefetch helpers so history queries do not SELECT optional columns (e.g. ``event_at``)
that may be missing on databases where migrations were not applied yet.
"""
from django.db.models import Prefetch

from .models import PriceHistory


def prefetch_price_histories_latest():
    """Latest-first price histories for PriceType.prefetch_related(...)."""
    return Prefetch(
        "price_histories",
        queryset=PriceHistory.objects.defer("event_at").order_by("-created_at"),
    )
