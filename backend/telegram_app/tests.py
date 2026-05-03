from io import BytesIO
from unittest.mock import AsyncMock, patch

from django.test import TestCase

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
