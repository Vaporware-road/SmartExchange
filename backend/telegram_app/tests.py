from io import BytesIO
from unittest.mock import AsyncMock, MagicMock, patch
import asyncio
import logging

from django.core.cache import cache
from django.db.utils import OperationalError
from django.test import TestCase
from rest_framework.test import APITestCase

from accounts.models import CustomUser
from accounts.plans import PLAN_GOLD
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


def _stub_aiogram_bot(bot_cls):
    instance = bot_cls.return_value
    instance.session.close = AsyncMock()
    return instance


class TelegramServiceOptionalCaptionTest(TestCase):
    @patch("telegram_app.services.telegram_client.Bot")
    def test_send_photo_without_caption_uses_no_parse_mode(self, bot_cls):
        bot_instance = _stub_aiogram_bot(bot_cls)
        bot_instance.send_photo = AsyncMock(return_value=None)

        service = TelegramService("token")
        image_stream = BytesIO(b"fake image bytes")
        image_stream.name = "prices.png"

        ok, _ = service.send_photo(chat_id="@channel", photo=image_stream, caption="", buttons=[])

        self.assertTrue(ok)
        bot_instance.send_photo.assert_awaited_once()
        call = bot_instance.send_photo.await_args
        self.assertIsNone(call.kwargs.get("parse_mode"))
        from aiogram.types import BufferedInputFile

        photo_arg = call.kwargs.get("photo")
        self.assertIsInstance(photo_arg, BufferedInputFile)


class TelegramServiceBotLifecycleTests(TestCase):
    @patch("telegram_app.services.telegram_client.Bot")
    def test_bot_is_constructed_inside_send_not_init(self, bot_cls):
        bot_instance = _stub_aiogram_bot(bot_cls)
        bot_instance.send_message = AsyncMock(return_value=MagicMock(message_id=7))

        service = TelegramService("token")
        bot_cls.assert_not_called()

        ok, _msg, mid = service.send_message(chat_id=1, text="hi", parse_mode=None)
        self.assertTrue(ok)
        self.assertEqual(mid, 7)
        bot_cls.assert_called_once()
        self.assertEqual(bot_cls.call_args.kwargs.get("token") or bot_cls.call_args.args[0], "token")
        bot_instance.session.close.assert_awaited()

    @patch("telegram_app.services.telegram_client.Bot")
    def test_bot_is_constructed_when_loop_already_running(self, bot_cls):
        bot_instance = _stub_aiogram_bot(bot_cls)
        bot_instance.send_message = AsyncMock(return_value=MagicMock(message_id=8))

        async def _inside_running_loop():
            service = TelegramService("token")
            bot_cls.assert_not_called()
            ok, _msg, _mid = service.send_message(chat_id=1, text="hi", parse_mode=None)
            return ok

        self.assertTrue(asyncio.run(_inside_running_loop()))
        bot_cls.assert_called_once()
        self.assertEqual(bot_cls.call_args.kwargs.get("token") or bot_cls.call_args.args[0], "token")
        bot_instance.send_message.assert_awaited()

    @patch("telegram_app.services.telegram_client.Bot")
    def test_send_message_surfaces_telegram_error(self, bot_cls):
        from aiogram.exceptions import TelegramBadRequest

        bot_instance = _stub_aiogram_bot(bot_cls)
        bot_instance.send_message = AsyncMock(
            side_effect=TelegramBadRequest(
                method=MagicMock(),
                message="can't parse entities: unsupported start tag",
            )
        )
        service = TelegramService("token")
        ok, err, mid = service.send_message(chat_id=1, text="<b>hi", parse_mode=None)
        self.assertFalse(ok)
        self.assertIsNone(mid)
        self.assertIn("can't parse entities", err)


class AutomationSettingsApiTests(APITestCase):
    """GET/PUT /api/telegram/automation-settings/ must not 500 (regression: stale SiteSettings cache)."""

    def setUp(self):
        cache.delete("site_settings")
        self.employee = CustomUser.objects.create_user(
            username="automation_tester",
            password="pass12345",
            role=CustomUser.ROLE_EMPLOYEE,
        )
        self.owner = CustomUser.objects.create_user(
            username="automation_owner",
            password="pass12345",
            role=CustomUser.ROLE_MANAGEMENT,
        )

    def test_get_automation_settings_ok(self):
        self.client.force_authenticate(self.employee)
        r = self.client.get("/api/telegram/automation-settings/")
        self.assertEqual(r.status_code, 200, r.content)
        self.assertIn("auto_post_on_update", r.json())
        self.assertIsInstance(r.json()["auto_post_on_update"], bool)

    def test_put_automation_settings_requires_client_owner(self):
        self.client.force_authenticate(self.employee)
        r = self.client.put(
            "/api/telegram/automation-settings/",
            {"auto_post_on_update": True},
            format="json",
        )
        self.assertEqual(r.status_code, 403, r.content)

    def test_put_automation_settings_updates_flag(self):
        self.client.force_authenticate(self.owner)
        r = self.client.put(
            "/api/telegram/automation-settings/",
            {"auto_post_on_update": True},
            format="json",
        )
        self.assertEqual(r.status_code, 200, r.content)
        self.assertTrue(r.json()["auto_post_on_update"])
        self.assertTrue(SiteSettings.objects.get(pk=1).auto_post_on_update)

    @patch(
        "setting.models.SiteSettings.load",
        side_effect=OperationalError("no such column: setting_sitesettings.prices_webhook_url"),
    )
    def test_get_automation_settings_returns_200_when_site_settings_db_unreadable(self, _mock_load):
        """Regression: avoid 500 when ORM cannot read SiteSettings (stale schema)."""
        self.client.force_authenticate(self.employee)
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
        self.client.force_authenticate(self.owner)
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


class InBotAdminPanelTests(TestCase):
    def setUp(self):
        self.owner = CustomUser.objects.create_user(
            username="botowner",
            password="pass12345",
            role=CustomUser.ROLE_MANAGEMENT,
            plan=PLAN_GOLD,
            telegram_id="6296044948",
        )
        self.bot = TelegramBot.objects.create(
            name="Owned Bot",
            token="999:ADMIN",
            is_active=True,
            owner=self.owner,
        )
        self.engine = ConversationEngine(self.bot)
        self.admin_session = self.engine.get_or_create_session(6296044948)
        self.customer_session = self.engine.get_or_create_session(111)

    def test_admin_start_opens_admin_panel(self):
        out = self.engine.process_update(self.admin_session, text="/start")
        self.admin_session.refresh_from_db()
        self.assertEqual(self.admin_session.state, BotSession.State.ADMIN_MENU)
        self.assertIn("Admin panel", out["text"])
        labels = {b["text"] for row in out["buttons"] for b in row}
        self.assertIn("Pending requests", labels)
        self.assertIn("Analytics Dashboard", labels)
        self.assertNotIn("Customer menu", labels)

    def test_admin_analytics_dashboard(self):
        self.engine.process_update(self.admin_session, text="/start")
        out = self.engine.process_update(self.admin_session, text="Analytics Dashboard")
        self.admin_session.refresh_from_db()
        self.assertEqual(self.admin_session.state, BotSession.State.ADMIN_ANALYTICS)
        self.assertIn("Analytics", out["text"])
        labels = {b["text"] for row in out["buttons"] for b in row}
        self.assertIn("Exchange Requests", labels)

    def test_admin_customer_analysis(self):
        self.engine.process_update(self.admin_session, text="/start")
        out = self.engine.process_update(self.admin_session, text="Customer Analysis")
        self.assertIn("Customer Analysis", out["text"])
        self.assertIn("Inactive", out["text"])
        labels = {b["text"] for row in out["buttons"] for b in row}
        self.assertIn("Set customer tag", labels)
        self.assertIn("Admin menu", labels)

    def test_admin_reengage_audience_label_is_special(self):
        self.engine.process_update(self.admin_session, text="/start")
        out = self.engine.process_update(self.admin_session, text="Re-engagement")
        labels = {b["text"] for row in out["buttons"] for b in row}
        self.assertIn("Audience: Special", labels)
        self.assertNotIn("Audience: Special currencies", labels)
        self.assertIn("Admin menu", labels)

    def test_admin_analytics_exchange_and_members(self):
        customer = CustomerProfile.objects.create(telegram_user_id=222, tag="global")
        ExchangeRequest.objects.create(
            customer=customer,
            bot=self.bot,
            source_currency="USD",
            target_currency="EUR",
            amount="50",
            ttl_minutes=5,
            status=ExchangeRequest.Status.NEW,
        )
        self.engine.process_update(self.admin_session, text="/start")
        self.engine.process_update(self.admin_session, text="Analytics Dashboard")
        out = self.engine.process_update(self.admin_session, text="Exchange Requests")
        self.assertIn("Choose a filter", out["text"])
        out = self.engine.process_update(self.admin_session, text="Pending Requests")
        self.assertIn("New", out["text"])
        out = self.engine.process_update(self.admin_session, text="Back to Analytics")
        out = self.engine.process_update(self.admin_session, text="New members")
        out = self.engine.process_update(self.admin_session, text="Last month")
        self.assertIn("Channel subscribers gained", out["text"])
        self.assertIn("New bot DM users", out["text"])

    def test_customer_start_stays_customer_menu(self):
        out = self.engine.process_update(self.customer_session, text="/start")
        self.customer_session.refresh_from_db()
        self.assertEqual(self.customer_session.state, BotSession.State.MAIN_MENU)
        self.assertEqual(out["buttons"], MAIN_MENU_BUTTONS)

    def test_admin_can_list_and_change_pending_state(self):
        customer = CustomerProfile.objects.create(telegram_user_id=111, tag="global")
        req = ExchangeRequest.objects.create(
            customer=customer,
            bot=self.bot,
            source_currency="USD",
            target_currency="EUR",
            amount="100",
            price_at_request=None,
            ttl_minutes=5,
            status=ExchangeRequest.Status.NEW,
        )
        self.engine.process_update(self.admin_session, text="/start")
        out = self.engine.process_update(self.admin_session, text="Pending requests")
        self.assertIn(f"Req #{req.pk}", out["text"])
        out = self.engine.process_update(
            self.admin_session, text=f"Req #{req.pk} USD→EUR"
        )
        self.assertIn(f"Request #{req.pk}", out["text"])
        labels = {b["text"] for row in out["buttons"] for b in row}
        self.assertIn("Change state", labels)
        self.assertIn("Confirm (Hold the request)", labels)
        self.assertIn("Admin menu", labels)
        out = self.engine.process_update(self.admin_session, text="Change state")
        labels = {b["text"] for row in out["buttons"] for b in row}
        self.assertIn("New", labels)
        self.assertIn("Canceled", labels)
        self.assertIn("Successful", labels)
        self.assertIn("Back", labels)
        out = self.engine.process_update(self.admin_session, text="Successful")
        req.refresh_from_db()
        self.assertEqual(req.status, ExchangeRequest.Status.SUCCESSFUL)
        self.assertIn("Successful", out["text"])

    def test_admin_hold_extends_ttl(self):
        customer = CustomerProfile.objects.create(telegram_user_id=112, tag="global")
        req = ExchangeRequest.objects.create(
            customer=customer,
            bot=self.bot,
            source_currency="USD",
            target_currency="EUR",
            amount="10",
            ttl_minutes=5,
            status=ExchangeRequest.Status.NEW,
        )
        self.engine.process_update(self.admin_session, text="/start")
        self.engine.process_update(self.admin_session, text="Pending requests")
        self.engine.process_update(
            self.admin_session, text=f"Req #{req.pk} USD→EUR"
        )
        out = self.engine.process_update(
            self.admin_session, text="Confirm (Hold the request)"
        )
        req.refresh_from_db()
        self.assertEqual(req.ttl_minutes, 10)
        self.assertIn("TTL increase : 10", out["text"])

    def test_set_customer_tag_from_analysis(self):
        CustomerProfile.objects.create(
            telegram_user_id=111, username="alice", tag="global"
        )
        self.engine.process_update(self.admin_session, text="/start")
        self.engine.process_update(self.admin_session, text="Customer Analysis")
        out = self.engine.process_update(self.admin_session, text="Set customer tag")
        self.assertIn("Write any userid or chose from the list:", out["text"])
        self.assertIn("111", out["text"])
        labels = {b["text"] for row in out["buttons"] for b in row}
        self.assertIn("Admin menu", labels)
        out = self.engine.process_update(self.admin_session, text="111")
        self.assertIn("Choose a tag", out["text"])
        out = self.engine.process_update(self.admin_session, text="Tag: VIP")
        profile = CustomerProfile.objects.get(telegram_user_id=111)
        self.assertEqual(profile.tag, "vip")
        self.assertIn("vip", out["text"])

    def test_sub_role_operator_menu_is_limited(self):
        from accounts.models import CustomUser
        from telegram_app.services.bot_admins import sync_bot_admins_for_owner

        operator = CustomUser.objects.create_user(
            username="tg_sub_op",
            password=None,
            role=CustomUser.ROLE_EMPLOYEE,
            owner=self.owner,
            sub_role=CustomUser.SUB_ROLE_OPERATOR,
            telegram_username="subop",
            telegram_id="700001",
            first_name="Sub",
            last_name="Op",
        )
        operator.set_unusable_password()
        operator.save(update_fields=["password"])
        sync_bot_admins_for_owner(self.owner)
        session = self.engine.get_or_create_session(700001)
        out = self.engine.process_update(session, text="/start")
        labels = {b["text"] for row in out["buttons"] for b in row}
        self.assertIn("Pending requests", labels)
        self.assertIn("Recent requests", labels)
        self.assertNotIn("Analytics Dashboard", labels)
        self.assertNotIn("Re-engagement", labels)

    def test_sub_role_operator_cannot_bypass_analytics_callback(self):
        from accounts.models import CustomUser
        from telegram_app.services.admin_conversation import (
            CB_ADMIN_ANALYTICS_EXCHANGE,
            handle_admin_action,
        )
        from telegram_app.services.bot_admins import sync_bot_admins_for_owner

        operator = CustomUser.objects.create_user(
            username="tg_sub_op_cb",
            password=None,
            role=CustomUser.ROLE_EMPLOYEE,
            owner=self.owner,
            sub_role=CustomUser.SUB_ROLE_OPERATOR,
            telegram_username="subopcb",
            telegram_id="700003",
            first_name="Sub",
            last_name="Op",
        )
        operator.set_unusable_password()
        operator.save(update_fields=["password"])
        sync_bot_admins_for_owner(self.owner)
        session = self.engine.get_or_create_session(700003)
        self.engine.process_update(session, text="/start")
        out = handle_admin_action(session, CB_ADMIN_ANALYTICS_EXCHANGE)
        session.refresh_from_db()
        self.assertEqual(session.state, BotSession.State.ADMIN_MENU)
        self.assertIn("Admin panel", out["text"])

    def test_sub_role_operator_cannot_bypass_typed_analytics_label(self):
        from accounts.models import CustomUser
        from telegram_app.services.admin_conversation import BTN_ADMIN_EXCHANGE_REQUESTS
        from telegram_app.services.bot_admins import sync_bot_admins_for_owner

        operator = CustomUser.objects.create_user(
            username="tg_sub_op_label",
            password=None,
            role=CustomUser.ROLE_EMPLOYEE,
            owner=self.owner,
            sub_role=CustomUser.SUB_ROLE_OPERATOR,
            telegram_username="suboplabel",
            telegram_id="700004",
            first_name="Sub",
            last_name="Op",
        )
        operator.set_unusable_password()
        operator.save(update_fields=["password"])
        sync_bot_admins_for_owner(self.owner)
        session = self.engine.get_or_create_session(700004)
        self.engine.process_update(session, text="/start")
        out = self.engine.process_update(session, text=BTN_ADMIN_EXCHANGE_REQUESTS)
        session.refresh_from_db()
        self.assertEqual(session.state, BotSession.State.ADMIN_MENU)
        self.assertIn("Admin panel", out["text"])

    def test_sub_role_head_operator_has_reengage_not_analytics(self):
        from accounts.models import CustomUser
        from telegram_app.services.bot_admins import sync_bot_admins_for_owner

        head = CustomUser.objects.create_user(
            username="tg_sub_head",
            password=None,
            role=CustomUser.ROLE_EMPLOYEE,
            owner=self.owner,
            sub_role=CustomUser.SUB_ROLE_HEAD_OPERATOR,
            telegram_username="subhead",
            telegram_id="700002",
            first_name="Sub",
            last_name="Head",
        )
        head.set_unusable_password()
        head.save(update_fields=["password"])
        sync_bot_admins_for_owner(self.owner)
        session = self.engine.get_or_create_session(700002)
        out = self.engine.process_update(session, text="/start")
        labels = {b["text"] for row in out["buttons"] for b in row}
        self.assertIn("Re-engagement", labels)
        self.assertNotIn("Analytics Dashboard", labels)

    def test_non_owner_management_denied(self):
        other = CustomUser.objects.create_user(
            username="othermgmt",
            password="pass12345",
            role=CustomUser.ROLE_MANAGEMENT,
            telegram_id="555555",
        )
        session = self.engine.get_or_create_session(555555)
        out = self.engine.process_update(session, text="/admin")
        self.assertIn("not registered", out["text"].lower())
        self.assertEqual(session.state, BotSession.State.START)
        _ = other  # created for telegram_id uniqueness



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
        self.assertEqual(
            out["text"],
            "🎉✅ Request received!\n\n"
            "We're on it — an operator will contact you very soon. "
            "Thank you for choosing us! 🙏",
        )
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
            status=ExchangeRequest.Status.NEW,
        )
        ExchangeRequest.objects.create(
            customer=customer,
            bot=self.bot,
            source_currency="GBP",
            target_currency="USD",
            amount=Decimal("10"),
            ttl_minutes=1,
            status=ExchangeRequest.Status.NEW,
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
    def test_notify_keeps_new_status_when_send_ok(self, service_cls):
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
        self.assertEqual(self.req.status, ExchangeRequest.Status.NEW)

    @patch("telegram_app.services.admin_notify.TelegramService")
    def test_notify_keeps_new_status_when_send_fails(self, service_cls):
        CustomUser.objects.create_user(
            username="sa3",
            password="x",
            role=CustomUser.ROLE_SUPER_ADMIN,
            telegram_id="998",
        )
        service_cls.return_value.send_message.return_value = (
            False,
            "can't parse entities: unsupported start tag",
            None,
        )
        result = notify_staff_of_exchange_request(self.req, bot=self.bot)
        self.assertEqual(result["sent"], 0)
        self.assertEqual(result["failed"], 1)
        self.assertIn("can't parse entities", result["last_error"])
        self.req.refresh_from_db()
        self.assertEqual(self.req.status, ExchangeRequest.Status.NEW)


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
        self.bot = TelegramBot.objects.create(
            name="mgmt-bot",
            token="123456:AA-test-token-mgmt",
            owner=self.mgmt,
            is_active=True,
        )
        self.customer = CustomerProfile.objects.create(
            telegram_user_id=55, username="c1", tag="global"
        )
        BotSession.objects.create(
            telegram_user_id=55,
            bot=self.bot,
            state=BotSession.State.MAIN_MENU,
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

    def test_staff_customer_tag_is_admin_and_locked(self):
        CustomUser.objects.create_user(
            username="staff-cust",
            password="pass12345",
            role=CustomUser.ROLE_SUPER_ADMIN,
            telegram_id="55",
        )
        self.client.force_authenticate(self.mgmt)
        listed = self.client.get("/api/telegram/customers/")
        self.assertEqual(listed.status_code, 200, listed.content)
        rows = listed.json()
        if isinstance(rows, dict):
            rows = rows.get("results", [])
        match = next(row for row in rows if row["telegram_user_id"] == 55)
        self.assertTrue(match["is_admin"])
        self.assertEqual(match["display_tag"], "admin")
        r = self.client.patch(
            f"/api/telegram/customers/{self.customer.pk}/",
            {"tag": "vip"},
            format="json",
        )
        self.assertEqual(r.status_code, 400, r.content)
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.tag, "global")


class TelegramAdminVerifyApiTests(APITestCase):
    def setUp(self):
        self.mgmt = CustomUser.objects.create_user(
            username="hub-mgmt",
            password="pass12345",
            role=CustomUser.ROLE_MANAGEMENT,
        )
        self.other = CustomUser.objects.create_user(
            username="hub-other",
            password="pass12345",
            role=CustomUser.ROLE_MANAGEMENT,
        )

    def test_verify_no_owned_bot_returns_404(self):
        self.client.force_authenticate(self.mgmt)
        r = self.client.post("/api/telegram/admin/verify-bot/", {}, format="json")
        self.assertEqual(r.status_code, 404, r.content)
        body = r.json()
        self.assertFalse(body.get("ok", True))
        self.assertEqual(body.get("code"), "no_bot")

    @patch("telegram_app.admin_api.TelegramService")
    def test_verify_get_me_ok(self, service_cls):
        bot = TelegramBot.objects.create(
            name="Owned",
            token="111:AAA",
            owner=self.mgmt,
            is_active=True,
            default_exchange_ttl_minutes=7,
        )
        service_cls.return_value.get_me.return_value = (
            True,
            {"id": 99, "username": "owned_bot", "first_name": "Owned", "is_bot": True},
            None,
        )
        self.client.force_authenticate(self.mgmt)
        r = self.client.post("/api/telegram/admin/verify-bot/", {}, format="json")
        self.assertEqual(r.status_code, 200, r.content)
        body = r.json()
        self.assertTrue(body["ok"])
        self.assertEqual(body["bot"]["id"], bot.id)
        self.assertEqual(body["bot"]["default_exchange_ttl_minutes"], 7)
        self.assertEqual(body["bot"]["username"], "owned_bot")
        service_cls.assert_called_once()
        service_cls.return_value.get_me.assert_called_once()

    @patch("telegram_app.admin_api.TelegramService")
    def test_verify_get_me_fail(self, service_cls):
        TelegramBot.objects.create(
            name="Owned",
            token="111:AAA",
            owner=self.mgmt,
            is_active=True,
        )
        service_cls.return_value.get_me.return_value = (
            False,
            None,
            "Unauthorized",
        )
        self.client.force_authenticate(self.mgmt)
        r = self.client.post("/api/telegram/admin/verify-bot/", {}, format="json")
        self.assertEqual(r.status_code, 400, r.content)
        body = r.json()
        self.assertFalse(body.get("ok", True))
        self.assertEqual(body.get("code"), "get_me_failed")


class TelegramAdminDashboardApiTests(APITestCase):
    def setUp(self):
        self.mgmt = CustomUser.objects.create_user(
            username="dash-mgmt",
            password="pass12345",
            role=CustomUser.ROLE_MANAGEMENT,
        )
        self.other = CustomUser.objects.create_user(
            username="dash-other",
            password="pass12345",
            role=CustomUser.ROLE_MANAGEMENT,
        )
        self.bot = TelegramBot.objects.create(
            name="DashBot",
            token="222:BBB",
            owner=self.mgmt,
            is_active=True,
        )
        self.other_bot = TelegramBot.objects.create(
            name="OtherBot",
            token="333:CCC",
            owner=self.other,
            is_active=True,
        )
        self.mine = CustomerProfile.objects.create(
            telegram_user_id=1001, username="mine", tag="vip"
        )
        self.theirs = CustomerProfile.objects.create(
            telegram_user_id=1002, username="theirs", tag="global"
        )
        BotSession.objects.create(
            telegram_user_id=1001,
            bot=self.bot,
            state=BotSession.State.MAIN_MENU,
        )
        BotSession.objects.create(
            telegram_user_id=1002,
            bot=self.other_bot,
            state=BotSession.State.MAIN_MENU,
        )
        ExchangeRequest.objects.create(
            customer=self.mine,
            bot=self.bot,
            source_currency="USD",
            target_currency="IRR",
            amount=Decimal("10"),
            ttl_minutes=5,
            status=ExchangeRequest.Status.SUCCESSFUL,
        )
        ExchangeRequest.objects.create(
            customer=self.theirs,
            bot=self.other_bot,
            source_currency="EUR",
            target_currency="IRR",
            amount=Decimal("20"),
            ttl_minutes=5,
            status=ExchangeRequest.Status.NEW,
        )

    def test_dashboard_scoped_to_owned_bot(self):
        self.client.force_authenticate(self.mgmt)
        r = self.client.get("/api/telegram/admin/dashboard/")
        self.assertEqual(r.status_code, 200, r.content)
        body = r.json()
        self.assertEqual(body["bot"]["id"], self.bot.id)
        self.assertEqual(body["customers_status"]["by_tag"]["vip"], 1)
        self.assertEqual(body["customers_status"]["by_tag"]["total"], 1)
        self.assertEqual(body["reports"]["new"], 0)
        self.assertEqual(body["reports"]["pending"], 0)
        self.assertEqual(body["reports"]["successful"], 1)
        currencies = {
            row["currency"] for row in body["exchange_requests"]["most_requested_currencies"]
        }
        self.assertIn("USD", currencies)
        self.assertNotIn("EUR", currencies)
        self.assertTrue(body["analytics"]["channel_views"]["stub"])

    def test_dashboard_forbidden_other_bot_id(self):
        self.client.force_authenticate(self.mgmt)
        r = self.client.get(
            f"/api/telegram/admin/dashboard/?bot_id={self.other_bot.id}"
        )
        self.assertEqual(r.status_code, 403, r.content)

    def _exchange_list_ids(self, response):
        body = response.json()
        items = body["results"] if isinstance(body, dict) and "results" in body else body
        return [row["id"] for row in items]

    def test_exchange_requests_filter_by_bot_id(self):
        self.client.force_authenticate(self.mgmt)
        r = self.client.get(f"/api/telegram/exchange-requests/?bot_id={self.bot.id}")
        self.assertEqual(r.status_code, 200, r.content)
        ids = self._exchange_list_ids(r)
        mine = list(
            ExchangeRequest.objects.filter(bot=self.bot).values_list("id", flat=True)
        )
        theirs = list(
            ExchangeRequest.objects.filter(bot=self.other_bot).values_list(
                "id", flat=True
            )
        )
        self.assertTrue(mine)
        for pk in mine:
            self.assertIn(pk, ids)
        for pk in theirs:
            self.assertNotIn(pk, ids)

        default = self.client.get("/api/telegram/exchange-requests/")
        self.assertEqual(default.status_code, 200, default.content)
        default_ids = self._exchange_list_ids(default)
        for pk in theirs:
            self.assertNotIn(pk, default_ids)

    def test_exchange_requests_forbidden_other_bot_id(self):
        self.client.force_authenticate(self.mgmt)
        r = self.client.get(
            f"/api/telegram/exchange-requests/?bot_id={self.other_bot.id}"
        )
        self.assertEqual(r.status_code, 403, r.content)

    def test_exchange_requests_invalid_bot_id(self):
        self.client.force_authenticate(self.mgmt)
        r = self.client.get("/api/telegram/exchange-requests/?bot_id=not-a-number")
        self.assertEqual(r.status_code, 400, r.content)

    def test_dashboard_and_exchange_list_include_new_request_for_bot(self):
        self.client.force_authenticate(self.mgmt)
        customer = CustomerProfile.objects.create(
            telegram_user_id=1099, username="newreq"
        )
        req = ExchangeRequest.objects.create(
            customer=customer,
            bot=self.bot,
            source_currency="GBP",
            target_currency="IRR",
            amount=Decimal("5"),
            ttl_minutes=5,
            status=ExchangeRequest.Status.NEW,
        )
        other_req = ExchangeRequest.objects.create(
            customer=self.theirs,
            bot=self.other_bot,
            source_currency="TRY",
            target_currency="IRR",
            amount=Decimal("8"),
            ttl_minutes=5,
            status=ExchangeRequest.Status.NEW,
        )

        dash = self.client.get(f"/api/telegram/admin/dashboard/?bot_id={self.bot.id}")
        self.assertEqual(dash.status_code, 200, dash.content)
        dash_ids = [item["id"] for item in dash.json()["exchange_requests"]["items"]]
        self.assertIn(req.id, dash_ids)
        self.assertNotIn(other_req.id, dash_ids)

        listed = self.client.get(
            f"/api/telegram/exchange-requests/?bot_id={self.bot.id}"
        )
        self.assertEqual(listed.status_code, 200, listed.content)
        list_ids = self._exchange_list_ids(listed)
        self.assertIn(req.id, list_ids)
        self.assertNotIn(other_req.id, list_ids)

    def test_exchange_request_patch_status_and_hold(self):
        self.client.force_authenticate(self.mgmt)
        customer = CustomerProfile.objects.create(telegram_user_id=2100)
        req = ExchangeRequest.objects.create(
            customer=customer,
            bot=self.bot,
            source_currency="USD",
            target_currency="EUR",
            amount=Decimal("3"),
            ttl_minutes=5,
            status=ExchangeRequest.Status.NEW,
        )
        patched = self.client.patch(
            f"/api/telegram/exchange-requests/{req.pk}/",
            {"status": "successful"},
            format="json",
        )
        self.assertEqual(patched.status_code, 200, patched.content)
        self.assertEqual(patched.json()["status"], "successful")
        req.refresh_from_db()
        self.assertEqual(req.status, ExchangeRequest.Status.SUCCESSFUL)

        held = self.client.post(f"/api/telegram/exchange-requests/{req.pk}/hold/")
        self.assertEqual(held.status_code, 200, held.content)
        self.assertEqual(held.json()["ttl_minutes"], 10)
        req.refresh_from_db()
        self.assertEqual(req.ttl_minutes, 10)

        req.status = ExchangeRequest.Status.NEW
        req.ttl_minutes = 10
        req.save(update_fields=["status", "ttl_minutes"])
        patched_hold = self.client.patch(
            f"/api/telegram/exchange-requests/{req.pk}/",
            {"action": "hold"},
            format="json",
        )
        self.assertEqual(patched_hold.status_code, 200, patched_hold.content)
        req.refresh_from_db()
        self.assertEqual(req.ttl_minutes, 15)

    def test_employee_cannot_patch_or_hold_exchange_request(self):
        employee = CustomUser.objects.create_user(
            username="dash-emp",
            password="pass12345",
            role=CustomUser.ROLE_EMPLOYEE,
        )
        customer = CustomerProfile.objects.create(telegram_user_id=2101)
        req = ExchangeRequest.objects.create(
            customer=customer,
            bot=self.bot,
            source_currency="USD",
            target_currency="EUR",
            amount=Decimal("3"),
            ttl_minutes=5,
            status=ExchangeRequest.Status.NEW,
        )
        self.client.force_authenticate(employee)
        patched = self.client.patch(
            f"/api/telegram/exchange-requests/{req.pk}/",
            {"status": "successful"},
            format="json",
        )
        self.assertEqual(patched.status_code, 403)
        held = self.client.post(f"/api/telegram/exchange-requests/{req.pk}/hold/")
        self.assertEqual(held.status_code, 403)
        req.refresh_from_db()
        self.assertEqual(req.status, ExchangeRequest.Status.NEW)
        self.assertEqual(req.ttl_minutes, 5)


class TelegramAdminReengageApiTests(APITestCase):
    def setUp(self):
        self.mgmt = CustomUser.objects.create_user(
            username="re-mgmt",
            password="pass12345",
            role=CustomUser.ROLE_MANAGEMENT,
        )
        self.other = CustomUser.objects.create_user(
            username="re-other",
            password="pass12345",
            role=CustomUser.ROLE_MANAGEMENT,
        )
        self.bot = TelegramBot.objects.create(
            name="ReBot",
            token="444:DDD",
            owner=self.mgmt,
            is_active=True,
        )
        self.other_bot = TelegramBot.objects.create(
            name="ReOther",
            token="555:EEE",
            owner=self.other,
            is_active=True,
        )
        CustomerProfile.objects.create(
            telegram_user_id=2001, username="vip1", tag="vip"
        )
        CustomerProfile.objects.create(
            telegram_user_id=2002, username="g1", tag="global"
        )
        BotSession.objects.create(
            telegram_user_id=2001,
            bot=self.bot,
            state=BotSession.State.MAIN_MENU,
        )
        BotSession.objects.create(
            telegram_user_id=2002,
            bot=self.bot,
            state=BotSession.State.MAIN_MENU,
        )

    @patch("telegram_app.services.reengage_service.TelegramService")
    def test_reengage_vip_audience(self, service_cls):
        service_cls.return_value.send_message.return_value = (True, "ok", 1)
        self.client.force_authenticate(self.mgmt)
        r = self.client.post(
            "/api/telegram/admin/reengage/",
            {"audience": "vip", "message": "Hello VIP"},
            format="json",
        )
        self.assertEqual(r.status_code, 200, r.content)
        body = r.json()
        self.assertEqual(body["sent"], 1)
        self.assertEqual(body["failed"], 0)
        service_cls.return_value.send_message.assert_called_once_with(
            chat_id=2001, text="Hello VIP", parse_mode=None
        )

    @patch("telegram_app.services.reengage_service.TelegramService")
    def test_reengage_excludes_staff_admin_ids(self, service_cls):
        CustomUser.objects.create_user(
            username="vip-admin",
            password="pass12345",
            role=CustomUser.ROLE_SUPER_ADMIN,
            telegram_id="2001",
        )
        service_cls.return_value.send_message.return_value = (True, "ok", 1)
        self.client.force_authenticate(self.mgmt)
        r = self.client.post(
            "/api/telegram/admin/reengage/",
            {"audience": "vip", "message": "Hello VIP"},
            format="json",
        )
        self.assertEqual(r.status_code, 200, r.content)
        body = r.json()
        self.assertEqual(body["sent"], 0)
        self.assertEqual(body["failed"], 0)
        service_cls.return_value.send_message.assert_not_called()

    def test_reengage_forbidden_other_bot(self):
        self.client.force_authenticate(self.mgmt)
        r = self.client.post(
            "/api/telegram/admin/reengage/",
            {
                "bot_id": self.other_bot.id,
                "audience": "global",
                "message": "Nope",
            },
            format="json",
        )
        self.assertEqual(r.status_code, 403, r.content)

    @patch("telegram_app.services.reengage_service.TelegramService")
    def test_reengage_inactive_audience(self, service_cls):
        service_cls.return_value.send_message.return_value = (True, "ok", 1)
        past = timezone.now() - timedelta(days=45)
        BotSession.objects.filter(telegram_user_id=2002, bot=self.bot).update(
            last_activity=past
        )
        self.client.force_authenticate(self.mgmt)
        r = self.client.post(
            "/api/telegram/admin/reengage/",
            {"audience": "inactive", "message": "Miss you"},
            format="json",
        )
        self.assertEqual(r.status_code, 200, r.content)
        body = r.json()
        self.assertEqual(body["sent"], 1)
        service_cls.return_value.send_message.assert_called_once_with(
            chat_id=2002, text="Miss you", parse_mode=None
        )

    @patch("telegram_app.services.reengage_service.TelegramService")
    def test_reengage_surfaces_send_error(self, service_cls):
        service_cls.return_value.send_message.return_value = (
            False,
            "can't parse entities: unsupported start tag",
            None,
        )
        self.client.force_authenticate(self.mgmt)
        r = self.client.post(
            "/api/telegram/admin/reengage/",
            {"audience": "vip", "message": "<b>broken"},
            format="json",
        )
        self.assertEqual(r.status_code, 200, r.content)
        body = r.json()
        self.assertEqual(body["sent"], 0)
        self.assertEqual(body["failed"], 1)
        self.assertIn("can't parse entities", body["last_error"])


class AnalyticsServiceTests(TestCase):
    def setUp(self):
        self.bot = TelegramBot.objects.create(name="AnalyticsBot", token="777:GGG")
        self.customer = CustomerProfile.objects.create(
            telegram_user_id=9001, tag=CustomerProfile.Tag.VIP
        )
        BotSession.objects.create(
            telegram_user_id=9001,
            bot=self.bot,
            state=BotSession.State.MAIN_MENU,
        )
        ExchangeRequest.objects.create(
            customer=self.customer,
            bot=self.bot,
            source_currency="USD",
            target_currency="EUR",
            amount=Decimal("1"),
            ttl_minutes=5,
            status=ExchangeRequest.Status.SUCCESSFUL,
        )

    def test_daily_usage_backfill(self):
        from telegram_app.services.analytics_service import (
            backfill_daily_usage,
            daily_usage_rows,
        )

        backfill_daily_usage(self.bot, days=7)
        rows = daily_usage_rows(self.bot)
        self.assertTrue(len(rows) >= 1)

    def test_new_members_dual(self):
        from telegram_app.models import BotCustomerGrowthSnapshot, TelegramChannel
        from telegram_app.services.analytics_service import new_members_dual

        ch = TelegramChannel.objects.create(
            bot=self.bot, name="News", chat_id="-1001", bot_admin_verified=True, last_member_count=1100
        )
        from telegram_app.models import ChannelMemberSnapshot

        past = timezone.now() - timedelta(days=35)
        snap = ChannelMemberSnapshot.objects.create(
            channel=ch, member_count=1000, bot_is_admin=True
        )
        ChannelMemberSnapshot.objects.filter(pk=snap.pk).update(sampled_at=past)
        BotCustomerGrowthSnapshot.objects.create(
            bot=self.bot, date=timezone.now().date(), new_customers=3
        )
        dual = new_members_dual(self.bot, 1)
        self.assertGreaterEqual(dual["channel_growth"], 100)
        self.assertGreaterEqual(dual["bot_dm_growth"], 0)

    def test_customer_analysis_vip_ratio_and_peak(self):
        from telegram_app.services.analytics_service import customer_analysis

        global_customer = CustomerProfile.objects.create(
            telegram_user_id=9002, tag=CustomerProfile.Tag.GLOBAL
        )
        BotSession.objects.create(
            telegram_user_id=9002,
            bot=self.bot,
            state=BotSession.State.MAIN_MENU,
        )
        ExchangeRequest.objects.create(
            customer=global_customer,
            bot=self.bot,
            source_currency="EUR",
            target_currency="USD",
            amount=Decimal("1"),
            ttl_minutes=5,
            status=ExchangeRequest.Status.SUCCESSFUL,
        )
        analysis = customer_analysis(self.bot)
        self.assertIn("peak_hours", analysis)
        self.assertEqual(len(analysis["peak_hours"]), 24)
        self.assertIsNotNone(analysis["vip_vs_ordinary_request_ratio"])


class ChannelMemberSnapshotTests(TestCase):
    @patch("telegram_app.services.telegram_client.TelegramService")
    def test_snapshot_channel_members_for_bot(self, service_cls):
        from telegram_app.models import ChannelMemberSnapshot, TelegramChannel
        from telegram_app.services.analytics_service import snapshot_channel_members_for_bot

        bot = TelegramBot.objects.create(name="SnapBot", token="111:AAA")
        ch = TelegramChannel.objects.create(bot=bot, name="Main", chat_id="-10099")
        service_cls.return_value.get_me.return_value = (True, {"id": 42}, None)
        service_cls.return_value.get_chat_member.return_value = (
            True,
            {"status": "administrator"},
            None,
        )
        service_cls.return_value.get_chat_member_count.return_value = (True, 1500, None)

        result = snapshot_channel_members_for_bot(bot)
        self.assertEqual(result["sampled"], 1)
        ch.refresh_from_db()
        self.assertEqual(ch.last_member_count, 1500)
        self.assertTrue(ch.bot_admin_verified)
        self.assertEqual(ChannelMemberSnapshot.objects.filter(channel=ch).count(), 1)


class ReengageCampaignRunnerTests(TestCase):
    @patch("telegram_app.services.reengage_service.TelegramService")
    def test_run_due_campaigns(self, service_cls):
        from telegram_app.models import CampaignDeliveryLog, ReengageCampaign
        from telegram_app.services.reengage_service import run_due_campaigns

        bot = TelegramBot.objects.create(name="CampRun", token="222:BBB")
        CustomerProfile.objects.create(telegram_user_id=5001, tag="global")
        BotSession.objects.create(
            telegram_user_id=5001,
            bot=bot,
            state=BotSession.State.MAIN_MENU,
        )
        service_cls.return_value.send_message.return_value = (True, "ok", 1)
        ReengageCampaign.objects.create(
            bot=bot,
            audience="global",
            message="Hello",
            schedule=ReengageCampaign.Schedule.DAILY,
            is_active=True,
            next_run_at=timezone.now() - timedelta(minutes=1),
        )
        summary = run_due_campaigns()
        self.assertEqual(summary["campaigns_run"], 1)
        self.assertEqual(summary["total_sent"], 1)
        self.assertEqual(CampaignDeliveryLog.objects.count(), 1)


class ReengageCampaignApiTests(APITestCase):
    def setUp(self):
        self.mgmt = CustomUser.objects.create_user(
            username="camp-mgmt",
            password="pass12345",
            role=CustomUser.ROLE_MANAGEMENT,
        )
        self.bot = TelegramBot.objects.create(
            name="CampBot",
            token="888:HHH",
            owner=self.mgmt,
            is_active=True,
        )

    def test_create_and_list_campaign(self):
        self.client.force_authenticate(self.mgmt)
        r = self.client.post(
            "/api/telegram/admin/campaigns/",
            {
                "bot_id": self.bot.id,
                "audience": "global",
                "message": "Weekly hello",
                "schedule": "weekly",
                "is_active": True,
            },
            format="json",
        )
        self.assertEqual(r.status_code, 201, r.content)
        r2 = self.client.get(f"/api/telegram/admin/campaigns/?bot_id={self.bot.id}")
        self.assertEqual(r2.status_code, 200)
        self.assertEqual(len(r2.json()), 1)

    @patch("telegram_app.services.reengage_service.TelegramService")
    def test_create_offer_send_now(self, service_cls):
        service_cls.return_value.send_message.return_value = (True, "ok", 1)
        CustomerProfile.objects.create(telegram_user_id=3001, tag="global")
        BotSession.objects.create(
            telegram_user_id=3001,
            bot=self.bot,
            state=BotSession.State.MAIN_MENU,
        )
        self.client.force_authenticate(self.mgmt)
        r = self.client.post(
            "/api/telegram/admin/offers/",
            {
                "bot_id": self.bot.id,
                "title": "Deal",
                "body": "10% off",
                "audience": "global",
                "send_now": True,
            },
            format="json",
        )
        self.assertEqual(r.status_code, 201, r.content)
        self.assertEqual(r.json()["send_result"]["sent"], 1)


class DashboardSnapshotApiTests(APITestCase):
    def setUp(self):
        self.mgmt = CustomUser.objects.create_user(
            username="snap-mgmt",
            password="pass12345",
            role=CustomUser.ROLE_MANAGEMENT,
        )
        self.bot = TelegramBot.objects.create(
            name="SnapBot",
            token="999:III",
            owner=self.mgmt,
            is_active=True,
        )

    def test_dashboard_includes_channel_members(self):
        from telegram_app.models import BotDailyUsageSnapshot

        BotDailyUsageSnapshot.objects.create(
            bot=self.bot,
            date=timezone.now().date(),
            active_users=5,
        )
        self.client.force_authenticate(self.mgmt)
        r = self.client.get("/api/telegram/admin/dashboard/")
        self.assertEqual(r.status_code, 200, r.content)
        body = r.json()
        self.assertIn("channel_members", body["analytics"])
        self.assertIn("new_members_detail", body["exchange_requests"])

    def test_channel_snapshots_endpoint(self):
        from telegram_app.models import TelegramChannel

        ch = TelegramChannel.objects.create(
            bot=self.bot,
            name="Snap Ch",
            chat_id="-1001",
            bot_admin_verified=True,
            last_member_count=500,
        )
        from telegram_app.models import ChannelMemberSnapshot

        ChannelMemberSnapshot.objects.create(
            channel=ch, member_count=400, bot_is_admin=True
        )
        self.client.force_authenticate(self.mgmt)
        r = self.client.get("/api/telegram/admin/snapshots/channel-members/?months=1")
        self.assertEqual(r.status_code, 200, r.content)
        body = r.json()
        self.assertIn("growth", body)
        self.assertIn("history", body)
        self.assertEqual(len(body["history"]), 1)


class DuplicateBotTokenTests(TestCase):
    def test_poller_keeps_one_row_per_token(self):
        from telegram_app.management.commands.poll_telegram_bots import bots_one_per_token

        keeper = TelegramBot.objects.create(name="Keep", token="111:AAA", is_active=True)
        duplicate = TelegramBot.objects.create(name="Dup", token="111:AAA", is_active=True)
        other = TelegramBot.objects.create(name="Other", token="222:BBB", is_active=True)
        keepers, skipped = bots_one_per_token([keeper, duplicate, other])
        self.assertEqual([b.pk for b in keepers], [keeper.pk, other.pk])
        self.assertEqual([(d.pk, k.pk) for d, k in skipped], [(duplicate.pk, keeper.pk)])

    def test_detail_serializer_rejects_duplicate_token(self):
        from telegram_app.serializers import TelegramBotDetailSerializer

        TelegramBot.objects.create(name="Keep", token="111:AAA", is_active=True)
        ser = TelegramBotDetailSerializer(data={"name": "Dup", "token": "111:AAA"})
        self.assertFalse(ser.is_valid())
        self.assertIn("token", ser.errors)


class BotfatherTokenValidationTests(TestCase):
    def test_rejects_placeholder_without_colon(self):
        from telegram_app.services.telegram_token import is_valid_botfather_token

        self.assertFalse(is_valid_botfather_token("token_ig"))
        self.assertFalse(is_valid_botfather_token(""))
        self.assertFalse(is_valid_botfather_token(None))

    def test_accepts_botfather_shape(self):
        from telegram_app.services.telegram_token import is_valid_botfather_token

        self.assertTrue(
            is_valid_botfather_token(
                "123456789:AAHabcdefghijklmnopqrstuvwxyz0123456789"
            )
        )
