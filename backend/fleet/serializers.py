from rest_framework import serializers

from accounts.plans import PLAN_CHOICES

from .models import CustomerDeployment, Sale
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


class SaleSerializer(serializers.ModelSerializer):
    customer_display = serializers.SerializerMethodField()
    account_name = serializers.CharField(source="account.name", read_only=True, default="")
    recorded_by_display = serializers.SerializerMethodField()
    license_key = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = (
            "id",
            "customer",
            "customer_display",
            "customer_email",
            "account",
            "account_name",
            "amount",
            "currency",
            "sale_plan",
            "sold_at",
            "reference",
            "note",
            "recorded_by",
            "recorded_by_display",
            "license_key",
            "created_at",
        )
        read_only_fields = (
            "id",
            "customer_display",
            "account",
            "account_name",
            "recorded_by",
            "recorded_by_display",
            "created_at",
        )

    def get_customer_display(self, sale):
        if sale.customer is None:
            return sale.customer_email
        return sale.customer.get_full_name() or sale.customer.username

    def get_recorded_by_display(self, sale):
        if sale.recorded_by is None:
            return ""
        return sale.recorded_by.get_full_name() or sale.recorded_by.username

    def get_license_key(self, sale):
        """The key this sale put the customer on.

        Recording the sale issues it and hangs it on the instance; reading an
        older sale finds it on the customer's live deployment instead.
        """
        issued = getattr(sale, "license_key", "")
        if issued:
            return issued
        if sale.customer_id is None:
            return ""
        deployment = (
            sale.customer.deployments.exclude(license_key="")
            .order_by("-created_at")
            .first()
        )
        return getattr(deployment, "license_key", "")

    def validate_customer(self, value):
        if value is None:
            raise serializers.ValidationError("Pick the customer this sale belongs to.")
        return value

    def create(self, validated_data):
        customer = validated_data["customer"]
        validated_data.setdefault("customer_email", customer.email or "")
        validated_data["account"] = customer.account
        validated_data["recorded_by"] = self.context["request"].user
        return super().create(validated_data)


class AccountOverviewSerializer(serializers.Serializer):
    """One signed-up desk as the owner console lists it."""

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    slug = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    is_paid = serializers.BooleanField(read_only=True)
    owner = serializers.SerializerMethodField()
    user_count = serializers.IntegerField(read_only=True)
    sales_total = serializers.SerializerMethodField()

    def get_owner(self, account):
        owner = getattr(account, "owner_user", None)
        if owner is None:
            return None
        return {
            "id": owner.id,
            "username": owner.username,
            "email": owner.email,
            "full_name": owner.get_full_name(),
            "is_active": owner.is_active,
            "role": owner.role,
            "email_verified_at": owner.email_verified_at,
            "last_login": owner.last_login,
            "trial_started_at": owner.trial_started_at,
            "trial_expires_at": owner.trial_expires_at,
            "days_remaining": days_remaining(owner),
        }

    def get_sales_total(self, account):
        return str(getattr(account, "sales_total", None) or 0)
