"""Seed minimal price types for Web App E2E testing (idempotent)."""
import os
import sys
from decimal import Decimal

import django

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SmartExchangePanel.settings")
django.setup()

from category.models import Category, Currency, PriceType
from change_price.models import PriceHistory

usd, _ = Currency.objects.get_or_create(
    code="USD", defaults={"name": "US Dollar", "symbol": "$"}
)
cat, _ = Category.objects.get_or_create(
    slug="usd-test",
    defaults={"name": "دلار آمریکا"},
)
for trade, name, slug, price in (
    ("buy", "خرید دلار", "buy-usd", "177777"),
    ("sell", "فروش دلار", "sell-usd", "155555"),
):
    pt, created = PriceType.objects.get_or_create(
        category=cat,
        slug=slug,
        defaults={
            "name": name,
            "source_currency": usd,
            "target_currency": usd,
            "trade_type": trade,
            "is_active": True,
        },
    )
    if not PriceHistory.objects.filter(price_type=pt).exists():
        PriceHistory.objects.create(price_type=pt, price=Decimal(price))

print("seeded", cat.name, PriceType.objects.filter(category=cat).count(), "price types")
