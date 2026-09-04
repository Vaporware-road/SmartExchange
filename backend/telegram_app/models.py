import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q

from category.models import Category
from special_price.models import SpecialPriceType


class TelegramBot(models.Model):
    """Model representing a Telegram bot."""

    name = models.CharField(
        max_length=100,
        verbose_name="Bot Name",
        help_text="A friendly name for this bot",
    )
    token = models.CharField(
        max_length=200,
        verbose_name="Bot Token",
        help_text="Telegram bot token from @BotFather",
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
    webhook_secret_token = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        db_index=True,
        verbose_name="Webhook Secret",
        help_text="Secret UUID used in inbound webhook URL",
    )
    gateway_enabled = models.BooleanField(
        default=False,
        verbose_name="Gateway Enabled",
        help_text="Enable inbound auto-reply for customer messages",
    )
    default_category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="gateway_bots",
        verbose_name="Default Price Board",
        help_text="Category board shown when no currency keyword is matched",
    )
    order_button_text = models.CharField(
        max_length=128,
        default="🛒 ثبت سفارش سریع",
        blank=True,
        verbose_name="Order Button Text",
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
