from unittest.mock import patch

from django.core.cache import cache
from django.test import TestCase, override_settings

from bot_gateway.models import BotCustomer, Platform
from bot_gateway.services.auth_tokens import decode_customer_token, issue_customer_token
from bot_gateway.services.rates_cache import CACHE_KEY, get_cached_live_rates, refresh_live_rates_cache
from bot_gateway.services.triggers import match_trigger


class TriggerTests(TestCase):
    def test_start_trigger(self):
        trigger, cat = match_trigger("/start")
        self.assertEqual(trigger, "start")
        self.assertIsNone(cat)

    def test_price_keyword(self):
        trigger, cat = match_trigger("قیمت")
        self.assertEqual(trigger, "price_keyword")
        self.assertIsNone(cat)

    def test_other_message(self):
        trigger, _ = match_trigger("random hello xyz")
        self.assertEqual(trigger, "other")


class AuthTokenTests(TestCase):
    def test_round_trip(self):
        customer = BotCustomer.objects.create(
            platform=Platform.TELEGRAM,
            telegram_chat_id=12345,
        )
        token = issue_customer_token(customer, bot_id=1)
        payload = decode_customer_token(token)
        self.assertEqual(payload["sub"], str(customer.uuid))
        self.assertEqual(payload["typ"], "bot_customer")
        self.assertEqual(payload["bot_id"], 1)


@override_settings(
    CACHES={
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "bot-gateway-tests",
        }
    }
)
class RatesCacheTests(TestCase):
    def setUp(self):
        cache.clear()

    @patch("bot_gateway.services.formatter.build_all_formatted_captions")
    @patch("bot_gateway.services.rates_cache.build_prices_public_snapshot")
    def test_refresh_and_get(self, mock_snapshot, mock_captions):
        mock_snapshot.return_value = {"categories": [], "special_prices": []}
        mock_captions.return_value = {}
        refresh_live_rates_cache("test")
        data = get_cached_live_rates()
        self.assertEqual(data, {"categories": [], "special_prices": []})
        self.assertIsNotNone(cache.get(CACHE_KEY))
