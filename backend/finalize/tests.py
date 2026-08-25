from django.test import TestCase
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
from price_publisher.services.publisher import PricePublisherService
from telegram_app.models import TelegramBot, TelegramChannel
from template_editor.models import Template
from template_editor.api_views import _validate_telegram_buttons_json


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
    @patch("finalize.api_views.is_instagram_configured", return_value=True)
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
    @patch("finalize.api_views.is_instagram_configured", return_value=False)
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
    @patch("finalize.api_views.is_instagram_configured", return_value=True)
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
