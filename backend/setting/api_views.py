"""
DRF API views for settings: site settings, bots, channels, logs.
"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import ScopedRateThrottle

from accounts.permissions import IsSuperAdmin, IsSuperAdminOrManagement
from telegram_app.models import TelegramBot, TelegramChannel

from .models import SiteSettings, Log
from .serializers import (
    SiteSettingsSerializer,
    TelegramBotSerializer,
    TelegramChannelSerializer,
    LogSerializer,
)


class SiteSettingsAPIView(APIView):
    """GET/PUT /api/settings/site/ - singleton site settings."""

    permission_classes = [IsAuthenticated, IsSuperAdmin]
    throttle_scope = "settings"
    throttle_classes = [ScopedRateThrottle]

    def get(self, request):
        settings_obj = SiteSettings.load()
        serializer = SiteSettingsSerializer(settings_obj)
        return Response(serializer.data)

    def put(self, request):
        settings_obj = SiteSettings.load()
        serializer = SiteSettingsSerializer(settings_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class TelegramBotViewSet(ModelViewSet):
    """CRUD for Telegram bots."""

    permission_classes = [IsAuthenticated, IsSuperAdmin]
    throttle_scope = "settings"
    throttle_classes = [ScopedRateThrottle]
    queryset = TelegramBot.objects.all().order_by("-created_at")
    serializer_class = TelegramBotSerializer


class TelegramChannelViewSet(ModelViewSet):
    """CRUD for Telegram channels."""

    permission_classes = [IsAuthenticated, IsSuperAdmin]
    throttle_scope = "settings"
    throttle_classes = [ScopedRateThrottle]
    queryset = TelegramChannel.objects.select_related("bot").all().order_by("-created_at")
    serializer_class = TelegramChannelSerializer


class LogListAPIView(APIView):
    """GET /api/settings/logs/ - paginated logs with filters."""

    permission_classes = [IsAuthenticated, IsSuperAdmin]
    throttle_scope = "settings"
    throttle_classes = [ScopedRateThrottle]

    def get(self, request):
        from rest_framework.pagination import PageNumberPagination

        level = request.query_params.get("level", "")
        source = request.query_params.get("source", "")
        search = request.query_params.get("search", "")

        qs = Log.objects.select_related("user").all()

        if level:
            qs = qs.filter(level=level)
        if source:
            qs = qs.filter(source=source)
        if search:
            qs = qs.filter(message__icontains=search)

        paginator = PageNumberPagination()
        paginator.page_size = 50
        page = paginator.paginate_queryset(qs, request)
        if page is not None:
            serializer = LogSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = LogSerializer(qs, many=True)
        return Response(serializer.data)
