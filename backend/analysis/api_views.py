"""
DRF API views for analysis dashboard.
"""
import logging

from django.conf import settings
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .views import AnalyticsDashboardView

logger = logging.getLogger(__name__)


def _empty_analytics_dashboard_payload(detail: str) -> dict:
    """Same shape as ``get_analytics_data`` so the SPA never breaks on degraded responses."""
    return {
        "degraded": True,
        "detail": detail,
        "generated_at": timezone.localtime(timezone.now()).isoformat(),
        "latest_cards": [],
        "special_cards": [],
        "top_movers": [],
        "price_statistics": {},
        "finalization_stats": {},
        "overall_stats": {},
        "timeline_data": [],
        "special_timeline_data": [],
        "category_summary": [],
        "telegram_engagement": {"timeline": [], "channels": []},
    }


class AnalysisDashboardAPIView(APIView):
    """
    GET /api/analysis/dashboard/ - full analytics data for charts and cards.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            view = AnalyticsDashboardView()
            view.request = request
            view.kwargs = {}
            data = view.get_analytics_data()
            return Response(data)
        except Exception as exc:
            logger.exception("AnalysisDashboardAPIView.get failed")
            detail = str(exc) if settings.DEBUG else "Analytics temporarily unavailable."
            # Return 200 so optional home-dashboard analytics never triggers a global
            # client redirect to the generic 500 page (see frontend axios interceptor).
            return Response(_empty_analytics_dashboard_payload(detail))
