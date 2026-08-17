from django.conf import settings
from django.contrib.auth import login, logout
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from core.exceptions import error_response
from .models import CustomUser, UserActivityLog
from .plans import allowed_plans_for, is_impersonating, user_plan
from .tokens import issue_tokens_for_user
from .serializers import (
    LoginSerializer,
    UserSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
    ProgrammerRegisterSerializer,
    ProgrammerUserUpdateSerializer,
    UserActivityLogSerializer,
)
from .utils import get_client_ip, get_user_agent, log_activity
from .permissions import IsSuperAdminOrManagement, IsSuperAdmin, IsProgrammer


def _mask_bot_token(plain: str) -> str:
    if not plain:
        return ""
    if len(plain) <= 8:
        return "••••"
    return f"{plain[:4]}…{plain[-4:]}"


def programmer_user_account_payload(user, request):
    """Detail payload for programmer hub account tabs."""
    from price_publisher.models import PriceTemplate
    from price_publisher.serializers import PriceTemplateSerializer
    from template_editor.models import Template
    from template_editor.serializers import TemplateSerializer

    bots = []
    for bot in user.telegram_bots.prefetch_related("channels").order_by("-created_at"):
        channels = [
            {
                "id": ch.id,
                "name": ch.name,
                "chat_id": ch.chat_id,
                "is_active": ch.is_active,
            }
            for ch in bot.channels.all()
        ]
        bots.append(
            {
                "id": bot.id,
                "name": bot.name,
                "display_name": bot.display_name,
                "is_active": bot.is_active,
                "token_masked": _mask_bot_token(bot.get_plain_token()),
                "restrict_to_known_channels": bot.restrict_to_known_channels,
                "log_all_messages": bot.log_all_messages,
                "default_exchange_ttl_minutes": bot.default_exchange_ttl_minutes,
                "created_at": bot.created_at,
                "updated_at": bot.updated_at,
                "channels": channels,
            }
        )

    audit_logs = UserActivityLogSerializer(
        UserActivityLog.objects.filter(user=user).order_by("-created_at")[:100],
        many=True,
    ).data

    plan_keys = allowed_plans_for(user_plan(user))
    price = PriceTemplate.objects.filter(plan__in=plan_keys).order_by("name")
    editor = (
        Template.objects.filter(plan__in=plan_keys)
        .select_related("category")
        .order_by("name")
    )

    return {
        "user": UserSerializer(user).data,
        "bots": bots,
        "audit_logs": audit_logs,
        "templates": {
            "price_templates": PriceTemplateSerializer(
                price, many=True, context={"request": request}
            ).data,
            "editor_templates": TemplateSerializer(
                editor, many=True, context={"request": request}
            ).data,
        },
        "telegram_analytics": _telegram_analytics_for_user(user),
    }


def _telegram_analytics_for_user(user):
    """Condensed dashboard metrics for each owned bot (programmer profile tab)."""
    from telegram_app.models import TelegramBot
    from telegram_app.services.analytics_service import build_profile_analytics_summary

    result = []
    for bot in TelegramBot.objects.filter(owner=user).order_by("-created_at"):
        result.append(
            {
                "bot_id": bot.id,
                "bot_name": bot.display_name or bot.name,
                "is_active": bot.is_active,
                "analytics": build_profile_analytics_summary(bot),
            }
        )
    return result


class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        username = request.data.get('username', '')
        try:
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
        except Exception as e:
            # Never log raw exception message (may contain credentials). Log only attempted username.
            log_activity(
                None,
                UserActivityLog.ACTION_LOGIN_FAILED,
                request,
                details=username.strip()[:100] if username else "login_failed",
            )
            raise

        login(request, user)

        refresh = issue_tokens_for_user(user)

        log_activity(user, UserActivityLog.ACTION_LOGIN_SUCCESS, request)

        return Response({
            'user': UserSerializer(user).data,
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        })


class DemoLoginAPIView(APIView):
    """POST: instant demo access — logs in the configured demo account (no password).

    Backs the "demo" autologin buttons on the marketing page. The demo account is
    role=management (created via ``manage.py ensure_demo_user``), so it can explore the
    panel but cannot manage users or site settings.
    """

    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        if not settings.DEMO_LOGIN_ENABLED:
            return error_response(
                "Demo login is disabled.",
                code="demo_login_disabled",
                status_code=status.HTTP_403_FORBIDDEN,
            )

        username = settings.DEMO_USERNAME
        try:
            user = CustomUser.objects.get(username=username, is_active=True)
        except CustomUser.DoesNotExist:
            log_activity(
                None,
                UserActivityLog.ACTION_LOGIN_FAILED,
                request,
                details="demo_login_no_demo_user",
            )
            return error_response(
                "Demo user not configured. Run `python manage.py ensure_demo_user`.",
                code="demo_user_not_found",
                status_code=status.HTTP_404_NOT_FOUND,
            )

        login(request, user)

        refresh = issue_tokens_for_user(user)

        log_activity(user, UserActivityLog.ACTION_LOGIN_SUCCESS, request, details="demo_login")

        return Response({
            'user': UserSerializer(user).data,
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        })


class LogoutAPIView(APIView):
    def post(self, request):
        user = getattr(request, 'user', None)
        if user and user.is_authenticated:
            log_activity(user, UserActivityLog.ACTION_LOGOUT, request)

        refresh_token = request.data.get('refresh')
        if refresh_token:
            try:
                RefreshToken(refresh_token).blacklist()
            except (TokenError, Exception):
                pass
        logout(request)
        return Response({'detail': 'Logged out.'}, status=status.HTTP_200_OK)


class MeAPIView(APIView):
    """Return current user JSON, or JSON null when anonymous (no 403 noise on login page)."""

    permission_classes = [AllowAny]

    def get(self, request):
        if not request.user.is_authenticated:
            # JSON ``null`` (DRF Response(None) renders an empty body and breaks clients expecting JSON).
            return JsonResponse(None, safe=False)
        payload = UserSerializer(request.user).data
        token = getattr(request, "auth", None)
        if token is not None:
            impersonator_id = token.get("impersonator_id")
            if impersonator_id:
                payload["impersonated_by"] = {
                    "id": impersonator_id,
                    "username": token.get("impersonator_username"),
                }
        return Response(payload)


class UserListCreateAPIView(ListCreateAPIView):
    """GET: list users (programmers). POST: create user (super admin)."""

    pagination_class = None
    queryset = CustomUser.objects.all().order_by('-date_joined')

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAuthenticated(), IsProgrammer()]
        return [IsAuthenticated(), IsSuperAdmin()]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserSerializer


class ProgrammerRegisterAPIView(APIView):
    permission_classes = [IsAuthenticated, IsProgrammer]

    def post(self, request):
        serializer = ProgrammerRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        payload = UserSerializer(user).data
        payload["generated_password"] = user._generated_password
        return Response(payload, status=status.HTTP_201_CREATED)


class ProgrammerUserDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, IsProgrammer]

    def get(self, request, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return error_response(
                "User not found.",
                code="user_not_found",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        return Response(programmer_user_account_payload(user, request))

    def patch(self, request, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return error_response(
                "User not found.",
                code="user_not_found",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        serializer = ProgrammerUserUpdateSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(UserSerializer(user).data)


class ProgrammerTemplateLibraryAPIView(APIView):
    permission_classes = [IsAuthenticated, IsProgrammer]

    def get(self, request):
        from price_publisher.models import PriceTemplate
        from price_publisher.serializers import PriceTemplateSerializer
        from template_editor.models import Template
        from template_editor.serializers import TemplateSerializer

        price = PriceTemplate.objects.order_by("name")
        editor = Template.objects.select_related("category").order_by("name")
        return Response({
            "price_templates": PriceTemplateSerializer(
                price, many=True, context={"request": request}
            ).data,
            "editor_templates": TemplateSerializer(
                editor, many=True, context={"request": request}
            ).data,
        })

    def patch(self, request):
        from accounts.plans import PLAN_RANK, normalize_plan
        from price_publisher.models import PriceTemplate
        from template_editor.models import Template

        kind = str(request.data.get("kind") or "").strip()
        pk = request.data.get("id")
        plan = normalize_plan(request.data.get("plan"))
        if kind not in ("price", "editor"):
            return error_response(
                "kind must be price or editor.",
                code="invalid_template_kind",
            )
        if plan not in PLAN_RANK:
            return error_response("Invalid plan.", code="invalid_plan")
        try:
            pk = int(pk)
        except (TypeError, ValueError):
            return error_response("Invalid template id.", code="invalid_template_id")
        if kind == "price":
            try:
                obj = PriceTemplate.objects.get(pk=pk)
            except PriceTemplate.DoesNotExist:
                return error_response(
                    "Template not found.",
                    code="template_not_found",
                    status_code=status.HTTP_404_NOT_FOUND,
                )
        else:
            try:
                obj = Template.objects.get(pk=pk)
            except Template.DoesNotExist:
                return error_response(
                    "Template not found.",
                    code="template_not_found",
                    status_code=status.HTTP_404_NOT_FOUND,
                )
        obj.plan = plan
        obj.save(update_fields=["plan"])
        return Response({"id": obj.id, "kind": kind, "plan": obj.plan})


class ImpersonateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsProgrammer]

    def post(self, request, pk):
        if is_impersonating(request):
            return error_response(
                "Already impersonating. Exit first.",
                code="already_impersonating",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        try:
            target = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return error_response(
                "User not found.",
                code="user_not_found",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        if target.pk == request.user.pk:
            return error_response(
                "Cannot impersonate yourself.",
                code="cannot_impersonate_self",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        if not target.is_active:
            return error_response(
                "User is inactive.",
                code="user_inactive",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        refresh = issue_tokens_for_user(target, impersonator=request.user)
        log_activity(
            request.user,
            UserActivityLog.ACTION_IMPERSONATE_START,
            request,
            details=f"target_id={target.pk} username={target.username}",
        )
        return Response({
            "user": UserSerializer(target).data,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        })


class UserDetailAPIView(RetrieveUpdateAPIView):
    """GET/PATCH/PUT: retrieve or update user. Super Admin only."""
    permission_classes = [IsAuthenticated, IsSuperAdmin]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.method in ('PUT', 'PATCH'):
            return UserUpdateSerializer
        return UserSerializer


class ForceLogoutAPIView(APIView):
    """POST: invalidate all tokens for a user. Super Admin only."""
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def post(self, request, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return error_response(
                "User not found.",
                code="user_not_found",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        user.token_version += 1
        user.save(update_fields=['token_version'])
        return Response({'detail': 'All sessions invalidated for this user.'}, status=status.HTTP_200_OK)


class ActivityLogListAPIView(ListAPIView):
    """GET: list user activity logs with filters. Super Admin only."""
    permission_classes = [IsAuthenticated, IsSuperAdmin]
    serializer_class = UserActivityLogSerializer
    queryset = UserActivityLog.objects.select_related('user').all()

    def get_queryset(self):
        qs = super().get_queryset()
        user_id = self.request.query_params.get('user')
        if user_id:
            qs = qs.filter(user_id=user_id)
        action_type = self.request.query_params.get('action_type')
        if action_type:
            qs = qs.filter(action_type=action_type)
        date_from = self.request.query_params.get('date_from')
        if date_from:
            qs = qs.filter(created_at__date__gte=date_from)
        date_to = self.request.query_params.get('date_to')
        if date_to:
            qs = qs.filter(created_at__date__lte=date_to)
        return qs
