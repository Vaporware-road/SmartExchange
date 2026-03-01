from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import api_views

router = DefaultRouter()
router.register(r"templates", api_views.TemplateViewSet, basename="api-template-editor-template")

urlpatterns = [
    path(
        "templates/<int:pk>/config/",
        api_views.TemplateConfigUpdateAPIView.as_view(),
        name="api-template-editor-config",
    ),
    path(
        "templates/<int:pk>/preview/",
        api_views.TemplatePreviewAPIView.as_view(),
        name="api-template-editor-preview",
    ),
    path(
        "variables/",
        api_views.TemplateVariablesAPIView.as_view(),
        name="api-template-editor-variables",
    ),
    path(
        "fonts/",
        api_views.TemplateFontsAPIView.as_view(),
        name="api-template-editor-fonts",
    ),
    path("", include(router.urls)),
]
