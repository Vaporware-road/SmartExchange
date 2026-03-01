"""
DRF API views for template editor (Template model with config JSONField).
"""
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsSuperAdminOrManagement
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

from .models import Template
from .serializers import TemplateSerializer
from .variables import get_variable_catalog
from .utils import get_available_fonts


class TemplateViewSet(ModelViewSet):
    """CRUD for Template (template_editor.Template)."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]
    queryset = Template.objects.select_related(
        "category", "special_price_type"
    ).order_by("-created_at")
    serializer_class = TemplateSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class TemplateConfigUpdateAPIView(APIView):
    """PUT /api/template-editor/templates/<id>/config/ - update config JSON only."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]

    def put(self, request, pk):
        template = get_object_or_404(Template, pk=pk)
        config = request.data.get("config")
        if config is None:
            return Response(
                {"detail": "config field is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not isinstance(config, dict):
            return Response(
                {"detail": "config must be a JSON object"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        template.config = config
        template.save()
        return Response(TemplateSerializer(template).data)


class TemplatePreviewAPIView(APIView):
    """
    GET/POST /api/template-editor/templates/<id>/preview/
    Renders the template with config and returns PNG image or error JSON.
    POST can override config in body for live preview.
    """

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]

    def get(self, request, pk):
        return self._render_preview(request, pk)

    def post(self, request, pk):
        return self._render_preview(request, pk)

    def _render_preview(self, request, pk):
        from .views import PreviewView

        template = get_object_or_404(Template, pk=pk)
        preview_view = PreviewView()
        preview_view.request = request
        response = preview_view._render_preview(request, pk)
        return response


class TemplateVariablesAPIView(APIView):
    """GET /api/template-editor/variables/ - return variable catalog for editor sidebar."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]

    def get(self, request):
        return Response(get_variable_catalog())


class TemplateFontsAPIView(APIView):
    """GET /api/template-editor/fonts/ - return available font list for editor dropdown."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]

    def get(self, request):
        fonts = get_available_fonts()
        return Response([{"filename": f[0], "display_name": f[1]} for f in fonts])
