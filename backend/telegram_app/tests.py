from io import BytesIO
from unittest.mock import AsyncMock, patch

from django.core.cache import cache
from django.db.utils import OperationalError
from django.test import TestCase
from rest_framework.test import APITestCase
from unittest.mock import patch

from accounts.models import CustomUser
from setting.models import SiteSettings
from telegram_app.services.telegram_client import TelegramService


class TelegramServiceOptionalCaptionTest(TestCase):
    @patch("telegram_app.services.telegram_client.Bot")
    def test_send_photo_without_caption_uses_no_parse_mode(self, bot_cls):
        bot_instance = bot_cls.return_value
        bot_instance.send_photo = AsyncMock(return_value=None)

        service = TelegramService("token")
        image_stream = BytesIO(b"fake image bytes")
        image_stream.name = "prices.png"

        ok, _ = service.send_photo(chat_id="@channel", photo=image_stream, caption="", buttons=[])

        self.assertTrue(ok)
        bot_instance.send_photo.assert_awaited_once()
        call = bot_instance.send_photo.await_args
        self.assertIsNone(call.kwargs.get("parse_mode"))


class AutomationSettingsApiTests(APITestCase):
    """GET/PUT /api/telegram/automation-settings/ must not 500 (regression: stale SiteSettings cache)."""

    def setUp(self):
        cache.delete("site_settings")
        self.user = CustomUser.objects.create_user(
            username="automation_tester",
            password="pass12345",
            role=CustomUser.ROLE_EMPLOYEE,
        )

    def test_get_automation_settings_ok(self):
        self.client.force_authenticate(self.user)
        r = self.client.get("/api/telegram/automation-settings/")
        self.assertEqual(r.status_code, 200, r.content)
        self.assertIn("auto_post_on_update", r.json())
        self.assertIsInstance(r.json()["auto_post_on_update"], bool)

    def test_put_automation_settings_updates_flag(self):
        self.client.force_authenticate(self.user)
        r = self.client.put("/api/telegram/automation-settings/", {"auto_post_on_update": True}, format="json")
        self.assertEqual(r.status_code, 200, r.content)
        self.assertTrue(r.json()["auto_post_on_update"])
        self.assertTrue(SiteSettings.objects.get(pk=1).auto_post_on_update)

    @patch(
        "setting.models.SiteSettings.load",
        side_effect=OperationalError("no such column: setting_sitesettings.prices_webhook_url"),
    )
    def test_get_automation_settings_returns_200_when_site_settings_db_unreadable(self, _mock_load):
        """Regression: avoid 500 when ORM cannot read SiteSettings (stale schema)."""
        self.client.force_authenticate(self.user)
        r = self.client.get("/api/telegram/automation-settings/")
        self.assertEqual(r.status_code, 200, r.content)
        data = r.json()
        self.assertFalse(data["auto_post_on_update"])
        self.assertTrue(data.get("degraded"))
        self.assertIn("migrate", (data.get("detail") or "").lower())

    @patch(
        "setting.models.SiteSettings.load",
        side_effect=OperationalError("no such column: setting_sitesettings.prices_webhook_url"),
    )
    def test_put_automation_settings_returns_400_when_site_settings_db_unreadable(self, _mock_load):
        self.client.force_authenticate(self.user)
        r = self.client.put("/api/telegram/automation-settings/", {"auto_post_on_update": True}, format="json")
        self.assertEqual(r.status_code, 400, r.content)
        self.assertIn("migrate", (r.json().get("detail") or "").lower())
