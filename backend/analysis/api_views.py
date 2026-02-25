"""
DRF API views for analysis dashboard.
"""
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .views import AnalyticsDashboardView


class AnalysisDashboardAPIView(APIView):
    """
    GET /api/analysis/dashboard/ - full analytics data for charts and cards.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        view = AnalyticsDashboardView()
        view.request = request
        view.kwargs = {}
        data = view.get_analytics_data()
        return Response(data)
