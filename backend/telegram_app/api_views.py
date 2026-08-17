"""
DRF API views for Telegram app: channels, send message, default settings, bots,
and auto-post configuration.
"""
import json
from django.db.models import Count
from rest_framework import status, serializers as drf_serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from accounts.permissions import (
    IsSuperAdminOrManagement,
    IsSuperAdminOrManagementOrEmployee,
)
from rest_framework.exceptions import MethodNotAllowed, NotFound, PermissionDenied, ValidationError
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import action

from .admin_api import (
    ChannelMemberSnapshotsAPIView,
    DashboardAPIView,
    ReengageAPIView,
    ReengageCampaignDetailAPIView,
    ReengageCampaignListCreateAPIView,
    ReengageOfferDetailAPIView,
    ReengageOfferListCreateAPIView,
    VerifyBotAPIView,
)
from .models import (
    AutoPostConfig,
    BotSession,
    CustomerProfile,
    DefaultMessageSettings,
    ExchangeRequest,
    PriceAlert,
    TelegramBot,
    TelegramChannel,
)
from .ownership import (
    bots_queryset_for_user,
    resolve_bot_for_user,
    user_is_management,
    user_is_super_admin,
)
from .services.customer_tags import AdminTagImmutable, set_customer_tag
from .services.exchange_ops import hold_request, set_request_status
from .services.telegram_client import TelegramService
from setting.utils import (
    log_telegram_event,
    read_auto_post_on_update_safe,
    write_auto_post_on_update_safe,
)
from core.exceptions import error_response
from .serializers import (
    AutoPostConfigSerializer,
    CustomerProfileSerializer,
    CustomerTagUpdateSerializer,
    DefaultMessageSettingsSerializer,
    ExchangeRequestSerializer,
    PriceAlertSerializer,
    SendMessageSerializer,
    TelegramBotDetailSerializer,
    TelegramBotSerializer,
    TelegramChannelSerializer,
)


class TelegramChannelListAPIView(APIView):
    """GET /api/telegram/channels/ - list active channels with their bots."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagementOrEmployee]

    def get(self, request):
        channels = (
            TelegramChannel.objects.filter(
                is_active=True,
                bot__is_active=True,
                bot_id__in=bots_queryset_for_user(request.user).values("id"),
            )
            .select_related("bot")
            .order_by("-created_at")
        )
        serializer = TelegramChannelSerializer(channels, many=True)
        return Response(serializer.data)


class SendMessageAPIView(APIView):
    """POST /api/telegram/send-message/ - send a message to a channel."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagementOrEmployee]

    def _build_message_from_payload(self, data):
        """Build message text from banner_key and price fields when provided."""
        banner_key = (data.get("banner_key") or "").strip()
        if not banner_key or banner_key == "none":
            return (data.get("message") or "").strip()

        parts = []
        if banner_key == "buy_gbp_double" or banner_key == "sell_gbp_double":
            cash = data.get("cash_price")
            account = data.get("account_price")
            if cash is not None:
                parts.append(f"Cash: {cash}")
            if account is not None:
                parts.append(f"Account: {account}")
            label = "Buy GBP" if banner_key == "buy_gbp_double" else "Sell GBP"
            if parts:
                parts.insert(0, label)
        else:
            single = data.get("price")
            if single is not None:
                parts.append(f"Price: {single}")
            if banner_key == "generic_single" and parts:
                parts.insert(0, "Price update")

        custom = (data.get("message") or "").strip()
        if custom:
            parts.append(custom)
        return "\n".join(parts) if parts else custom

    def post(self, request):
        serializer = SendMessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        bot = data["bot"]
        channel = data["channel"]
        message = self._build_message_from_payload(data)
        if not message:
            message = (request.data.get("message") or "").strip() or "—"

        if channel.bot_id != bot.id:
            return error_response(
                "Channel does not belong to the selected bot.",
                code="telegram_channel_bot_mismatch",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        try:
            client = TelegramService(bot.get_plain_token())
            success, response, _ = client.send_message(channel.chat_id, message)

            if success:
                log_telegram_event(
                    level="INFO",
                    message="Message sent via API",
                    details={
                        "event": "api_send_message",
                        "bot_id": bot.id,
                        "bot_name": bot.name,
                        "channel_id": channel.id,
                        "channel_name": channel.name,
                        "chat_id": str(channel.chat_id),
                        "message_length": len(message),
                    },
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
                details={
                    "event": "api_send_message_error",
                    "bot_id": bot.id,
                    "channel_id": channel.id,
                    "error": str(e),
                },
                user=request.user,
            )
            return error_response(
                "Could not send Telegram message.",
                code="telegram_send_failed",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                extra={"success": False, "detail": str(e)},
            )


class DefaultMessageSettingsListAPIView(APIView):
    """GET /api/telegram/default-settings/ - list default settings (optionally by bot)."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagementOrEmployee]

    def get(self, request):
        bot_id = request.query_params.get("bot")
        qs = DefaultMessageSettings.objects.select_related("bot").filter(
            bot_id__in=bots_queryset_for_user(request.user).values("id")
        ).order_by("-updated_at")
        if bot_id:
            qs = qs.filter(bot_id=bot_id)
        serializer = DefaultMessageSettingsSerializer(qs, many=True)
        return Response(serializer.data)


class DefaultMessageSettingsDetailAPIView(APIView):
    """GET/PUT /api/telegram/default-settings/<id>/ - get or update a default setting."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagementOrEmployee]

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
                    return error_response(
                        "Invalid JSON.",
                        code="invalid_json",
                        status_code=status.HTTP_400_BAD_REQUEST,
                        errors={"default_buttons": "Invalid JSON."},
                    )
            serializer.validated_data["default_buttons"] = default_buttons

        serializer.save()
        return Response(serializer.data)


class DefaultMessageSettingsCreateAPIView(APIView):
    """POST /api/telegram/default-settings/ - create default settings for a bot."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagementOrEmployee]

    def post(self, request):
        data = dict(request.data)
        default_buttons = data.get("default_buttons")
        if default_buttons is not None and isinstance(default_buttons, str):
            try:
                data["default_buttons"] = json.loads(default_buttons)
            except json.JSONDecodeError:
                return error_response(
                    "Invalid JSON.",
                    code="invalid_json",
                    status_code=status.HTTP_400_BAD_REQUEST,
                    errors={"default_buttons": "Invalid JSON."},
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
    permission_classes = [IsAuthenticated, IsSuperAdminOrManagementOrEmployee]

    def get_queryset(self):
        return bots_queryset_for_user(self.request.user).order_by("-created_at")

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return TelegramBotDetailSerializer
        return TelegramBotSerializer

    def perform_create(self, serializer):
        owner = self.request.user if user_is_management(self.request.user) else None
        if user_is_super_admin(self.request.user):
            owner = self.request.user
        serializer.save(owner=owner)
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
                return error_response(
                    "No active channel found for this bot to test against.",
                    code="telegram_no_active_channel",
                    status_code=status.HTTP_400_BAD_REQUEST,
                    extra={"success": False},
                )
            chat_id = channel.chat_id

        try:
            client = TelegramService(bot.get_plain_token())
            success, response, _ = client.send_message(
                chat_id, "✅ Test message from Telegram Management Hub"
            )
            log_telegram_event(
                level="INFO",
                message="Bot test-connection executed",
                details={
                    "event": "bot_test_connection",
                    "bot_id": bot.id,
                    "bot_name": bot.name,
                    "chat_id": str(chat_id),
                    "success": success,
                },
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
                details={
                    "event": "bot_test_connection_error",
                    "bot_id": bot.id,
                    "error": str(exc),
                },
                user=request.user,
            )
            return error_response(
                "Bot connection test failed.",
                code="telegram_test_connection_failed",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                extra={"success": False, "detail": str(exc)},
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
    permission_classes = [IsAuthenticated, IsSuperAdminOrManagementOrEmployee]

    def get_queryset(self):
        return (
            TelegramChannel.objects.filter(
                bot_id__in=bots_queryset_for_user(self.request.user).values("id")
            )
            .select_related("bot")
            .order_by("-created_at")
        )


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
    permission_classes = [IsAuthenticated, IsSuperAdminOrManagementOrEmployee]

    def get_queryset(self):
        return (
            AutoPostConfig.objects.filter(
                channel__bot_id__in=bots_queryset_for_user(self.request.user).values(
                    "id"
                )
            )
            .select_related("channel", "category", "special_price_type")
            .all()
        )

class AutomationSettingsSerializer(drf_serializers.Serializer):
    auto_post_on_update = drf_serializers.BooleanField(required=False, default=False)


class AutomationSettingsAPIView(APIView):
    """
    GET/PUT /api/telegram/automation-settings/

    Exposes a simple boolean flag stored on SiteSettings so the frontend can
    control whether auto-post-on-update behaviour is enabled. Actual scheduling
    is handled elsewhere.
    """

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagementOrEmployee]

    def get(self, request):
        payload = read_auto_post_on_update_safe()
        body = {"auto_post_on_update": payload["value"]}
        if not payload["ok"]:
            body["degraded"] = True
            body["detail"] = payload["detail"]
        return Response(body)

    def put(self, request):
        serializer = AutomationSettingsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        flag = serializer.validated_data["auto_post_on_update"]
        result = write_auto_post_on_update_safe(flag)
        if not result["ok"]:
            return Response(
                {"detail": result["detail"]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response({"auto_post_on_update": bool(flag)})


class TelegramCustomerWebhookAPIView(APIView):
    """
    POST /api/telegram/webhook/<bot_id>/

    Telegram customer-bot ingress. Always returns 200 after accepting the body
    so Telegram does not retry aggressively on application errors.
    """

    authentication_classes = []
    permission_classes = [AllowAny]
    throttle_classes = []

    def post(self, request, bot_id: int):
        from .services.dispatcher import process_update_payload

        try:
            bot = TelegramBot.objects.get(pk=bot_id, is_active=True)
        except TelegramBot.DoesNotExist:
            return Response({"ok": False, "detail": "bot not found"}, status=status.HTTP_404_NOT_FOUND)

        payload = request.data
        if not isinstance(payload, dict):
            return Response({"ok": False, "detail": "invalid json"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            process_update_payload(bot, payload)
        except Exception:
            # Still 200 — Telegram retries on non-2xx and can amplify outages.
            try:
                log_telegram_event(
                    level="ERROR",
                    message="Customer webhook handler failed",
                    details={"event": "customer_webhook_error", "bot_id": bot_id},
                )
            except Exception:
                pass
        return Response({"ok": True})


class CustomerProfileViewSet(ModelViewSet):
    """
    Staff: list/retrieve customers; PATCH tag (management / super_admin only).
    """

    queryset = CustomerProfile.objects.all().order_by("-updated_at")
    serializer_class = CustomerProfileSerializer
    http_method_names = ["get", "patch", "head", "options"]

    def get_permissions(self):
        return [IsAuthenticated(), IsSuperAdminOrManagement()]

    def get_queryset(self):
        qs = CustomerProfile.objects.annotate(
            request_count=Count("exchange_requests")
        )
        bot_id = self.request.query_params.get("bot_id")
        if bot_id is not None and str(bot_id).strip() != "":
            bot, code, message = resolve_bot_for_user(
                self.request.user, bot_id=bot_id
            )
            if bot is None:
                if code in ("bot_not_found", "no_bot"):
                    raise NotFound(detail=message)
                if code == "bot_forbidden":
                    raise PermissionDenied(detail=message)
                raise ValidationError({"bot_id": message})
            user_ids = BotSession.objects.filter(bot=bot).values("telegram_user_id")
            qs = qs.filter(telegram_user_id__in=user_ids)
        elif not user_is_super_admin(self.request.user):
            bot_ids = bots_queryset_for_user(self.request.user).values("id")
            user_ids = BotSession.objects.filter(bot_id__in=bot_ids).values_list(
                "telegram_user_id", flat=True
            )
            qs = qs.filter(telegram_user_id__in=user_ids)
        return qs.order_by("-request_count", "telegram_user_id")

    def get_serializer_class(self):
        if self.action in ("partial_update", "update"):
            return CustomerTagUpdateSerializer
        return CustomerProfileSerializer

    def partial_update(self, request, *args, **kwargs):
        customer = self.get_object()
        serializer = CustomerTagUpdateSerializer(
            customer, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        try:
            set_customer_tag(customer, serializer.validated_data["tag"])
        except AdminTagImmutable as exc:
            raise ValidationError({"tag": str(exc)}) from exc
        customer.refresh_from_db()
        return Response(CustomerProfileSerializer(customer).data)


class ExchangeRequestViewSet(ModelViewSet):
    queryset = ExchangeRequest.objects.select_related("customer", "bot").order_by(
        "-created_at"
    )
    serializer_class = ExchangeRequestSerializer
    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]
    http_method_names = ["get", "patch", "post", "head", "options"]

    def get_queryset(self):
        qs = ExchangeRequest.objects.select_related("customer", "bot").order_by(
            "-created_at"
        )
        bot_id = self.request.query_params.get("bot_id")
        if bot_id is not None and str(bot_id).strip() != "":
            bot, code, message = resolve_bot_for_user(
                self.request.user, bot_id=bot_id
            )
            if bot is None:
                if code in ("bot_not_found", "no_bot"):
                    raise NotFound(detail=message)
                if code == "bot_forbidden":
                    raise PermissionDenied(detail=message)
                raise ValidationError({"bot_id": message})
            return qs.filter(bot=bot)
        if user_is_super_admin(self.request.user):
            return qs
        return qs.filter(bot_id__in=bots_queryset_for_user(self.request.user).values("id"))

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed("POST")

    def partial_update(self, request, *args, **kwargs):
        req = self.get_object()
        status_value = request.data.get("status")
        if not status_value:
            raise ValidationError({"status": "This field is required."})
        try:
            set_request_status(req, status_value)
        except ValueError as exc:
            raise ValidationError({"status": str(exc)}) from exc
        req.refresh_from_db()
        return Response(ExchangeRequestSerializer(req).data)

    @action(detail=True, methods=["post"])
    def hold(self, request, pk=None):
        req = self.get_object()
        ttl = hold_request(req)
        req.refresh_from_db()
        payload = ExchangeRequestSerializer(req).data
        payload["ttl_minutes"] = ttl
        return Response(payload)


class PriceAlertViewSet(ReadOnlyModelViewSet):
    queryset = PriceAlert.objects.select_related("customer").order_by("-created_at")
    serializer_class = PriceAlertSerializer
    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]

    def get_queryset(self):
        qs = PriceAlert.objects.select_related("customer").order_by("-created_at")
        if user_is_super_admin(self.request.user):
            return qs
        bot_ids = bots_queryset_for_user(self.request.user).values("id")
        user_ids = BotSession.objects.filter(bot_id__in=bot_ids).values_list(
            "telegram_user_id", flat=True
        )
        return qs.filter(customer__telegram_user_id__in=user_ids)
