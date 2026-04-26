"""
DRF API views for template editor (Template model with config JSONField).
"""
import logging
import os
import uuid
from pathlib import Path
from urllib.parse import urlparse

from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import get_object_or_404
from django.utils.text import get_valid_filename
from rest_framework import status
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from accounts.permissions import IsSuperAdminOrManagement
from category.models import PriceType
from finalize.models import Finalization
from core.exceptions import error_response
from core.utils import MAX_ASSET_SIZE, format_price_display, validate_uploaded_image

from .models import Template
from .serializers import TemplateSerializer
from .utils import get_available_fonts
from .variables import get_variable_catalog, extend_variable_catalog_with_category
from .widget_sync import _sync_widgets_from_config

logger = logging.getLogger(__name__)


def _validate_config_json_widgets(config_json):
    if not isinstance(config_json, dict):
        raise DRFValidationError({"config_json": "config_json must be a JSON object"})
    widgets = config_json.get("widgets")
    if widgets is None:
        return
    if not isinstance(widgets, list):
        raise DRFValidationError({"config_json.widgets": "widgets must be a JSON array"})
    for idx, widget in enumerate(widgets):
        if not isinstance(widget, dict):
            raise DRFValidationError({f"config_json.widgets[{idx}]": "Each widget must be an object"})
        wtype = str(widget.get("type") or "").strip()
        if not wtype:
            raise DRFValidationError({f"config_json.widgets[{idx}].type": "Widget type is required"})
        for field in ("x", "y", "width", "height"):
            if widget.get(field) is None:
                raise DRFValidationError({f"config_json.widgets[{idx}].{field}": "This field is required"})


def _safe_sync_widgets(template, user):
    try:
        _sync_widgets_from_config(template, user)
    except Exception as exc:
        logger.exception(
            "template_editor widget sync failed template_id=%s",
            getattr(template, "pk", None),
        )
        raise DRFValidationError(
            f"Widget sync failed: {exc}"
        ) from exc


def _validate_telegram_buttons_json(raw):
    if raw is None:
        return
    if not isinstance(raw, list):
        raise DRFValidationError({"telegram_buttons_json": "Must be a JSON array."})

    def _validate_button(btn, key_prefix):
        if not isinstance(btn, dict):
            raise DRFValidationError({key_prefix: "Each button must be an object."})
        text = btn.get("text") or btn.get("label")
        url = btn.get("url")
        if not text or not str(text).strip():
            raise DRFValidationError({f"{key_prefix}.text": "Button text is required."})
        if not url or not str(url).strip():
            raise DRFValidationError({f"{key_prefix}.url": "Button url is required."})
        parsed = urlparse(str(url).strip())
        if parsed.scheme not in ("http", "https") or not parsed.netloc:
            raise DRFValidationError({f"{key_prefix}.url": "Button url must be a valid http(s) URL."})

    for idx, item in enumerate(raw):
        if isinstance(item, list):
            if not item:
                raise DRFValidationError(
                    {f"telegram_buttons_json[{idx}]": "Button row cannot be empty."}
                )
            for b_idx, btn in enumerate(item):
                _validate_button(btn, f"telegram_buttons_json[{idx}][{b_idx}]")
        else:
            _validate_button(item, f"telegram_buttons_json[{idx}]")


class TemplateViewSet(ModelViewSet):
    """CRUD for Template (template_editor.Template)."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]
    queryset = Template.objects.select_related(
        "category", "special_price_type"
    ).order_by("-created_at")
    serializer_class = TemplateSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def perform_create(self, serializer):
        instance = serializer.save()
        _safe_sync_widgets(instance, getattr(self.request, "user", None))

    def perform_update(self, serializer):
        instance = serializer.save()
        _safe_sync_widgets(instance, getattr(self.request, "user", None))


class TemplateConfigUpdateAPIView(APIView):
    """PUT /api/template-editor/templates/<id>/config/ — config, config_json, and/or canvas fields."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def put(self, request, pk):
        template = get_object_or_404(Template, pk=pk)
        config = request.data.get("config")
        config_json = request.data.get("config_json")
        has_canvas = any(
            k in request.data for k in ("canvas_width", "canvas_height", "orientation")
        )
        has_meta = any(
            k in request.data
            for k in (
                "is_active",
                "publish_order",
                "telegram_caption_template",
                "telegram_buttons_json",
            )
        )
        if config is None and config_json is None and not has_canvas and not has_meta:
            return error_response(
                "Provide at least one updatable field.",
                code="template_config_empty_payload",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        if config is not None and not isinstance(config, dict):
            return error_response(
                "config must be a JSON object",
                code="template_config_invalid_type",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        if config_json is not None and not isinstance(config_json, dict):
            return error_response(
                "config_json must be a JSON object",
                code="template_config_json_invalid_type",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        if config_json is not None:
            try:
                _validate_config_json_widgets(config_json)
            except DRFValidationError as exc:
                return error_response(
                    "Template config JSON is invalid.",
                    code="template_config_json_invalid",
                    status_code=status.HTTP_400_BAD_REQUEST,
                    errors=exc.detail if isinstance(exc.detail, dict) else None,
                )
        if config is not None:
            template.config = config
        if config_json is not None:
            template.config_json = config_json

        if "canvas_width" in request.data and request.data["canvas_width"] is not None:
            try:
                template.canvas_width = max(
                    1, min(10000, int(request.data["canvas_width"]))
                )
            except (TypeError, ValueError):
                return error_response(
                    "Canvas width must be a positive integer.",
                    code="template_canvas_width_invalid",
                    status_code=status.HTTP_400_BAD_REQUEST,
                    errors={"canvas_width": "Must be a positive integer."},
                )
        if "canvas_height" in request.data and request.data["canvas_height"] is not None:
            try:
                template.canvas_height = max(
                    1, min(10000, int(request.data["canvas_height"]))
                )
            except (TypeError, ValueError):
                return error_response(
                    "Canvas height must be a positive integer.",
                    code="template_canvas_height_invalid",
                    status_code=status.HTTP_400_BAD_REQUEST,
                    errors={"canvas_height": "Must be a positive integer."},
                )
        if "orientation" in request.data and request.data["orientation"] not in (
            None,
            "",
        ):
            ov = request.data["orientation"]
            if ov not in ("landscape", "portrait"):
                return error_response(
                    'Orientation must be "landscape" or "portrait".',
                    code="template_orientation_invalid",
                    status_code=status.HTTP_400_BAD_REQUEST,
                    errors={"orientation": 'Must be "landscape" or "portrait".'},
                )
            template.orientation = ov

        if "is_active" in request.data and request.data["is_active"] is not None:
            template.is_active = bool(request.data["is_active"])
        if "publish_order" in request.data and request.data["publish_order"] is not None:
            try:
                template.publish_order = max(
                    0, min(32767, int(request.data["publish_order"]))
                )
            except (TypeError, ValueError):
                return error_response(
                    "Publish order must be a non-negative integer.",
                    code="template_publish_order_invalid",
                    status_code=status.HTTP_400_BAD_REQUEST,
                    errors={"publish_order": "Must be a non-negative integer."},
                )
        if "telegram_caption_template" in request.data:
            v = request.data.get("telegram_caption_template")
            template.telegram_caption_template = "" if v is None else str(v)
        if "telegram_buttons_json" in request.data:
            tb = request.data.get("telegram_buttons_json")
            if isinstance(tb, list):
                try:
                    _validate_telegram_buttons_json(tb)
                except DRFValidationError as exc:
                    return error_response(
                        "Telegram buttons are invalid.",
                        code="template_telegram_buttons_invalid",
                        status_code=status.HTTP_400_BAD_REQUEST,
                        errors=exc.detail if isinstance(exc.detail, dict) else None,
                    )
                template.telegram_buttons_json = tb
            elif tb is not None:
                return error_response(
                    "Telegram buttons must be a JSON array.",
                    code="template_telegram_buttons_invalid",
                    status_code=status.HTTP_400_BAD_REQUEST,
                    errors={"telegram_buttons_json": "Must be a JSON array."},
                )

        template.save()
        try:
            _sync_widgets_from_config(template, getattr(request, "user", None))
        except Exception as exc:
            logger.exception(
                "template_editor widget sync failed after config save template_id=%s",
                template.pk,
            )
            return Response(
                {
                    "error": True,
                    "message": "Widget sync failed after save.",
                    "code": "template_widget_sync_failed",
                    "errors": {"sync_error": str(exc)},
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        from .canvas_sync import sync_template_dimensions_from_background

        if template.image and sync_template_dimensions_from_background(template):
            template.save(
                update_fields=["canvas_width", "canvas_height", "config", "updated_at"]
            )
        return Response(TemplateSerializer(template).data)


class TemplateEditorMediaUploadAPIView(APIView):
    """
    GET /api/template-editor/media/ — list recent uploaded images under template_editor/uploads/.
    POST /api/template-editor/media/ — upload an image (field: file or image). Returns { "url": "/media/..." }.
    """

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        base = Path(settings.MEDIA_ROOT) / "template_editor" / "uploads"
        if not base.is_dir():
            return Response({"results": []})
        rows = []
        for p in sorted(base.iterdir(), key=lambda x: x.stat().st_mtime, reverse=True)[:80]:
            if p.is_file() and p.suffix.lower() in (
                ".jpg",
                ".jpeg",
                ".png",
                ".gif",
                ".webp",
            ):
                rel = f"template_editor/uploads/{p.name}"
                url = f"{settings.MEDIA_URL.rstrip('/')}/{rel}"
                rows.append({"url": url, "name": p.name})
        return Response({"results": rows})

    def post(self, request):
        file_obj = request.FILES.get("file") or request.FILES.get("image")
        if not file_obj:
            return error_response(
                "No file provided. Use 'file' or 'image' form field.",
                code="file_required",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        try:
            validate_uploaded_image(file_obj, max_size=MAX_ASSET_SIZE)
        except ValueError as e:
            return error_response(
                str(e),
                code="invalid_image_upload",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        name = get_valid_filename(file_obj.name) or "image"
        ext = os.path.splitext(name)[1].lower()
        if ext not in (".jpg", ".jpeg", ".png", ".gif", ".webp"):
            return error_response(
                "Only image files (jpg, png, gif, webp) are allowed.",
                code="unsupported_file_type",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        rel_path = f"template_editor/uploads/{uuid.uuid4().hex}{ext}"
        path = default_storage.save(rel_path, file_obj)
        url = f"{settings.MEDIA_URL.rstrip('/')}/{path}"
        return Response({"url": url})


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
        cat = request.query_params.get("category")
        if cat is not None and str(cat).strip() != "":
            try:
                cid = int(cat)
                return Response(extend_variable_catalog_with_category(cid))
            except (TypeError, ValueError):
                pass
        return Response(get_variable_catalog())


class TemplateFontsAPIView(APIView):
    """GET /api/template-editor/fonts/ - return available font list for editor dropdown."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]

    def get(self, request):
        fonts = get_available_fonts()
        return Response([{"filename": f[0], "display_name": f[1]} for f in fonts])


class TemplatePriceBindingsPreviewAPIView(APIView):
    """GET /api/template-editor/price-bindings-preview/?category=<id>."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]

    @staticmethod
    def _format_price(value):
        if value is None:
            return ""
        return format_price_display(value)

    def get(self, request):
        raw_category = request.query_params.get("category")
        try:
            category_id = int(raw_category)
        except (TypeError, ValueError):
            return error_response(
                "Valid category id is required.",
                code="template_price_bindings_preview_category_required",
                status_code=status.HTTP_400_BAD_REQUEST,
                errors={"category": "Must be an integer category id."},
            )

        price_types = list(
            PriceType.objects.filter(category_id=category_id, is_active=True)
            .prefetch_related("price_histories")
            .order_by("order", "id")
        )
        if not price_types:
            return Response([])

        latest_finalization = (
            Finalization.objects.filter(category_id=category_id)
            .order_by("-finalized_at")
            .first()
        )
        finalized_price_map = {}
        if latest_finalization:
            finalized_price_map = {
                fp.price_history.price_type_id: fp.price_history
                for fp in latest_finalization.finalized_prices.select_related("price_history")
            }

        rows = []
        for pt in price_types:
            slug = (pt.slug or "").strip()
            if not slug:
                continue

            key = f"price__{slug}"
            source = "none"
            picked = None

            finalized = finalized_price_map.get(pt.id)
            if finalized is not None:
                picked = finalized
                source = "finalized"
            else:
                latest = pt.price_histories.first()
                if latest is not None:
                    picked = latest
                    source = "latest"

            previous_price = self._format_price(getattr(picked, "price", None)) if picked else ""
            rows.append(
                {
                    "key": key,
                    "label": pt.name,
                    "previous_price": previous_price,
                    "source": source,
                    "has_value": bool(previous_price),
                    "price_type_id": pt.id,
                }
            )
        return Response(rows)
