from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models import Prefetch, Max
from django.conf import settings
from django.core.files.storage import default_storage
from django.utils.text import get_valid_filename
import os
import uuid

from core.utils import validate_uploaded_image, MAX_IMAGE_SIZE
from .models import Category, Currency, PriceType
from .serializers import (
    CategorySerializer,
    CategoryListSerializer,
    CategoryExplorerSerializer,
    PriceTypeSerializer,
)


class CurrencyListAPIView(APIView):
    """GET /api/categories/currencies/ - list all currencies for forms."""

    def get(self, request):
        currencies = Currency.objects.all().order_by("code")
        data = [{"id": c.id, "code": c.code, "name": c.name, "symbol": c.symbol or ""} for c in currencies]
        return Response(data)


class CategoryViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        qs = Category.objects.all()
        if self.action == "list":
            qs = qs.prefetch_related(
                Prefetch(
                    "price_types",
                    queryset=PriceType.objects.order_by("order", "id"),
                ),
                "price_types__price_histories",
            )
        return qs

    def get_serializer_class(self):
        if self.action == "list":
            return CategoryExplorerSerializer
        return CategorySerializer

    @action(detail=True, methods=["post"], url_path="price-types/reorder")
    def reorder_price_types(self, request, pk=None):
        """POST /api/categories/<id>/price-types/reorder/ with body: { "order": [id1, id2, ...] }"""
        category = self.get_object()
        order_ids = request.data.get("order") or []
        if not isinstance(order_ids, list):
            return Response(
                {"detail": "Invalid payload. Expected { \"order\": [id, ...] }."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # Validate all ids belong to this category
        qs = PriceType.objects.filter(category=category)
        ids_in_category = set(qs.values_list("id", flat=True))
        for i, pt_id in enumerate(order_ids):
            if pt_id not in ids_in_category:
                continue
            qs.filter(pk=pt_id).update(order=i)
        return Response({"status": "ok"})

    @action(detail=True, methods=["post"], url_path="telegram-media", parser_classes=[MultiPartParser, FormParser])
    def upload_telegram_media(self, request, pk=None):
        """POST /api/categories/<id>/telegram-media/ with multipart file. Returns { "url": "/media/..." }."""
        category = self.get_object()
        file_obj = request.FILES.get("file") or request.FILES.get("image")
        if not file_obj:
            return Response(
                {"detail": "No file provided. Use 'file' or 'image' form field."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            validate_uploaded_image(file_obj, max_size=MAX_IMAGE_SIZE)
        except ValueError as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # Restrict to images (extension kept for storage naming only; content already validated)
        name = get_valid_filename(file_obj.name) or "image"
        ext = os.path.splitext(name)[1].lower()
        if ext not in (".jpg", ".jpeg", ".png", ".gif", ".webp"):
            return Response(
                {"detail": "Only image files (jpg, png, gif, webp) are allowed."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        rel_path = f"telegram_category/{category.pk}/{uuid.uuid4().hex}{ext}"
        path = default_storage.save(rel_path, file_obj)
        url = f"{settings.MEDIA_URL.rstrip('/')}/{path}"
        category.telegram_media_url = url
        category.save(update_fields=["telegram_media_url", "updated_at"])
        return Response({"url": url})


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
            next_order = (
                PriceType.objects.filter(category_id=category_id).aggregate(Max("order"))["order__max"]
                or -1
            ) + 1
            serializer.save(category_id=category_id, order=next_order)
        else:
            serializer.save()
