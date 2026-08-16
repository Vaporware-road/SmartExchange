from io import BytesIO
from unittest.mock import AsyncMock, MagicMock, patch
import logging

from django.core.cache import cache
from django.db.utils import OperationalError
from django.test import TestCase
from rest_framework.test import APITestCase

from accounts.models import CustomUser
from setting.models import SiteSettings
from telegram_app.services.conversation import (
    CB_ALERT_CONFIRM,
    CB_ALERT_DEC,
    CB_ALERT_EDIT,
    CB_ALERT_INC,
    CB_EXCH_CONFIRM,
    CB_EXCH_EDIT,
    CB_MENU_EXCHANGE,
    CB_MENU_NOTIFICATIONS,
    CB_MENU_PROFILE,
    CB_PROFILE_ID,
    ConversationEngine,
    MAIN_MENU_BUTTONS,
    MAIN_MENU_TEXT,
)
from telegram_app.services.dispatcher import process_update_payload, upsert_customer_profile
from telegram_app.services.telegram_client import TelegramService
from telegram_app.services.ttl_parse import parse_ttl_minutes
from telegram_app.services.admin_notify import (
    notify_staff_of_exchange_request,
    staff_notify_recipients,
)
from telegram_app.services.alert_checker import (
    alert_in_cooldown,
    alert_should_fire,
    check_price_alerts,
)
from telegram_app.models import (
    BotSession,
    CustomerProfile,
    ExchangeRequest,
    PriceAlert,
    TelegramBot,
)
from telegram_app.services import currency_catalog
from decimal import Decimal
from datetime import timedelta
from django.utils import timezone
from category.models import Category, Currency, PriceType
from change_price.models import PriceHistory


class CurrencyCatalogTests(TestCase):
    def setUp(self):
        currency_catalog.clear_currency_cache()

    def tearDown(self):
        currency_catalog.clear_currency_cache()

    def test_catalog_loads_and_paginates(self):
        currencies = currency_catalog.load_currencies()
        self.assertGreater(len(currencies), 100)

        usd = currency_catalog.get_currency("usd")
        self.assertIsNotNone(usd)
        self.assertEqual(usd.code, "USD")
        self.assertEqual(usd.name, "US Dollar")

        page_size = 8
        first, page_index, has_prev, has_next = currency_catalog.paginate(
            page=0, page_size=page_size
        )
        self.assertEqual(page_index, 0)
        self.assertFalse(has_prev)
        self.assertTrue(has_next)
        self.assertEqual(len(first), page_size)
        self.assertEqual(first[0].code, currencies[0].code)

        second, page_index, has_prev, has_next = currency_catalog.paginate(
            page=1, page_size=page_size
        )
        self.assertEqual(page_index, 1)
        self.assertTrue(has_prev)
        self.assertTrue(has_next)
        self.assertEqual(len(second), page_size)
        self.assertNotEqual(first[0].code, second[0].code)

        next_token = currency_catalog.encode_next_callback(0)
        prev_token = currency_catalog.encode_prev_callback(1)
        self.assertEqual(
            currency_catalog.decode_catalog_callback(next_token),
            currency_catalog.CatalogCallback(kind="page", page=1),
        )
        self.assertEqual(
            currency_catalog.decode_catalog_callback(prev_token),
            currency_catalog.CatalogCallback(kind="page", page=0),
        )

        select_token = currency_catalog.encode_select_callback("eur")
        decoded = currency_catalog.decode_catalog_callback(select_token)
        self.assertEqual(decoded, currency_catalog.CatalogCallback(kind="select", code="EUR"))

    def test_guess_currency_handles_typos_and_names(self):
        self.assertEqual(currency_catalog.guess_currency("usd").code, "USD")
        self.assertEqual(currency_catalog.guess_currency("US Doller").code, "USD")
        self.assertEqual(currency_catalog.guess_currency("euro").code, "EUR")
        self.assertIsNone(currency_catalog.guess_currency("zzzznotacurrency"))

    def test_top_exchanged_falls_back_to_defaults(self):
        top = currency_catalog.top_exchanged_currencies(10)
        self.assertEqual(len(top), 10)
        codes = {c.code for c in top}
        self.assertIn("USD", codes)
        self.assertIn("EUR", codes)

    def test_top_exchanged_ranks_by_request_history(self):
        customer = CustomerProfile.objects.create(telegram_user_id=55)
        bot = TelegramBot.objects.create(name="C", token="1:x", is_active=True)
        for _ in range(3):
            ExchangeRequest.objects.create(
                customer=customer,
                bot=bot,
                source_currency="TRY",
                target_currency="AED",
                amount=Decimal("1"),
                price_at_request=Decimal("1"),
                ttl_minutes=30,
            )
        currency_catalog.clear_currency_cache()
        top = currency_catalog.top_exchanged_currencies(10)
        codes = [c.code for c in top]
        self.assertTrue(codes.index("TRY") < codes.index("USD") or codes[0] in {"TRY", "AED"})
        self.assertIn("TRY", codes[:4])
        self.assertIn("AED", codes[:4])


class ReplyKeyboardBuilderTests(TestCase):
    def test_build_reply_keyboard_accepts_flat_row_dicts(self):
        # Regression: CANCEL_ROW was once a single row passed as the whole keyboard.
        markup = TelegramService._build_reply_keyboard([{"text": "Cancel"}])
        self.assertIsNotNone(markup)
        self.assertEqual(markup.keyboard[0][0].text, "Cancel")

    def test_build_reply_keyboard_accepts_string_cells(self):
        markup = TelegramService._build_reply_keyboard([["USD", "EUR"], ["Cancel"]])
        self.assertEqual(markup.keyboard[0][0].text, "USD")
        self.assertEqual(markup.keyboard[1][0].text, "Cancel")


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
        # Intentional OperationalError: mute logger.exception noise from the safe reader.
        logging.disable(logging.CRITICAL)
        try:
            r = self.client.get("/api/telegram/automation-settings/")
        finally:
            logging.disable(logging.NOTSET)
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
        logging.disable(logging.CRITICAL)
        try:
            r = self.client.put(
                "/api/telegram/automation-settings/",
                {"auto_post_on_update": True},
                format="json",
            )
        finally:
            logging.disable(logging.NOTSET)
        self.assertEqual(r.status_code, 400, r.content)
        self.assertIn("migrate", (r.json().get("detail") or "").lower())


class ConversationEnginePhase2Tests(TestCase):
    def setUp(self):
        self.bot = TelegramBot.objects.create(name="Customer Bot", token="123:ABC", is_active=True)
        self.engine = ConversationEngine(self.bot)
        self.session = self.engine.get_or_create_session(424242)

    def test_start_returns_main_menu_with_three_buttons(self):
        out = self.engine.process_update(self.session, text="/start")
        self.session.refresh_from_db()
        self.assertEqual(self.session.state, BotSession.State.MAIN_MENU)
        self.assertEqual(out["text"], MAIN_MENU_TEXT)
        self.assertEqual(out.get("keyboard"), "reply")
        self.assertFalse(out.get("remove_keyboard"))
        self.assertFalse(out["edit_previous"])
        self.assertEqual(out["buttons"], MAIN_MENU_BUTTONS)
        labels = {btn["text"] for row in out["buttons"] for btn in row}
        self.assertEqual(
            labels,
            {"Customer profile", "Registering for exchange", "Notification System"},
        )

    def test_menu_commands_open_profile_exchange_and_alerts(self):
        self.engine.process_update(self.session, text="/start")
        CustomerProfile.objects.create(telegram_user_id=424242, tag="vip")

        out = self.engine.process_update(self.session, text="/profile")
        self.assertIn("Tag: vip", out["text"])
        self.assertEqual(self.session.state, BotSession.State.PROFILE)

        out = self.engine.process_update(self.session, text="/exchange")
        self.assertIn("source currency", out["text"].lower())
        self.assertIn("top 10", out["text"].lower())
        self.assertEqual(self.session.state, BotSession.State.EXCHANGE_SOURCE)
        labels = {b["text"] for row in out["buttons"] for b in row}
        self.assertIn("USD", labels)
        self.assertIn("Cancel", labels)

        # Typed typo should resolve and advance to target pick.
        out = self.engine.process_update(self.session, text="dolr")
        self.assertEqual(self.session.state, BotSession.State.EXCHANGE_TARGET)
        self.assertIn("USD", out["text"])
        self.assertIn("target", out["text"].lower())

        out = self.engine.process_update(self.session, text="/notifications")
        self.assertIn("Notification System", out["text"])
        self.assertEqual(self.session.state, BotSession.State.ALERT_MENU)

        out = self.engine.process_update(self.session, text="Price increase Alert")
        self.assertEqual(self.session.state, BotSession.State.ALERT_SOURCE)
        self.assertIn("top 10", out["text"].lower())
        labels = {b["text"] for row in out["buttons"] for b in row}
        self.assertIn("USD", labels)
        self.assertIn("Cancel", labels)
        self.assertNotIn("Next", labels)

        out = self.engine.process_update(self.session, text="dolr")
        self.assertEqual(self.session.state, BotSession.State.ALERT_TARGET)
        self.assertIn("USD", out["text"])
        self.assertIn("top 10", out["text"].lower())

    def test_legacy_reply_labels_still_open_flows(self):
        self.engine.process_update(self.session, text="/start")
        out = self.engine.process_update(self.session, text="Registering for exchange")
        self.assertEqual(self.session.state, BotSession.State.EXCHANGE_SOURCE)
        out = self.engine.process_update(self.session, text="Notification System")
        self.assertEqual(self.session.state, BotSession.State.ALERT_MENU)


class CustomerWebhookPhase2Tests(APITestCase):
    def setUp(self):
        from telegram_app.bot import factory as bot_factory
        from telegram_app.services.bot_menu import clear_menu_configured_cache

        bot_factory._DISPATCHERS.clear()
        clear_menu_configured_cache()
        self.bot = TelegramBot.objects.create(name="Hook Bot", token="999:XYZ", is_active=True)

    def tearDown(self):
        from telegram_app.bot import factory as bot_factory
        from telegram_app.services.bot_menu import clear_menu_configured_cache

        bot_factory._DISPATCHERS.clear()
        clear_menu_configured_cache()

    def test_webhook_404_for_unknown_bot(self):
        r = self.client.post("/api/telegram/webhook/99999/", {"update_id": 1}, format="json")
        self.assertEqual(r.status_code, 404)

    @patch("aiogram.client.bot.Bot.set_chat_menu_button", new_callable=AsyncMock)
    @patch("aiogram.client.bot.Bot.set_my_commands", new_callable=AsyncMock)
    @patch("aiogram.client.bot.Bot.send_message", new_callable=AsyncMock)
    def test_webhook_start_sends_main_menu(self, send_message, _set_cmds, _set_menu):
        send_message.return_value = MagicMock(message_id=10)

        payload = {
            "update_id": 1001,
            "message": {
                "message_id": 7,
                "text": "/start",
                "chat": {"id": 555},
                "from": {
                    "id": 555,
                    "username": "alice",
                    "first_name": "Alice",
                    "language_code": "en",
                },
            },
        }
        r = self.client.post(
            f"/api/telegram/webhook/{self.bot.pk}/",
            payload,
            format="json",
        )
        self.assertEqual(r.status_code, 200, r.content)
        self.assertTrue(r.json().get("ok"))
        send_message.assert_awaited()
        call_kwargs = send_message.await_args.kwargs
        self.assertEqual(call_kwargs["chat_id"], 555)
        self.assertEqual(call_kwargs["text"], MAIN_MENU_TEXT)

        profile = upsert_customer_profile(payload)
        self.assertIsNotNone(profile)
        self.assertEqual(profile.telegram_user_id, 555)
        self.assertEqual(profile.username, "alice")

        session = BotSession.objects.get(telegram_user_id=555, bot=self.bot)
        self.assertEqual(session.state, BotSession.State.MAIN_MENU)

    @patch("aiogram.client.bot.Bot.set_chat_menu_button", new_callable=AsyncMock)
    @patch("aiogram.client.bot.Bot.set_my_commands", new_callable=AsyncMock)
    @patch("aiogram.client.bot.Bot.send_message", new_callable=AsyncMock)
    def test_process_update_payload_answers_callback_stub(self, send_message, _set_cmds, _set_menu):
        send_message.return_value = MagicMock(message_id=10)

        process_update_payload(
            self.bot,
            {
                "update_id": 2001,
                "message": {
                    "message_id": 1,
                    "text": "/start",
                    "chat": {"id": 777},
                    "from": {"id": 777, "username": "bob"},
                },
            },
        )
        process_update_payload(
            self.bot,
            {
                "update_id": 2002,
                "message": {
                    "message_id": 2,
                    "text": "Registering for exchange",
                    "chat": {"id": 777},
                    "from": {"id": 777, "username": "bob"},
                },
            },
        )
        self.assertEqual(send_message.await_count, 2)
        last_kwargs = send_message.await_args.kwargs
        self.assertIn("source currency", last_kwargs["text"].lower())

    @patch("aiogram.client.bot.Bot.set_chat_menu_button", new_callable=AsyncMock)
    @patch("aiogram.client.bot.Bot.set_my_commands", new_callable=AsyncMock)
    @patch("aiogram.client.bot.Bot.send_message", new_callable=AsyncMock)
    def test_reply_keyboard_navigation_sends_not_edits(self, send_message, _set_cmds, _set_menu):
        send_message.return_value = MagicMock(message_id=10)

        process_update_payload(
            self.bot,
            {
                "update_id": 3001,
                "message": {
                    "message_id": 1,
                    "text": "/start",
                    "chat": {"id": 888},
                    "from": {"id": 888, "username": "cara"},
                },
            },
        )
        process_update_payload(
            self.bot,
            {
                "update_id": 3002,
                "message": {
                    "message_id": 2,
                    "text": "Customer profile",
                    "chat": {"id": 888},
                    "from": {"id": 888, "username": "cara"},
                },
            },
        )
        self.assertEqual(send_message.await_count, 2)

    @patch("aiogram.client.bot.Bot.set_chat_menu_button", new_callable=AsyncMock)
    @patch("aiogram.client.bot.Bot.set_my_commands", new_callable=AsyncMock)
    @patch("aiogram.types.CallbackQuery.answer", new_callable=AsyncMock)
    @patch("telegram_app.bot.middlewares.cache.add", return_value=False)
    def test_busy_user_skips_duplicate_callback(self, _cache_add, answer, _set_cmds, _set_menu):
        process_update_payload(
            self.bot,
            {
                "update_id": 4001,
                "callback_query": {
                    "id": "cq-busy",
                    "data": CB_MENU_EXCHANGE,
                    "from": {"id": 999, "username": "dana"},
                    "message": {"message_id": 9, "chat": {"id": 999}},
                },
            },
        )
        answer.assert_awaited()
        self.assertEqual(answer.await_args.args[0], "Please wait…")


class TtlParseTests(TestCase):
    def test_parse_ttl_variants(self):
        self.assertEqual(parse_ttl_minutes("30"), 30)
        self.assertEqual(parse_ttl_minutes("30m"), 30)
        self.assertEqual(parse_ttl_minutes("1h"), 60)
        self.assertEqual(parse_ttl_minutes("2d"), 2880)
        self.assertIsNone(parse_ttl_minutes("nope"))
        self.assertIsNone(parse_ttl_minutes("0"))


class ExchangeAndAlertFlowTests(TestCase):
    def setUp(self):
        self.bot = TelegramBot.objects.create(
            name="Flow Bot",
            token="1:token",
            is_active=True,
            default_exchange_ttl_minutes=7,
        )
        self.engine = ConversationEngine(self.bot)
        self.session = self.engine.get_or_create_session(9001)
        CustomerProfile.objects.create(telegram_user_id=9001, username="flow")

    def _seed_exchange_draft(self):
        self.engine.process_update(self.session, text="/start")
        self.engine.process_update(self.session, callback_data=CB_MENU_EXCHANGE, message_id=1)
        ctx = dict(self.session.context or {})
        ctx["draft"] = {
            "flow": "exchange",
            "source_currency": "USD",
            "target_currency": "EUR",
            "amount": "100",
        }
        self.session.context = ctx
        self.session.state = BotSession.State.EXCHANGE_SUMMARY
        self.session.save()

    @patch("telegram_app.services.conversation.notify_staff_of_exchange_request")
    def test_exchange_confirm_creates_request_and_notifies(self, notify_mock):
        notify_mock.return_value = {"sent": 1, "failed": 0, "recipients": 1}
        self._seed_exchange_draft()
        out = self.engine.process_update(
            self.session, callback_data=CB_EXCH_CONFIRM, message_id=5
        )
        self.assertEqual(out["text"], "The Operator will contact you very soon")
        self.assertEqual(out["buttons"], MAIN_MENU_BUTTONS)
        req = ExchangeRequest.objects.get(customer__telegram_user_id=9001)
        self.assertEqual(req.source_currency, "USD")
        self.assertEqual(req.target_currency, "EUR")
        self.assertIsNone(req.price_at_request)
        self.assertEqual(req.ttl_minutes, 7)
        notify_mock.assert_called_once()
        self.assertEqual(self.session.state, BotSession.State.MAIN_MENU)

    def test_exchange_amount_goes_straight_to_summary(self):
        self.engine.process_update(self.session, text="/exchange")
        ctx = dict(self.session.context or {})
        ctx["draft"] = {
            "flow": "exchange",
            "source_currency": "USD",
            "target_currency": "EUR",
        }
        self.session.context = ctx
        self.session.state = BotSession.State.EXCHANGE_AMOUNT
        self.session.save()
        out = self.engine.process_update(self.session, text="250")
        self.assertEqual(self.session.state, BotSession.State.EXCHANGE_SUMMARY)
        self.assertIn("Amount: 250", out["text"])
        self.assertNotIn("TTL", out["text"])
        self.assertNotIn("Price:", out["text"])

    def test_legacy_price_state_recovers_to_summary(self):
        ctx = dict(self.session.context or {})
        ctx["draft"] = {
            "flow": "exchange",
            "source_currency": "USD",
            "target_currency": "EUR",
            "amount": "10",
            "price_at_request": "1",
        }
        self.session.context = ctx
        self.session.state = BotSession.State.EXCHANGE_PRICE
        self.session.save()
        out = self.engine.process_update(self.session, text="ignored")
        self.assertEqual(self.session.state, BotSession.State.EXCHANGE_SUMMARY)
        self.assertIn("Amount: 10", out["text"])

    def test_exchange_edit_returns_field_picker(self):
        self._seed_exchange_draft()
        out = self.engine.process_update(
            self.session, callback_data=CB_EXCH_EDIT, message_id=6
        )
        self.assertIn("edit", out["text"].lower())
        labels = {b["text"] for row in out["buttons"] for b in row}
        self.assertIn("Amount", labels)
        self.assertNotIn("Price", labels)
        self.assertNotIn("TTL", labels)

    def test_alert_confirm_creates_active_alert(self):
        self.engine.process_update(self.session, text="/start")
        self.engine.process_update(
            self.session, callback_data=CB_ALERT_INC, message_id=1
        )
        ctx = dict(self.session.context or {})
        ctx["draft"] = {
            "flow": "alert",
            "direction": PriceAlert.Direction.INCREASE,
            "source_currency": "USD",
            "target_currency": "GBP",
            "target_price": "1.25",
        }
        self.session.context = ctx
        self.session.state = BotSession.State.ALERT_SUMMARY
        self.session.save()
        out = self.engine.process_update(
            self.session, callback_data=CB_ALERT_CONFIRM, message_id=2
        )
        self.assertIn("Confirmed", out["text"])
        alert = PriceAlert.objects.get(customer__telegram_user_id=9001)
        self.assertTrue(alert.is_active)
        self.assertEqual(alert.direction, PriceAlert.Direction.INCREASE)

    def test_alert_edit_then_confirm_decrease(self):
        self.engine.process_update(self.session, text="/start")
        self.engine.process_update(
            self.session, callback_data=CB_ALERT_DEC, message_id=1
        )
        ctx = dict(self.session.context or {})
        ctx["draft"] = {
            "flow": "alert",
            "direction": PriceAlert.Direction.DECREASE,
            "source_currency": "USD",
            "target_currency": "EUR",
            "target_price": "2.00",
        }
        self.session.context = ctx
        self.session.state = BotSession.State.ALERT_SUMMARY
        self.session.save()

        out = self.engine.process_update(
            self.session, callback_data=CB_ALERT_EDIT, message_id=3
        )
        self.assertIn("edit", out["text"].lower())
        labels = {b["text"] for row in out["buttons"] for b in row}
        self.assertIn("Target price", labels)

        out = self.engine.process_update(
            self.session, callback_data="alert:ef:price", message_id=4
        )
        self.assertIn("target price", out["text"].lower())
        out = self.engine.process_update(self.session, text="1.75")
        self.assertIn("summary", out["text"].lower())
        self.assertEqual(self.session.context["draft"]["target_price"], "1.75")

        out = self.engine.process_update(
            self.session, callback_data=CB_ALERT_CONFIRM, message_id=5
        )
        self.assertIn("Confirmed", out["text"])
        alert = PriceAlert.objects.get(customer__telegram_user_id=9001)
        self.assertEqual(alert.direction, PriceAlert.Direction.DECREASE)
        self.assertEqual(alert.target_price, Decimal("1.75"))

    def test_profile_id_shows_telegram_user_id(self):
        self.engine.process_update(self.session, text="/start")
        self.engine.process_update(
            self.session, callback_data=CB_MENU_PROFILE, message_id=1
        )
        out = self.engine.process_update(
            self.session, callback_data=CB_PROFILE_ID, message_id=2
        )
        self.assertIn("9001", out["text"])

    def test_running_exchanges_list_and_cancel(self):
        from telegram_app.services.conversation import CB_PROFILE_RUNNING

        customer = CustomerProfile.objects.get(telegram_user_id=9001)
        live = ExchangeRequest.objects.create(
            customer=customer,
            bot=self.bot,
            source_currency="USD",
            target_currency="EUR",
            amount=Decimal("50"),
            ttl_minutes=30,
            status=ExchangeRequest.Status.PENDING,
        )
        ExchangeRequest.objects.create(
            customer=customer,
            bot=self.bot,
            source_currency="GBP",
            target_currency="USD",
            amount=Decimal("10"),
            ttl_minutes=1,
            status=ExchangeRequest.Status.PENDING,
            created_at=timezone.now() - timedelta(minutes=5),
        )
        # Force created_at on expired row (auto_now_add ignored on create above for second?)
        expired = ExchangeRequest.objects.filter(
            customer=customer, source_currency="GBP"
        ).first()
        ExchangeRequest.objects.filter(pk=expired.pk).update(
            created_at=timezone.now() - timedelta(minutes=5)
        )

        self.engine.process_update(self.session, callback_data=CB_MENU_PROFILE)
        out = self.engine.process_update(
            self.session, callback_data=CB_PROFILE_RUNNING
        )
        self.assertIn(f"#{live.pk}", out["text"])
        self.assertNotIn("GBP→USD", out["text"])
        labels = {b["text"] for row in out["buttons"] for b in row}
        self.assertIn(f"Cancel #{live.pk}", labels)

        out = self.engine.process_update(
            self.session, text=f"Cancel #{live.pk}"
        )
        self.assertIn("Cancelled", out["text"])
        live.refresh_from_db()
        self.assertEqual(live.status, ExchangeRequest.Status.CANCELLED)
        self.assertIn("No running exchanges", out["text"])


class AdminNotifyTests(TestCase):
    def setUp(self):
        self.bot = TelegramBot.objects.create(name="N", token="2:t", is_active=True)
        self.customer = CustomerProfile.objects.create(telegram_user_id=1)
        self.req = ExchangeRequest.objects.create(
            customer=self.customer,
            bot=self.bot,
            source_currency="USD",
            target_currency="EUR",
            amount=Decimal("10"),
            price_at_request=Decimal("1"),
            ttl_minutes=30,
        )

    def test_staff_recipients_filter_roles_and_telegram_id(self):
        CustomUser.objects.create_user(
            username="sa",
            password="x",
            role=CustomUser.ROLE_SUPER_ADMIN,
            telegram_id="111",
        )
        CustomUser.objects.create_user(
            username="mg",
            password="x",
            role=CustomUser.ROLE_MANAGEMENT,
            telegram_id="222",
        )
        CustomUser.objects.create_user(
            username="emp",
            password="x",
            role=CustomUser.ROLE_EMPLOYEE,
            telegram_id="333",
        )
        CustomUser.objects.create_user(
            username="empty",
            password="x",
            role=CustomUser.ROLE_SUPER_ADMIN,
            telegram_id="",
        )
        ids = set(staff_notify_recipients().values_list("telegram_id", flat=True))
        self.assertEqual(ids, {"111", "222"})

    @patch("telegram_app.services.admin_notify.TelegramService")
    def test_notify_marks_notified_when_at_least_one_send_ok(self, service_cls):
        CustomUser.objects.create_user(
            username="sa2",
            password="x",
            role=CustomUser.ROLE_SUPER_ADMIN,
            telegram_id="999",
        )
        service_cls.return_value.send_message.return_value = (True, "ok", None)
        result = notify_staff_of_exchange_request(self.req, bot=self.bot)
        self.assertEqual(result["sent"], 1)
        self.req.refresh_from_db()
        self.assertEqual(self.req.status, ExchangeRequest.Status.NOTIFIED)


class AlertCheckerMathTests(TestCase):
    def setUp(self):
        self.customer = CustomerProfile.objects.create(telegram_user_id=42)
        self.bot = TelegramBot.objects.create(name="A", token="3:t", is_active=True)
        usd, _ = Currency.objects.get_or_create(code="USD", defaults={"name": "US Dollar"})
        eur, _ = Currency.objects.get_or_create(code="EUR", defaults={"name": "Euro"})
        cat = Category.objects.create(name="AlertCat")
        self.pt = PriceType.objects.create(
            category=cat,
            name="USD/EUR buy",
            source_currency=usd,
            target_currency=eur,
            trade_type="buy",
            is_active=True,
        )
        PriceHistory.objects.create(price_type=self.pt, price=Decimal("1.50"))

    def test_increase_and_decrease_thresholds(self):
        inc = PriceAlert(
            direction=PriceAlert.Direction.INCREASE,
            target_price=Decimal("1.50"),
        )
        dec = PriceAlert(
            direction=PriceAlert.Direction.DECREASE,
            target_price=Decimal("1.50"),
        )
        self.assertTrue(alert_should_fire(inc, Decimal("1.50")))
        self.assertTrue(alert_should_fire(inc, Decimal("1.51")))
        self.assertFalse(alert_should_fire(inc, Decimal("1.49")))
        self.assertTrue(alert_should_fire(dec, Decimal("1.50")))
        self.assertTrue(alert_should_fire(dec, Decimal("1.49")))
        self.assertFalse(alert_should_fire(dec, Decimal("1.51")))

    def test_cooldown(self):
        alert = PriceAlert.objects.create(
            customer=self.customer,
            direction=PriceAlert.Direction.INCREASE,
            source_currency="USD",
            target_currency="EUR",
            target_price=Decimal("1.00"),
            last_triggered_at=timezone.now(),
        )
        self.assertTrue(alert_in_cooldown(alert))
        alert.last_triggered_at = timezone.now() - timedelta(hours=2)
        self.assertFalse(alert_in_cooldown(alert))

    @patch("telegram_app.services.alert_checker.TelegramService")
    def test_check_price_alerts_triggers_once(self, service_cls):
        service_cls.return_value.send_message.return_value = (True, "ok", None)
        alert = PriceAlert.objects.create(
            customer=self.customer,
            direction=PriceAlert.Direction.INCREASE,
            source_currency="USD",
            target_currency="EUR",
            target_price=Decimal("1.40"),
            is_active=True,
        )
        stats = check_price_alerts()
        self.assertEqual(stats["triggered"], 1)
        alert.refresh_from_db()
        self.assertIsNotNone(alert.last_triggered_at)
        stats2 = check_price_alerts()
        self.assertEqual(stats2["triggered"], 0)
        self.assertEqual(stats2["skipped_cooldown"], 1)


class CustomerTagApiTests(APITestCase):
    def setUp(self):
        self.mgmt = CustomUser.objects.create_user(
            username="mgmt",
            password="pass12345",
            role=CustomUser.ROLE_MANAGEMENT,
        )
        self.employee = CustomUser.objects.create_user(
            username="emp2",
            password="pass12345",
            role=CustomUser.ROLE_EMPLOYEE,
        )
        self.customer = CustomerProfile.objects.create(
            telegram_user_id=55, username="c1", tag="global"
        )

    def test_management_can_patch_tag(self):
        self.client.force_authenticate(self.mgmt)
        r = self.client.patch(
            f"/api/telegram/customers/{self.customer.pk}/",
            {"tag": "vip"},
            format="json",
        )
        self.assertEqual(r.status_code, 200, r.content)
        self.assertEqual(r.json()["tag"], "vip")
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.tag, "vip")

    def test_management_can_retrieve_customer_detail(self):
        self.client.force_authenticate(self.mgmt)
        r = self.client.get(f"/api/telegram/customers/{self.customer.pk}/")
        self.assertEqual(r.status_code, 200, r.content)
        self.assertEqual(r.json()["telegram_user_id"], 55)
        self.assertEqual(r.json()["tag"], "global")

    def test_employee_cannot_patch_tag(self):
        self.client.force_authenticate(self.employee)
        r = self.client.patch(
            f"/api/telegram/customers/{self.customer.pk}/",
            {"tag": "special"},
            format="json",
        )
        self.assertEqual(r.status_code, 403)
