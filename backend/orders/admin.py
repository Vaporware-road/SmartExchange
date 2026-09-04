from django.contrib import admin

from orders.models import OrderIntake


@admin.register(OrderIntake)
class OrderIntakeAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "status",
        "trade_type",
        "category",
        "amount",
        "platform",
        "created_at",
    )
    list_filter = ("status", "platform", "trade_type")
    search_fields = ("uuid", "customer_note", "admin_note")
    readonly_fields = ("uuid", "created_at", "reviewed_at")
