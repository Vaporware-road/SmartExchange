from django.conf import settings
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.db.models import Q
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from core.exceptions import error_response
from .models import CustomUser, OtpCode, UserActivityLog
from .plans import allowed_plans_for, is_impersonating, user_plan
from .trial import ensure_trial_started, trial_is_expired
from .google import google_enabled, verify_id_token
from .otp import issue_code, verify_code
from .scoping import unscoped
from .tokens import issue_tokens_for_user
from .emails import mark_email_verified, read_verification_token, send_verification_email
from .serializers import (
    GoogleSignupSerializer,
    LoginSerializer,
    SignupSerializer,
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
    throttle_scope = "login"
    throttle_classes = [ScopedRateThrottle]

    def post(self, request):
        username = request.data.get("identifier") or request.data.get("username") or ""
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

        # An expired trial does not block sign-in any more: the wall is
        # read-only, so the customer gets in, sees their data and reads the
        # upgrade message instead of a locked door.
        ensure_trial_started(user)
        login(request, user)

        refresh = issue_tokens_for_user(user)

        log_activity(user, UserActivityLog.ACTION_LOGIN_SUCCESS, request)

        return Response({
            'user': UserSerializer(user).data,
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        })


class SignupAPIView(APIView):
    """POST: register with an email address and land straight in your own panel.

    Access is granted immediately — the trial clock starts here, not at
    verification — so a wrong SMTP setting can never cost a customer their
    signup. The verification mail is sent best-effort and only clears the
    banner in the panel.
    """

    permission_classes = [AllowAny]
    authentication_classes = []
    throttle_scope = "signup"
    throttle_classes = [ScopedRateThrottle]

    def post(self, request):
        if not settings.SIGNUP_ENABLED:
            return error_response(
                "Self-serve signup is disabled on this install.",
                code="signup_disabled",
                status_code=status.HTTP_403_FORBIDDEN,
            )

        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        send_verification_email(user)
        log_activity(
            user,
            UserActivityLog.ACTION_SIGNUP,
            request,
            details="self_serve_signup",
        )

        refresh = issue_tokens_for_user(user)
        return Response(
            {
                "user": UserSerializer(user).data,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            },
            status=status.HTTP_201_CREATED,
        )


class VerifyEmailAPIView(APIView):
    """POST: confirm an address from the link in the signup email.

    Anonymous on purpose — the signed token is the proof, and the customer may
    open the link in a browser that never held their session.
    """

    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        token = (request.data.get("token") or "").strip()
        user = read_verification_token(token) if token else None
        if user is None:
            return error_response(
                "This confirmation link is invalid or has expired.",
                code="verification_invalid",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        mark_email_verified(user)
        return Response({"verified": True, "email": user.email})


class ResendVerificationAPIView(APIView):
    """POST: send the confirmation link again to the signed-in account."""

    permission_classes = [IsAuthenticated]
    throttle_scope = "signup"
    throttle_classes = [ScopedRateThrottle]

    def post(self, request):
        user = request.user
        if user.email_verified_at is not None:
            return Response({"sent": False, "already_verified": True})
        sent = send_verification_email(user)
        return Response({"sent": bool(sent), "already_verified": False})


class GoogleAuthAPIView(APIView):
    """POST: sign in or sign up with a Google id-token.

    Links to an existing account by *verified* email when there is one, so a
    customer who signed up with a password can later use the Google button
    without ending up with two accounts. Otherwise it opens a new desk with the
    address already proven — Google has verified it, so there is nothing for an
    OTP to add.
    """

    permission_classes = [AllowAny]
    authentication_classes = []
    throttle_scope = "login"
    throttle_classes = [ScopedRateThrottle]

    def post(self, request):
        if not google_enabled():
            return error_response(
                "Google sign-in is not configured on this install.",
                code="google_auth_disabled",
                status_code=status.HTTP_403_FORBIDDEN,
            )

        claims = verify_id_token(request.data.get("credential") or request.data.get("id_token"))
        if claims is None:
            log_activity(None, UserActivityLog.ACTION_LOGIN_FAILED, request, details="google_token_rejected")
            return error_response(
                "That Google sign-in could not be verified.",
                code="google_token_invalid",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        email = claims["email"].strip().lower()
        with unscoped():
            user = (
                CustomUser.objects.filter(google_sub=claims["sub"]).first()
                or CustomUser.objects.filter(email__iexact=email).first()
            )
            created = user is None
            if created:
                if not settings.SIGNUP_ENABLED:
                    return error_response(
                        "Self-serve signup is disabled on this install.",
                        code="signup_disabled",
                        status_code=status.HTTP_403_FORBIDDEN,
                    )
                user = GoogleSignupSerializer().create_from_claims(claims)
            else:
                _link_google_account(user, claims)

        if not user.is_active:
            return error_response(
                "This account is disabled.",
                code="account_disabled",
                status_code=status.HTTP_403_FORBIDDEN,
            )

        ensure_trial_started(user)
        login(request, user)
        log_activity(
            user,
            UserActivityLog.ACTION_SIGNUP if created else UserActivityLog.ACTION_LOGIN_SUCCESS,
            request,
            details="google",
        )
        refresh = issue_tokens_for_user(user)
        return Response(
            {
                "user": UserSerializer(user).data,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "created": created,
            },
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )


def _link_google_account(user, claims):
    """Attach the Google subject to an account that matched by verified email."""
    updates = []
    if not user.google_sub:
        user.google_sub = claims["sub"]
        updates.append("google_sub")
    if user.email_verified_at is None:
        user.email_verified_at = timezone.now()
        updates.append("email_verified_at")
    if updates:
        user.save(update_fields=updates)


class OtpRequestAPIView(APIView):
    """POST: send the signed-in user a fresh one-time code.

    Authenticated rather than anonymous: signup already hands out tokens, so
    the customer is always signed in by the time they confirm, and an
    anonymous version would be an address-enumeration oracle.
    """

    permission_classes = [IsAuthenticated]
    throttle_scope = "otp"
    throttle_classes = [ScopedRateThrottle]

    def post(self, request):
        user = request.user
        if user.email_verified_at is not None:
            return Response({"sent": False, "already_verified": True})

        otp, delivered = issue_code(user, purpose=OtpCode.PURPOSE_VERIFY_EMAIL)
        if otp is None:
            return error_response(
                "Add an email address or a phone number before requesting a code.",
                code="otp_no_destination",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {
                "sent": bool(delivered),
                "channel": otp.channel,
                "expires_at": otp.expires_at,
                "already_verified": False,
            }
        )


class OtpVerifyAPIView(APIView):
    """POST: exchange a one-time code for a verified address."""

    permission_classes = [IsAuthenticated]
    throttle_scope = "otp"
    throttle_classes = [ScopedRateThrottle]

    def post(self, request):
        user = request.user
        if user.email_verified_at is not None:
            return Response({"verified": True, "already_verified": True})

        ok, reason = verify_code(
            user, request.data.get("code"), purpose=OtpCode.PURPOSE_VERIFY_EMAIL
        )
        if not ok:
            return error_response(
                _OTP_MESSAGES.get(reason, "That code is not valid."),
                code=reason,
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        mark_email_verified(user)
        return Response({"verified": True, "already_verified": False})


_OTP_MESSAGES = {
    "otp_not_requested": "Request a code before entering one.",
    "otp_expired": "That code has expired. Request a new one.",
    "otp_too_many_attempts": "Too many wrong attempts. Request a new code.",
    "otp_invalid": "That code is not correct.",
}


class CompleteOnboardingAPIView(APIView):
    """POST: mark the guided tour done for the signed-in user.

    Recorded on the row, not in the browser, so the tour does not reappear on a
    second device. ``replay=true`` clears it again for the "show me the tour"
    entry in the user menu.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        replay = str(request.data.get("replay", "")).lower() in ("1", "true", "yes")
        request.user.onboarding_completed_at = None if replay else timezone.now()
        request.user.save(update_fields=["onboarding_completed_at"])
        return Response({"onboarding_completed_at": request.user.onboarding_completed_at})


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
        serializer = ProgrammerRegisterSerializer(data=request.data, context={"request": request})
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
    """GET: every login and action, with the IP it came from. Owner console.

    ``IsProgrammer`` rather than ``IsSuperAdmin``: this is the program owner's
    audit trail across every customer, so it sits with the rest of
    ``/programmer`` and a developer account can read it.
    """

    permission_classes = [IsAuthenticated, IsProgrammer]
    serializer_class = UserActivityLogSerializer

    def get_queryset(self):
        qs = UserActivityLog.objects.select_related("user", "user__account").all()
        ip = self.request.query_params.get("ip")
        if ip:
            qs = qs.filter(ip_address__icontains=ip.strip())
        search = (self.request.query_params.get("q") or "").strip()
        if search:
            qs = qs.filter(
                Q(user__email__icontains=search)
                | Q(user__username__icontains=search)
                | Q(user__first_name__icontains=search)
                | Q(user__last_name__icontains=search)
                | Q(details__icontains=search)
                | Q(ip_address__icontains=search)
            )
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
