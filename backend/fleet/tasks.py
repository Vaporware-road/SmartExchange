"""Scheduled fleet work: provisioning, reminders, teardown, and check-in.

Every task here is safe to run on a host that is not the trial host — the
Docker-touching ones short-circuit when provisioning is disabled rather than
failing, so the same beat schedule ships to every install.
"""

from __future__ import annotations

import logging
from datetime import timedelta

import requests
from celery import shared_task
from django.conf import settings
from django.utils import timezone

from .models import CustomerDeployment
from .provisioning import ProvisioningDisabled, ProvisioningError, archive, provision

logger = logging.getLogger(__name__)

CHECKIN_TIMEOUT_SECONDS = 15


def _log(level, message, **fields):
    """Mirror fleet events into the panel log table the owner already reads."""
    try:
        from setting.utils import log_structured

        log_structured(level=level, source="system", message=message, **fields)
    except Exception:
        logger.exception("fleet: failed to write log row")


@shared_task(
    bind=True,
    autoretry_for=(ProvisioningError,),
    max_retries=3,
    retry_backoff=True,
    retry_jitter=True,
)
def provision_trial_task(self, *, deployment_id: int):
    deployment = CustomerDeployment.objects.filter(pk=deployment_id).first()
    if deployment is None:
        logger.info("fleet: provision skipped, deployment %s is gone", deployment_id)
        return {"provisioned": False, "reason": "missing"}
    if deployment.status == CustomerDeployment.STATUS_ACTIVE:
        return {"provisioned": False, "reason": "already_active"}

    deployment.status = CustomerDeployment.STATUS_PROVISIONING
    deployment.save(update_fields=["status"])
    try:
        provision(deployment)
    except ProvisioningDisabled as exc:
        # Expected on every host that is not the trial host.
        deployment.status = CustomerDeployment.STATUS_PENDING
        deployment.save(update_fields=["status"])
        logger.info("fleet: %s", exc)
        return {"provisioned": False, "reason": "disabled"}
    except ProvisioningError:
        deployment.status = CustomerDeployment.STATUS_FAILED
        deployment.save(update_fields=["status"])
        _log("ERROR", f"Trial provisioning failed for {deployment.slug}",
             event="fleet_provision_failed", slug=deployment.slug)
        raise

    _log("INFO", f"Trial stack provisioned: {deployment.domain}",
         event="fleet_provisioned", slug=deployment.slug, domain=deployment.domain)
    return {"provisioned": True, "domain": deployment.domain}


@shared_task
def send_trial_expiry_reminders_task():
    """Warn before day 14, once per trial.

    ``trial_expiry_notified_at`` is the stamp that makes this once-only; it is
    cleared whenever a trial is extended so the next window warns again.
    """
    from accounts.models import CustomUser

    now = timezone.now()
    window_end = now + timedelta(days=settings.TRIAL_REMINDER_DAYS)
    due = (
        CustomUser.objects.filter(
            is_active=True,
            trial_expires_at__isnull=False,
            trial_expires_at__gt=now,
            trial_expires_at__lte=window_end,
            trial_expiry_notified_at__isnull=True,
        )
        .exclude(role=CustomUser.ROLE_SUPER_ADMIN)
        .exclude(is_superuser=True)
    )

    notified = 0
    for user in due:
        days_left = max(0, int((user.trial_expires_at - now).total_seconds() // 86400))
        _log(
            "WARNING",
            f"Trial for {user.username} expires in {days_left} day(s)",
            event="trial_expiry_reminder",
            user_id=user.pk,
            username=user.username,
            exchange_name=user.exchange_name,
            trial_expires_at=user.trial_expires_at.isoformat(),
            days_left=days_left,
        )
        _notify_staff_of_trial_expiry(user, days_left)
        user.trial_expiry_notified_at = now
        user.save(update_fields=["trial_expiry_notified_at"])
        notified += 1

    return {"notified": notified}


def _notify_staff_of_trial_expiry(user, days_left):
    """Best-effort Telegram DM to staff. Never raises into the reminder loop."""
    try:
        from telegram_app.models import TelegramBot
        from telegram_app.services.admin_notify import staff_notify_recipients
        from telegram_app.services.staff_access import normalize_telegram_id
        from telegram_app.services.telegram_client import TelegramService

        bot = TelegramBot.objects.filter(is_active=True).first()
        recipients = list(staff_notify_recipients())
        if bot is None or not recipients:
            return
        client = TelegramService(bot.get_plain_token())
        text = (
            "⏳ Trial expiring\n"
            f"👤 {user.get_full_name()} ({user.username})\n"
            f"🏢 {user.exchange_name or '—'}\n"
            f"📆 {days_left} day(s) left — expires {user.trial_expires_at:%Y-%m-%d}\n\n"
            "Convert or extend from the fleet view in the Developer Hub."
        )
        for staff in recipients:
            chat_id = normalize_telegram_id(staff.telegram_id)
            if chat_id:
                client.send_message(chat_id=chat_id, text=text, parse_mode=None)
    except Exception:
        logger.exception("fleet: trial expiry staff notification failed")


@shared_task
def teardown_lapsed_trials_task():
    """Archive trial stacks whose grace window has run out.

    Expiry itself is already enforced live by TrialAccessMiddleware; this is
    the later, irreversible half — the customer keeps a grace window in which
    a conversion still finds their data in place.
    """
    now = timezone.now()
    cutoff = now - timedelta(days=settings.TRIAL_GRACE_DAYS)
    lapsed = CustomerDeployment.objects.filter(
        deployment_type=CustomerDeployment.TYPE_TRIAL,
        status__in=CustomerDeployment.LIVE_STATUSES,
        customer__trial_expires_at__isnull=False,
        customer__trial_expires_at__lte=cutoff,
    ).select_related("customer")

    archived = 0
    for deployment in lapsed:
        try:
            archive(deployment)
        except ProvisioningDisabled:
            # No Docker here; still retire the record so the panel is truthful.
            deployment.status = CustomerDeployment.STATUS_ARCHIVED
            deployment.archived_at = now
            deployment.save(update_fields=["status", "archived_at"])
        except ProvisioningError:
            logger.exception("fleet: teardown failed for %s", deployment.slug)
            continue

        customer = deployment.customer
        if customer.is_active:
            customer.is_active = False
            customer.save(update_fields=["is_active"])
        _log("INFO", f"Lapsed trial archived: {deployment.slug}",
             event="fleet_trial_archived", slug=deployment.slug)
        archived += 1

    return {"archived": archived}


@shared_task
def send_fleet_checkin_task():
    """Report this install's non-sensitive metadata to the owner panel.

    Runs on every install — trial container and customer-server alike. It
    sends the license key, the app version and uptime, and nothing else: no
    prices, no customers, no credentials. That keeps the isolation rule that
    governs customer-server deployments intact.
    """
    url = getattr(settings, "FLEET_CHECKIN_URL", "")
    license_key = getattr(settings, "FLEET_LICENSE_KEY", "")
    if not url or not license_key:
        return {"sent": False, "reason": "not_configured"}

    payload = {
        "license_key": license_key,
        "app_version": getattr(settings, "APP_VERSION", ""),
        "uptime_seconds": _process_uptime_seconds(),
    }
    try:
        response = requests.post(url, json=payload, timeout=CHECKIN_TIMEOUT_SECONDS)
    except requests.RequestException as exc:
        logger.warning("fleet: check-in request failed: %s", exc)
        return {"sent": False, "reason": "request_failed"}

    if response.status_code != 200:
        logger.warning("fleet: check-in rejected with HTTP %s", response.status_code)
        return {"sent": False, "reason": f"http_{response.status_code}"}
    return {"sent": True}


def _process_uptime_seconds():
    try:
        with open("/proc/uptime", encoding="utf-8") as handle:
            return int(float(handle.read().split()[0]))
    except (OSError, ValueError, IndexError):
        return None
