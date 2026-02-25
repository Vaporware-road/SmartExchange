from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from setting.utils import log_event
from .models import SpecialPriceHistory, SpecialPriceType
from .serializers import (
    SpecialPriceHistorySerializer,
    SpecialPriceTypeSerializer,
    SpecialPriceUpdateSerializer,
)


class SpecialPriceTypeViewSet(viewsets.ModelViewSet):
    queryset = SpecialPriceType.objects.prefetch_related(
        "special_price_histories"
    ).select_related("source_currency", "target_currency").all()
    serializer_class = SpecialPriceTypeSerializer


class SpecialPriceUpdateAPIView(APIView):
    """Update the price for a special price type."""

    def post(self, request, pk):
        try:
            spt = SpecialPriceType.objects.get(pk=pk)
        except SpecialPriceType.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SpecialPriceUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        old = SpecialPriceHistory.objects.filter(special_price_type=spt).first()
        old_price = old.price if old else None

        ph = SpecialPriceHistory.objects.create(
            special_price_type=spt,
            price=serializer.validated_data["price"],
            notes=serializer.validated_data.get("notes", ""),
        )

        log_event(
            level="INFO",
            source="system",
            message=f"Special price updated: {spt.name}",
            details=f"Old: {old_price}, New: {ph.price}",
            user=request.user if request.user.is_authenticated else None,
        )

        return Response(
            SpecialPriceHistorySerializer(ph).data,
            status=status.HTTP_201_CREATED,
        )


class SpecialPriceHistoryAPIView(ListAPIView):
    serializer_class = SpecialPriceHistorySerializer
    pagination_class = None

    def get_queryset(self):
        return SpecialPriceHistory.objects.filter(
            special_price_type_id=self.kwargs["pk"]
        ).order_by("-created_at")
