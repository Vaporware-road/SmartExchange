from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager
from .plans import PLAN_BRONZE, PLAN_CHOICES


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_SUPER_ADMIN = 'super_admin'
    ROLE_MANAGEMENT = 'management'
    ROLE_EMPLOYEE = 'employee'
    ROLE_DEVELOPER = 'developer'

    ROLE_CHOICES = (
        (ROLE_SUPER_ADMIN, 'Super Admin'),
        (ROLE_MANAGEMENT, 'Management'),
        (ROLE_EMPLOYEE, 'Employee'),
        (ROLE_DEVELOPER, 'Developer'),
    )

    # Sub-roles refine what a Telegram bot admin (including delegated employees)
    # may do inside the in-bot admin panel. Full admins keep SUB_ROLE_ADMIN.
    SUB_ROLE_ADMIN = 'admin'
    SUB_ROLE_OPERATOR = 'operator'
    SUB_ROLE_HEAD_OPERATOR = 'head_operator'

    SUB_ROLE_CHOICES = (
        (SUB_ROLE_ADMIN, 'Admin'),
        (SUB_ROLE_OPERATOR, 'Operator'),
        (SUB_ROLE_HEAD_OPERATOR, 'Head Operator'),
    )

    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    full_name = models.CharField(max_length=255, blank=True)
    exchange_name = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=120, blank=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    phone = models.CharField(max_length=40, blank=True)
    telegram_id = models.CharField(max_length=64, blank=True)
    website = models.URLField(max_length=256, blank=True, default='')
    collaboration_type = models.CharField(max_length=32, blank=True, default='', help_text='Partnership model / service tier')
    registered_by = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='registered_users',
        help_text='Admin who registered this user'
    )
    # Delegated Telegram bot admins: employee-role users granted access to the
    # in-bot admin panel of their owner's bots via telegram_app.BotAdmin rows.
    owner = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='sub_users',
        help_text='Panel user this delegated operator reports to'
    )
    sub_role = models.CharField(max_length=24, choices=SUB_ROLE_CHOICES, default=SUB_ROLE_ADMIN)
    telegram_username = models.CharField(max_length=128, blank=True, default='')
    plan = models.CharField(max_length=16, choices=PLAN_CHOICES, default=PLAN_BRONZE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_EMPLOYEE)
    trial_started_at = models.DateTimeField(null=True, blank=True)
    trial_expires_at = models.DateTimeField(null=True, blank=True)
    trial_expiry_notified_at = models.DateTimeField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    token_version = models.PositiveIntegerField(default=0, help_text='Incremented on force logout to invalidate all tokens.')

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def save(self, *args, **kwargs):
        composed = f"{self.first_name} {self.last_name}".strip()
        if composed:
            self.full_name = composed
        if self.email == "":
            self.email = None
        super().save(*args, **kwargs)

    def get_full_name(self):
        composed = f"{self.first_name} {self.last_name}".strip()
        return composed or self.full_name or self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.get_full_name()


class UserActivityLog(models.Model):
    """Audit log for logins, logouts, and sensitive actions."""

    ACTION_LOGIN_SUCCESS = 'login_success'
    ACTION_LOGIN_FAILED = 'login_failed'
    ACTION_LOGOUT = 'logout'
    ACTION_PRICE_UPDATE = 'price_update'
    ACTION_BULK_PRICE_UPDATE = 'bulk_price_update'
    ACTION_SPECIAL_PRICE_UPDATE = 'special_price_update'
    ACTION_TEMPLATE_CHANGE = 'template_change'
    ACTION_FINALIZE = 'finalize'
    ACTION_IMPERSONATE_START = 'impersonate_start'
    ACTION_OTHER = 'other'

    ACTION_CHOICES = (
        (ACTION_LOGIN_SUCCESS, 'Login success'),
        (ACTION_LOGIN_FAILED, 'Login failed'),
        (ACTION_LOGOUT, 'Logout'),
        (ACTION_PRICE_UPDATE, 'Price update'),
        (ACTION_BULK_PRICE_UPDATE, 'Bulk price update'),
        (ACTION_SPECIAL_PRICE_UPDATE, 'Special price update'),
        (ACTION_TEMPLATE_CHANGE, 'Template change'),
        (ACTION_FINALIZE, 'Finalize'),
        (ACTION_IMPERSONATE_START, 'Impersonate start'),
        (ACTION_OTHER, 'Other'),
    )

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='activity_logs',
    )
    action_type = models.CharField(max_length=32, choices=ACTION_CHOICES)
    ip_address = models.CharField(max_length=45, blank=True)  # IPv6 max length
    user_agent = models.TextField(blank=True)
    details = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['action_type', '-created_at']),
            models.Index(fields=['user', '-created_at']),
        ]
        verbose_name = 'User activity log'
        verbose_name_plural = 'User activity logs'

    def __str__(self):
        return f'{self.action_type} - {self.created_at}'
