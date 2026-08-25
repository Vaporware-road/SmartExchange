from django.conf import settings
from django.db import models
from django.utils import timezone

from accounts.plans import PLAN_BRONZE, PLAN_CHOICES

from .licensing import generate_license_key


class CustomerDeployment(models.Model):
    """One MrExchange installation belonging to one customer.

    Trial installs live on our own VPS as an isolated stack per signup;
    licensed installs live on the customer's VPS and domain and are invisible
    to this database except through the metadata they report at check-in.
    """

    TYPE_TRIAL = "trial"
    TYPE_CUSTOMER_SERVER = "customer_server"

    TYPE_CHOICES = (
        (TYPE_TRIAL, "Trial (our VPS)"),
        (TYPE_CUSTOMER_SERVER, "Customer server"),
    )

    STATUS_PENDING = "pending"
    STATUS_PROVISIONING = "provisioning"
    STATUS_ACTIVE = "active"
    STATUS_EXPIRED = "expired"
    STATUS_SUSPENDED = "suspended"
    STATUS_ARCHIVED = "archived"
    STATUS_FAILED = "failed"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_PROVISIONING, "Provisioning"),
        (STATUS_ACTIVE, "Active"),
        (STATUS_EXPIRED, "Expired"),
        (STATUS_SUSPENDED, "Suspended"),
        (STATUS_ARCHIVED, "Archived"),
        (STATUS_FAILED, "Failed"),
    )

    LIVE_STATUSES = (STATUS_PENDING, STATUS_PROVISIONING, STATUS_ACTIVE)

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="deployments",
    )
    deployment_type = models.CharField(max_length=24, choices=TYPE_CHOICES)
    slug = models.SlugField(
        max_length=63,
        unique=True,
        help_text="Stack / container project name; also the trial subdomain label.",
    )
    domain = models.CharField(max_length=253, blank=True, default="")
    license_key = models.CharField(max_length=32, blank=True, default="", db_index=True)
    plan = models.CharField(max_length=16, choices=PLAN_CHOICES, default=PLAN_BRONZE)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=STATUS_PENDING)

    installed_version = models.CharField(max_length=32, blank=True, default="")
    last_checkin_at = models.DateTimeField(null=True, blank=True)
    last_checkin_uptime_seconds = models.BigIntegerField(null=True, blank=True)

    provisioned_at = models.DateTimeField(null=True, blank=True)
    renews_at = models.DateTimeField(null=True, blank=True)
    archived_at = models.DateTimeField(null=True, blank=True)

    notes = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["license_key"],
                condition=models.Q(license_key__gt=""),
                name="fleet_unique_license_key",
            ),
            models.UniqueConstraint(
                fields=["customer"],
                condition=models.Q(
                    deployment_type="trial",
                    status__in=("pending", "provisioning", "active"),
                ),
                name="fleet_one_live_trial_per_customer",
            ),
        ]
        indexes = [
            models.Index(fields=["deployment_type", "status"]),
            models.Index(fields=["-last_checkin_at"]),
        ]

    def __str__(self):
        return f"{self.slug} ({self.get_deployment_type_display()})"

    @property
    def is_licensed(self):
        return self.deployment_type == self.TYPE_CUSTOMER_SERVER

    def issue_license(self, *, renews_at=None):
        """Assign a fresh license key. Reissuing invalidates the previous one."""
        self.license_key = generate_license_key()
        if renews_at is not None:
            self.renews_at = renews_at
        return self.license_key

    def record_checkin(self, *, app_version="", uptime_seconds=None, now=None):
        self.last_checkin_at = now or timezone.now()
        if app_version:
            self.installed_version = app_version[:32]
        self.last_checkin_uptime_seconds = uptime_seconds
        update_fields = ["last_checkin_at", "installed_version", "last_checkin_uptime_seconds"]
        if self.status in (self.STATUS_PENDING, self.STATUS_PROVISIONING):
            self.status = self.STATUS_ACTIVE
            update_fields.append("status")
        self.save(update_fields=update_fields)
