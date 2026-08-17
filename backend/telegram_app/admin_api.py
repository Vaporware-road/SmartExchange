"""
Telegram hub admin APIs: verify-bot, dashboard aggregates, re-engage send,
campaign/offer CRUD, channel member snapshots.
"""

from __future__ import annotations

from django.utils import timezone
from rest_framework import serializers as drf_serializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsSuperAdminOrManagement
from core.exceptions import error_response

from .models import (
    ChannelMemberSnapshot,
    ReengageCampaign,
    ReengageOffer,
    TelegramChannel,
)
from .ownership import resolve_bot_for_user
from .serializers import (
    ExchangeRequestSerializer,
    PriceAlertSerializer,
    TelegramChannelSerializer,
)
from .services.analytics_service import build_dashboard_payload, new_members_dual
from .services.reengage_service import (
    REENGAGE_BATCH_CAP,
    schedule_next_run,
    send_offer,
    send_to_audience,
)
from .services.telegram_client import TelegramService


def _bot_summary(bot, telegram_me=None):
    payload = {
        "id": bot.id,
        "name": bot.name,
        "display_name": bot.display_name or "",
        "username": (telegram_me or {}).get("username") or "",
        "telegram_id": (telegram_me or {}).get("id"),
        "is_active": bot.is_active,
        "default_exchange_ttl_minutes": bot.default_exchange_ttl_minutes,
        "restrict_to_known_channels": bot.restrict_to_known_channels,
        "log_all_messages": bot.log_all_messages,
    }
    return payload


class VerifyBotAPIView(APIView):
    """POST /api/telegram/admin/verify-bot/ — getMe gate for hub unlock."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]

    def post(self, request):
        bot_id = request.data.get("bot_id")
        bot, code, message = resolve_bot_for_user(request.user, bot_id=bot_id)
        if bot is None:
            status_code = (
                status.HTTP_404_NOT_FOUND
                if code in ("bot_not_found", "no_bot")
                else status.HTTP_403_FORBIDDEN
                if code == "bot_forbidden"
                else status.HTTP_400_BAD_REQUEST
            )
            return error_response(
                message,
                code=code or "no_bot",
                status_code=status_code,
                extra={"ok": False},
            )

        token = bot.get_plain_token()
        if not token:
            return error_response(
                "Bot has no token configured.",
                code="no_token",
                status_code=status.HTTP_400_BAD_REQUEST,
                extra={"ok": False},
            )

        try:
            client = TelegramService(token)
            ok, info, err = client.get_me()
        except Exception as exc:
            return error_response(
                "Could not reach Telegram.",
                code="telegram_unreachable",
                status_code=status.HTTP_502_BAD_GATEWAY,
                extra={"ok": False, "detail": str(exc)},
            )

        if not ok:
            return error_response(
                err or "Telegram getMe failed.",
                code="get_me_failed",
                status_code=status.HTTP_400_BAD_REQUEST,
                extra={"ok": False, "detail": err},
            )

        return Response(
            {
                "ok": True,
                "bot": _bot_summary(bot, info),
                "telegram": info,
            }
        )


class DashboardAPIView(APIView):
    """GET /api/telegram/admin/dashboard/?bot_id= — scoped hub aggregates."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]

    def get(self, request):
        bot_id = request.query_params.get("bot_id")
        bot, code, message = resolve_bot_for_user(request.user, bot_id=bot_id)
        if bot is None:
            status_code = (
                status.HTTP_404_NOT_FOUND
                if code in ("bot_not_found", "no_bot")
                else status.HTTP_403_FORBIDDEN
                if code == "bot_forbidden"
                else status.HTTP_400_BAD_REQUEST
            )
            return error_response(
                message,
                code=code or "no_bot",
                status_code=status_code,
            )

        payload = build_dashboard_payload(
            bot,
            exchange_serializer=ExchangeRequestSerializer,
            alert_serializer=PriceAlertSerializer,
            channel_serializer=TelegramChannelSerializer,
            bot_summary=_bot_summary(bot),
        )
        return Response(payload)


class ChannelMemberSnapshotsAPIView(APIView):
    """GET /api/telegram/admin/snapshots/channel-members/?bot_id=&months="""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]

    def get(self, request):
        bot_id = request.query_params.get("bot_id")
        bot, code, message = resolve_bot_for_user(request.user, bot_id=bot_id)
        if bot is None:
            return error_response(
                message,
                code=code or "no_bot",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        try:
            months = int(request.query_params.get("months", "1"))
        except ValueError:
            months = 1
        dual = new_members_dual(bot, months)
        channels = TelegramChannel.objects.filter(bot=bot, is_active=True)
        history = []
        for ch in channels:
            snaps = ChannelMemberSnapshot.objects.filter(
                channel=ch, bot_is_admin=True
            ).order_by("-sampled_at")[:30]
            history.append(
                {
                    "channel_id": ch.id,
                    "name": ch.name,
                    "snapshots": [
                        {
                            "member_count": s.member_count,
                            "sampled_at": s.sampled_at.isoformat(),
                        }
                        for s in snaps
                    ],
                }
            )
        return Response({"growth": dual, "history": history})


class ReengageSerializer(drf_serializers.Serializer):
    bot_id = drf_serializers.IntegerField(required=False, allow_null=True)
    audience = drf_serializers.ChoiceField(
        choices=("global", "vip", "special", "inactive")
    )
    message = drf_serializers.CharField(max_length=4096, trim_whitespace=True)


class ReengageAPIView(APIView):
    """POST /api/telegram/admin/reengage/ — one-shot audience DM send."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]

    def post(self, request):
        serializer = ReengageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        bot, code, message = resolve_bot_for_user(
            request.user, bot_id=data.get("bot_id")
        )
        if bot is None:
            status_code = (
                status.HTTP_404_NOT_FOUND
                if code in ("bot_not_found", "no_bot")
                else status.HTTP_403_FORBIDDEN
                if code == "bot_forbidden"
                else status.HTTP_400_BAD_REQUEST
            )
            return error_response(
                message,
                code=code or "no_bot",
                status_code=status_code,
            )

        result = send_to_audience(bot, data["audience"], data["message"])
        if result.get("error"):
            return error_response(
                result["error"],
                code=result.get("error", "send_failed"),
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        result["batch_cap"] = REENGAGE_BATCH_CAP
        return Response(result)


class ReengageCampaignSerializer(drf_serializers.ModelSerializer):
    bot_id = drf_serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = ReengageCampaign
        fields = (
            "id",
            "bot",
            "bot_id",
            "audience",
            "message",
            "schedule",
            "is_active",
            "next_run_at",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "bot", "created_at", "updated_at", "next_run_at")


class ReengageCampaignListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]

    def get(self, request):
        bot_id = request.query_params.get("bot_id")
        bot, code, message = resolve_bot_for_user(request.user, bot_id=bot_id)
        if bot is None:
            return error_response(message, code=code or "no_bot", status_code=404)
        qs = ReengageCampaign.objects.filter(bot=bot).order_by("-created_at")
        return Response(ReengageCampaignSerializer(qs, many=True).data)

    def post(self, request):
        bot_id = request.data.get("bot_id")
        bot, code, message = resolve_bot_for_user(request.user, bot_id=bot_id)
        if bot is None:
            return error_response(message, code=code or "no_bot", status_code=404)
        serializer = ReengageCampaignSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data.pop("bot_id", None)
        campaign = serializer.save(
            bot=bot,
            created_by=request.user,
            next_run_at=timezone.now(),
        )
        schedule_next_run(campaign)
        return Response(
            ReengageCampaignSerializer(campaign).data,
            status=status.HTTP_201_CREATED,
        )


class ReengageCampaignDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]

    def _get_campaign(self, request, pk):
        try:
            campaign = ReengageCampaign.objects.select_related("bot").get(pk=pk)
        except ReengageCampaign.DoesNotExist:
            return None, error_response("Not found.", code="not_found", status_code=404)
        bot, code, message = resolve_bot_for_user(request.user, bot_id=campaign.bot_id)
        if bot is None:
            return None, error_response(message, code=code or "forbidden", status_code=403)
        return campaign, None

    def patch(self, request, pk):
        campaign, err = self._get_campaign(request, pk)
        if err:
            return err
        serializer = ReengageCampaignSerializer(
            campaign, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        campaign, err = self._get_campaign(request, pk)
        if err:
            return err
        campaign.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReengageOfferSerializer(drf_serializers.ModelSerializer):
    bot_id = drf_serializers.IntegerField(write_only=True, required=False)
    send_now = drf_serializers.BooleanField(write_only=True, required=False, default=False)

    class Meta:
        model = ReengageOffer
        fields = (
            "id",
            "bot",
            "bot_id",
            "title",
            "body",
            "audience",
            "valid_until",
            "is_active",
            "send_now",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "bot", "created_at", "updated_at")


class ReengageOfferListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]

    def get(self, request):
        bot_id = request.query_params.get("bot_id")
        bot, code, message = resolve_bot_for_user(request.user, bot_id=bot_id)
        if bot is None:
            return error_response(message, code=code or "no_bot", status_code=404)
        qs = ReengageOffer.objects.filter(bot=bot).order_by("-created_at")
        return Response(ReengageOfferSerializer(qs, many=True).data)

    def post(self, request):
        bot_id = request.data.get("bot_id")
        bot, code, message = resolve_bot_for_user(request.user, bot_id=bot_id)
        if bot is None:
            return error_response(message, code=code or "no_bot", status_code=404)
        serializer = ReengageOfferSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        send_now = serializer.validated_data.pop("send_now", False)
        serializer.validated_data.pop("bot_id", None)
        offer = serializer.save(bot=bot, created_by=request.user)
        result = None
        if send_now:
            result = send_offer(offer)
        data = ReengageOfferSerializer(offer).data
        if result:
            data["send_result"] = result
        return Response(data, status=status.HTTP_201_CREATED)


class ReengageOfferDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]

    def _get_offer(self, request, pk):
        try:
            offer = ReengageOffer.objects.select_related("bot").get(pk=pk)
        except ReengageOffer.DoesNotExist:
            return None, error_response("Not found.", code="not_found", status_code=404)
        bot, code, message = resolve_bot_for_user(request.user, bot_id=offer.bot_id)
        if bot is None:
            return None, error_response(message, code=code or "forbidden", status_code=403)
        return offer, None

    def patch(self, request, pk):
        offer, err = self._get_offer(request, pk)
        if err:
            return err
        serializer = ReengageOfferSerializer(offer, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        offer, err = self._get_offer(request, pk)
        if err:
            return err
        offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, pk):
        """POST to send an existing offer now."""
        offer, err = self._get_offer(request, pk)
        if err:
            return err
        result = send_offer(offer)
        return Response({"offer": ReengageOfferSerializer(offer).data, "send_result": result})
