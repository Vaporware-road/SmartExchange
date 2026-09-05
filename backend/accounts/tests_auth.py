"""Email login, one-time codes, Google sign-in and the read-only trial wall."""
from unittest.mock import patch

from django.conf import settings
from django.core import mail
from django.core.cache import cache
from django.test import override_settings
from django.utils import timezone
from rest_framework.test import APITestCase

from accounts.models import CustomUser, OtpCode, UserActivityLog
from accounts.otp import issue_code, verify_code
from accounts.scoping import unscoped
from category.models import Category


def _signup(**overrides):
    fields = {
        "username": "desk",
        "password": "pass12345",
        "role": CustomUser.ROLE_MANAGEMENT,
        "email": "desk@example.com",
    }
    fields.update(overrides)
    with unscoped():
        return CustomUser.objects.create_user(**fields)


class EmailLoginTests(APITestCase):
    def setUp(self):
        cache.clear()
        self.user = _signup()

    def test_login_with_email(self):
        r = self.client.post(
            "/api/auth/login/",
            {"identifier": "desk@example.com", "password": "pass12345"},
            format="json",
        )
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["user"]["username"], "desk")

    def test_login_with_email_is_case_insensitive(self):
        r = self.client.post(
            "/api/auth/login/",
            {"identifier": "DESK@Example.com", "password": "pass12345"},
            format="json",
        )
        self.assertEqual(r.status_code, 200)

    def test_username_login_still_works(self):
        r = self.client.post(
            "/api/auth/login/", {"username": "desk", "password": "pass12345"}, format="json"
        )
        self.assertEqual(r.status_code, 200)

    def test_wrong_password_is_rejected_and_logged(self):
        r = self.client.post(
            "/api/auth/login/",
            {"identifier": "desk@example.com", "password": "nope"},
            format="json",
        )
        self.assertEqual(r.status_code, 400)
        with unscoped():
            self.assertTrue(
                UserActivityLog.objects.filter(
                    action_type=UserActivityLog.ACTION_LOGIN_FAILED
                ).exists()
            )

    def test_an_expired_trial_can_still_sign_in(self):
        self.user.trial_started_at = timezone.now() - timezone.timedelta(days=30)
        self.user.trial_expires_at = timezone.now() - timezone.timedelta(days=1)
        self.user.save(update_fields=["trial_started_at", "trial_expires_at"])
        r = self.client.post(
            "/api/auth/login/",
            {"identifier": "desk@example.com", "password": "pass12345"},
            format="json",
        )
        self.assertEqual(r.status_code, 200)


class TrialWallTests(APITestCase):
    def setUp(self):
        cache.clear()
        self.user = _signup()
        self.user.trial_started_at = timezone.now() - timezone.timedelta(days=30)
        self.user.trial_expires_at = timezone.now() - timezone.timedelta(days=1)
        self.user.save(update_fields=["trial_started_at", "trial_expires_at"])
        tokens = self.client.post(
            "/api/auth/login/",
            {"identifier": "desk@example.com", "password": "pass12345"},
            format="json",
        ).json()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {tokens['access']}")

    def test_reads_still_work(self):
        self.assertEqual(self.client.get("/api/categories/").status_code, 200)

    def test_writes_are_walled_with_support_channels(self):
        r = self.client.post("/api/categories/", {"name": "Gold"}, format="json")
        self.assertEqual(r.status_code, 403)
        body = r.json()
        self.assertEqual(body["code"], "trial_expired")
        self.assertIn("support_channels", body)
        with unscoped():
            self.assertFalse(Category.all_objects.filter(name="Gold").exists())


# The real 15/hour ceiling is exercised by the throttle itself; here it would
# only make the multi-attempt tests depend on each other through the cache.
@override_settings(
    REST_FRAMEWORK={**settings.REST_FRAMEWORK, "DEFAULT_THROTTLE_RATES": {
        **settings.REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"], "otp": "1000/hour",
    }}
)
class OtpTests(APITestCase):
    def setUp(self):
        cache.clear()
        self.user = _signup()
        self.client.force_authenticate(self.user)

    def test_request_emails_a_code_and_verify_marks_the_address_proven(self):
        r = self.client.post("/api/auth/otp/request/", {}, format="json")
        self.assertEqual(r.status_code, 200)
        self.assertTrue(r.json()["sent"])
        self.assertEqual(r.json()["channel"], OtpCode.CHANNEL_EMAIL)
        self.assertEqual(len(mail.outbox), 1)

        code = self._sent_code()
        r = self.client.post("/api/auth/otp/verify/", {"code": code}, format="json")
        self.assertEqual(r.status_code, 200)
        self.user.refresh_from_db()
        self.assertIsNotNone(self.user.email_verified_at)

    def test_the_code_is_never_stored_in_the_clear(self):
        self.client.post("/api/auth/otp/request/", {}, format="json")
        otp = OtpCode.objects.get(user=self.user)
        self.assertNotIn(self._sent_code(), otp.code_hash)

    def test_a_code_cannot_be_reused(self):
        self.client.post("/api/auth/otp/request/", {}, format="json")
        code = self._sent_code()
        self.client.post("/api/auth/otp/verify/", {"code": code}, format="json")
        self.user.email_verified_at = None
        self.user.save(update_fields=["email_verified_at"])
        r = self.client.post("/api/auth/otp/verify/", {"code": code}, format="json")
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()["code"], "otp_not_requested")

    def test_the_code_dies_after_five_wrong_guesses(self):
        self.client.post("/api/auth/otp/request/", {}, format="json")
        code = self._sent_code()
        wrong = "000000" if code != "000000" else "111111"
        for _ in range(OtpCode.MAX_ATTEMPTS):
            self.client.post("/api/auth/otp/verify/", {"code": wrong}, format="json")
        r = self.client.post("/api/auth/otp/verify/", {"code": code}, format="json")
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()["code"], "otp_too_many_attempts")

    def test_an_expired_code_is_refused(self):
        otp, _ = issue_code(self.user)
        otp.expires_at = timezone.now() - timezone.timedelta(seconds=1)
        otp.save(update_fields=["expires_at"])
        ok, reason = verify_code(self.user, self._sent_code())
        self.assertFalse(ok)
        self.assertEqual(reason, "otp_expired")

    def test_requesting_again_retires_the_previous_code(self):
        self.client.post("/api/auth/otp/request/", {}, format="json")
        first = self._sent_code()
        self.client.post("/api/auth/otp/request/", {}, format="json")
        r = self.client.post("/api/auth/otp/verify/", {"code": first}, format="json")
        self.assertEqual(r.status_code, 400)

    @override_settings(SMS_PROVIDER="mock")
    def test_sms_is_the_fallback_when_there_is_no_email(self):
        self.user.email = ""
        self.user.phone = "+447700900000"
        self.user.save(update_fields=["email", "phone"])
        r = self.client.post("/api/auth/otp/request/", {}, format="json")
        self.assertEqual(r.json()["channel"], OtpCode.CHANNEL_SMS)
        self.assertTrue(r.json()["sent"])

    def _sent_code(self):
        """The most recent code, read back out of the outbox."""
        import re

        body = mail.outbox[-1].body
        return re.search(r"\b(\d{6})\b", body).group(1)


_CLAIMS = {
    "sub": "google-sub-1",
    "email": "new@example.com",
    "email_verified": True,
    "given_name": "New",
    "family_name": "Customer",
}


@override_settings(GOOGLE_OAUTH_CLIENT_ID="client-id.apps.googleusercontent.com")
class GoogleAuthTests(APITestCase):
    def setUp(self):
        cache.clear()

    def test_disabled_without_a_client_id(self):
        with override_settings(GOOGLE_OAUTH_CLIENT_ID=""):
            r = self.client.post("/api/auth/google/", {"credential": "x"}, format="json")
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()["code"], "google_auth_disabled")

    @patch("accounts.api_views.verify_id_token", return_value=None)
    def test_an_unverifiable_token_is_rejected(self, _verify):
        r = self.client.post("/api/auth/google/", {"credential": "forged"}, format="json")
        self.assertEqual(r.status_code, 401)

    @patch("accounts.api_views.verify_id_token", return_value=_CLAIMS)
    def test_a_new_google_user_gets_their_own_verified_account(self, _verify):
        r = self.client.post("/api/auth/google/", {"credential": "ok"}, format="json")
        self.assertEqual(r.status_code, 201)
        self.assertTrue(r.json()["created"])
        with unscoped():
            user = CustomUser.objects.get(email="new@example.com")
        self.assertEqual(user.google_sub, "google-sub-1")
        self.assertIsNotNone(user.email_verified_at)
        self.assertIsNotNone(user.trial_expires_at)
        self.assertFalse(user.has_usable_password())
        self.assertIsNotNone(user.account_id)

    @patch("accounts.api_views.verify_id_token", return_value=_CLAIMS)
    def test_an_existing_password_account_is_linked_not_duplicated(self, _verify):
        existing = _signup(username="existing", email="new@example.com")
        r = self.client.post("/api/auth/google/", {"credential": "ok"}, format="json")
        self.assertEqual(r.status_code, 200)
        self.assertFalse(r.json()["created"])
        existing.refresh_from_db()
        self.assertEqual(existing.google_sub, "google-sub-1")
        with unscoped():
            self.assertEqual(CustomUser.objects.filter(email="new@example.com").count(), 1)

    @patch(
        "accounts.api_views.verify_id_token",
        return_value={**_CLAIMS, "email_verified": True, "sub": "google-sub-2"},
    )
    def test_signing_in_twice_reuses_the_same_account(self, _verify):
        self.client.post("/api/auth/google/", {"credential": "ok"}, format="json")
        r = self.client.post("/api/auth/google/", {"credential": "ok"}, format="json")
        self.assertEqual(r.status_code, 200)
        with unscoped():
            self.assertEqual(CustomUser.objects.filter(email="new@example.com").count(), 1)
