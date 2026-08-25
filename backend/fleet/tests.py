from datetime import timedelta
from unittest.mock import patch

from django.test import TestCase, override_settings
from django.utils import timezone
from rest_framework.test import APIRequestFactory, force_authenticate

from accounts.models import CustomUser
from accounts.tasks import expire_trials_task
from accounts.trial import ensure_trial_started

from .api_views import (
    FleetCheckinAPIView,
    LicenseReissueAPIView,
    LicensedDeploymentListAPIView,
    TrialConvertAPIView,
    TrialCustomerListAPIView,
    TrialExtendAPIView,
)
from .licensing import generate_license_key
from .models import CustomerDeployment
from .services import convert_to_licensed, ensure_trial_deployment
from .tasks import (
    archive_trial_stack_task,
    send_trial_expiry_reminders_task,
    teardown_lapsed_trials_task,
)


def make_customer(username="acme", **extra):
    return CustomUser.objects.create_user(
        username=username,
        password="pw-for-tests",
        exchange_name=extra.pop("exchange_name", "Acme Exchange"),
        **extra,
    )


class LicenseKeyTest(TestCase):
    def test_key_shape_is_stable_and_unambiguous(self):
        key = generate_license_key()
        self.assertTrue(key.startswith("MREX-"))
        self.assertEqual(len(key.split("-")), 5)
        self.assertFalse(set("IO01") & set(key.replace("MREX", "")))

    def test_keys_are_unique_across_a_large_sample(self):
        keys = {generate_license_key() for _ in range(500)}
        self.assertEqual(len(keys), 500)


class TrialDeploymentTest(TestCase):
    def test_starting_a_trial_registers_a_deployment(self):
        user = make_customer()
        self.assertTrue(ensure_trial_started(user))

        deployment = CustomerDeployment.objects.get(customer=user)
        self.assertEqual(deployment.deployment_type, CustomerDeployment.TYPE_TRIAL)
        self.assertEqual(deployment.status, CustomerDeployment.STATUS_PENDING)
        self.assertEqual(deployment.slug, "trial-acme-exchange")
        self.assertEqual(deployment.domain, "trial-acme-exchange.mrexchange.co.uk")
        self.assertTrue(deployment.license_key)

    def test_second_call_neither_restarts_the_trial_nor_duplicates_the_stack(self):
        user = make_customer()
        ensure_trial_started(user)
        first_expiry = user.trial_expires_at

        self.assertFalse(ensure_trial_started(user))
        self.assertEqual(user.trial_expires_at, first_expiry)
        self.assertEqual(CustomerDeployment.objects.filter(customer=user).count(), 1)

    def test_two_customers_with_the_same_exchange_name_get_distinct_stacks(self):
        first = make_customer("acme1")
        second = make_customer("acme2")
        ensure_trial_deployment(first)
        ensure_trial_deployment(second)

        slugs = set(CustomerDeployment.objects.values_list("slug", flat=True))
        self.assertEqual(len(slugs), 2)

    @override_settings(INDIVIDUAL_TRIAL_DAYS=21)
    def test_trial_length_follows_the_setting(self):
        user = make_customer()
        ensure_trial_started(user)
        span = user.trial_expires_at - user.trial_started_at
        self.assertEqual(span, timedelta(days=21))


@override_settings(TRIAL_GRACE_DAYS=7, TRIAL_REMINDER_DAYS=3)
class TrialLifecycleTaskTest(TestCase):
    def test_reminder_fires_once_inside_the_window(self):
        user = make_customer()
        user.trial_started_at = timezone.now() - timedelta(days=12)
        user.trial_expires_at = timezone.now() + timedelta(days=2)
        user.save()

        with patch("fleet.tasks._notify_staff_of_trial_expiry") as notify:
            self.assertEqual(send_trial_expiry_reminders_task(), {"notified": 1})
            notify.assert_called_once()
            self.assertEqual(send_trial_expiry_reminders_task(), {"notified": 0})

        user.refresh_from_db()
        self.assertIsNotNone(user.trial_expiry_notified_at)

    def test_reminder_ignores_trials_outside_the_window(self):
        user = make_customer()
        user.trial_expires_at = timezone.now() + timedelta(days=10)
        user.save()

        with patch("fleet.tasks._notify_staff_of_trial_expiry"):
            self.assertEqual(send_trial_expiry_reminders_task(), {"notified": 0})

    def test_expiry_does_not_deactivate_until_the_grace_window_is_over(self):
        user = make_customer()
        user.trial_expires_at = timezone.now() - timedelta(days=2)
        user.save()

        self.assertEqual(expire_trials_task(), {"deactivated": 0})
        user.refresh_from_db()
        self.assertTrue(user.is_active)

    def test_expiry_deactivates_once_the_grace_window_has_passed(self):
        user = make_customer()
        user.trial_expires_at = timezone.now() - timedelta(days=9)
        user.save()

        self.assertEqual(expire_trials_task(), {"deactivated": 1})
        user.refresh_from_db()
        self.assertFalse(user.is_active)

    def test_expiry_leaves_the_reminder_stamp_alone(self):
        user = make_customer()
        user.trial_expires_at = timezone.now() - timedelta(days=9)
        user.save()

        expire_trials_task()
        user.refresh_from_db()
        self.assertIsNone(user.trial_expiry_notified_at)

    def test_lapsed_stacks_are_archived_even_where_docker_is_unavailable(self):
        user = make_customer()
        user.trial_expires_at = timezone.now() - timedelta(days=9)
        user.save()
        ensure_trial_deployment(user)

        self.assertEqual(teardown_lapsed_trials_task(), {"archived": 1})
        deployment = CustomerDeployment.objects.get(customer=user)
        self.assertEqual(deployment.status, CustomerDeployment.STATUS_ARCHIVED)
        user.refresh_from_db()
        self.assertFalse(user.is_active)

    def test_archive_task_retires_the_record_where_docker_is_unavailable(self):
        user = make_customer()
        user.trial_expires_at = timezone.now() + timedelta(days=5)
        user.save()
        deployment, _ = ensure_trial_deployment(user)

        result = archive_trial_stack_task(deployment_id=deployment.pk)

        self.assertEqual(result, {"archived": False, "reason": "disabled"})
        deployment.refresh_from_db()
        self.assertEqual(deployment.status, CustomerDeployment.STATUS_ARCHIVED)
        self.assertIsNotNone(deployment.archived_at)

    def test_teardown_leaves_trials_still_inside_the_grace_window(self):
        user = make_customer()
        user.trial_expires_at = timezone.now() - timedelta(days=1)
        user.save()
        ensure_trial_deployment(user)

        self.assertEqual(teardown_lapsed_trials_task(), {"archived": 0})


class FleetCheckinAPITest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = make_customer()
        self.deployment, _ = ensure_trial_deployment(self.user)

    def post(self, payload):
        request = self.factory.post("/api/fleet/checkin/", payload, format="json")
        return FleetCheckinAPIView.as_view()(request)

    def test_valid_key_records_metadata_and_activates_the_record(self):
        response = self.post(
            {
                "license_key": self.deployment.license_key,
                "app_version": "2026.08.1",
                "uptime_seconds": 4242,
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["ok"])

        self.deployment.refresh_from_db()
        self.assertEqual(self.deployment.installed_version, "2026.08.1")
        self.assertEqual(self.deployment.last_checkin_uptime_seconds, 4242)
        self.assertEqual(self.deployment.status, CustomerDeployment.STATUS_ACTIVE)
        self.assertIsNotNone(self.deployment.last_checkin_at)

    def test_unknown_key_is_refused_without_revealing_anything(self):
        response = self.post({"license_key": "MREX-ZZZZ-ZZZZ-ZZZZ-ZZZZ"})
        self.assertEqual(response.status_code, 403)
        self.assertNotIn("ok", response.data)

    def test_archived_install_stops_being_accepted(self):
        self.deployment.status = CustomerDeployment.STATUS_ARCHIVED
        self.deployment.save(update_fields=["status"])

        response = self.post({"license_key": self.deployment.license_key})
        self.assertEqual(response.status_code, 403)

    def test_operational_data_is_rejected_rather_than_ignored(self):
        response = self.post(
            {"license_key": self.deployment.license_key, "prices": {"GBP_BUY": 1}}
        )
        self.assertEqual(response.status_code, 400)

        self.deployment.refresh_from_db()
        self.assertIsNone(self.deployment.last_checkin_at)

    def test_key_matching_ignores_case_and_padding(self):
        response = self.post({"license_key": f"  {self.deployment.license_key.lower()} "})
        self.assertEqual(response.status_code, 200)


class OwnerPanelAPITest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.owner = CustomUser.objects.create_user(
            username="owner", password="pw-for-tests", role=CustomUser.ROLE_SUPER_ADMIN
        )
        self.staff = CustomUser.objects.create_user(
            username="staff", password="pw-for-tests", role=CustomUser.ROLE_MANAGEMENT
        )
        self.customer = make_customer()
        ensure_trial_started(self.customer)

    def call(self, view, method, path, user, payload=None, **kwargs):
        request = getattr(self.factory, method)(path, payload or {}, format="json")
        force_authenticate(request, user=user)
        return view.as_view()(request, **kwargs)

    def test_trial_list_shows_days_remaining_and_the_stack(self):
        response = self.call(TrialCustomerListAPIView, "get", "/api/fleet/trials/", self.owner)
        self.assertEqual(response.status_code, 200)
        row = response.data[0]
        self.assertEqual(row["username"], "acme")
        self.assertEqual(row["days_remaining"], 13)
        self.assertEqual(row["deployment"]["deployment_type"], CustomerDeployment.TYPE_TRIAL)

    def test_fleet_views_are_closed_to_non_programmers(self):
        response = self.call(TrialCustomerListAPIView, "get", "/api/fleet/trials/", self.staff)
        self.assertEqual(response.status_code, 403)

    def test_extend_pushes_expiry_out_and_rearms_the_reminder(self):
        self.customer.trial_expiry_notified_at = timezone.now()
        self.customer.is_active = False
        self.customer.save()
        original = self.customer.trial_expires_at

        response = self.call(
            TrialExtendAPIView, "post",
            f"/api/fleet/trials/{self.customer.pk}/extend/",
            self.owner, {"days": 7}, pk=self.customer.pk,
        )
        self.assertEqual(response.status_code, 200)

        self.customer.refresh_from_db()
        self.assertEqual(self.customer.trial_expires_at - original, timedelta(days=7))
        self.assertIsNone(self.customer.trial_expiry_notified_at)
        self.assertTrue(self.customer.is_active)

    def test_convert_issues_a_licence_and_clears_the_trial_clock(self):
        response = self.call(
            TrialConvertAPIView, "post",
            f"/api/fleet/trials/{self.customer.pk}/convert/",
            self.owner, {"domain": "Panel.Acme.Example/"}, pk=self.customer.pk,
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["domain"], "panel.acme.example")
        self.assertEqual(response.data["deployment_type"], CustomerDeployment.TYPE_CUSTOMER_SERVER)
        self.assertTrue(response.data["license_key"])
        self.assertIsNotNone(response.data["renews_at"])

        self.customer.refresh_from_db()
        self.assertIsNone(self.customer.trial_expires_at)
        self.assertTrue(self.customer.is_active)

    def test_convert_retires_the_trial_record_and_queues_its_teardown(self):
        trial = CustomerDeployment.objects.get(
            customer=self.customer, deployment_type=CustomerDeployment.TYPE_TRIAL
        )
        with patch("fleet.api_views.archive_trial_stack_task.delay") as teardown:
            with self.captureOnCommitCallbacks(execute=True):
                self.call(
                    TrialConvertAPIView, "post",
                    f"/api/fleet/trials/{self.customer.pk}/convert/",
                    self.owner, {"domain": "panel.acme.example"}, pk=self.customer.pk,
                )

        teardown.assert_called_once_with(deployment_id=trial.pk)
        trial.refresh_from_db()
        self.assertEqual(trial.status, CustomerDeployment.STATUS_ARCHIVED)
        self.assertIn("panel.acme.example", trial.notes)

    def test_a_converted_customer_can_be_given_a_fresh_trial_later(self):
        trial = CustomerDeployment.objects.get(
            customer=self.customer, deployment_type=CustomerDeployment.TYPE_TRIAL
        )
        convert_to_licensed(trial, domain="panel.acme.example")

        self.customer.trial_expires_at = timezone.now() + timedelta(days=14)
        self.customer.save(update_fields=["trial_expires_at"])
        second, created = ensure_trial_deployment(self.customer)

        self.assertTrue(created)
        self.assertNotEqual(second.pk, trial.pk)

    def test_convert_refuses_a_domain_another_install_already_uses(self):
        self.call(
            TrialConvertAPIView, "post",
            f"/api/fleet/trials/{self.customer.pk}/convert/",
            self.owner, {"domain": "panel.acme.example"}, pk=self.customer.pk,
        )
        other = make_customer("beta", exchange_name="Beta Exchange")
        ensure_trial_started(other)

        response = self.call(
            TrialConvertAPIView, "post",
            f"/api/fleet/trials/{other.pk}/convert/",
            self.owner, {"domain": "panel.acme.example"}, pk=other.pk,
        )
        self.assertEqual(response.status_code, 400)

    def test_licensed_list_holds_only_customer_server_installs(self):
        self.call(
            TrialConvertAPIView, "post",
            f"/api/fleet/trials/{self.customer.pk}/convert/",
            self.owner, {"domain": "panel.acme.example"}, pk=self.customer.pk,
        )
        response = self.call(
            LicensedDeploymentListAPIView, "get", "/api/fleet/deployments/", self.owner
        )
        self.assertEqual(response.status_code, 200)
        rows = response.data["results"] if isinstance(response.data, dict) else response.data
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["domain"], "panel.acme.example")

    def test_reissue_replaces_the_key_and_the_old_one_stops_working(self):
        deployment = CustomerDeployment.objects.get(customer=self.customer)
        old_key = deployment.license_key

        response = self.call(
            LicenseReissueAPIView, "post",
            f"/api/fleet/deployments/{deployment.pk}/reissue-license/",
            self.owner, pk=deployment.pk,
        )
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data["license_key"], old_key)

        checkin = self.factory.post(
            "/api/fleet/checkin/", {"license_key": old_key}, format="json"
        )
        self.assertEqual(FleetCheckinAPIView.as_view()(checkin).status_code, 403)


class DeliveryTierEndToEndTest(TestCase):
    """Walk one customer through both tiers, the way phase 6 asks for.

    Signup → trial record → reminder → convert → licensed record → the
    customer-server install's first check-in, all without Docker.
    """

    def setUp(self):
        self.factory = APIRequestFactory()
        self.owner = CustomUser.objects.create_user(
            username="fleet-owner", password="pw-for-tests", role=CustomUser.ROLE_SUPER_ADMIN
        )
        self.customer = make_customer(username="lifecycle")

    def test_trial_signup_through_to_a_licensed_install_checking_in(self):
        ensure_trial_started(self.customer)
        trial = CustomerDeployment.objects.get(
            customer=self.customer, deployment_type=CustomerDeployment.TYPE_TRIAL
        )
        self.assertEqual(trial.status, CustomerDeployment.STATUS_PENDING)

        # Tier 1: the trial reports in from its own stack on our VPS.
        checkin = self.factory.post(
            "/api/fleet/checkin/",
            {"license_key": trial.license_key, "app_version": "2026.08.1"},
            format="json",
        )
        self.assertEqual(FleetCheckinAPIView.as_view()(checkin).status_code, 200)
        trial.refresh_from_db()
        self.assertEqual(trial.status, CustomerDeployment.STATUS_ACTIVE)

        # Day 11 of 14: the reminder fires once.
        self.customer.trial_expires_at = timezone.now() + timedelta(days=2)
        self.customer.save(update_fields=["trial_expires_at"])
        self.assertEqual(send_trial_expiry_reminders_task(), {"notified": 1})

        # Tier 2: sales closes, and the owner converts.
        request = self.factory.post(
            f"/api/fleet/trials/{self.customer.pk}/convert/",
            {"domain": "panel.lifecycle.example"},
            format="json",
        )
        force_authenticate(request, user=self.owner)
        with patch("fleet.api_views.archive_trial_stack_task.delay"):
            with self.captureOnCommitCallbacks(execute=True):
                response = TrialConvertAPIView.as_view()(request, pk=self.customer.pk)
        self.assertEqual(response.status_code, 201)
        licensed_key = response.data["license_key"]

        trial.refresh_from_db()
        self.assertEqual(trial.status, CustomerDeployment.STATUS_ARCHIVED)
        self.customer.refresh_from_db()
        self.assertIsNone(self.customer.trial_expires_at)
        self.assertTrue(self.customer.is_active)

        # The trial's key is dead; only the licensed install can check in now.
        stale = self.factory.post(
            "/api/fleet/checkin/", {"license_key": trial.license_key}, format="json"
        )
        self.assertEqual(FleetCheckinAPIView.as_view()(stale).status_code, 403)

        live = self.factory.post(
            "/api/fleet/checkin/",
            {"license_key": licensed_key, "app_version": "2026.08.1", "uptime_seconds": 90},
            format="json",
        )
        self.assertEqual(FleetCheckinAPIView.as_view()(live).status_code, 200)

        licensed = CustomerDeployment.objects.get(license_key=licensed_key)
        self.assertEqual(licensed.deployment_type, CustomerDeployment.TYPE_CUSTOMER_SERVER)
        self.assertEqual(licensed.status, CustomerDeployment.STATUS_ACTIVE)
        self.assertIsNotNone(licensed.last_checkin_at)
