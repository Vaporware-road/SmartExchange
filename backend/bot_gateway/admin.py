from django.contrib import admin

from bot_gateway.models import BotCustomer, BotInteractionLog, WhatsAppConfig


@admin.register(BotCustomer)
class BotCustomerAdmin(admin.ModelAdmin):
    list_display = ("uuid", "platform", "telegram_chat_id", "whatsapp_phone", "last_seen_at")
    list_filter = ("platform", "auth_status")
    search_fields = ("telegram_chat_id", "whatsapp_phone", "display_name", "username")
    readonly_fields = ("uuid", "first_seen_at", "last_seen_at")


@admin.register(BotInteractionLog)
class BotInteractionLogAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "platform",
        "direction",
        "trigger_type",
        "was_rate_limited",
        "response_ms",
        "customer",
    )
    list_filter = ("platform", "direction", "trigger_type", "was_rate_limited")
    search_fields = ("message_text", "update_id")
    readonly_fields = ("created_at",)


@admin.register(WhatsAppConfig)
class WhatsAppConfigAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number_id", "is_active", "updated_at")
    list_filter = ("is_active",)
