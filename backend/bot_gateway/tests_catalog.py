from django.core.cache import cache
from django.test import TestCase

from bot_gateway.services.price_catalog import build_price_catalog


class PriceCatalogTests(TestCase):
    def setUp(self):
        # The rates snapshot is cached for 15s and Django does not reset caches
        # between tests, so without this a neighbouring test's empty snapshot
        # leaks in and the catalog comes back empty.
        cache.clear()

    def test_skips_empty_prices(self):
        snapshot = {
            "categories": [
                {
                    "id": 1,
                    "name": "US Dollar",
                    "slug": "usd",
                    "price_types": [
                        {
                            "id": 10,
                            "name": "خرید دلار",
                            "trade_type": "buy",
                            "is_active": True,
                            "latest_price": "177777",
                            "target_currency": {"code": "USD"},
                        },
                        {
                            "id": 11,
                            "name": "فروش دلار",
                            "trade_type": "sell",
                            "is_active": True,
                            "latest_price": "155555",
                            "target_currency": {"code": "USD"},
                        },
                        {
                            "id": 12,
                            "name": "USDT",
                            "trade_type": "buy",
                            "is_active": True,
                            "latest_price": None,
                        },
                    ],
                }
            ]
        }
        catalog = build_price_catalog(snapshot)
        self.assertEqual(len(catalog), 2)
        self.assertEqual(catalog[0]["name"], "خرید دلار")
        self.assertEqual(catalog[0]["category_name"], "US Dollar")
