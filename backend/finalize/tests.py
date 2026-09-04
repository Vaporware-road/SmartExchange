from django.test import TestCase, override_settings
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.exceptions import ValidationError as DRFValidationError
from unittest.mock import patch, MagicMock
from decimal import Decimal
from celery.exceptions import TimeoutError as CeleryTimeoutError

from accounts.models import CustomUser
from category.models import Category, Currency, PriceType
from change_price.models import PriceHistory
from finalize.api_views import FinalizeCategoryAPIView, FinalizeSpecialPriceAPIView
from special_price.models import SpecialPriceHistory, SpecialPricePair, SpecialPriceType
from finalize.services import ExternalAPIService
from price_publisher.services.publisher import PricePublisherService
from telegram_app.models import TelegramBot, TelegramChannel
from template_editor.models import Template
from template_editor.api_views import _validate_telegram_buttons_json


@override_settings(
    EXTERNAL_API_URL='https://test.example/rates',
    EXTERNAL_API_KEY='test-api-key'
)
class ExternalAPIServiceTest(TestCase):
    """Test cases for ExternalAPIService"""

    def setUp(self):
        """Set up test data"""
        # Create currencies
        self.usdt_currency, _ = Currency.objects.get_or_create(
            code='USDT',
            defaults={'name': 'Tether', 'symbol': 'USDT'}
        )
        self.irr_currency, _ = Currency.objects.get_or_create(
            code='IRR',
            defaults={'name': 'Iranian Rial', 'symbol': 'IRR'}
        )
        self.gbp_currency, _ = Currency.objects.get_or_create(
            code='GBP',
            defaults={'name': 'British Pound', 'symbol': 'GBP'}
        )

        # Create category
        self.tether_category = Category.objects.create(
            name='تتر',
            description='Tether category'
        )

        # Create price types
        self.usdt_sell_price_type = PriceType.objects.create(
            category=self.tether_category,
            name='فروش تتر تومان',
            source_currency=self.usdt_currency,
            target_currency=self.irr_currency,
            trade_type='sell'
        )

        self.usdt_buy_price_type = PriceType.objects.create(
            category=self.tether_category,
            name='خرید تتر تومان',
            source_currency=self.usdt_currency,
            target_currency=self.irr_currency,
            trade_type='buy'
        )

    @patch('finalize.services.requests.post')
    def test_send_usdt_sell_price_150000(self, mock_post):
        """Test sending USDT sell price of 150000 toman"""
        mock_post_response = MagicMock()
        mock_post_response.status_code = 200
        mock_post.return_value = mock_post_response

        price_history = PriceHistory.objects.create(
            price_type=self.usdt_sell_price_type,
            price=Decimal('150000.00')
        )
        price_items = [(self.usdt_sell_price_type, price_history)]

        results = ExternalAPIService.send_finalized_prices(price_items)

        self.assertIn("sent", results)
        self.assertIn("failed", results)
        self.assertIn("skipped", results)

        post_calls = mock_post.call_args_list
        usdt_sell_called = False
        usdt_sell_rate = None
        for call in post_calls:
            payload = call[1].get('json', {})
            if payload.get('currency') == 'USDT_SELL':
                usdt_sell_called = True
                usdt_sell_rate = payload.get('rate')
                break

        self.assertTrue(usdt_sell_called, "USDT_SELL should be sent to API")
        self.assertEqual(usdt_sell_rate, 150000.0)

        self.assertEqual(len(results["sent"]), 1)
        self.assertEqual(results["sent"][0]["currency"], "USDT_SELL")
        self.assertEqual(results["sent"][0]["rate"], 150000.0)

    @patch('finalize.services.requests.post')
    def test_send_usdt_buy_and_sell_prices(self, mock_post):
        """Test sending both USDT buy and sell prices"""
        mock_post_response = MagicMock()
        mock_post_response.status_code = 200
        mock_post.return_value = mock_post_response

        # Create price histories
        buy_price_history = PriceHistory.objects.create(
            price_type=self.usdt_buy_price_type,
            price=Decimal('148000.00')
        )

        sell_price_history = PriceHistory.objects.create(
            price_type=self.usdt_sell_price_type,
            price=Decimal('150000.00')
        )

        # Prepare price items
        price_items = [
            (self.usdt_buy_price_type, buy_price_history),
            (self.usdt_sell_price_type, sell_price_history)
        ]

        # Send finalized prices
        results = ExternalAPIService.send_finalized_prices(price_items)

        # Check POST calls
        post_calls = mock_post.call_args_list
        rates_sent = {}

        for call in post_calls:
            args, kwargs = call
            payload = kwargs.get('json', {})
            currency = payload.get('currency')
            rate = payload.get('rate')
            if currency:
                rates_sent[currency] = rate

        # Verify both rates were sent
        self.assertIn("USDT_BUY", rates_sent)
        self.assertIn("USDT_SELL", rates_sent)
        self.assertEqual(rates_sent["USDT_BUY"], 148000.0)
        self.assertEqual(rates_sent["USDT_SELL"], 150000.0)

    @patch('finalize.services.requests.post')
    def test_usdt_sell_price_not_overwritten_by_existing_api_value(self, mock_post):
        """Test that USDT_SELL is sent with value from price_items (no API fetch)"""
        mock_post_response = MagicMock()
        mock_post_response.status_code = 200
        mock_post.return_value = mock_post_response

        # Create price history with valid price
        sell_price_history = PriceHistory.objects.create(
            price_type=self.usdt_sell_price_type,
            price=Decimal('150000.00')
        )

        # Prepare price items
        price_items = [
            (self.usdt_sell_price_type, sell_price_history)
        ]

        # Send finalized prices
        results = ExternalAPIService.send_finalized_prices(price_items)

        # Check that USDT_SELL was sent with the correct value (150000), not 1
        post_calls = mock_post.call_args_list
        usdt_sell_rate = None

        for call in post_calls:
            args, kwargs = call
            payload = kwargs.get('json', {})
            if payload.get('currency') == 'USDT_SELL':
                usdt_sell_rate = payload.get('rate')
                break

        # Verify the correct rate was sent
        self.assertIsNotNone(usdt_sell_rate, "USDT_SELL should be sent")
        self.assertEqual(
            usdt_sell_rate, 
            150000.0, 
            f"USDT_SELL rate should be 150000.0, not {usdt_sell_rate}"
        )
        self.assertNotEqual(
            usdt_sell_rate, 
            1.0, 
            "USDT_SELL rate should not be 1.0 (invalid existing value)"
        )

    @patch('finalize.services.requests.post')
    def test_usdt_gbp_pair_skipped(self, mock_post):
        """Test that USDT/GBP pairs are NOT sent (only USDT/IRR)"""
        usdt_gbp_type = PriceType.objects.create(
            category=self.tether_category,
            name='تتر به پوند',
            source_currency=self.usdt_currency,
            target_currency=self.gbp_currency,
            trade_type='sell'
        )
        price_history = PriceHistory.objects.create(
            price_type=usdt_gbp_type,
            price=Decimal('0.79')
        )
        price_items = [(usdt_gbp_type, price_history)]

        results = ExternalAPIService.send_finalized_prices(price_items)

        self.assertEqual(len(results["sent"]), 0, "USDT/GBP should not be sent")
        self.assertGreater(len(results["skipped"]), 0)
        self.assertEqual(mock_post.call_count, 0, "No POST for USDT/GBP")

    @patch('finalize.services.requests.post')
    def test_gbp_account_only_sent(self, mock_post):
        """Test that only GBP account (حسابی) is sent, not cash"""
        gbp_account_type = PriceType.objects.create(
            category=Category.objects.create(name='پوند', description='Pound'),
            name='خرید حسابی',
            source_currency=self.gbp_currency,
            target_currency=self.irr_currency,
            trade_type='buy'
        )
        gbp_cash_type = PriceType.objects.create(
            category=gbp_account_type.category,
            name='خرید نقدی',
            source_currency=self.gbp_currency,
            target_currency=self.irr_currency,
            trade_type='sell'
        )
        mock_post.return_value = MagicMock(status_code=200)

        price_items = [
            (gbp_account_type, PriceHistory.objects.create(price_type=gbp_account_type, price=Decimal('163000'))),
            (gbp_cash_type, PriceHistory.objects.create(price_type=gbp_cash_type, price=Decimal('162000')))
        ]

        results = ExternalAPIService.send_finalized_prices(price_items)

        self.assertEqual(len(results["sent"]), 1)
        self.assertEqual(results["sent"][0]["currency"], "GBP_BUY")
        self.assertEqual(results["sent"][0]["rate"], 163000.0)
        self.assertEqual(mock_post.call_count, 1, "Only GBP account sent")


class PublisherTemplateSelectionTest(TestCase):
    def setUp(self):
        self.category_a = Category.objects.create(name="یورو")
        self.category_b = Category.objects.create(name="تتر")
        self.template_a = Template.objects.create(
            name="eur-template",
            category=self.category_a,
            config_json={"widgets": [{"type": "text", "x": 0, "y": 0, "width": 1, "height": 1}]},
        )
        self.template_b = Template.objects.create(
            name="usdt-template",
            category=self.category_b,
            config_json={"widgets": [{"type": "text", "x": 0, "y": 0, "width": 1, "height": 1}]},
        )
        self.service = PricePublisherService()

    def test_ignores_pinned_template_from_other_category(self):
        self.category_a.last_used_template = self.template_b
        self.category_a.save(update_fields=["last_used_template", "updated_at"])

        selected = self.service._select_next_template_editor_for_category(self.category_a)

        self.assertEqual(selected.category_id, self.category_a.id)
        self.assertEqual(selected.id, self.template_a.id)


class FinalizeCategorySoftFeedbackTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = CustomUser.objects.create_user(
            username="manager1",
            password="x",
            role=CustomUser.ROLE_MANAGEMENT,
        )
        self.bot = TelegramBot.objects.create(name="bot", token="token")
        self.channel = TelegramChannel.objects.create(
            bot=self.bot, name="main", chat_id="@channel"
        )
        self.category = Category.objects.create(name="پوند")
        self.irr, _ = Currency.objects.get_or_create(
            code="IRR", defaults={"name": "Rial"}
        )
        self.gbp, _ = Currency.objects.get_or_create(
            code="GBP", defaults={"name": "Pound"}
        )
        self.price_type = PriceType.objects.create(
            category=self.category,
            name="خرید نقدی",
            source_currency=self.gbp,
            target_currency=self.irr,
            trade_type="buy",
        )
        self.history = PriceHistory.objects.create(
            price_type=self.price_type,
            price=Decimal("12345"),
        )

    @patch("finalize.api_views.publish_category_prices_task.apply_async")
    def test_category_finalize_fails_when_template_contract_invalid(self, mock_apply_async):
        async_result = MagicMock()
        async_result.get.return_value = {
            "success": False,
            "response": "Template contract violation",
            "caption": "",
            "publish_path": "template_contract_error",
            "render_fallback_reason": "template_missing_or_invalid",
        }
        mock_apply_async.return_value = async_result

        request = self.factory.post(
            f"/api/finalize/category/{self.category.id}/",
            {"channel_id": self.channel.id, "notes": ""},
            format="json",
        )
        force_authenticate(request, user=self.user)

        response = FinalizeCategoryAPIView.as_view()(request, category_id=self.category.id)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["publish_path"], "template_contract_error")
        self.assertEqual(response.data["render_fallback_reason"], "template_missing_or_invalid")
        self.assertIn("Template contract", response.data["telegram_response"])

    @patch("finalize.api_views.publish_category_prices_task.apply_async")
    def test_publish_timeout_returns_controlled_failure(self, mock_apply_async):
        async_result = MagicMock()
        async_result.id = "task-timeout-1"
        async_result.get.side_effect = CeleryTimeoutError("timeout")
        mock_apply_async.return_value = async_result

        request = self.factory.post(
            f"/api/finalize/category/{self.category.id}/",
            {"channel_id": self.channel.id, "notes": ""},
            format="json",
        )
        force_authenticate(request, user=self.user)

        response = FinalizeCategoryAPIView.as_view()(request, category_id=self.category.id)

        self.assertEqual(response.status_code, 201)
        self.assertFalse(response.data["message_sent"])
        self.assertEqual(response.data["publish_path"], "worker_timeout")
        self.assertEqual(response.data["render_fallback_reason"], "task_timeout")
        self.assertIn("timed out", response.data["telegram_response"].lower())


class InstagramFinalizeEnqueueTest(TestCase):
    """Instagram post-finalize task is scheduled on_commit for single category/special finalize."""

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = CustomUser.objects.create_user(
            username="manager_ig",
            password="x",
            role=CustomUser.ROLE_MANAGEMENT,
        )
        self.bot = TelegramBot.objects.create(name="bot_ig", token="token_ig")
        self.channel = TelegramChannel.objects.create(
            bot=self.bot, name="main_ig", chat_id="@channel_ig"
        )
        self.category = Category.objects.create(name="پوند_ig")
        self.irr, _ = Currency.objects.get_or_create(
            code="IRR", defaults={"name": "Rial"}
        )
        self.gbp, _ = Currency.objects.get_or_create(
            code="GBP", defaults={"name": "Pound"}
        )
        self.price_type = PriceType.objects.create(
            category=self.category,
            name="خرید نقدی",
            source_currency=self.gbp,
            target_currency=self.irr,
            trade_type="buy",
        )
        self.history = PriceHistory.objects.create(
            price_type=self.price_type,
            price=Decimal("99999"),
        )
        self.spt = SpecialPriceType.objects.create(
            name="Special IG Type",
            source_currency=self.gbp,
            target_currency=self.irr,
            trade_type="buy",
        )
        self.pair = SpecialPricePair.objects.create(
            special_price_type=self.spt,
            name="Main pair",
            source_currency=self.gbp,
            target_currency=self.irr,
            trade_type="buy",
        )
        self.sp_history = SpecialPriceHistory.objects.create(
            special_price_type=self.spt,
            pair=self.pair,
            price=Decimal("111"),
        )

    @patch("finalize.api_views.schedule_instagram_post_finalize")
    @patch("finalize.api_views.is_ready_for_publish", return_value=True)
    @patch("finalize.api_views.publish_category_prices_task.apply_async")
    def test_category_finalize_schedules_instagram_on_commit(
        self, mock_apply_async, _mock_ig_configured, mock_schedule_ig
    ):
        async_result = MagicMock()
        async_result.get.return_value = {
            "success": True,
            "response": "ok",
            "caption": "cap",
            "publish_path": "ok",
            "render_fallback_reason": None,
            "template_id": 1,
        }
        mock_apply_async.return_value = async_result

        request = self.factory.post(
            f"/api/finalize/category/{self.category.id}/",
            {"channel_id": self.channel.id, "notes": ""},
            format="json",
        )
        force_authenticate(request, user=self.user)

        with self.captureOnCommitCallbacks(execute=True):
            response = FinalizeCategoryAPIView.as_view()(request, category_id=self.category.id)

        self.assertEqual(response.status_code, 201)
        mock_schedule_ig.assert_called_once_with(
            category_ids=[self.category.id],
            special_price_history_ids=[],
            theme="dark",
        )

    @patch("finalize.api_views.schedule_instagram_post_finalize")
    @patch("finalize.api_views.is_ready_for_publish", return_value=False)
    @patch("finalize.api_views.publish_category_prices_task.apply_async")
    def test_category_finalize_does_not_schedule_instagram_when_not_configured(
        self, mock_apply_async, _mock_ig_off, mock_schedule_ig
    ):
        async_result = MagicMock()
        async_result.get.return_value = {
            "success": True,
            "response": "ok",
            "caption": "cap",
            "publish_path": "ok",
            "render_fallback_reason": None,
            "template_id": 1,
        }
        mock_apply_async.return_value = async_result

        request = self.factory.post(
            f"/api/finalize/category/{self.category.id}/",
            {"channel_id": self.channel.id, "notes": ""},
            format="json",
        )
        force_authenticate(request, user=self.user)

        with self.captureOnCommitCallbacks(execute=True):
            response = FinalizeCategoryAPIView.as_view()(request, category_id=self.category.id)

        self.assertEqual(response.status_code, 201)
        mock_schedule_ig.assert_not_called()

    @patch("finalize.api_views.schedule_instagram_post_finalize")
    @patch("finalize.api_views.is_ready_for_publish", return_value=True)
    @patch("finalize.api_views.publish_special_price_task.apply_async")
    def test_special_price_finalize_schedules_instagram_on_commit(
        self, mock_apply_async, _mock_ig_configured, mock_schedule_ig
    ):
        async_result = MagicMock()
        async_result.get.return_value = {
            "success": True,
            "response": "ok",
            "caption": "cap",
            "publish_path": "ok",
            "render_fallback_reason": None,
            "template_id": 1,
        }
        mock_apply_async.return_value = async_result

        request = self.factory.post(
            f"/api/finalize/special-price/{self.sp_history.id}/",
            {"channel_id": self.channel.id, "notes": ""},
            format="json",
        )
        force_authenticate(request, user=self.user)

        with self.captureOnCommitCallbacks(execute=True):
            response = FinalizeSpecialPriceAPIView.as_view()(
                request, special_price_history_id=self.sp_history.id
            )

        self.assertEqual(response.status_code, 201)
        mock_schedule_ig.assert_called_once_with(
            category_ids=[],
            special_price_history_ids=[self.sp_history.id],
            theme="dark",
        )


class TelegramButtonsValidationTest(TestCase):
    def test_rejects_invalid_button_url(self):
        with self.assertRaises(DRFValidationError):
            _validate_telegram_buttons_json(
                [[{"text": "bad", "url": "javascript:alert(1)"}]]
            )

    def test_accepts_valid_buttons(self):
        _validate_telegram_buttons_json(
            [[{"text": "site", "url": "https://example.com"}]]
        )
