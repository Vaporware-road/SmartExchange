from django.conf import settings
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView

from accounts.permissions import IsSuperAdminOrManagement, IsSuperAdminOrManagementOrEmployee
from bot_gateway.auth import BotCustomerAuthentication
from bot_gateway.permissions import IsBotCustomer
from bot_gateway.serializers import PublicOrderIntakeCreateSerializer
from bot_gateway.services.price_catalog import build_price_catalog
from bot_gateway.services.rates_cache import get_cached_live_rates
from orders.models import OrderIntake
from orders.serializers import OrderIntakeCreateSerializer, OrderIntakeSerializer


class BotCustomerAuthMeView(APIView):
    authentication_classes = [BotCustomerAuthentication]
    permission_classes = [IsBotCustomer]
    throttle_scope = "bot_gateway"
    throttle_classes = [ScopedRateThrottle]

    def get(self, request):
        customer = request.user
        rates = get_cached_live_rates()
        return Response(
            {
                "uuid": str(customer.uuid),
                "platform": customer.platform,
                "display_name": customer.display_name,
                "username": customer.username,
                "rates": rates,
                "price_catalog": build_price_catalog(rates),
            }
        )


class BotGatewayOrderSubmitView(APIView):
    authentication_classes = [BotCustomerAuthentication]
    permission_classes = [IsBotCustomer]
    throttle_scope = "bot_gateway"
    throttle_classes = [ScopedRateThrottle]

    def post(self, request):
        customer = request.user
        serializer = OrderIntakeCreateSerializer(
            data=request.data,
            context={"customer": customer, "request": request},
        )
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        return Response(
            OrderIntakeSerializer(order).data,
            status=status.HTTP_201_CREATED,
        )


class PublicOrderIntakeContextView(APIView):
    """Public order form bootstrap: live cached rates and categories."""

    permission_classes = [AllowAny]
    authentication_classes = []
    throttle_scope = "public_prices"
    throttle_classes = [ScopedRateThrottle]

    def get(self, request):
        rates = get_cached_live_rates()
        return Response(
            {
                "rates": rates,
                "price_catalog": build_price_catalog(rates),
                "order_url": _customer_order_url(),
            }
        )


class PublicOrderSubmitView(APIView):
    """Submit an order from the public web form (no bot JWT required)."""

    permission_classes = [AllowAny]
    authentication_classes = []
    throttle_scope = "bot_gateway"
    throttle_classes = [ScopedRateThrottle]

    def post(self, request):
        serializer = PublicOrderIntakeCreateSerializer(
            data=request.data,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


def _customer_order_url() -> str:
    base = getattr(settings, "BOT_GATEWAY_FRONTEND_URL", "").rstrip("/")
    if not base:
        base = "http://localhost:3000"
    return f"{base}/webapp/order"


class BotGatewayStatsView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]

    def get(self, request):
        from datetime import timedelta

        from django.core.cache import cache
        from django.utils import timezone

        from bot_gateway.models import BotCustomer, BotInteractionLog
        from bot_gateway.services.rates_cache import CACHE_KEY, CAPTIONS_KEY

        since = timezone.now() - timedelta(hours=24)
        return Response(
            {
                "customers": BotCustomer.objects.count(),
                "interactions_24h": BotInteractionLog.objects.filter(
                    created_at__gte=since
                ).count(),
                "pending_orders": OrderIntake.objects.filter(
                    status=OrderIntake.Status.PENDING
                ).count(),
                "cache": {
                    "rates_cached": cache.get(CACHE_KEY) is not None,
                    "captions_cached": cache.get(CAPTIONS_KEY) is not None,
                },
            }
        )
