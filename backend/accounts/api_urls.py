from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import api_views

urlpatterns = [
    path("login/", api_views.LoginAPIView.as_view(), name="api-login"),
    path("logout/", api_views.LogoutAPIView.as_view(), name="api-logout"),
    path("me/", api_views.MeAPIView.as_view(), name="api-me"),
    path("token/refresh/", TokenRefreshView.as_view(), name="api-token-refresh"),
]
