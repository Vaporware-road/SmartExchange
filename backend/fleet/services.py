"""Trial and licensed-install lifecycle, independent of how it is triggered.

The API views, the Celery tasks and the management commands all go through
here so a trial started from the signup flow and one started by an operator
end up in exactly the same state.
"""

from __future__ import annotations

import logging
from datetime import timedelta

from django.conf import settings
from django.db import transaction
from django.utils import timezone

from accounts.plans import normalize_plan

from .models import CustomerDeployment
from .provisioning import unique_slug_for, domain_for

logger = logging.getLogger(__name__)


def trial_grace_ends_at(user):
    """When an expired trial stops being recoverable and gets archived."""
    if not user.trial_expires_at:
        return None
    return user.trial_expires_at + timedelta(days=settings.TRIAL_GRACE_DAYS)


def days_remaining(user, now=None):
    if not user.trial_expires_at:
        return None
    delta = user.trial_expires_at - (now or timezone.now())
    # Round towards the customer: 0 means "expires today", negative means lapsed.
    return int(delta.total_seconds() // 86400)


@transaction.atomic
def ensure_trial_deployment(user):
    """Record the trial install for ``user``, creating it on first call.

    Returns ``(deployment, created)``. Provisioning itself is a separate,
    retryable step so a Docker hiccup never blocks account creation.
    """
    existing = (
        CustomerDeployment.objects.select_for_update()
        .filter(
            customer=user,
            deployment_type=CustomerDeployment.TYPE_TRIAL,
            status__in=CustomerDeployment.LIVE_STATUSES,
        )
        .first()
    )
    if existing is not None:
        return existing, False

    slug = unique_slug_for(user)
    deployment = CustomerDeployment(
        customer=user,
        deployment_type=CustomerDeployment.TYPE_TRIAL,
        slug=slug,
        domain=domain_for(slug),
        plan=normalize_plan(getattr(user, "plan", None)),
        status=CustomerDeployment.STATUS_PENDING,
        renews_at=user.trial_expires_at,
    )
    deployment.issue_license()
    deployment.save()
    return deployment, True


@transaction.atomic
def convert_to_licensed(
    trial_deployment,
    *,
    domain,
    plan=None,
    renews_at=None,
    notes="",
):
    """Turn a converted trial into the customer's licensed install record.

    The trial record is retired here so it stops occupying the one-live-trial
    slot and stops showing up as a trial customer; tearing the trial's actual
    containers down is a separate, Docker-touching step the caller schedules.
    The returned record is the one the owner panel tracks from here on, and it
    carries a freshly issued license key.
    """
    customer = trial_deployment.customer
    licensed = CustomerDeployment(
        customer=customer,
        deployment_type=CustomerDeployment.TYPE_CUSTOMER_SERVER,
        slug=f"{trial_deployment.slug}-live"[: CustomerDeployment._meta.get_field("slug").max_length],
        domain=domain.strip().lower(),
        plan=normalize_plan(plan or trial_deployment.plan),
        status=CustomerDeployment.STATUS_PENDING,
        notes=notes,
    )
    licensed.issue_license(
        renews_at=renews_at or (timezone.now() + timedelta(days=settings.LICENSE_TERM_DAYS))
    )
    licensed.save()

    # The customer is no longer on a trial clock; the license is what gates
    # access from now on, so clear the fields TrialAccessMiddleware reads.
    customer.trial_expires_at = None
    customer.trial_expiry_notified_at = None
    customer.is_active = True
    customer.save(
        update_fields=["trial_expires_at", "trial_expiry_notified_at", "is_active"]
    )

    retire_trial_deployment(trial_deployment, reason=f"converted to {licensed.domain}")
    return licensed


def retire_trial_deployment(trial_deployment, *, reason="", now=None):
    """Mark a trial record finished without touching Docker.

    Called on conversion, and as the fallback whenever the host has no
    provisioning to tear down, so the owner panel never shows a trial that is
    no longer a trial.
    """
    if trial_deployment.status == CustomerDeployment.STATUS_ARCHIVED:
        return trial_deployment
    trial_deployment.status = CustomerDeployment.STATUS_ARCHIVED
    trial_deployment.archived_at = now or timezone.now()
    if reason:
        trial_deployment.notes = f"{trial_deployment.notes}\n{reason}".strip()
        trial_deployment.save(update_fields=["status", "archived_at", "notes"])
    else:
        trial_deployment.save(update_fields=["status", "archived_at"])
    return trial_deployment


def extend_trial(user, *, days):
    """Push a trial's expiry out and re-arm its reminder."""
    if days <= 0:
        raise ValueError("days must be positive")
    base = max(user.trial_expires_at or timezone.now(), timezone.now())
    user.trial_expires_at = base + timedelta(days=days)
    user.trial_expiry_notified_at = None
    user.is_active = True
    user.save(
        update_fields=["trial_expires_at", "trial_expiry_notified_at", "is_active"]
    )
    CustomerDeployment.objects.filter(
        customer=user,
        deployment_type=CustomerDeployment.TYPE_TRIAL,
        status__in=CustomerDeployment.LIVE_STATUSES,
    ).update(renews_at=user.trial_expires_at)
    return user
