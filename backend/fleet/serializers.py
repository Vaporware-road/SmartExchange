from rest_framework import serializers

from accounts.plans import PLAN_CHOICES

from .models import CustomerDeployment
from .services import days_remaining, trial_grace_ends_at


class CustomerDeploymentSerializer(serializers.ModelSerializer):
    customer_username = serializers.CharField(source="customer.username", read_only=True)
    customer_name = serializers.CharField(source="customer.get_full_name", read_only=True)
    exchange_name = serializers.CharField(source="customer.exchange_name", read_only=True)

    class Meta:
        model = CustomerDeployment
        fields = (
            "id",
            "customer",
            "customer_username",
            "customer_name",
            "exchange_name",
            "deployment_type",
            "slug",
            "domain",
            "license_key",
            "plan",
            "status",
            "installed_version",
            "last_checkin_at",
            "last_checkin_uptime_seconds",
            "provisioned_at",
            "renews_at",
            "archived_at",
            "notes",
            "created_at",
        )
        read_only_fields = fields


class TrialCustomerSerializer(serializers.Serializer):
    """A trial customer as the owner panel sees them: the account plus its stack.

    Read live from the shared database — trials run on our own VPS, so unlike
    licensed installs there is nothing to wait for a check-in to learn.
    """

    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    full_name = serializers.CharField(source="get_full_name", read_only=True)
    exchange_name = serializers.CharField(read_only=True)
    country = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    phone = serializers.CharField(read_only=True)
    plan = serializers.CharField(read_only=True)
    collaboration_type = serializers.CharField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    trial_started_at = serializers.DateTimeField(read_only=True)
    trial_expires_at = serializers.DateTimeField(read_only=True)
    trial_expiry_notified_at = serializers.DateTimeField(read_only=True)
    days_remaining = serializers.SerializerMethodField()
    grace_ends_at = serializers.SerializerMethodField()
    deployment = serializers.SerializerMethodField()

    def get_days_remaining(self, user):
        return days_remaining(user)

    def get_grace_ends_at(self, user):
        return trial_grace_ends_at(user)

    def get_deployment(self, user):
        deployment = getattr(user, "trial_deployment", None)
        if deployment is None:
            return None
        return CustomerDeploymentSerializer(deployment).data


class ExtendTrialSerializer(serializers.Serializer):
    days = serializers.IntegerField(min_value=1, max_value=90, default=14)


class ConvertTrialSerializer(serializers.Serializer):
    domain = serializers.CharField(max_length=253)
    plan = serializers.ChoiceField(choices=PLAN_CHOICES, required=False)
    renews_at = serializers.DateTimeField(required=False)
    notes = serializers.CharField(required=False, allow_blank=True, default="")

    def validate_domain(self, value):
        domain = value.strip().lower().removeprefix("https://").removeprefix("http://").strip("/")
        if not domain or " " in domain or "." not in domain:
            raise serializers.ValidationError("Enter the customer's fully qualified domain.")
        if CustomerDeployment.objects.filter(domain=domain).exists():
            raise serializers.ValidationError("Another deployment already uses this domain.")
        return domain


class CheckinSerializer(serializers.Serializer):
    """Everything an install is allowed to report. Nothing operational.

    Unknown keys are rejected rather than ignored so a future version cannot
    quietly start sending customer data to this endpoint.
    """

    license_key = serializers.CharField(max_length=64)
    app_version = serializers.CharField(max_length=32, required=False, allow_blank=True, default="")
    uptime_seconds = serializers.IntegerField(required=False, allow_null=True, min_value=0, default=None)

    def validate(self, attrs):
        extra = set(self.initial_data) - set(self.fields)
        if extra:
            raise serializers.ValidationError(
                {"non_field_errors": f"Unsupported fields: {', '.join(sorted(extra))}"}
            )
        return attrs
