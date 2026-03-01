from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from .models import CustomUser, UserActivityLog
from .serializers import (
    LoginSerializer,
    UserSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
    UserActivityLogSerializer,
)
from .utils import get_client_ip, get_user_agent, log_activity
from .permissions import IsSuperAdminOrManagement, IsSuperAdmin


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

        refresh = RefreshToken.for_user(user)
        refresh.access_token['token_version'] = user.token_version

        log_activity(user, UserActivityLog.ACTION_LOGIN_SUCCESS, request)

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
    def get(self, request):
        return Response(UserSerializer(request.user).data)


class UserListCreateAPIView(ListCreateAPIView):
    """GET: list users. POST: create user. Super Admin only."""
    permission_classes = [IsAuthenticated, IsSuperAdmin]
    queryset = CustomUser.objects.all().order_by('-date_joined')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserSerializer


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
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
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
