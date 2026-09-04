from django.conf import settings
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsSuperAdminOrManagementOrEmployee
from orders.models import OrderIntake
from orders.serializers import (
    OrderIntakeReviewSerializer,
    OrderIntakeSerializer,
)


class OrderIntakeLinkView(APIView):
    """Return the public customer order URL for sharing."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagementOrEmployee]

    def get(self, request):
        configured = getattr(settings, "BOT_GATEWAY_FRONTEND_URL", "").rstrip("/")
        origin = (request.headers.get("Origin") or "").rstrip("/")
        base = configured or origin or "http://localhost:3000"
        return Response(
            {
                "url": f"{base}/webapp/order",
                "configured_base": configured or None,
            }
        )


class OrderPendingCountView(APIView):
    """Lightweight pending order count for sidebar badge."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagementOrEmployee]

    def get(self, request):
        pending = OrderIntake.objects.filter(status=OrderIntake.Status.PENDING).count()
        return Response({"pending": pending})


class OrderIntakeListView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdminOrManagementOrEmployee]

    def get(self, request):
        qs = OrderIntake.objects.select_related(
            "customer", "category", "price_type"
        ).order_by("-created_at")
        status_filter = request.query_params.get("status")
        if status_filter:
            qs = qs.filter(status=status_filter)
        return Response(OrderIntakeSerializer(qs[:200], many=True).data)


class OrderIntakeDetailView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdminOrManagementOrEmployee]

    def delete(self, request, uuid):
        order = OrderIntake.objects.filter(uuid=uuid).first()
        if not order:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderIntakeReviewView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdminOrManagementOrEmployee]

    def patch(self, request, uuid):
        order = OrderIntake.objects.filter(uuid=uuid).first()
        if not order:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = OrderIntakeReviewSerializer(order, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        order = serializer.save(
            reviewed_by=request.user,
            reviewed_at=timezone.now(),
        )
        return Response(OrderIntakeSerializer(order).data)
