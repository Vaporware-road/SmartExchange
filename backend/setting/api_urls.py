from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import api_views

router = DefaultRouter()
router.register(r"bots", api_views.TelegramBotViewSet, basename="api-setting-bot")
router.register(r"channels", api_views.TelegramChannelViewSet, basename="api-setting-channel")

urlpatterns = [
    path("site/", api_views.SiteSettingsAPIView.as_view(), name="api-settings-site"),
    path("logs/", api_views.LogListAPIView.as_view(), name="api-settings-logs"),
    path("", include(router.urls)),
]
