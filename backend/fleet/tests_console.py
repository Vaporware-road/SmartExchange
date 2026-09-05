"""Owner console: logins and IPs, accounts, sales, support channels."""
from decimal import Decimal

from django.utils import timezone
from rest_framework.test import APITestCase

from accounts.models import CustomUser, UserActivityLog
from accounts.scoping import unscoped
from fleet.models import Sale
from setting.models import SupportChannel


class OwnerConsoleTests(APITestCase):
    def setUp(self):
        with unscoped():
            self.owner = CustomUser.objects.create_user(
                username="dev", password="pass12345", role=CustomUser.ROLE_DEVELOPER
            )
            self.desk = CustomUser.objects.create_user(
                username="desk",
                password="pass12345",
                role=CustomUser.ROLE_MANAGEMENT,
                email="desk@example.com",
                trial_started_at=timezone.now(),
                trial_expires_at=timezone.now() - timezone.timedelta(days=1),
            )
            self.other = CustomUser.objects.create_user(
                username="other",
                password="pass12345",
                role=CustomUser.ROLE_MANAGEMENT,
                email="other@example.com",
            )
        self.client.force_authenticate(self.owner)

    # --- logins & IPs ---------------------------------------------------

    def test_activity_shows_email_and_filters_by_ip(self):
        with unscoped():
            UserActivityLog.objects.create(
                user=self.desk,
                action_type=UserActivityLog.ACTION_LOGIN_SUCCESS,
                ip_address="203.0.113.9",
            )
            UserActivityLog.objects.create(
                user=self.other,
                action_type=UserActivityLog.ACTION_LOGIN_SUCCESS,
                ip_address="198.51.100.4",
            )

        body = self.client.get("/api/auth/activity/?ip=203.0.113").json()
        rows = body["results"] if isinstance(body, dict) and "results" in body else body
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["email"], "desk@example.com")
        self.assertEqual(rows[0]["ip_address"], "203.0.113.9")

    def test_activity_free_text_search_matches_email(self):
        with unscoped():
            UserActivityLog.objects.create(
                user=self.other,
                action_type=UserActivityLog.ACTION_SIGNUP,
                ip_address="198.51.100.4",
            )
        body = self.client.get("/api/auth/activity/?q=other@example").json()
        rows = body["results"] if isinstance(body, dict) and "results" in body else body
        self.assertEqual([row["email"] for row in rows], ["other@example.com"])

    def test_activity_is_owner_only(self):
        self.client.force_authenticate(self.desk)
        self.assertEqual(self.client.get("/api/auth/activity/").status_code, 403)

    # --- accounts -------------------------------------------------------

    def test_accounts_list_shows_every_desk_with_its_owner(self):
        body = self.client.get("/api/fleet/accounts/").json()
        rows = body["results"] if isinstance(body, dict) and "results" in body else body
        emails = {row["owner"]["email"] for row in rows if row["owner"]}
        self.assertIn("desk@example.com", emails)
        self.assertIn("other@example.com", emails)

    def test_suspending_an_account_deactivates_it_and_burns_its_tokens(self):
        version = self.desk.token_version
        r = self.client.post(
            f"/api/fleet/accounts/{self.desk.account_id}/suspend/",
            {"is_active": False},
            format="json",
        )
        self.assertEqual(r.status_code, 200)
        self.desk.refresh_from_db()
        self.assertFalse(self.desk.is_active)
        self.assertGreater(self.desk.token_version, version)

    def test_accounts_list_is_owner_only(self):
        self.client.force_authenticate(self.desk)
        self.assertEqual(self.client.get("/api/fleet/accounts/").status_code, 403)

    # --- sales ----------------------------------------------------------

    def test_recording_a_sale_lifts_the_trial_wall_and_issues_a_key(self):
        r = self.client.post(
            "/api/fleet/sales/",
            {
                "customer": self.desk.pk,
                "amount": "399.00",
                "currency": "USD",
                "sale_plan": Sale.PLAN_ONE_TIME,
                "reference": "INV-1",
            },
            format="json",
        )
        self.assertEqual(r.status_code, 201, r.content)

        self.desk.refresh_from_db()
        self.assertIsNone(self.desk.trial_expires_at)
        with unscoped():
            sale = Sale.objects.get(pk=r.json()["id"])
        self.assertEqual(sale.amount, Decimal("399.00"))
        self.assertEqual(sale.customer_email, "desk@example.com")
        self.assertEqual(sale.account_id, self.desk.account_id)
        self.assertEqual(sale.recorded_by_id, self.owner.pk)
        self.assertTrue(self.desk.deployments.first().license_key)

    def test_a_lifted_wall_lets_the_customer_write_again(self):
        self.client.post(
            "/api/fleet/sales/",
            {"customer": self.desk.pk, "amount": "1", "currency": "USD"},
            format="json",
        )
        self.client.force_authenticate(self.desk)
        r = self.client.post("/api/categories/", {"name": "Gold"}, format="json")
        self.assertEqual(r.status_code, 201)

    def test_sales_are_owner_only(self):
        self.client.force_authenticate(self.desk)
        self.assertEqual(self.client.get("/api/fleet/sales/").status_code, 403)
        self.assertEqual(
            self.client.post(
                "/api/fleet/sales/", {"customer": self.desk.pk, "amount": "1"}, format="json"
            ).status_code,
            403,
        )

    # --- support channels -----------------------------------------------

    def test_support_channel_crud_and_public_exposure(self):
        r = self.client.post(
            "/api/settings/support-channels/",
            {"kind": SupportChannel.KIND_WHATSAPP, "label": "Sales", "value": "+44 7700 900000"},
            format="json",
        )
        self.assertEqual(r.status_code, 201, r.content)
        self.assertEqual(r.json()["icon"], "fab fa-whatsapp")
        self.assertEqual(r.json()["href"], "https://wa.me/447700900000")

        self.client.force_authenticate(self.desk)
        site = self.client.get("/api/settings/site/").json()
        self.assertEqual([c["label"] for c in site["support_channels"]], ["Sales"])

    def test_an_inactive_channel_is_not_published(self):
        channel = SupportChannel.objects.create(
            kind=SupportChannel.KIND_PHONE, label="Old", value="+1", is_active=False
        )
        site = self.client.get("/api/settings/site/").json()
        self.assertNotIn("Old", [c["label"] for c in site["support_channels"]])
        self.assertEqual(
            self.client.patch(
                f"/api/settings/support-channels/{channel.pk}/",
                {"is_active": True},
                format="json",
            ).status_code,
            200,
        )

    def test_support_channels_are_owner_only_to_edit(self):
        self.client.force_authenticate(self.desk)
        r = self.client.post(
            "/api/settings/support-channels/",
            {"kind": SupportChannel.KIND_PHONE, "label": "x", "value": "+1"},
            format="json",
        )
        self.assertEqual(r.status_code, 403)
