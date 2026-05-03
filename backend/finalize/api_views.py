"""
DRF API views for finalization flows.
"""
import logging
from django.conf import settings
from django.db import transaction
from django.db.models import Prefetch
from django.db.utils import OperationalError
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import ScopedRateThrottle
from celery.exceptions import TimeoutError as CeleryTimeoutError

from accounts.permissions import IsSuperAdminOrManagement
from category.models import Category, PriceType
from special_price.models import SpecialPriceType, SpecialPriceHistory
from telegram_app.models import TelegramChannel
from price_publisher.tasks import publish_category_prices_task, publish_special_price_task
from setting.utils import log_finalize_event, log_telegram_event

from instagram_hub.services.instagram_config import is_instagram_configured
from instagram_hub.tasks import post_finalize_to_instagram_task

from .models import Finalization, FinalizedPriceHistory, SpecialPriceFinalization
from .tasks import send_finalized_prices_task, send_finalized_special_prices_task
from .views import sort_gbp_price_types
from .serializers import (
    FinalizeCategoryRequestSerializer,
    FinalizeSpecialPriceRequestSerializer,
    FinalizeAllRequestSerializer,
)

logger = logging.getLogger(__name__)

# Omit from SELECT so older DBs without these columns still load the finalize dashboard.
# Round-robin still works after migrate (column then exists); until then values default in memory.
_DASHBOARD_CATEGORY_DEFER = ("last_used_template",)
_DASHBOARD_SPECIAL_TYPE_DEFER = ("last_used_template",)


def _wait_for_publication_task(async_result):
    timeout_seconds = max(1, int(getattr(settings, "FINALIZE_TASK_WAIT_TIMEOUT", 75)))
    try:
        payload = async_result.get(timeout=timeout_seconds)
        if isinstance(payload, dict):
            return payload
        return {
            "success": False,
            "response": f"Invalid task response: {type(payload).__name__}",
            "caption": None,
            "publish_path": "unknown",
            "render_fallback_reason": "invalid_task_response",
        }
    except CeleryTimeoutError:
        logger.exception("Publication task timeout task_id=%s", async_result.id)
        return {
            "success": False,
            "response": f"Publication timed out after {timeout_seconds}s",
            "caption": None,
            "publish_path": "worker_timeout",
            "render_fallback_reason": "task_timeout",
        }
    except Exception as exc:
        logger.exception("Publication task failed task_id=%s", async_result.id)
        return {
            "success": False,
            "response": str(exc),
            "caption": None,
            "publish_path": "worker_error",
            "render_fallback_reason": "task_error",
        }


def _get_publication_destinations():
    """Return list of publication destinations with enabled flag for frontend."""
    destinations = [
        {"id": "telegram", "label": "Telegram Channel", "enabled": True},
    ]
    try:
        from instagram_hub.services.instagram_config import is_instagram_configured
        destinations.append({
            "id": "instagram",
            "label": "Instagram",
            "enabled": is_instagram_configured(),
        })
    except Exception:
        destinations.append({"id": "instagram", "label": "Instagram", "enabled": False})
    external_url = getattr(settings, "EXTERNAL_API_URL", None)
    external_key = getattr(settings, "EXTERNAL_API_KEY", None)
    destinations.append({
        "id": "external_api",
        "label": "Mobile App / Web",
        "enabled": bool(external_url and external_key),
    })
    return destinations


def _build_finalize_dashboard_data():
    """Build dashboard data: categories with pending prices and pending special prices."""
    # Separate summary query avoids edge cases after iterating the prefetched queryset.
    category_summaries = list(
        Category.objects.order_by("name").values("id", "name", "slug", "description")
    )
    categories = (
        Category.objects.defer(*_DASHBOARD_CATEGORY_DEFER)
        .prefetch_related(
            Prefetch(
                "price_types",
                queryset=PriceType.objects.prefetch_related("price_histories").select_related(
                    "source_currency", "target_currency"
                ),
            )
        )
        .order_by("name")
    )

    pending_by_category = []
    for category in categories:
        latest_finalization = Finalization.objects.filter(
            category=category
        ).order_by("-finalized_at").first()

        if latest_finalization:
            try:
                finalized_history_ids = set(
                    latest_finalization.finalized_prices.values_list(
                        "price_history_id", flat=True
                    )
                )
                finalized_price_map = {}
                for fph in latest_finalization.finalized_prices.select_related(
                    "price_history__price_type"
                ):
                    try:
                        ph = fph.price_history
                    except Exception:
                        logger.warning(
                            "Skipping finalized row with missing price_history "
                            "(finalized_price_history_id=%s)",
                            getattr(fph, "pk", None),
                        )
                        continue
                    if ph is not None and getattr(ph, "price_type_id", None):
                        finalized_price_map[ph.price_type_id] = ph
            except Exception:
                logger.exception(
                    "Corrupt finalization data for category_id=%s; treating as no prior finalization",
                    getattr(category, "pk", None),
                )
                finalized_history_ids = set()
                finalized_price_map = {}
        else:
            finalized_history_ids = set()
            finalized_price_map = {}

        price_types = list(category.price_types.all())
        category_name_lower = category.name.lower()
        if "پوند" in category.name or "pound" in category_name_lower or "gbp" in category_name_lower:
            price_types = sort_gbp_price_types(price_types)

        category_pending = []
        for price_type in price_types:
            latest_price = price_type.price_histories.first()
            if latest_price and latest_price.id not in finalized_history_ids:
                item = {
                    "price_type_id": price_type.id,
                    "price_type_name": price_type.name,
                    "price_history_id": latest_price.id,
                    "price": str(latest_price.price),
                    "created_at": latest_price.created_at.isoformat(),
                    "has_older_finalized": len(finalized_history_ids) > 0,
                }
                if price_type.id in finalized_price_map:
                    prev_ph = finalized_price_map[price_type.id]
                    item["previous_price"] = str(prev_ph.price)
                else:
                    item["previous_price"] = None
                category_pending.append(item)

        if category_pending:
            pending_by_category.append(
                {
                    "category_id": category.id,
                    "category_name": category.name,
                    "category_slug": category.slug,
                    "pending_prices": category_pending,
                }
            )

    special_price_types = (
        SpecialPriceType.objects.defer(*_DASHBOARD_SPECIAL_TYPE_DEFER)
        .prefetch_related(
            Prefetch(
                "special_price_histories",
                queryset=SpecialPriceHistory.objects.order_by("-created_at"),
            )
        )
        .select_related("source_currency", "target_currency")
        .order_by("name")
    )

    pending_special_prices = []
    for special_price_type in special_price_types:
        latest_price = special_price_type.special_price_histories.first()
        if latest_price:
            is_finalized = SpecialPriceFinalization.objects.filter(
                special_price_history=latest_price
            ).exists()
            if not is_finalized:
                prev_finalization = (
                    SpecialPriceFinalization.objects.filter(
                        special_price_history__special_price_type=special_price_type
                    )
                    .order_by("-finalized_at")
                    .select_related("special_price_history")
                    .first()
                )
                previous_price = None
                if prev_finalization and prev_finalization.special_price_history_id:
                    try:
                        previous_price = str(
                            prev_finalization.special_price_history.price
                        )
                    except Exception:
                        logger.warning(
                            "Skipping previous special price (special_price_finalization_id=%s)",
                            getattr(prev_finalization, "pk", None),
                        )
                        previous_price = None
                pending_special_prices.append(
                    {
                        "special_price_type_id": special_price_type.id,
                        "special_price_type_name": special_price_type.name,
                        "price_history_id": latest_price.id,
                        "price": str(latest_price.price),
                        "created_at": latest_price.created_at.isoformat(),
                        "previous_price": previous_price,
                    }
                )

    return {
        "categories": category_summaries,
        "pending_by_category": pending_by_category,
        "has_pending": len(pending_by_category) > 0,
        "pending_special_prices": pending_special_prices,
        "has_pending_special": len(pending_special_prices) > 0,
        "publication_destinations": _get_publication_destinations(),
    }


class FinalizeDashboardAPIView(APIView):
    """GET /api/finalize/dashboard/ - categories with pending prices. Read-only: any authenticated user (incl. Employee)."""

    permission_classes = [IsAuthenticated]
    throttle_scope = "finalize"
    throttle_classes = [ScopedRateThrottle]

    def get(self, request):
        try:
            data = _build_finalize_dashboard_data()
            return Response(data)
        except Exception as exc:
            logger.exception("FinalizeDashboardAPIView.get failed")
            try:
                destinations = _get_publication_destinations()
            except Exception:
                destinations = [{"id": "telegram", "label": "Telegram Channel", "enabled": True}]
            if isinstance(exc, OperationalError):
                detail = (
                    "Database schema mismatch (often fixed by: python manage.py migrate). "
                    "See server logs for the exact SQL error."
                )
            else:
                detail = (
                    "Finalize dashboard could not be loaded. Check server logs or run migrations."
                )
            payload = {
                "categories": [],
                "pending_by_category": [],
                "has_pending": False,
                "pending_special_prices": [],
                "has_pending_special": False,
                "publication_destinations": destinations,
                "degraded": True,
                "detail": detail,
            }
            if settings.DEBUG:
                payload["debug_exception"] = repr(exc)
            return Response(payload, status=status.HTTP_200_OK)


class FinalizeCategoryAPIView(APIView):
    """POST /api/finalize/category/<id>/ - finalize a category."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]
    throttle_scope = "finalize"
    throttle_classes = [ScopedRateThrottle]

    def post(self, request, category_id):
        category = get_object_or_404(
            Category.objects.defer(*_DASHBOARD_CATEGORY_DEFER), id=category_id
        )
        channels = TelegramChannel.objects.filter(is_active=True).select_related("bot")

        serializer = FinalizeCategoryRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        channel_id = serializer.validated_data["channel_id"]
        notes = serializer.validated_data.get("notes", "")

        channel = get_object_or_404(TelegramChannel, id=channel_id, is_active=True)

        latest_finalization = Finalization.objects.filter(
            category=category
        ).order_by("-finalized_at").first()

        if latest_finalization:
            finalized_history_ids = set(
                latest_finalization.finalized_prices.values_list("price_history_id", flat=True)
            )
            finalized_price_map = {
                fph.price_history.price_type_id: fph.price_history
                for fph in latest_finalization.finalized_prices.select_related(
                    "price_history__price_type"
                )
            }
        else:
            finalized_history_ids = set()
            finalized_price_map = {}

        price_types = PriceType.objects.filter(category=category).select_related(
            "source_currency", "target_currency"
        )
        category_name_lower = category.name.lower()
        if "پوند" in category.name or "pound" in category_name_lower or "gbp" in category_name_lower:
            price_types = sort_gbp_price_types(price_types)

        price_items = []
        pending_prices = []

        for price_type in price_types:
            latest_price = price_type.price_histories.first()
            if not latest_price:
                continue

            if latest_price.id not in finalized_history_ids:
                price_items.append((price_type, latest_price))
                pending_prices.append({"price_type": price_type, "price_history": latest_price})
            else:
                if price_type.id in finalized_price_map:
                    finalized_price = finalized_price_map[price_type.id]
                    price_items.append((price_type, finalized_price))
                else:
                    price_items.append((price_type, latest_price))

        if not price_items:
            return Response(
                {"detail": f'No prices found for category "{category.name}".'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        notes_text = notes.strip() if notes else None

        api_sent_successfully = None

        publish_async = publish_category_prices_task.apply_async(
            kwargs={
                "category_id": category.id,
                "channel_id": channel.id,
                "notes": notes_text,
                "price_history_ids": [price_history.id for _, price_history in price_items],
            }
        )
        publication = _wait_for_publication_task(publish_async)
        message_sent = bool(publication.get("success"))
        image_caption = publication.get("caption")
        template_id = publication.get("template_id")
        publication_response = publication.get("response", "")
        publish_path = publication.get("publish_path", "unknown")
        render_fallback_reason = publication.get("render_fallback_reason")

        if render_fallback_reason == "template_missing_or_invalid":
            return Response(
                {
                    "detail": "Publish blocked: category template is missing or invalid.",
                    "telegram_response": publication_response,
                    "publish_path": publish_path,
                    "render_fallback_reason": render_fallback_reason,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        strict = getattr(settings, "FINALIZE_STRICT_TELEGRAM", False)
        if strict and not message_sent:
            return Response(
                {
                    "detail": "Telegram publication failed. Finalization was not saved (strict mode).",
                    "telegram_response": publication_response,
                    "publish_path": publish_path,
                    "render_fallback_reason": render_fallback_reason,
                },
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        with transaction.atomic():
            finalization = Finalization.objects.create(
                category=category,
                channel=channel if message_sent else None,
                finalized_by=request.user,
                message_sent=message_sent,
                image_caption=image_caption if message_sent else None,
                telegram_response=publication_response or None,
                notes=notes,
            )
            for item in pending_prices:
                FinalizedPriceHistory.objects.create(
                    finalization=finalization,
                    price_history=item["price_history"],
                )
            transaction.on_commit(
                lambda: send_finalized_prices_task.delay(
                    price_history_ids=[price_history.id for _, price_history in price_items]
                )
            )

        total_prices_count = len(price_items)
        new_prices_count = len(pending_prices)
        log_finalize_event(
            level="INFO" if message_sent else "WARNING",
            message=f"Category finalized: {category.name}",
            details={
                "event": "finalize_category",
                "category_id": category.id,
                "category_name": category.name,
                "finalization_id": finalization.id,
                "total_prices": total_prices_count,
                "new_prices": new_prices_count,
                "message_sent": message_sent,
                "publish_path": publish_path,
                "render_fallback_reason": render_fallback_reason,
            },
            user=request.user,
        )
        if message_sent:
            log_telegram_event(
                level="INFO",
                message="Category prices published to Telegram",
                details={
                    "event": "finalize_category_telegram_publish",
                    "category_id": category.id,
                    "category_name": category.name,
                    "channel_id": channel.id,
                    "channel_name": channel.name,
                },
                user=request.user,
            )

        return Response(
            {
                "success": True,
                "finalization_id": finalization.id,
                "message_sent": message_sent,
                "total_prices": total_prices_count,
                "new_prices": new_prices_count,
                "api_sent_successfully": api_sent_successfully,
                "api_sync_queued": True,
                "telegram_response": publication_response,
                "template_id": template_id,
                "publish_path": publish_path,
                "render_fallback_reason": render_fallback_reason,
            },
            status=status.HTTP_201_CREATED,
        )


class FinalizeSpecialPriceAPIView(APIView):
    """POST /api/finalize/special-price/<id>/ - finalize a special price (id is special_price_history_id)."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]
    throttle_scope = "finalize"
    throttle_classes = [ScopedRateThrottle]

    def post(self, request, special_price_history_id):
        special_price_history = get_object_or_404(
            SpecialPriceHistory.objects.select_related("special_price_type").defer(
                "special_price_type__last_used_template"
            ),
            id=special_price_history_id,
        )
        special_price_type = special_price_history.special_price_type

        existing = SpecialPriceFinalization.objects.filter(
            special_price_history=special_price_history
        ).first()
        if existing:
            return Response(
                {"detail": "This special price is already finalized."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = FinalizeSpecialPriceRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        channel_id = serializer.validated_data["channel_id"]
        notes = serializer.validated_data.get("notes", "")

        channel = get_object_or_404(TelegramChannel, id=channel_id, is_active=True)
        notes_text = notes.strip() if notes else None

        publish_async = publish_special_price_task.apply_async(
            kwargs={
                "special_price_history_id": special_price_history.id,
                "channel_id": channel.id,
                "notes": notes_text,
            }
        )
        publication = _wait_for_publication_task(publish_async)
        message_sent = bool(publication.get("success"))
        image_caption = publication.get("caption")
        template_id = publication.get("template_id")
        publication_response = publication.get("response", "")
        publish_path = publication.get("publish_path", "unknown")
        render_fallback_reason = publication.get("render_fallback_reason")

        strict = getattr(settings, "FINALIZE_STRICT_TELEGRAM", False)
        if strict and not message_sent:
            return Response(
                {
                    "detail": "Telegram publication failed. Finalization was not saved (strict mode).",
                    "telegram_response": publication_response,
                    "publish_path": publish_path,
                    "render_fallback_reason": render_fallback_reason,
                },
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        with transaction.atomic():
            finalization = SpecialPriceFinalization.objects.create(
                special_price_history=special_price_history,
                channel=channel if message_sent else None,
                finalized_by=request.user,
                message_sent=message_sent,
                image_caption=image_caption if message_sent else None,
                telegram_response=publication_response or None,
                notes=notes,
            )
            transaction.on_commit(
                lambda: send_finalized_special_prices_task.delay(
                    special_price_history_ids=[special_price_history.id]
                )
            )

        log_finalize_event(
            level="INFO" if message_sent else "WARNING",
            message=f"Special price finalized: {special_price_type.name}",
            details={
                "event": "finalize_special_price",
                "special_price_type_id": special_price_type.id,
                "special_price_history_id": special_price_history.id,
                "price": str(special_price_history.price),
                "finalization_id": finalization.id,
                "message_sent": message_sent,
                "publish_path": publish_path,
                "render_fallback_reason": render_fallback_reason,
            },
            user=request.user,
        )

        return Response(
            {
                "success": True,
                "finalization_id": finalization.id,
                "message_sent": message_sent,
                "telegram_response": publication_response,
                "template_id": template_id,
                "publish_path": publish_path,
                "render_fallback_reason": render_fallback_reason,
            },
            status=status.HTTP_201_CREATED,
        )


class FinalizeAllAPIView(APIView):
    """POST /api/finalize/all/ - finalize multiple categories and special prices in one request."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]
    throttle_scope = "finalize"
    throttle_classes = [ScopedRateThrottle]

    def post(self, request):
        serializer = FinalizeAllRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        channel_id = serializer.validated_data["channel_id"]
        category_ids = serializer.validated_data.get("category_ids") or []
        special_price_history_ids = serializer.validated_data.get("special_price_history_ids") or []

        if not category_ids and not special_price_history_ids:
            return Response(
                {"detail": "Provide at least one category_ids or special_price_history_ids."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        channel = get_object_or_404(TelegramChannel, id=channel_id, is_active=True)
        notes = ""

        results = []

        for cat_id in category_ids:
            try:
                category = get_object_or_404(
                    Category.objects.defer(*_DASHBOARD_CATEGORY_DEFER), id=cat_id
                )
                self._finalize_one_category(request, category, channel, notes)
                results.append({"id": cat_id, "type": "category", "success": True})
            except Exception as exc:
                logger.exception("Finalize all: category %s failed", cat_id)
                results.append({
                    "id": cat_id,
                    "type": "category",
                    "success": False,
                    "error": str(exc) or "Unknown error",
                })

        for sp_id in special_price_history_ids:
            try:
                special_price_history = get_object_or_404(
                    SpecialPriceHistory.objects.select_related("special_price_type").defer(
                        "special_price_type__last_used_template"
                    ),
                    id=sp_id,
                )
                special_price_type = special_price_history.special_price_type
                if SpecialPriceFinalization.objects.filter(
                    special_price_history=special_price_history
                ).exists():
                    results.append({
                        "id": sp_id,
                        "type": "special",
                        "success": False,
                        "error": "Already finalized.",
                    })
                    continue
                notes_text = notes.strip() if notes else None
                publish_async = publish_special_price_task.apply_async(
                    kwargs={
                        "special_price_history_id": special_price_history.id,
                        "channel_id": channel.id,
                        "notes": notes_text,
                    }
                )
                publication = _wait_for_publication_task(publish_async)
                message_sent = bool(publication.get("success"))
                image_caption = publication.get("caption")
                publication_response = publication.get("response", "")
                publish_path = publication.get("publish_path", "unknown")
                render_fallback_reason = publication.get("render_fallback_reason")
                strict = getattr(settings, "FINALIZE_STRICT_TELEGRAM", False)
                if strict and not message_sent:
                    results.append({
                        "id": sp_id,
                        "type": "special",
                        "success": False,
                        "error": "Telegram publication failed (strict mode).",
                    })
                    continue
                with transaction.atomic():
                    finalization = SpecialPriceFinalization.objects.create(
                        special_price_history=special_price_history,
                        channel=channel if message_sent else None,
                        finalized_by=request.user,
                        message_sent=message_sent,
                        image_caption=image_caption if message_sent else None,
                        telegram_response=publication_response or None,
                        notes=notes,
                    )
                    transaction.on_commit(
                        lambda: send_finalized_special_prices_task.delay(
                            special_price_history_ids=[special_price_history.id]
                        )
                    )
                log_finalize_event(
                    level="INFO" if message_sent else "WARNING",
                    message=f"Special price finalized (all): {special_price_type.name}",
                    details={
                        "event": "finalize_special_price_bulk",
                        "special_price_type_id": special_price_type.id,
                        "special_price_history_id": special_price_history.id,
                        "finalization_id": finalization.id,
                        "message_sent": message_sent,
                        "publish_path": publish_path,
                        "render_fallback_reason": render_fallback_reason,
                    },
                    user=request.user,
                )
                results.append({
                    "id": sp_id,
                    "type": "special",
                    "success": True,
                    "message_sent": message_sent,
                    "telegram_response": publication_response,
                    "publish_path": publish_path,
                    "render_fallback_reason": render_fallback_reason,
                })
            except Exception as exc:
                logger.exception("Finalize all: special price %s failed", sp_id)
                results.append({
                    "id": sp_id,
                    "type": "special",
                    "success": False,
                    "error": str(exc) or "Unknown error",
                })

        if is_instagram_configured() and (category_ids or special_price_history_ids):
            transaction.on_commit(
                lambda: post_finalize_to_instagram_task.delay(
                    category_ids=category_ids,
                    special_price_history_ids=special_price_history_ids,
                    theme="dark",
                )
            )

        return Response({"results": results}, status=status.HTTP_200_OK)

    def _finalize_one_category(self, request, category, channel, notes):
        """Run finalization for one category. Raises on failure."""
        latest_finalization = Finalization.objects.filter(
            category=category
        ).order_by("-finalized_at").first()

        if latest_finalization:
            finalized_history_ids = set(
                latest_finalization.finalized_prices.values_list("price_history_id", flat=True)
            )
            finalized_price_map = {
                fph.price_history.price_type_id: fph.price_history
                for fph in latest_finalization.finalized_prices.select_related(
                    "price_history__price_type"
                )
            }
        else:
            finalized_history_ids = set()
            finalized_price_map = {}

        price_types = PriceType.objects.filter(category=category).select_related(
            "source_currency", "target_currency"
        )
        category_name_lower = category.name.lower()
        if "پوند" in category.name or "pound" in category_name_lower or "gbp" in category_name_lower:
            price_types = sort_gbp_price_types(price_types)

        price_items = []
        pending_prices = []

        for price_type in price_types:
            latest_price = price_type.price_histories.first()
            if not latest_price:
                continue
            if latest_price.id not in finalized_history_ids:
                price_items.append((price_type, latest_price))
                pending_prices.append({"price_type": price_type, "price_history": latest_price})
            else:
                if price_type.id in finalized_price_map:
                    price_items.append((price_type, finalized_price_map[price_type.id]))
                else:
                    price_items.append((price_type, latest_price))

        if not price_items:
            raise ValueError(f'No prices found for category "{category.name}".')

        notes_text = notes.strip() if notes else None

        publish_async = publish_category_prices_task.apply_async(
            kwargs={
                "category_id": category.id,
                "channel_id": channel.id,
                "notes": notes_text,
                "price_history_ids": [price_history.id for _, price_history in price_items],
            }
        )
        publication = _wait_for_publication_task(publish_async)
        message_sent = bool(publication.get("success"))
        image_caption = publication.get("caption")
        template_id = publication.get("template_id")
        publication_response = publication.get("response", "")
        publish_path = publication.get("publish_path", "unknown")
        render_fallback_reason = publication.get("render_fallback_reason")

        strict = getattr(settings, "FINALIZE_STRICT_TELEGRAM", False)
        if strict and not message_sent:
            raise ValueError(
                "Telegram publication failed (strict mode). Finalization was not saved."
            )

        with transaction.atomic():
            finalization = Finalization.objects.create(
                category=category,
                channel=channel if message_sent else None,
                finalized_by=request.user,
                message_sent=message_sent,
                image_caption=image_caption if message_sent else None,
                telegram_response=publication_response or None,
                notes=notes,
            )
            for item in pending_prices:
                FinalizedPriceHistory.objects.create(
                    finalization=finalization,
                    price_history=item["price_history"],
                )
            transaction.on_commit(
                lambda: send_finalized_prices_task.delay(
                    price_history_ids=[price_history.id for _, price_history in price_items]
                )
            )

        log_finalize_event(
            level="INFO" if message_sent else "WARNING",
            message=f"Category finalized (all): {category.name}",
            details={
                "event": "finalize_category_bulk",
                "category_id": category.id,
                "category_name": category.name,
                "finalization_id": finalization.id,
                "new_prices": len(pending_prices),
                "message_sent": message_sent,
                "publish_path": publish_path,
                "template_id": template_id,
                "render_fallback_reason": render_fallback_reason,
            },
            user=request.user,
        )
