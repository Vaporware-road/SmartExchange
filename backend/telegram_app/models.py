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
    last_member_count = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Last Member Count",
        help_text="Cached subscriber count from the latest snapshot job.",
    )
    last_member_sampled_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Last Member Sampled At",
    )
    bot_admin_verified = models.BooleanField(
        default=False,
        verbose_name="Bot Admin Verified",
        help_text="Whether the bot was an administrator at the last snapshot.",
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
        indexes = [
            models.Index(fields=["tag"], name="customerprofile_tag_idx"),
        ]

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
        ADMIN_MENU = "ADMIN_MENU", "Admin Menu"
        ADMIN_REQUEST_LIST = "ADMIN_REQUEST_LIST", "Admin Request List"
        ADMIN_REQUEST_DETAIL = "ADMIN_REQUEST_DETAIL", "Admin Request Detail"
        ADMIN_CHANGE_STATE = "ADMIN_CHANGE_STATE", "Admin Change State"
        ADMIN_SET_TAG = "ADMIN_SET_TAG", "Admin Set Tag"
        ADMIN_ANALYTICS = "ADMIN_ANALYTICS", "Admin Analytics"
        ADMIN_ANALYTICS_EXCHANGE = "ADMIN_ANALYTICS_EXCHANGE", "Admin Analytics Exchange"
        ADMIN_ANALYTICS_MEMBERS = "ADMIN_ANALYTICS_MEMBERS", "Admin Analytics Members"
        ADMIN_REENGAGE = "ADMIN_REENGAGE", "Admin Re-engage"
        ADMIN_REENGAGE_AUDIENCE = "ADMIN_REENGAGE_AUDIENCE", "Admin Re-engage Audience"
        ADMIN_REENGAGE_COMPOSE = "ADMIN_REENGAGE_COMPOSE", "Admin Re-engage Compose"
        ADMIN_REENGAGE_SCHEDULE = "ADMIN_REENGAGE_SCHEDULE", "Admin Re-engage Schedule"
        ADMIN_OFFER_CREATE = "ADMIN_OFFER_CREATE", "Admin Offer Create"

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
        indexes = [
            models.Index(
                fields=["bot", "last_activity"],
                name="botsess_bot_activity_idx",
            ),
        ]
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
        NEW = "new", "New"
        CANCELLED = "cancelled", "Canceled"
        SUCCESSFUL = "successful", "Successful"

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
        default=Status.NEW,
        verbose_name="Status",
        db_index=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Exchange Request"
        verbose_name_plural = "Exchange Requests"
        ordering = ["-created_at"]
        indexes = [
            models.Index(
                fields=["bot", "status", "created_at"],
                name="exreq_bot_stat_created_idx",
            ),
            models.Index(
                fields=["customer", "created_at"],
                name="exreq_cust_created_idx",
            ),
        ]

    def __str__(self):
        return (
            f"{self.source_currency}->{self.target_currency} "
            f"{self.amount} ({self.status})"
        )

    def expires_at(self):
        return self.created_at + timedelta(minutes=int(self.ttl_minutes or 0))

    def is_running(self, *, now=None) -> bool:
        """New and still within TTL."""
        if self.status != self.Status.NEW:
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


class BotDailyUsageSnapshot(models.Model):
    """Daily count of distinct active bot users (from BotSession.last_activity)."""

    bot = models.ForeignKey(
        TelegramBot,
        on_delete=models.CASCADE,
        related_name="daily_usage_snapshots",
        verbose_name="Bot",
    )
    date = models.DateField(verbose_name="Date", db_index=True)
    active_users = models.PositiveIntegerField(default=0, verbose_name="Active Users")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Bot Daily Usage Snapshot"
        verbose_name_plural = "Bot Daily Usage Snapshots"
        ordering = ["-date"]
        constraints = [
            models.UniqueConstraint(
                fields=["bot", "date"],
                name="unique_bot_daily_usage_per_date",
            )
        ]

    def __str__(self):
        return f"{self.bot_id} {self.date}: {self.active_users} users"


class ChannelMemberSnapshot(models.Model):
    """Historical channel subscriber counts sampled via getChatMemberCount."""

    channel = models.ForeignKey(
        TelegramChannel,
        on_delete=models.CASCADE,
        related_name="member_snapshots",
        verbose_name="Channel",
    )
    member_count = models.PositiveIntegerField(verbose_name="Member Count")
    bot_is_admin = models.BooleanField(default=False, verbose_name="Bot Is Admin")
    sampled_at = models.DateTimeField(auto_now_add=True, verbose_name="Sampled At", db_index=True)

    class Meta:
        verbose_name = "Channel Member Snapshot"
        verbose_name_plural = "Channel Member Snapshots"
        ordering = ["-sampled_at"]

    def __str__(self):
        return f"{self.channel_id} @ {self.sampled_at}: {self.member_count}"


class BotCustomerGrowthSnapshot(models.Model):
    """Daily count of new bot DM users (first BotSession on this bot)."""

    bot = models.ForeignKey(
        TelegramBot,
        on_delete=models.CASCADE,
        related_name="customer_growth_snapshots",
        verbose_name="Bot",
    )
    date = models.DateField(verbose_name="Date", db_index=True)
    new_customers = models.PositiveIntegerField(default=0, verbose_name="New Customers")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Bot Customer Growth Snapshot"
        verbose_name_plural = "Bot Customer Growth Snapshots"
        ordering = ["-date"]
        constraints = [
            models.UniqueConstraint(
                fields=["bot", "date"],
                name="unique_bot_customer_growth_per_date",
            )
        ]

    def __str__(self):
        return f"{self.bot_id} {self.date}: +{self.new_customers}"


class ReengageCampaign(models.Model):
    """Scheduled audience re-engagement DM campaign."""

    class Audience(models.TextChoices):
        GLOBAL = "global", "Global"
        VIP = "vip", "VIP"
        SPECIAL = "special", "Special"
        INACTIVE = "inactive", "Inactive"

    class Schedule(models.TextChoices):
        DAILY = "daily", "Daily"
        WEEKLY = "weekly", "Weekly"
        MONTHLY = "monthly", "Monthly"

    bot = models.ForeignKey(
        TelegramBot,
        on_delete=models.CASCADE,
        related_name="reengage_campaigns",
        verbose_name="Bot",
    )
    audience = models.CharField(
        max_length=16,
        choices=Audience.choices,
        verbose_name="Audience",
    )
    message = models.TextField(verbose_name="Message")
    schedule = models.CharField(
        max_length=16,
        choices=Schedule.choices,
        default=Schedule.WEEKLY,
        verbose_name="Schedule",
    )
    is_active = models.BooleanField(default=True, verbose_name="Active")
    next_run_at = models.DateTimeField(verbose_name="Next Run At", db_index=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reengage_campaigns",
        verbose_name="Created By",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Re-engage Campaign"
        verbose_name_plural = "Re-engage Campaigns"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.bot_id} {self.audience} ({self.schedule})"


class ReengageOffer(models.Model):
    """Reusable offer template for re-engagement."""

    class Audience(models.TextChoices):
        GLOBAL = "global", "Global"
        VIP = "vip", "VIP"
        SPECIAL = "special", "Special"
        INACTIVE = "inactive", "Inactive"

    bot = models.ForeignKey(
        TelegramBot,
        on_delete=models.CASCADE,
        related_name="reengage_offers",
        verbose_name="Bot",
    )
    title = models.CharField(max_length=255, verbose_name="Title")
    body = models.TextField(verbose_name="Body")
    audience = models.CharField(
        max_length=16,
        choices=Audience.choices,
        default=Audience.GLOBAL,
        verbose_name="Audience",
    )
    valid_until = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Valid Until",
    )
    is_active = models.BooleanField(default=True, verbose_name="Active")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reengage_offers",
        verbose_name="Created By",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Re-engage Offer"
        verbose_name_plural = "Re-engage Offers"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class CampaignDeliveryLog(models.Model):
    """Audit trail for campaign or offer send runs."""

    bot = models.ForeignKey(
        TelegramBot,
        on_delete=models.CASCADE,
        related_name="campaign_delivery_logs",
        verbose_name="Bot",
    )
    campaign = models.ForeignKey(
        ReengageCampaign,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="delivery_logs",
        verbose_name="Campaign",
    )
    offer = models.ForeignKey(
        ReengageOffer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="delivery_logs",
        verbose_name="Offer",
    )
    sent = models.PositiveIntegerField(default=0, verbose_name="Sent")
    failed = models.PositiveIntegerField(default=0, verbose_name="Failed")
    skipped = models.PositiveIntegerField(default=0, verbose_name="Skipped")
    run_at = models.DateTimeField(auto_now_add=True, verbose_name="Run At", db_index=True)

    class Meta:
        verbose_name = "Campaign Delivery Log"
        verbose_name_plural = "Campaign Delivery Logs"
        ordering = ["-run_at"]

    def __str__(self):
        return f"bot={self.bot_id} sent={self.sent} @ {self.run_at}"
