from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase

from accounts.models import CustomUser, UserActivityLog
from accounts.plans import PLAN_BRONZE, PLAN_GOLD
from price_publisher.models import PriceTemplate
from telegram_app.models import BotAdmin, TelegramBot


def _tiny_png():
    return SimpleUploadedFile(
        "bg.png",
        b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01"
        b"\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc\xf8\x0f\x00"
        b"\x00\x01\x01\x00\x05\x18\xd8N\x00\x00\x00\x00IEND\xaeB`\x82",
        content_type="image/png",
    )


class ProgrammerHubApiTests(APITestCase):
    def setUp(self):
        self.programmer = CustomUser.objects.create_user(
            username="dev",
            password="pass12345",
            role=CustomUser.ROLE_DEVELOPER,
        )
        self.staff = CustomUser.objects.create_user(
            username="desk",
            password="pass12345",
            role=CustomUser.ROLE_MANAGEMENT,
            plan=PLAN_BRONZE,
            email="desk@example.com",
        )
        self.employee = CustomUser.objects.create_user(
            username="emp",
            password="pass12345",
            role=CustomUser.ROLE_EMPLOYEE,
        )

    def test_employee_cannot_list_users(self):
        self.client.force_authenticate(self.employee)
        r = self.client.get("/api/auth/users/")
        self.assertEqual(r.status_code, 403)

    def test_programmer_lists_users(self):
        self.client.force_authenticate(self.programmer)
        r = self.client.get("/api/auth/users/")
        self.assertEqual(r.status_code, 200)
        body = r.json()
        items = body["results"] if isinstance(body, dict) and "results" in body else body
        self.assertGreaterEqual(len(items), 2)

    def test_register_and_upgrade_plan(self):
        self.client.force_authenticate(self.programmer)
        r = self.client.post(
            "/api/auth/programmer/users/",
            {
                "first_name": "Ada",
                "last_name": "Lovelace",
                "exchange_name": "Ada FX",
                "country": "UK",
                "email": "ada@example.com",
                "phone": "+44111",
                "telegram_id": "123",
                "telegram_bot_token": "111:bot-token-plain",
                "plan": "silver",
            },
            format="json",
        )
        self.assertEqual(r.status_code, 201, r.content)
        data = r.json()
        self.assertEqual(data["plan"], "silver")
        self.assertEqual(data["role"], CustomUser.ROLE_MANAGEMENT)
        self.assertTrue(data.get("generated_password"))
        self.assertIn("…", data.get("telegram_bot_token_masked") or "")
        user = CustomUser.objects.get(email="ada@example.com")
        bot = TelegramBot.objects.get(owner=user)
        self.assertNotEqual(bot.token, "111:bot-token-plain")
        self.assertEqual(bot.get_plain_token(), "111:bot-token-plain")

        r2 = self.client.patch(
            f"/api/auth/programmer/users/{user.pk}/",
            {"plan": "gold"},
            format="json",
        )
        self.assertEqual(r2.status_code, 200, r2.content)
        self.assertEqual(r2.json()["plan"], "gold")

    def test_programmer_user_account_detail_tabs(self):
        self.client.force_authenticate(self.programmer)
        TelegramBot.objects.create(
            name="Desk Bot",
            token="222:desk-bot-token",
            owner=self.staff,
            is_active=True,
        )
        UserActivityLog.objects.create(
            user=self.staff,
            action_type=UserActivityLog.ACTION_LOGIN_SUCCESS,
            details="test",
        )
        PriceTemplate.objects.create(
            name="Bronze board",
            template_type=PriceTemplate.TemplateType.DEFAULT,
            background_image=_tiny_png(),
            plan=PLAN_BRONZE,
        )
        PriceTemplate.objects.create(
            name="Gold board",
            template_type=PriceTemplate.TemplateType.DEFAULT,
            background_image=_tiny_png(),
            plan=PLAN_GOLD,
        )
        r = self.client.get(f"/api/auth/programmer/users/{self.staff.pk}/")
        self.assertEqual(r.status_code, 200, r.content)
        data = r.json()
        self.assertEqual(data["user"]["id"], self.staff.pk)
        self.assertEqual(len(data["bots"]), 1)
        self.assertIn("…", data["bots"][0]["token_masked"])
        self.assertEqual(len(data["audit_logs"]), 1)
        price_names = {row["name"] for row in data["templates"]["price_templates"]}
        self.assertIn("Bronze board", price_names)
        self.assertNotIn("Gold board", price_names)
        self.assertIn("telegram_analytics", data)
        self.assertEqual(len(data["telegram_analytics"]), 1)
        self.assertIn("analytics", data["telegram_analytics"][0])

    def test_impersonate_and_nested_denied(self):
        self.client.force_authenticate(self.programmer)
        r = self.client.post(f"/api/auth/impersonate/{self.staff.pk}/")
        self.assertEqual(r.status_code, 200, r.content)
        access = r.json()["access"]
        self.assertTrue(
            UserActivityLog.objects.filter(
                user=self.programmer,
                action_type=UserActivityLog.ACTION_IMPERSONATE_START,
            ).exists()
        )
        self.client.force_authenticate(user=None)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
        me = self.client.get("/api/auth/me/")
        self.assertEqual(me.status_code, 200)
        self.assertEqual(me.json()["username"], "desk")
        self.assertEqual(me.json()["impersonated_by"]["username"], "dev")
        nested = self.client.post(f"/api/auth/impersonate/{self.employee.pk}/")
        self.assertIn(nested.status_code, (400, 403))

    def test_cannot_impersonate_self(self):
        self.client.force_authenticate(self.programmer)
        r = self.client.post(f"/api/auth/impersonate/{self.programmer.pk}/")
        self.assertEqual(r.status_code, 400)

    def test_bronze_cannot_fetch_gold_template(self):
        gold_tpl = PriceTemplate.objects.create(
            name="Gold board",
            template_type=PriceTemplate.TemplateType.DEFAULT,
            background_image=_tiny_png(),
            plan=PLAN_GOLD,
        )
        bronze_tpl = PriceTemplate.objects.create(
            name="Bronze board",
            template_type=PriceTemplate.TemplateType.DEFAULT,
            background_image=_tiny_png(),
            plan=PLAN_BRONZE,
        )
        self.client.force_authenticate(self.staff)
        listed = self.client.get("/api/templates/")
        self.assertEqual(listed.status_code, 200)
        payload = listed.json()
        rows = payload if isinstance(payload, list) else payload.get("results", [])
        ids = {row["id"] for row in rows}
        self.assertIn(bronze_tpl.id, ids)
        self.assertNotIn(gold_tpl.id, ids)
        denied = self.client.get(f"/api/templates/{gold_tpl.id}/")
        self.assertEqual(denied.status_code, 403)
        ok = self.client.get(f"/api/templates/{bronze_tpl.id}/")
        self.assertEqual(ok.status_code, 200)


class ProgrammerDelegatedOperatorApiTests(APITestCase):
    """Registering/editing delegated sub-operators via the Programmer Hub."""

    def setUp(self):
        self.programmer = CustomUser.objects.create_user(
            username="dev2",
            password="pass12345",
            role=CustomUser.ROLE_DEVELOPER,
        )
        self.owner = CustomUser.objects.create_user(
            username="owner_client",
            password="pass12345",
            role=CustomUser.ROLE_MANAGEMENT,
            plan=PLAN_GOLD,
        )
        self.bot = TelegramBot.objects.create(
            name="Owner Bot",
            token="333:owner-bot-token",
            owner=self.owner,
            is_active=True,
        )

    def _register_payload(self, **overrides):
        payload = {
            "first_name": "Sub",
            "last_name": "Operator",
            "exchange_name": "Sub FX",
            "country": "IR",
            "email": "subop@example.com",
            "phone": "+98911",
            "telegram_id": "999000111",
            "telegram_username": "subop_tg",
            "sub_role": CustomUser.SUB_ROLE_OPERATOR,
            "owner_username": "owner_client",
        }
        payload.update(overrides)
        return payload

    def test_register_delegated_operator_grants_bot_admin(self):
        self.client.force_authenticate(self.programmer)
        r = self.client.post(
            "/api/auth/programmer/users/", self._register_payload(), format="json"
        )
        self.assertEqual(r.status_code, 201, r.content)
        data = r.json()
        self.assertEqual(data["role"], CustomUser.ROLE_EMPLOYEE)
        self.assertEqual(data["sub_role"], CustomUser.SUB_ROLE_OPERATOR)
        self.assertEqual(data["owner"], self.owner.pk)
        self.assertEqual(data["owner_name"], "owner_client")
        self.assertEqual(data["telegram_username"], "subop_tg")

        user = CustomUser.objects.get(email="subop@example.com")
        self.assertEqual(user.owner_id, self.owner.pk)
        # No bot is created for delegated operators (they use the owner's bot).
        self.assertFalse(TelegramBot.objects.filter(owner=user).exists())
        # Auto-synced BotAdmin row grants in-bot admin access.
        self.assertTrue(BotAdmin.objects.filter(bot=self.bot, user=user).exists())

    def test_register_client_account_still_requires_bot_token(self):
        self.client.force_authenticate(self.programmer)
        payload = self._register_payload(sub_role=CustomUser.SUB_ROLE_ADMIN, owner_username="")
        r = self.client.post("/api/auth/programmer/users/", payload, format="json")
        self.assertEqual(r.status_code, 400, r.content)
        self.assertIn("telegram_bot_token", r.json()["errors"])

    def test_register_delegated_operator_requires_owner(self):
        self.client.force_authenticate(self.programmer)
        payload = self._register_payload(owner_username="")
        r = self.client.post("/api/auth/programmer/users/", payload, format="json")
        self.assertEqual(r.status_code, 400, r.content)
        self.assertIn("owner_username", r.json()["errors"])

    def test_update_operator_owner_and_sub_role(self):
        user = CustomUser.objects.create_user(
            username="existing_op",
            password="pass12345",
            role=CustomUser.ROLE_EMPLOYEE,
            sub_role=CustomUser.SUB_ROLE_ADMIN,
        )
        self.client.force_authenticate(self.programmer)
        r = self.client.patch(
            f"/api/auth/programmer/users/{user.pk}/",
            {
                "sub_role": CustomUser.SUB_ROLE_HEAD_OPERATOR,
                "owner_username": "owner_client",
                "telegram_username": "existing_op_tg",
            },
            format="json",
        )
        self.assertEqual(r.status_code, 200, r.content)
        user.refresh_from_db()
        self.assertEqual(user.sub_role, CustomUser.SUB_ROLE_HEAD_OPERATOR)
        self.assertEqual(user.owner_id, self.owner.pk)
        self.assertEqual(user.telegram_username, "existing_op_tg")
        self.assertTrue(BotAdmin.objects.filter(bot=self.bot, user=user).exists())

    def test_update_clears_owner_when_username_empty(self):
        user = CustomUser.objects.create_user(
            username="op_to_revoke",
            password="pass12345",
            role=CustomUser.ROLE_EMPLOYEE,
            sub_role=CustomUser.SUB_ROLE_OPERATOR,
            owner=self.owner,
        )
        self.client.force_authenticate(self.programmer)
        r = self.client.patch(
            f"/api/auth/programmer/users/{user.pk}/",
            {"owner_username": "", "sub_role": CustomUser.SUB_ROLE_ADMIN},
            format="json",
        )
        self.assertEqual(r.status_code, 200, r.content)
        user.refresh_from_db()
        self.assertIsNone(user.owner)
        self.assertFalse(BotAdmin.objects.filter(bot=self.bot, user=user).exists())
