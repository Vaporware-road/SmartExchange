from django.urls import path
from . import api_views

# Do not set app_name here so that reverse("instagram_hub:connect") resolves
# from instagram_hub.urls (main urls), not from this API urlconf.
urlpatterns = [
    path("preview/", api_views.PreviewAPIView.as_view(), name="preview"),
    path("status/", api_views.StatusAPIView.as_view(), name="status"),
    path("config/", api_views.ConfigAPIView.as_view(), name="config"),
]
