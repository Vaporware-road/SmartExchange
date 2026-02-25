from django.db import transaction
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from category.models import Category, PriceType
from setting.utils import log_event
from .models import PriceHistory
from .serializers import (
    BulkPriceUpdateSerializer,
    PriceHistorySerializer,
    PriceUpdateSerializer,
    PriceTypeWithLatestPriceSerializer,
)


class PriceListAPIView(APIView):
    """All price types with their latest prices."""

    def get(self, request):
        price_types = (
            PriceType.objects.select_related(
                "category", "source_currency", "target_currency"
            )
            .prefetch_related("price_histories")
            .all()
        )

        data = []
        for pt in price_types:
            latest = pt.price_histories.first()
            data.append({
                "id": pt.id,
                "name": pt.name,
                "slug": pt.slug,
                "category_id": pt.category_id,
                "category_name": pt.category.name,
                "source_currency": pt.source_currency.code,
                "target_currency": pt.target_currency.code,
                "trade_type": pt.trade_type,
                "latest_price": latest.price if latest else None,
                "latest_price_at": latest.created_at if latest else None,
            })

        serializer = PriceTypeWithLatestPriceSerializer(data, many=True)
        return Response(serializer.data)


class PriceUpdateAPIView(APIView):
    """Update a single price type."""

    def post(self, request, price_type_id):
        try:
            price_type = PriceType.objects.select_related("category").get(id=price_type_id)
        except PriceType.DoesNotExist:
            return Response({"detail": "Price type not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PriceUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        old_price_obj = PriceHistory.objects.filter(price_type=price_type).first()
        old_price = old_price_obj.price if old_price_obj else None

        price_history = PriceHistory.objects.create(
            price_type=price_type,
            price=serializer.validated_data["price"],
            notes=serializer.validated_data.get("notes", ""),
        )

        log_event(
            level="INFO",
            source="system",
            message=f"Price updated for {price_type.name} ({price_type.category.name})",
            details=f"Old: {old_price}, New: {price_history.price}",
            user=request.user if request.user.is_authenticated else None,
        )

        return Response(
            PriceHistorySerializer(price_history).data,
            status=status.HTTP_201_CREATED,
        )


class BulkPriceUpdateAPIView(APIView):
    """Bulk-update prices for all price types in a category."""

    def post(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({"detail": "Category not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = BulkPriceUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        prices_map = serializer.validated_data["prices"]
        notes = serializer.validated_data.get("notes", "")

        price_types = PriceType.objects.filter(category=category)
        created = []

        with transaction.atomic():
            for pt in price_types:
                key = str(pt.id)
                if key not in prices_map:
                    continue
                ph = PriceHistory.objects.create(
                    price_type=pt,
                    price=prices_map[key],
                    notes=notes,
                )
                created.append(ph)

        log_event(
            level="INFO",
            source="system",
            message=f"Category prices updated: {category.name}",
            details=f"Updated {len(created)} price(s). Notes: {notes or 'None'}",
            user=request.user if request.user.is_authenticated else None,
        )

        return Response(
            PriceHistorySerializer(created, many=True).data,
            status=status.HTTP_201_CREATED,
        )


class PriceHistoryAPIView(ListAPIView):
    """Price history for a specific price type."""

    serializer_class = PriceHistorySerializer
    pagination_class = None

    def get_queryset(self):
        return PriceHistory.objects.filter(
            price_type_id=self.kwargs["price_type_id"]
        ).order_by("-created_at")
