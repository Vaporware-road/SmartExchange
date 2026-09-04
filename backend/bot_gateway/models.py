import uuid

from django.db import models
from django.utils import timezone

from category.models import Category
from instagram_hub.encryption import decrypt_token, encrypt_token


class Platform(models.TextChoices):
    TELEGRAM = "telegram", "Telegram"
    WHATSAPP = "whatsapp", "WhatsApp"
    WEB = "web", "Web"


class AuthStatus(models.TextChoices):
    ANONYMOUS = "anonymous", "Anonymous"
    VERIFIED = "verified", "Verified"


class TriggerType(models.TextChoices):
    START = "start", "Start"
    PRICE_KEYWORD = "price_keyword", "Price keyword"
    CURRENCY_MATCH = "currency_match", "Currency match"
    OTHER = "other", "Other"


class Direction(models.TextChoices):
    INBOUND = "inbound", "Inbound"
    OUTBOUND = "outbound", "Outbound"


class BotCustomer(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    platform = models.CharField(max_length=16, choices=Platform.choices)
    telegram_chat_id = models.BigIntegerField(null=True, blank=True, db_index=True)
    whatsapp_phone = models.CharField(max_length=32, blank=True, db_index=True)
    display_name = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=True)
    auth_status = models.CharField(
        max_length=16, choices=AuthStatus.choices, default=AuthStatus.ANONYMOUS
    )
    first_seen_at = models.DateTimeField(default=timezone.now)
    last_seen_at = models.DateTimeField(default=timezone.now)
    metadata = models.JSONField(default=dict, blank=True)

    class Meta:
        verbose_name = "Bot Customer"
        verbose_name_plural = "Bot Customers"
        constraints = [
            models.UniqueConstraint(
                fields=["platform", "telegram_chat_id"],
                condition=models.Q(telegram_chat_id__isnull=False),
                name="unique_bot_customer_telegram",
            ),
            models.UniqueConstraint(
                fields=["platform", "whatsapp_phone"],
                condition=~models.Q(whatsapp_phone=""),
                name="unique_bot_customer_whatsapp",
            ),
        ]
        indexes = [
            models.Index(fields=["platform", "last_seen_at"]),
        ]

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def __str__(self):
        if self.platform == Platform.TELEGRAM:
            return f"TG:{self.telegram_chat_id}"
        return f"WA:{self.whatsapp_phone or self.uuid}"


class BotInteractionLog(models.Model):
    customer = models.ForeignKey(
        BotCustomer, on_delete=models.CASCADE, related_name="interactions"
    )
    platform = models.CharField(max_length=16, choices=Platform.choices)
    direction = models.CharField(max_length=8, choices=Direction.choices)
    message_text = models.TextField(blank=True)
    trigger_type = models.CharField(
        max_length=32, choices=TriggerType.choices, default=TriggerType.OTHER
    )
    response_ms = models.PositiveIntegerField(null=True, blank=True)
    was_rate_limited = models.BooleanField(default=False)
    update_id = models.CharField(max_length=64, blank=True, db_index=True)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        verbose_name = "Bot Interaction Log"
        verbose_name_plural = "Bot Interaction Logs"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["customer", "created_at"]),
        ]

    def __str__(self):
        return f"{self.platform} {self.direction} @ {self.created_at:%Y-%m-%d %H:%M}"


class WhatsAppConfig(models.Model):
    """Meta Cloud API credentials for WhatsApp Business messaging."""

    name = models.CharField(max_length=128, default="Default")
    phone_number_id = models.CharField(max_length=64, blank=True)
    waba_id = models.CharField(max_length=64, blank=True)
    access_token_encrypted = models.TextField(blank=True)
    app_secret_encrypted = models.TextField(blank=True)
    verify_token = models.CharField(max_length=128, blank=True)
    default_category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="whatsapp_configs",
    )
    order_button_text = models.CharField(
        max_length=128, default="🛒 ثبت سفارش سریع", blank=True
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "WhatsApp Config"
        verbose_name_plural = "WhatsApp Configs"
        ordering = ["-is_active", "name"]

    def __str__(self):
        return f"{self.name} (active={self.is_active})"

    def get_access_token(self) -> str:
        return decrypt_token(self.access_token_encrypted)

    def set_access_token(self, plain: str) -> None:
        self.access_token_encrypted = encrypt_token((plain or "").strip())

    def get_app_secret(self) -> str:
        return decrypt_token(self.app_secret_encrypted)

    def set_app_secret(self, plain: str) -> None:
        self.app_secret_encrypted = encrypt_token((plain or "").strip())
