"""Integration tests for Telegram bot customer Web App order flow."""
from decimal import Decimal

from django.core.cache import cache
from django.test import TestCase
from rest_framework.test import APIClient

from bot_gateway.models import BotCustomer, Platform
from bot_gateway.services.auth_tokens import issue_customer_token
from category.models import Category, Currency, PriceType
from change_price.models import PriceHistory
from orders.models import OrderIntake


class TelegramWebAppFlowTests(TestCase):
    def setUp(self):
        # The rates snapshot is cached for 15s and Django does not reset caches
        # between tests, so without this a neighbouring test's empty snapshot
        # leaks in and the catalog comes back empty.
        cache.clear()
        self.client = APIClient()
        usd, _ = Currency.objects.get_or_create(
            code="USD", defaults={"name": "US Dollar", "symbol": "$"}
        )
        self.category = Category.objects.create(name="US Dollar", slug="usd")
        self.pt_buy = PriceType.objects.create(
            category=self.category,
            name="خرید دلار",
            slug="buy-usd",
            source_currency=usd,
            target_currency=usd,
            trade_type="buy",
        )
        self.pt_sell = PriceType.objects.create(
            category=self.category,
            name="فروش دلار",
            slug="sell-usd",
            source_currency=usd,
            target_currency=usd,
            trade_type="sell",
        )
        PriceHistory.objects.create(price_type=self.pt_buy, price=Decimal("177777"))
        PriceHistory.objects.create(price_type=self.pt_sell, price=Decimal("155555"))
        self.customer = BotCustomer.objects.create(
            platform=Platform.TELEGRAM,
            telegram_chat_id=99887766,
            display_name="Telegram User",
            username="tguser",
        )
        self.token = issue_customer_token(self.customer, bot_id=1)

    def test_auth_me_with_bot_jwt(self):
        r = self.client.get(
            "/api/bot-gateway/auth/me/",
            HTTP_AUTHORIZATION=f"Bearer {self.token}",
        )
        self.assertEqual(r.status_code, 200)
        body = r.json()
        self.assertEqual(body["platform"], "telegram")
        self.assertIn("price_catalog", body)
        self.assertGreaterEqual(len(body["price_catalog"]), 2)

    def test_submit_order_with_bot_jwt(self):
        r = self.client.post(
            "/api/bot-gateway/orders/",
            {
                "trade_type": "buy",
                "category": self.category.id,
                "price_type": self.pt_buy.id,
                "amount": "500",
                "currency_code": "USD",
                "customer_note": "from telegram webapp",
            },
            format="json",
            HTTP_AUTHORIZATION=f"Bearer {self.token}",
        )
        self.assertEqual(r.status_code, 201, r.content)
        self.assertEqual(OrderIntake.objects.count(), 1)
        order = OrderIntake.objects.first()
        self.assertEqual(order.platform, Platform.TELEGRAM)
        self.assertEqual(order.status, OrderIntake.Status.PENDING)
        self.assertEqual(order.customer_id, self.customer.id)

    def test_submit_without_token_fails(self):
        r = self.client.post(
            "/api/bot-gateway/orders/",
            {"trade_type": "buy", "category": self.category.id, "amount": "100"},
            format="json",
        )
        self.assertIn(r.status_code, (401, 403))
