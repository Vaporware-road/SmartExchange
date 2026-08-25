"""Owner / mission-control fleet APIs, plus the install check-in endpoint.

Two views back the two halves of the owner panel:

* trial customers — queried live from this shared database, because trials run
  on our own VPS;
* licensed customers — read from CustomerDeployment, because those installs
  are deliberately isolated and only tell us what they report at check-in.
"""

from __future__ import annotations

import logging
from datetime import timedelta

from django.conf import settings
from django.db import transaction
from django.utils import timezone
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView

from accounts.models import CustomUser
from accounts.permissions import IsProgrammer

from .licensing import normalize_license_key
from .models import CustomerDeployment
from .serializers import (
    CheckinSerializer,
    ConvertTrialSerializer,
    CustomerDeploymentSerializer,
    ExtendTrialSerializer,
    TrialCustomerSerializer,
)
from .services import convert_to_licensed, ensure_trial_deployment, extend_trial
from .tasks import provision_trial_task

logger = logging.getLogger(__name__)


def _attach_trial_deployments(users):
    """One extra query for the whole page instead of one per row."""
    users = list(users)
    deployments = {
        deployment.customer_id: deployment
        for deployment in CustomerDeployment.objects.filter(
            customer__in=users,
            deployment_type=CustomerDeployment.TYPE_TRIAL,
        ).order_by("customer_id", "-created_at")
    }
    for user in users:
        user.trial_deployment = deployments.get(user.pk)
    return users


class TrialCustomerListAPIView(ListAPIView):
    """Every account currently on a trial clock, soonest to expire first."""

    permission_classes = [IsProgrammer]
    serializer_class = TrialCustomerSerializer

    def get_queryset(self):
        return (
            CustomUser.objects.filter(trial_expires_at__isnull=False)
            .exclude(role=CustomUser.ROLE_SUPER_ADMIN)
            .exclude(is_superuser=True)
            .order_by("trial_expires_at")
        )

    def list(self, request, *args, **kwargs):
        users = _attach_trial_deployments(self.get_queryset())
        return Response(self.get_serializer(users, many=True).data)


class TrialExtendAPIView(APIView):
    """Push a trial's expiry out — the panel's one-click extend."""

    permission_classes = [IsProgrammer]

    def post(self, request, pk):
        user = self._get_trial_user(pk)
        if user is None:
            return Response({"detail": "No trial for this user."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ExtendTrialSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        extend_trial(user, days=serializer.validated_data["days"])

        _attach_trial_deployments([user])
        return Response(TrialCustomerSerializer(user).data)

    @staticmethod
    def _get_trial_user(pk):
        return (
            CustomUser.objects.filter(pk=pk, trial_expires_at__isnull=False)
            .exclude(role=CustomUser.ROLE_SUPER_ADMIN)
            .first()
        )


class TrialConvertAPIView(APIView):
    """Convert a trial to a licensed customer-server install.

    This issues the license and records the new install. Moving the data onto
    the customer's VPS is the `convert_trial` management command — deliberately
    a separate, explicit step rather than something a button does silently.
    """

    permission_classes = [IsProgrammer]

    def post(self, request, pk):
        user = TrialExtendAPIView._get_trial_user(pk)
        if user is None:
            return Response({"detail": "No trial for this user."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ConvertTrialSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        trial = (
            CustomerDeployment.objects.filter(
                customer=user, deployment_type=CustomerDeployment.TYPE_TRIAL
            )
            .order_by("-created_at")
            .first()
        )
        if trial is None:
            trial, _ = ensure_trial_deployment(user)

        licensed = convert_to_licensed(
            trial,
            domain=serializer.validated_data["domain"],
            plan=serializer.validated_data.get("plan"),
            renews_at=serializer.validated_data.get("renews_at"),
            notes=serializer.validated_data.get("notes", ""),
        )
        return Response(
            CustomerDeploymentSerializer(licensed).data, status=status.HTTP_201_CREATED
        )


class TrialProvisionAPIView(APIView):
    """Create the trial's stack record and queue provisioning (or re-queue it)."""

    permission_classes = [IsProgrammer]

    def post(self, request, pk):
        user = TrialExtendAPIView._get_trial_user(pk)
        if user is None:
            return Response({"detail": "No trial for this user."}, status=status.HTTP_404_NOT_FOUND)

        deployment, _ = ensure_trial_deployment(user)
        transaction.on_commit(
            lambda: provision_trial_task.delay(deployment_id=deployment.pk)
        )
        return Response(
            CustomerDeploymentSerializer(deployment).data, status=status.HTTP_202_ACCEPTED
        )


class LicensedDeploymentListAPIView(ListAPIView):
    """Licensed installs, most recently seen first — the fleet table."""

    permission_classes = [IsProgrammer]
    serializer_class = CustomerDeploymentSerializer

    def get_queryset(self):
        return CustomerDeployment.objects.filter(
            deployment_type=CustomerDeployment.TYPE_CUSTOMER_SERVER
        ).select_related("customer")


class LicenseReissueAPIView(APIView):
    """One-click license reissue. The previous key stops working immediately."""

    permission_classes = [IsProgrammer]

    def post(self, request, pk):
        deployment = CustomerDeployment.objects.filter(pk=pk).select_related("customer").first()
        if deployment is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        renews_at = deployment.renews_at
        if renews_at is None or renews_at <= timezone.now():
            renews_at = timezone.now() + timedelta(days=settings.LICENSE_TERM_DAYS)
        deployment.issue_license(renews_at=renews_at)
        deployment.save(update_fields=["license_key", "renews_at"])
        return Response(CustomerDeploymentSerializer(deployment).data)


class FleetCheckinThrottle(AnonRateThrottle):
    scope = "fleet_checkin"


class FleetCheckinAPIView(APIView):
    """Daily heartbeat from every install, trial and licensed alike.

    Authenticated by the license key alone: the endpoint accepts only
    metadata and returns only that install's own license status, so a leaked
    key cannot be used to read or write anything belonging to a customer.
    """

    permission_classes = [AllowAny]
    authentication_classes = []
    throttle_classes = [FleetCheckinThrottle]

    def post(self, request):
        serializer = CheckinSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        key = normalize_license_key(serializer.validated_data["license_key"])

        deployment = CustomerDeployment.objects.filter(license_key=key).first()
        if deployment is None or deployment.status == CustomerDeployment.STATUS_ARCHIVED:
            # Same response either way: an unknown key learns nothing about
            # which keys exist.
            return Response({"detail": "Unknown license."}, status=status.HTTP_403_FORBIDDEN)

        deployment.record_checkin(
            app_version=serializer.validated_data.get("app_version", ""),
            uptime_seconds=serializer.validated_data.get("uptime_seconds"),
        )
        return Response(
            {
                "ok": True,
                "status": deployment.status,
                "plan": deployment.plan,
                "renews_at": deployment.renews_at,
            }
        )
