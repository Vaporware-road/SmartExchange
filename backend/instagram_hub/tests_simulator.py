"""
End-to-end Instagram pipeline simulator (mocked Meta API).

Run: python manage.py test instagram_hub.tests_simulator -v 2
"""

from decimal import Decimal
from io import BytesIO
from pathlib import Path
from unittest.mock import MagicMock, patch

from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from rest_framework.test import APIRequestFactory, force_authenticate

from category.models import Category, Currency, PriceType
from change_price.models import PriceHistory
from instagram_hub.models import InstagramConfig, InstagramPublicationLog
from instagram_hub.services.instagram_config import is_instagram_configured, is_ready_for_publish
from instagram_hub.tasks import (
    _feed_caption_with_config_extras,
    run_post_finalize_to_instagram,
)
from instagram_hub.utils import path_to_public_url

User = get_user_model()


class InstagramPipelineSimulator(TestCase):
    """Simulate config → image → publish → log for category finalize."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="ig_sim",
            password="x",
            role=getattr(User, "ROLE_MANAGEMENT", "management"),
        )
        self.factory = APIRequestFactory()
        self.irr, _ = Currency.objects.get_or_create(code="IRR", defaults={"name": "Rial"})
        self.usd, _ = Currency.objects.get_or_create(code="USD", defaults={"name": "Dollar"})
        self.category = Category.objects.create(name="دلار")
        self.price_type = PriceType.objects.create(
            category=self.category,
            name="خرید نقدی",
            source_currency=self.usd,
            target_currency=self.irr,
            trade_type="buy",
        )
        self.history = PriceHistory.objects.create(
            price_type=self.price_type,
            price=Decimal("58500"),
        )
        self.config = InstagramConfig.objects.create(
            name="Sim Config",
            is_active=True,
            app_id="123456789",
            ig_user_id="17841400000000000",
            feed_caption_suffix="تماس: 021-12345678",
            feed_hashtags="#صرافی #نرخ",
        )
        self.config.set_app_secret("secret")
        self.config.set_access_token("long-lived-token")
        self.config.save()

    @override_settings(INSTAGRAM_BASE_URL="https://panel.example.com")
    def test_step1_config_detection(self):
        self.assertTrue(is_instagram_configured())
        self.assertTrue(is_ready_for_publish())
        self.config.ig_user_id = ""
        self.config.save(update_fields=["ig_user_id"])
        self.assertFalse(is_instagram_configured())

    @override_settings(INSTAGRAM_BASE_URL="")
    def test_step1b_missing_base_url_not_ready(self):
        from instagram_hub.services.instagram_config import is_ready_for_publish

        self.assertTrue(is_instagram_configured())
        self.assertFalse(is_ready_for_publish())

    def test_step2_caption_extras(self):
        cap = _feed_caption_with_config_extras("دلار")
        self.assertIn("دلار", cap)
        self.assertIn("021-12345678", cap)
        self.assertIn("#صرافی", cap)

    @override_settings(
        MEDIA_ROOT="/tmp/ig_sim_media",
        INSTAGRAM_BASE_URL="https://panel.example.com",
        MEDIA_URL="/media/",
    )
    def test_step3_image_generation_and_public_url(self):
        from instagram_hub.services.image_generator import generate_price_images

        entries = [{"title": "خرید نقدی", "price": "58500"}]
        result = generate_price_images(
            price_entries=entries,
            theme="dark",
            category_title="دلار",
        )
        self.assertIsNotNone(result)
        post_path = result["post_path"]
        story_path = result["story_path"]
        self.assertTrue(Path(post_path).exists())
        self.assertTrue(Path(story_path).exists())

        post_url = path_to_public_url(post_path)
        self.assertTrue(post_url.startswith("https://panel.example.com/media/"))
        self.assertIn("generated_instagram", post_url)

        from PIL import Image

        with Image.open(post_path) as img:
            self.assertEqual(img.size, (1080, 1080))
        with Image.open(story_path) as img:
            self.assertEqual(img.size, (1080, 1920))

    @patch("instagram_hub.services.instagram_api.publish_media_container")
    @patch("instagram_hub.services.instagram_api.create_media_container")
    @override_settings(
        MEDIA_ROOT="/tmp/ig_sim_media",
        INSTAGRAM_BASE_URL="https://panel.example.com",
    )
    def test_step4_full_finalize_publish_pipeline(self, mock_create, mock_publish):
        mock_create.return_value = {
            "success": True,
            "container_id": "container_123",
            "message": "ok",
        }
        mock_publish.return_value = {
            "success": True,
            "media_id": "media_456",
            "message": "Published",
        }

        run_post_finalize_to_instagram(
            category_ids=[self.category.id],
            special_price_history_ids=[],
            theme="dark",
        )

        self.assertEqual(mock_create.call_count, 2)
        self.assertEqual(mock_publish.call_count, 2)

        logs = InstagramPublicationLog.objects.all()
        self.assertEqual(logs.count(), 2)
        self.assertTrue(all(l.success for l in logs))
        kinds = {l.kind for l in logs}
        self.assertEqual(kinds, {InstagramPublicationLog.KIND_FEED, InstagramPublicationLog.KIND_STORY})

    def test_step5_preview_api(self):
        from instagram_hub.api_views import PreviewAPIView

        request = self.factory.post(
            "/api/instagram-hub/preview/",
            {"category_ids": [self.category.id], "theme": "dark"},
            format="json",
        )
        force_authenticate(request, user=self.user)
        response = PreviewAPIView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data.get("post_url"))
        self.assertTrue(response.data.get("story_url"))

    def test_step6_config_api(self):
        from instagram_hub.api_views import ConfigAPIView

        request = self.factory.get("/api/instagram-hub/config/")
        force_authenticate(request, user=self.user)
        response = ConfigAPIView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["has_app_id"])
        self.assertTrue(response.data["has_token"])
        self.assertIn("connect_url", response.data)

    @patch("instagram_hub.services.instagram_oauth.requests.get")
    def test_step7_oauth_exchange(self, mock_get):
        from instagram_hub.services.instagram_oauth import perform_full_oauth_exchange

        def fake_get(url, params=None, timeout=None):
            resp = MagicMock()
            resp.ok = True
            if "oauth/access_token" in url and params.get("code"):
                resp.json.return_value = {"access_token": "short", "expires_in": 3600}
            elif "oauth/access_token" in url and params.get("grant_type") == "fb_exchange_token":
                resp.json.return_value = {"access_token": "long", "expires_in": 5184000}
            elif url.endswith("/me/accounts"):
                resp.json.return_value = {
                    "data": [
                        {
                            "id": "page1",
                            "name": "Page",
                            "instagram_business_account": {"id": "ig999"},
                        }
                    ]
                }
            else:
                resp.ok = False
                resp.json.return_value = {"error": {"message": "unexpected"}}
            return resp

        mock_get.side_effect = fake_get
        result = perform_full_oauth_exchange(
            code="auth_code",
            redirect_uri="https://panel.example.com/instagram-hub/callback/",
            config=self.config,
        )
        self.assertTrue(result["success"])
        self.config.refresh_from_db()
        self.assertEqual(self.config.ig_user_id, "ig999")
        self.assertTrue(self.config.get_decrypted_token())

    @patch("instagram_hub.services.instagram_oauth.requests.get")
    def test_step7b_oauth_fails_without_business_account(self, mock_get):
        from instagram_hub.services.instagram_oauth import perform_full_oauth_exchange

        def fake_get(url, params=None, timeout=None):
            resp = MagicMock()
            resp.ok = True
            if "oauth/access_token" in url and params.get("code"):
                resp.json.return_value = {"access_token": "short", "expires_in": 3600}
            elif "oauth/access_token" in url and params.get("grant_type") == "fb_exchange_token":
                resp.json.return_value = {"access_token": "long", "expires_in": 5184000}
            elif url.endswith("/me/accounts"):
                resp.json.return_value = {"data": [{"id": "page1", "name": "Page"}]}
            else:
                resp.ok = False
                resp.json.return_value = {"error": {"message": "unexpected"}}
            return resp

        mock_get.side_effect = fake_get
        old_token = self.config.get_decrypted_token()
        result = perform_full_oauth_exchange(
            code="auth_code",
            redirect_uri="https://panel.example.com/instagram-hub/callback/",
            config=self.config,
        )
        self.assertFalse(result["success"])
        self.config.refresh_from_db()
        self.assertEqual(self.config.get_decrypted_token(), old_token)
