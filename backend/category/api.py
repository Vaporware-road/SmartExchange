from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count

from .models import Category, Currency, PriceType
from .serializers import (
    CategorySerializer,
    CategoryListSerializer,
    PriceTypeSerializer,
)


class CurrencyListAPIView(APIView):
    """GET /api/categories/currencies/ - list all currencies for forms."""

    def get(self, request):
        currencies = Currency.objects.all().order_by("code")
        data = [{"id": c.id, "code": c.code, "name": c.name, "symbol": c.symbol or ""} for c in currencies]
        return Response(data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.prefetch_related("price_types").all()

    def get_serializer_class(self):
        if self.action == "list":
            return CategoryListSerializer
        return CategorySerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if self.action == "list":
            qs = qs.annotate(price_type_count=Count("price_types"))
        return qs


class PriceTypeViewSet(viewsets.ModelViewSet):
    serializer_class = PriceTypeSerializer

    def get_queryset(self):
        qs = PriceType.objects.select_related(
            "category", "source_currency", "target_currency"
        )
        category_id = self.kwargs.get("category_pk")
        if category_id:
            qs = qs.filter(category_id=category_id)
        return qs

    def perform_create(self, serializer):
        category_id = self.kwargs.get("category_pk")
        if category_id:
            serializer.save(category_id=category_id)
        else:
            serializer.save()
