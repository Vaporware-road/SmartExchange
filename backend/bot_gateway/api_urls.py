from django.urls import path

from bot_gateway.api_views import (
    BotCustomerAuthMeView,
    BotGatewayOrderSubmitView,
    BotGatewayStatsView,
    PublicOrderIntakeContextView,
    PublicOrderSubmitView,
)
from bot_gateway.views.webhook import WhatsAppWebhookView

urlpatterns = [
    path(
        "webhook/whatsapp/",
        WhatsAppWebhookView.as_view(),
        name="bot-gateway-whatsapp-webhook",
    ),
    path(
        "public/intake/",
        PublicOrderIntakeContextView.as_view(),
        name="bot-gateway-public-intake",
    ),
    path(
        "public/orders/",
        PublicOrderSubmitView.as_view(),
        name="bot-gateway-public-order-submit",
    ),
    path("auth/me/", BotCustomerAuthMeView.as_view(), name="bot-gateway-auth-me"),
    path("orders/", BotGatewayOrderSubmitView.as_view(), name="bot-gateway-order-submit"),
    path("stats/", BotGatewayStatsView.as_view(), name="bot-gateway-stats"),
]
