from django import forms
from django.contrib import admin
from django.contrib import messages
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .models import (
    BotCustomerGrowthSnapshot,
    BotDailyUsageSnapshot,
    BotSession,
    CampaignDeliveryLog,
    ChannelMemberSnapshot,
    CustomerProfile,
    DefaultMessageSettings,
    ExchangeRequest,
    PriceAlert,
    ReengageCampaign,
    ReengageOffer,
    TelegramBot,
    TelegramChannel,
)
from .services.telegram_client import TelegramService


@admin.register(TelegramBot)
class TelegramBotAdmin(admin.ModelAdmin):
    """Admin interface for TelegramBot model."""
    
    list_display = (
        'name',
        'is_active',
        'default_exchange_ttl_minutes',
        'created_at',
        'updated_at',
    )
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'token')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'token', 'is_active', 'default_exchange_ttl_minutes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        """Make token readonly if object exists to prevent accidental changes."""
        if obj:
            return self.readonly_fields + ('token',)
        return self.readonly_fields


@admin.register(TelegramChannel)
class TelegramChannelAdmin(admin.ModelAdmin):
    """Admin interface for TelegramChannel model."""
    
    list_display = ('name', 'bot', 'chat_id', 'is_active', 'last_member_count', 'bot_admin_verified', 'created_at')
    list_filter = ('bot', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'bot__name', 'chat_id')
    readonly_fields = ('created_at', 'updated_at')
    list_select_related = ('bot',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': (
                'name', 'bot', 'chat_id', 'is_active',
                'last_member_count', 'last_member_sampled_at', 'bot_admin_verified',
            )
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )       


@admin.register(DefaultMessageSettings)
class DefaultMessageSettingsAdmin(admin.ModelAdmin):
    list_display = ("bot", "active", "updated_at")
    list_filter = ("active", "updated_at", "bot")
    search_fields = ("bot__name",)
    readonly_fields = ("created_at", "updated_at", "preview_markup")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "bot",
                    "active",
                    "default_caption",
                    "default_buttons",
                    "preview_markup",
                )
            },
        ),
        (
            _("Metadata"),
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
    actions = ("preview_in_chat",)

    formfield_overrides = {
        models.JSONField: {
            "widget": forms.Textarea(
                attrs={
                    "rows": 6,
                    "class": "vLargeTextField monospace",
                    "placeholder": '[ [{"text": "View", "url": "https://example.com"}] ]',
                }
            )
        }
    }

    @admin.display(description=_("Preview"))
    def preview_markup(self, obj):
        if not obj:
            return _("Save to preview.")
        buttons = obj.default_buttons or []
        if not buttons:
            return _("No buttons configured.")
        markup = "<br>".join(
            " | ".join(f"{btn.get('text')} → {btn.get('url') or btn.get('callback_data')}" for btn in row)
            for row in buttons
        )
        return mark_safe(markup)

    @admin.action(description=_("Send preview to first active channel"))
    def preview_in_chat(self, request, queryset):
        for setting in queryset:
            channel = setting.bot.channels.filter(is_active=True).first()
            if not channel:
                self.message_user(
                    request,
                    _(f"No active channels for bot '{setting.bot}'."),
                    level=messages.WARNING,
                )
                continue

            try:
                client = TelegramService(setting.bot.get_plain_token())
                success, detail, _ = client.send_message(
                    chat_id=channel.chat_id,
                    text=setting.default_caption or "Preview caption",
                    buttons=setting.default_buttons,
                )
            except Exception as exc:  # pragma: no cover
                success = False
                detail = str(exc)

            if success:
                self.message_user(
                    request,
                    _(f"Preview sent to {channel.chat_id}: {detail}"),
                    level=messages.SUCCESS,
                )
            else:
                self.message_user(
                    request,
                    _(f"Failed to send preview to {channel.chat_id}: {detail}"),
                    level=messages.ERROR,
                )


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = (
        "telegram_user_id",
        "username",
        "first_name",
        "last_name",
        "tag",
        "language",
        "updated_at",
    )
    list_filter = ("tag", "language", "created_at")
    search_fields = ("telegram_user_id", "username", "first_name", "last_name")
    readonly_fields = ("created_at", "updated_at")


@admin.register(BotSession)
class BotSessionAdmin(admin.ModelAdmin):
    list_display = (
        "telegram_user_id",
        "bot",
        "state",
        "last_activity",
        "updated_at",
    )
    list_filter = ("state", "bot", "last_activity")
    search_fields = ("telegram_user_id", "bot__name")
    readonly_fields = ("created_at", "updated_at", "last_activity")
    list_select_related = ("bot",)


@admin.register(ExchangeRequest)
class ExchangeRequestAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "source_currency",
        "target_currency",
        "amount",
        "price_at_request",
        "ttl_minutes",
        "status",
        "created_at",
    )
    list_filter = ("status", "source_currency", "target_currency", "created_at")
    search_fields = (
        "customer__telegram_user_id",
        "customer__username",
        "source_currency",
        "target_currency",
    )
    readonly_fields = ("created_at", "updated_at")
    list_select_related = ("customer", "bot")


@admin.register(PriceAlert)
class PriceAlertAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "direction",
        "source_currency",
        "target_currency",
        "target_price",
        "is_active",
        "last_triggered_at",
        "created_at",
    )
    list_filter = ("direction", "is_active", "source_currency", "target_currency")
    search_fields = (
        "customer__telegram_user_id",
        "customer__username",
        "source_currency",
        "target_currency",
    )
    readonly_fields = ("created_at", "updated_at")
    list_select_related = ("customer",)


@admin.register(BotDailyUsageSnapshot)
class BotDailyUsageSnapshotAdmin(admin.ModelAdmin):
    list_display = ("bot", "date", "active_users", "created_at")
    list_filter = ("bot", "date")
    date_hierarchy = "date"


@admin.register(BotCustomerGrowthSnapshot)
class BotCustomerGrowthSnapshotAdmin(admin.ModelAdmin):
    list_display = ("bot", "date", "new_customers", "created_at")
    list_filter = ("bot", "date")
    date_hierarchy = "date"


@admin.register(ChannelMemberSnapshot)
class ChannelMemberSnapshotAdmin(admin.ModelAdmin):
    list_display = ("channel", "member_count", "bot_is_admin", "sampled_at")
    list_filter = ("bot_is_admin", "channel__bot")
    date_hierarchy = "sampled_at"
    list_select_related = ("channel", "channel__bot")


@admin.register(ReengageCampaign)
class ReengageCampaignAdmin(admin.ModelAdmin):
    list_display = ("bot", "audience", "schedule", "is_active", "next_run_at", "updated_at")
    list_filter = ("audience", "schedule", "is_active", "bot")
    search_fields = ("message",)
    list_select_related = ("bot", "created_by")


@admin.register(ReengageOffer)
class ReengageOfferAdmin(admin.ModelAdmin):
    list_display = ("title", "bot", "audience", "is_active", "valid_until", "updated_at")
    list_filter = ("audience", "is_active", "bot")
    search_fields = ("title", "body")
    list_select_related = ("bot", "created_by")


@admin.register(CampaignDeliveryLog)
class CampaignDeliveryLogAdmin(admin.ModelAdmin):
    list_display = ("bot", "campaign", "offer", "sent", "failed", "skipped", "run_at")
    list_filter = ("bot", "run_at")
    date_hierarchy = "run_at"
    list_select_related = ("bot", "campaign", "offer")