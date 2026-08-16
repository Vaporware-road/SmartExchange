from datetime import timedelta

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q
from django.utils import timezone

from category.models import Category
from special_price.models import SpecialPriceType
from instagram_hub.encryption import decrypt_token, encrypt_token


class TelegramBot(models.Model):
    """Model representing a Telegram bot."""

    name = models.CharField(
        max_length=100,
        verbose_name="Bot Name",
        help_text="A friendly name for this bot",
    )
    token = models.CharField(
        max_length=500,
        verbose_name="Bot Token",
        help_text="Telegram bot token from @BotFather (encrypted at rest)",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="telegram_bots",
        verbose_name="Owner",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active",
        help_text="Whether this bot is currently active",
    )
    display_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Display Name",
        help_text="Optional friendly display name",
    )
    notes = models.TextField(
        blank=True,
        verbose_name="Notes",
        help_text="Optional security or usage notes",
    )
    restrict_to_known_channels = models.BooleanField(
        default=False,
        verbose_name="Restrict to known channels",
        help_text="If set, only allow sending to channels registered in this panel",
    )
    log_all_messages = models.BooleanField(
        default=False,
        verbose_name="Log all messages",
        help_text="If set, log all messages sent via this bot",
    )
    default_exchange_ttl_minutes = models.PositiveIntegerField(
        default=5,
        validators=[MinValueValidator(1)],
        verbose_name="Default exchange TTL (minutes)",
        help_text="TTL applied to new exchange requests from this bot. End-users cannot change it.",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
    )

    class Meta:
        verbose_name = "Telegram Bot"
        verbose_name_plural = "Telegram Bots"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def get_plain_token(self):
        decrypted = decrypt_token(self.token)
        return decrypted or self.token

    def save(self, *args, **kwargs):
        if self.token and not str(self.token).startswith("gAAAAA"):
            self.token = encrypt_token(self.token)
        super().save(*args, **kwargs)


class TelegramChannel(models.Model):
    """Model representing a Telegram channel."""

    bot = models.ForeignKey(
        TelegramBot,
        on_delete=models.CASCADE,
        related_name="channels",
        verbose_name="Bot",
        help_text="The bot used to send messages to this channel",
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Channel Name",
        help_text="A friendly name for this channel",
    )
    chat_id = models.CharField(
        max_length=50,
        verbose_name="Chat ID",
        help_text="Telegram channel chat ID (e.g., @channelname or -1001234567890)",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active",
        help_text="Whether this channel is currently active",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
    )

    class Meta:
        verbose_name = "Telegram Channel"
        verbose_name_plural = "Telegram Channels"
        ordering = ["-created_at"]
        unique_together = ["bot", "chat_id"]

    def __str__(self):
        return f"{self.name} ({self.chat_id})"


class DefaultMessageSettings(models.Model):
    """Defines default caption and buttons per bot for rendered messages."""

    bot = models.ForeignKey(
        TelegramBot,
        on_delete=models.CASCADE,
        related_name="message_settings",
        verbose_name="Bot",
    )
    default_caption = models.TextField(
        blank=True,
        verbose_name="Default Caption",
        help_text="Optional caption appended to generated messages.",
    )
    default_buttons = models.JSONField(
        blank=True,
        default=list,
        verbose_name="Default Buttons",
        help_text="JSON structure describing inline buttons. Example: "
        '[{"text": "View", "url": "https://example.com"}]',
    )
    active = models.BooleanField(
        default=True,
        verbose_name="Active",
        help_text="Only one setting can be active per bot.",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Default Message Setting"
        verbose_name_plural = "Default Message Settings"
        ordering = ["-updated_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["bot"],
                condition=Q(active=True),
                name="unique_active_message_settings_per_bot",
            )
        ]

    def clean(self):
        super().clean()
        if self.active:
            conflict = (
                DefaultMessageSettings.objects.filter(bot=self.bot, active=True)
                .exclude(pk=self.pk)
                .exists()
            )
            if conflict:
                raise ValidationError(
                    {"active": "Another active setting already exists for this bot."}
                )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        if self.active:
            (
                DefaultMessageSettings.objects.filter(bot=self.bot, active=True)
                .exclude(pk=self.pk)
                .update(active=False)
            )

    def __str__(self):
        status = "active" if self.active else "inactive"
        return f"{self.bot} ({status})"


class AutoPostConfig(models.Model):
    """
    Configuration for automatic Telegram posting.

    This model is configuration-only; a scheduler (Celery/cron) can read it and
    call the existing price publisher services.
    """

    channel = models.ForeignKey(
        TelegramChannel,
        on_delete=models.CASCADE,
        related_name="auto_post_configs",
        verbose_name="Channel",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="auto_post_configs",
        null=True,
        blank=True,
        verbose_name="Category",
    )
    special_price_type = models.ForeignKey(
        SpecialPriceType,
        on_delete=models.CASCADE,
        related_name="auto_post_configs",
        null=True,
        blank=True,
        verbose_name="Special Price Type",
    )
    time_of_day = models.TimeField(
        verbose_name="Time of Day",
        help_text="Local time of day when auto-post should run.",
    )
    timezone = models.CharField(
        max_length=64,
        default="Asia/Tehran",
        verbose_name="Time Zone",
        help_text="IANA timezone name used when interpreting time_of_day.",
    )
    enabled = models.BooleanField(
        default=True,
        verbose_name="Enabled",
        help_text="Whether this configuration is currently active.",
    )
    notes = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Notes",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Auto Post Config"
        verbose_name_plural = "Auto Post Configs"
        ordering = ["-created_at"]

    def clean(self):
        super().clean()
        if not self.category and not self.special_price_type:
            raise ValidationError(
                "At least one of category or special_price_type must be set."
            )

    def __str__(self):
        target = self.category or self.special_price_type
        return f"AutoPost for {target} on {self.channel}"


class CustomerProfile(models.Model):
    """Telegram customer known to the conversational bot."""

    class Tag(models.TextChoices):
        GLOBAL = "global", "Global"
        VIP = "vip", "VIP"
        SPECIAL = "special", "Special"

    telegram_user_id = models.BigIntegerField(
        unique=True,
        verbose_name="Telegram User ID",
        help_text="Telegram user id from updates (unique per customer).",
    )
    username = models.CharField(
        max_length=255,
        blank=True,
        default="",
        verbose_name="Username",
    )
    first_name = models.CharField(
        max_length=255,
        blank=True,
        default="",
        verbose_name="First Name",
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        default="",
        verbose_name="Last Name",
    )
    language = models.CharField(
        max_length=16,
        blank=True,
        default="",
        verbose_name="Language",
        help_text="Telegram language_code or preferred language.",
    )
    tag = models.CharField(
        max_length=16,
        choices=Tag.choices,
        default=Tag.GLOBAL,
        verbose_name="Tag",
        help_text="Staff-assigned customer tag (global, vip, or special).",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Customer Profile"
        verbose_name_plural = "Customer Profiles"
        ordering = ["-created_at"]

    def __str__(self):
        label = self.username or self.first_name or str(self.telegram_user_id)
        return f"{label} ({self.telegram_user_id})"


class BotSession(models.Model):
    """Per-bot FSM session for a Telegram user."""

    class State(models.TextChoices):
        START = "START", "Start"
        MAIN_MENU = "MAIN_MENU", "Main Menu"
        PROFILE = "PROFILE", "Profile"
        EXCHANGE_SOURCE = "EXCHANGE_SOURCE", "Exchange Source"
        EXCHANGE_TARGET = "EXCHANGE_TARGET", "Exchange Target"
        EXCHANGE_AMOUNT = "EXCHANGE_AMOUNT", "Exchange Amount"
        EXCHANGE_PRICE = "EXCHANGE_PRICE", "Exchange Price"
        EXCHANGE_TTL = "EXCHANGE_TTL", "Exchange TTL"
        EXCHANGE_SUMMARY = "EXCHANGE_SUMMARY", "Exchange Summary"
        ALERT_MENU = "ALERT_MENU", "Alert Menu"
        ALERT_SOURCE = "ALERT_SOURCE", "Alert Source"
        ALERT_TARGET = "ALERT_TARGET", "Alert Target"
        ALERT_PRICE = "ALERT_PRICE", "Alert Price"
        ALERT_SUMMARY = "ALERT_SUMMARY", "Alert Summary"

    telegram_user_id = models.BigIntegerField(
        verbose_name="Telegram User ID",
        db_index=True,
    )
    bot = models.ForeignKey(
        TelegramBot,
        on_delete=models.CASCADE,
        related_name="bot_sessions",
        verbose_name="Bot",
    )
    state = models.CharField(
        max_length=64,
        choices=State.choices,
        default=State.START,
        verbose_name="State",
    )
    context = models.JSONField(
        default=dict,
        blank=True,
        verbose_name="Context",
        help_text="Opaque FSM draft / scratch data for the conversation.",
    )
    last_activity = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Activity",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Bot Session"
        verbose_name_plural = "Bot Sessions"
        ordering = ["-last_activity"]
        constraints = [
            models.UniqueConstraint(
                fields=["telegram_user_id", "bot"],
                name="unique_bot_session_per_user_bot",
            )
        ]

    def __str__(self):
        return f"Session {self.telegram_user_id} @ {self.bot_id} ({self.state})"


class ExchangeRequest(models.Model):
    """Customer exchange registration submitted via the bot."""

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        NOTIFIED = "notified", "Notified"
        CANCELLED = "cancelled", "Cancelled"
        CLOSED = "closed", "Closed"

    customer = models.ForeignKey(
        CustomerProfile,
        on_delete=models.CASCADE,
        related_name="exchange_requests",
        verbose_name="Customer",
    )
    bot = models.ForeignKey(
        TelegramBot,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="exchange_requests",
        verbose_name="Bot",
    )
    source_currency = models.CharField(
        max_length=8,
        verbose_name="Source Currency",
        help_text="ISO 4217 code.",
    )
    target_currency = models.CharField(
        max_length=8,
        verbose_name="Target Currency",
        help_text="ISO 4217 code.",
    )
    amount = models.DecimalField(
        max_digits=20,
        decimal_places=8,
        verbose_name="Amount",
    )
    price_at_request = models.DecimalField(
        max_digits=20,
        decimal_places=8,
        null=True,
        blank=True,
        verbose_name="Price at Request",
        help_text="Optional historical price; no longer collected from the bot.",
    )
    ttl_minutes = models.PositiveIntegerField(
        verbose_name="TTL (minutes)",
    )
    status = models.CharField(
        max_length=16,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name="Status",
        db_index=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Exchange Request"
        verbose_name_plural = "Exchange Requests"
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.source_currency}->{self.target_currency} "
            f"{self.amount} ({self.status})"
        )

    def expires_at(self):
        return self.created_at + timedelta(minutes=int(self.ttl_minutes or 0))

    def is_running(self, *, now=None) -> bool:
        """Pending/notified and still within TTL."""
        if self.status not in (self.Status.PENDING, self.Status.NOTIFIED):
            return False
        return self.expires_at() > (now or timezone.now())


class PriceAlert(models.Model):
    """Customer price increase/decrease alert subscription."""

    class Direction(models.TextChoices):
        INCREASE = "increase", "Increase"
        DECREASE = "decrease", "Decrease"

    customer = models.ForeignKey(
        CustomerProfile,
        on_delete=models.CASCADE,
        related_name="price_alerts",
        verbose_name="Customer",
    )
    direction = models.CharField(
        max_length=16,
        choices=Direction.choices,
        verbose_name="Direction",
    )
    source_currency = models.CharField(
        max_length=8,
        verbose_name="Source Currency",
        help_text="ISO 4217 code.",
    )
    target_currency = models.CharField(
        max_length=8,
        verbose_name="Target Currency",
        help_text="ISO 4217 code.",
    )
    target_price = models.DecimalField(
        max_digits=20,
        decimal_places=8,
        verbose_name="Target Price",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active",
        db_index=True,
    )
    last_triggered_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Last Triggered At",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Price Alert"
        verbose_name_plural = "Price Alerts"
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.direction} {self.source_currency}/{self.target_currency} "
            f"@ {self.target_price}"
        )
