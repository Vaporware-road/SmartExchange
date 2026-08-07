from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView

from core.prices_snapshot import build_prices_public_snapshot


class PublicPricesAPIView(APIView):
    """
    GET /api/public/prices/ — latest category and special prices as JSON.
    No authentication (invalid JWT must not block access).
    """

    permission_classes = [AllowAny]
    authentication_classes = []
    throttle_scope = "public_prices"
    throttle_classes = [ScopedRateThrottle]

    def get(self, request):
        return Response(build_prices_public_snapshot())
