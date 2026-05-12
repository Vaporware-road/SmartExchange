"""Instagram Hub API: preview, status, config, OAuth."""

from __future__ import annotations

import logging
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsSuperAdminOrManagement
from instagram_hub.services.image_generator import generate_price_images
from instagram_hub.utils import path_to_public_url

logger = logging.getLogger(__name__)


def _get_instagram_connect_url(request):
    """Build absolute URL for Instagram OAuth connect. Avoids NoReverseMatch when urlconf doesn't include instagram_hub.urls."""
    try:
        from django.urls import reverse
        return request.build_absolute_uri(reverse("instagram_hub:connect"))
    except Exception:
        return request.build_absolute_uri("/instagram-hub/connect/")


def _build_price_entries_from_category_ids(category_ids: list[int]) -> list[dict]:
    """Build list of {title, price, price_type_name} from category IDs (latest price per type)."""
    from category.models import Category, PriceType
    from change_price.prefetch_helpers import prefetch_price_histories_latest
    from django.db.models import Prefetch

    entries = []
    categories = Category.objects.prefetch_related(
        Prefetch(
            "price_types",
            queryset=PriceType.objects.prefetch_related(
                prefetch_price_histories_latest(),
            ).select_related(
                "source_currency", "target_currency"
            ),
        )
    ).filter(id__in=category_ids)

    for category in categories:
        for price_type in category.price_types.all():
            latest = price_type.price_histories.first()
            if latest is not None:
                entries.append({
                    "title": price_type.name,
                    "price_type_name": price_type.name,
                    "price": str(latest.price),
                })
    return entries


class PreviewAPIView(APIView):
    """POST /api/instagram-hub/preview/ — generate post + story images and return public URLs."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]

    def post(self, request):
        theme = (request.data.get("theme") or "dark").strip().lower()
        if theme not in ("dark", "light"):
            theme = "dark"
        category_title = (request.data.get("category_title") or "").strip() or None
        price_entries = request.data.get("price_entries")
        category_ids = request.data.get("category_ids")

        if price_entries is not None and isinstance(price_entries, list) and len(price_entries) > 0:
            entries = price_entries
        elif category_ids and isinstance(category_ids, list):
            ids = [int(x) for x in category_ids if str(x).isdigit()]
            if not ids:
                return Response(
                    {"detail": "Provide price_entries or valid category_ids."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            entries = _build_price_entries_from_category_ids(ids)
            if not entries and ids:
                first_id = ids[0]
                from category.models import Category
                cat = Category.objects.filter(id=first_id).first()
                if cat:
                    category_title = category_title or cat.name
        else:
            return Response(
                {"detail": "Provide price_entries or category_ids."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not entries:
            return Response(
                {"detail": "No price data to render."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        result = generate_price_images(
            price_entries=entries,
            theme=theme,
            category_title=category_title,
        )
        if not result:
            return Response(
                {"detail": "Image generation failed."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        post_path = result.get("post_path") or ""
        story_path = result.get("story_path") or ""
        post_url = path_to_public_url(post_path, request=request) if post_path else None
        story_url = path_to_public_url(story_path, request=request) if story_path else None

        return Response({
            "post_url": post_url or "",
            "story_url": story_url or "",
        }, status=status.HTTP_200_OK)


class StatusAPIView(APIView):
    """GET /api/instagram-hub/status/ — whether Instagram is configured (for Finalize)."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]

    def get(self, request):
        from instagram_hub.services.instagram_config import is_instagram_configured
        ok = is_instagram_configured()
        return Response({"instagram_configured": ok}, status=status.HTTP_200_OK)


def _active_instagram_config_qs():
    """Defer caption extras so GET works before instagram_hub.0002 is applied on older DBs."""
    from instagram_hub.models import InstagramConfig

    return InstagramConfig.objects.filter(is_active=True).order_by("pk").defer(
        "feed_caption_suffix",
        "feed_hashtags",
    )


def _read_optional_caption_fields(config) -> tuple[str, str]:
    if not config:
        return "", ""
    try:
        return (
            (config.feed_caption_suffix or "").strip(),
            (config.feed_hashtags or "").strip(),
        )
    except Exception:
        logger.warning("Instagram caption fields unreadable (missing DB columns?)", exc_info=True)
        return "", ""


class ConfigAPIView(APIView):
    """GET /api/instagram-hub/config/ — config status and connect URL. PATCH — save app_id, app_secret."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]

    def get(self, request):
        from django.db import DatabaseError

        connect_url = _get_instagram_connect_url(request)
        try:
            config = _active_instagram_config_qs().first()
        except DatabaseError as exc:
            logger.exception("Instagram hub config GET failed: %s", exc)
            return Response(
                {
                    "has_app_id": False,
                    "has_token": False,
                    "token_expires_at": None,
                    "connect_url": connect_url,
                    "feed_caption_suffix": "",
                    "feed_hashtags": "",
                    "detail": "Could not read Instagram settings. Run: python manage.py migrate instagram_hub",
                },
                status=status.HTTP_200_OK,
            )
        if not config:
            return Response({
                "has_app_id": False,
                "has_token": False,
                "token_expires_at": None,
                "connect_url": connect_url,
                "feed_caption_suffix": "",
                "feed_hashtags": "",
            })
        has_token = bool(config.get_decrypted_token() and (config.ig_user_id or "").strip())
        suffix, hashtags = _read_optional_caption_fields(config)
        return Response({
            "has_app_id": bool((config.app_id or "").strip()),
            "has_token": has_token,
            "token_expires_at": config.token_expires_at.isoformat() if config.token_expires_at else None,
            "connect_url": connect_url,
            "feed_caption_suffix": suffix,
            "feed_hashtags": hashtags,
        })

    def patch(self, request):
        from django.db import DatabaseError

        from instagram_hub.models import InstagramConfig

        try:
            config = _active_instagram_config_qs().first()
            if not config:
                config = InstagramConfig.objects.create(name="Default", is_active=True)
            app_id = (request.data.get("app_id") or "").strip()
            app_secret = (request.data.get("app_secret") or "").strip()
            if app_id:
                config.app_id = app_id[:64]
            if app_secret:
                config.set_app_secret(app_secret)
            if "feed_caption_suffix" in request.data:
                config.feed_caption_suffix = str(request.data.get("feed_caption_suffix") or "")[:8000]
            if "feed_hashtags" in request.data:
                config.feed_hashtags = str(request.data.get("feed_hashtags") or "")[:8000]
            config.save()
        except DatabaseError as exc:
            logger.warning("Instagram hub config PATCH failed (migrations?): %s", exc)
            return Response(
                {
                    "detail": "Database is missing Instagram Hub columns. Run: python manage.py migrate instagram_hub",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response({"success": True}, status=status.HTTP_200_OK)
