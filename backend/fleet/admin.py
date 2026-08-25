from django.contrib import admin

from .models import CustomerDeployment


@admin.register(CustomerDeployment)
class CustomerDeploymentAdmin(admin.ModelAdmin):
    list_display = (
        "slug",
        "customer",
        "deployment_type",
        "status",
        "plan",
        "domain",
        "last_checkin_at",
        "renews_at",
    )
    list_filter = ("deployment_type", "status", "plan")
    search_fields = ("slug", "domain", "license_key", "customer__username", "customer__exchange_name")
    readonly_fields = ("created_at", "updated_at", "last_checkin_at", "last_checkin_uptime_seconds")
    autocomplete_fields = ("customer",)
