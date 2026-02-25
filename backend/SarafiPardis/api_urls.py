"""
Unified API router for SmartExchange Panel.
All DRF endpoints are mounted under /api/.
"""
from django.urls import path, include

urlpatterns = [
    path("auth/", include("accounts.api_urls")),
    path("dashboard/", include("dashboard.api_urls")),
    path("categories/", include("category.api_urls")),
    path("prices/", include("change_price.api_urls")),
    path("special-prices/", include("special_price.api_urls")),
    path("finalize/", include("finalize.api_urls")),
    path("telegram/", include("telegram_app.api_urls")),
    path("settings/", include("setting.api_urls")),
    path("analysis/", include("analysis.api_urls")),
    path("templates/", include("price_publisher.api_urls")),
    path("template-editor/", include("template_editor.api_urls")),
]
