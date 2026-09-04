from django.test import TestCase
from rest_framework.test import APIClient

from bot_gateway.models import BotCustomer, Platform
from category.models import Category
from orders.models import OrderIntake


class PublicOrderIntakeTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name="USDT", slug="usdt")

    def test_public_intake_returns_rates(self):
        r = self.client.get("/api/bot-gateway/public/intake/")
        self.assertEqual(r.status_code, 200)
        self.assertIn("rates", r.json())
        self.assertIn("order_url", r.json())

    def test_public_order_submit(self):
        r = self.client.post(
            "/api/bot-gateway/public/orders/",
            {
                "customer_name": "Ali Test",
                "customer_phone": "09121234567",
                "trade_type": "buy",
                "category": self.category.id,
                "amount": "1000",
                "customer_note": "test",
            },
            format="json",
        )
        self.assertEqual(r.status_code, 201)
        self.assertEqual(OrderIntake.objects.count(), 1)
        order = OrderIntake.objects.first()
        self.assertEqual(order.platform, Platform.WEB)
        self.assertEqual(BotCustomer.objects.filter(platform=Platform.WEB).count(), 1)
