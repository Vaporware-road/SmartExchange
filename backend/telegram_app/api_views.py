"""
DRF API views for Telegram app: channels, send message, default settings, bots,
and auto-post configuration.
"""
import json
from rest_framework import status, serializers as drf_serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .models import TelegramBot, TelegramChannel, DefaultMessageSettings, AutoPostConfig
from .services.telegram_client import TelegramService
from setting.models import SiteSettings
from setting.utils import log_telegram_event
from .serializers import (
    TelegramChannelSerializer,
    TelegramBotSerializer,
    TelegramBotDetailSerializer,
    DefaultMessageSettingsSerializer,
    SendMessageSerializer,
    AutoPostConfigSerializer,
)


class TelegramChannelListAPIView(APIView):
    """GET /api/telegram/channels/ - list active channels with their bots."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        channels = (
            TelegramChannel.objects.filter(
                is_active=True,
                bot__is_active=True,
            )
            .select_related("bot")
            .order_by("-created_at")
        )
        serializer = TelegramChannelSerializer(channels, many=True)
        return Response(serializer.data)


class SendMessageAPIView(APIView):
    """POST /api/telegram/send-message/ - send a message to a channel."""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SendMessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        bot = data["bot"]
        channel = data["channel"]
        message = data["message"]

        if channel.bot_id != bot.id:
            return Response(
                {"detail": "Channel does not belong to the selected bot."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            client = TelegramService(bot.token)
            success, response = client.send_message(channel.chat_id, message)

            if success:
                log_telegram_event(
                    level="INFO",
                    message="Message sent via API",
                    details=f"Bot: {bot.name}, Channel: {channel.name}, Length: {len(message)}",
                    user=request.user,
                )
                return Response({"success": True, "detail": response})
            return Response(
                {"success": False, "detail": response},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            log_telegram_event(
                level="ERROR",
                message="Exception sending message via API",
                details=str(e),
                user=request.user,
            )
            return Response(
                {"success": False, "detail": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class DefaultMessageSettingsListAPIView(APIView):
    """GET /api/telegram/default-settings/ - list default settings (optionally by bot)."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        bot_id = request.query_params.get("bot")
        qs = DefaultMessageSettings.objects.select_related("bot").order_by("-updated_at")
        if bot_id:
            qs = qs.filter(bot_id=bot_id)
        serializer = DefaultMessageSettingsSerializer(qs, many=True)
        return Response(serializer.data)


class DefaultMessageSettingsDetailAPIView(APIView):
    """GET/PUT /api/telegram/default-settings/<id>/ - get or update a default setting."""

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        from django.shortcuts import get_object_or_404

        return get_object_or_404(DefaultMessageSettings, pk=pk)

    def get(self, request, pk):
        obj = self.get_object(pk)
        serializer = DefaultMessageSettingsSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = DefaultMessageSettingsSerializer(
            obj, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)

        default_buttons = request.data.get("default_buttons")
        if default_buttons is not None:
            if isinstance(default_buttons, str):
                try:
                    default_buttons = json.loads(default_buttons)
                except json.JSONDecodeError:
                    return Response(
                        {"default_buttons": ["Invalid JSON."]},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            serializer.validated_data["default_buttons"] = default_buttons

        serializer.save()
        return Response(serializer.data)


class DefaultMessageSettingsCreateAPIView(APIView):
    """POST /api/telegram/default-settings/ - create default settings for a bot."""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = dict(request.data)
        default_buttons = data.get("default_buttons")
        if default_buttons is not None and isinstance(default_buttons, str):
            try:
                data["default_buttons"] = json.loads(default_buttons)
            except json.JSONDecodeError:
                return Response(
                    {"default_buttons": ["Invalid JSON."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        serializer = DefaultMessageSettingsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TelegramBotViewSet(ModelViewSet):
    """
    CRUD for Telegram bots.

    List/retrieve operations hide the token; create/update use the detail serializer.
    """

    queryset = TelegramBot.objects.all().order_by("-created_at")
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return TelegramBotDetailSerializer
        return TelegramBotSerializer

    @action(detail=True, methods=["post"], url_path="test-connection")
    def test_connection(self, request, pk=None):
        """
        POST /api/telegram/bots/<id>/test-connection/

        Optionally accepts `chat_id` in the body; if omitted, uses the first
        active channel for this bot.
        """
        bot = self.get_object()
        chat_id = request.data.get("chat_id")

        if not chat_id:
            channel = bot.channels.filter(is_active=True).first()
            if not channel:
                return Response(
                    {
                        "success": False,
                        "detail": "No active channel found for this bot to test against.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            chat_id = channel.chat_id

        try:
            client = TelegramService(bot.token)
            success, response = client.send_message(
                chat_id, "✅ Test message from Telegram Management Hub"
            )
            log_telegram_event(
                level="INFO",
                message="Bot test-connection executed",
                details=f"Bot: {bot.name}, Chat: {chat_id}, Success: {success}",
                user=request.user,
            )
            if success:
                return Response({"success": True, "detail": response})
            return Response(
                {"success": False, "detail": response},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as exc:
            log_telegram_event(
                level="ERROR",
                message="Exception in bot test-connection",
                details=str(exc),
                user=request.user,
            )
            return Response(
                {"success": False, "detail": str(exc)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class TelegramChannelViewSet(ModelViewSet):
    """
    Full CRUD for Telegram channels (management).

    The existing TelegramChannelListAPIView continues to serve the simplified
    `/api/telegram/channels/` endpoint used by the finalize flows.
    """

    queryset = TelegramChannel.objects.select_related("bot").all().order_by(
        "-created_at"
    )
    serializer_class = TelegramChannelSerializer
    permission_classes = [IsAuthenticated]


class AutoPostConfigViewSet(ModelViewSet):
    """
    CRUD for AutoPostConfig.

    This is configuration-only; a separate scheduler can read these records and
    call the existing price publisher services.
    """

    queryset = AutoPostConfig.objects.select_related(
        "channel", "category", "special_price_type"
    ).all()
    serializer_class = AutoPostConfigSerializer
    permission_classes = [IsAuthenticated]


class AutomationSettingsSerializer(drf_serializers.Serializer):
    auto_post_on_update = drf_serializers.BooleanField()


class AutomationSettingsAPIView(APIView):
    """
    GET/PUT /api/telegram/automation-settings/

    Exposes a simple boolean flag stored on SiteSettings so the frontend can
    control whether auto-post-on-update behaviour is enabled. Actual scheduling
    is handled elsewhere.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        settings = SiteSettings.load()
        return Response(
            {
                "auto_post_on_update": getattr(
                    settings, "auto_post_on_update", False
                ),
            }
        )

    def put(self, request):
        serializer = AutomationSettingsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        settings = SiteSettings.load()
        settings.auto_post_on_update = serializer.validated_data[
            "auto_post_on_update"
        ]
        settings.save()
        return Response(
            {
                "auto_post_on_update": settings.auto_post_on_update,
            }
        )
