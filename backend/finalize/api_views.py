"""
DRF API views for finalization flows.
"""
import logging
from django.conf import settings
from django.db import transaction
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import ScopedRateThrottle

from accounts.permissions import IsSuperAdminOrManagement
from category.models import Category, PriceType
from special_price.models import SpecialPriceType, SpecialPriceHistory
from telegram_app.models import TelegramChannel
from price_publisher.services.publisher import (
    PricePublicationError,
    PricePublisherService,
)
from setting.utils import log_finalize_event, log_telegram_event

from instagram_hub.services.instagram_config import is_instagram_configured
from instagram_hub.tasks import enqueue_post_finalize_to_instagram

from .models import Finalization, FinalizedPriceHistory, SpecialPriceFinalization
from .services import ExternalAPIService
from .views import sort_gbp_price_types
from .serializers import (
    FinalizeCategoryRequestSerializer,
    FinalizeSpecialPriceRequestSerializer,
    FinalizeAllRequestSerializer,
)

logger = logging.getLogger(__name__)


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
    categories = Category.objects.prefetch_related(
        Prefetch(
            "price_types",
            queryset=PriceType.objects.prefetch_related("price_histories").select_related(
                "source_currency", "target_currency"
            ),
        )
    ).all()

    pending_by_category = []
    for category in categories:
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

    special_price_types = SpecialPriceType.objects.prefetch_related(
        Prefetch(
            "special_price_histories",
            queryset=SpecialPriceHistory.objects.order_by("-created_at"),
        )
    ).select_related("source_currency", "target_currency").all()

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
                    previous_price = str(prev_finalization.special_price_history.price)
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
        "categories": list(
            categories.values("id", "name", "slug", "description")
        ),
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
        data = _build_finalize_dashboard_data()
        return Response(data)


class FinalizeCategoryAPIView(APIView):
    """POST /api/finalize/category/<id>/ - finalize a category."""

    permission_classes = [IsAuthenticated, IsSuperAdminOrManagement]
    throttle_scope = "finalize"
    throttle_classes = [ScopedRateThrottle]

    def post(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
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

        api_sent_successfully = False
        api_results = None
        try:
            api_results = ExternalAPIService.send_finalized_prices(price_items)
            sent_count = len(api_results.get("sent", []))
            failed_count = len(api_results.get("failed", []))
            api_sent_successfully = sent_count > 0 and failed_count == 0
            log_finalize_event(
                level="INFO" if failed_count == 0 else "WARNING",
                message=f"External rates sync for category: {category.name}",
                details=f"Sent: {sent_count}, Failed: {failed_count}. Success: {api_sent_successfully}",
                user=request.user,
            )
        except Exception as exc:
            logger.exception("Error sending to external API")
            log_finalize_event(
                level="ERROR",
                message=f"External rates sync failed for category: {category.name}",
                details=str(exc),
                user=request.user,
            )

        publisher = PricePublisherService()
        message_sent = False
        image_caption = None
        publication_response = ""

        try:
            publication = publisher.publish_category_prices(
                category=category,
                price_items=price_items,
                channel=channel,
                notes=notes_text,
            )
            message_sent = publication.success
            image_caption = publication.caption
            publication_response = publication.response
        except PricePublicationError as exc:
            publication_response = str(exc)
        except Exception as exc:
            publication_response = str(exc)

        strict = getattr(settings, "FINALIZE_STRICT_TELEGRAM", False)
        if strict and not message_sent:
            return Response(
                {
                    "detail": "Telegram publication failed. Finalization was not saved (strict mode).",
                    "telegram_response": publication_response,
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

        total_prices_count = len(price_items)
        new_prices_count = len(pending_prices)
        log_finalize_event(
            level="INFO" if message_sent else "WARNING",
            message=f"Category finalized: {category.name}",
            details=f"Total: {total_prices_count}, New: {new_prices_count}. Telegram sent: {message_sent}",
            user=request.user,
        )
        if message_sent:
            log_telegram_event(
                level="INFO",
                message="Category prices published to Telegram",
                details=f"Category: {category.name}, Channel: {channel.name}",
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
                "telegram_response": publication_response,
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
            SpecialPriceHistory, id=special_price_history_id
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

        publisher = PricePublisherService()
        message_sent = False
        image_caption = None
        publication_response = ""

        try:
            publication = publisher.publish_special_price(
                special_price_type=special_price_type,
                price_history=special_price_history,
                channel=channel,
                notes=notes_text,
            )
            message_sent = publication.success
            image_caption = publication.caption
            publication_response = publication.response
        except PricePublicationError as exc:
            publication_response = str(exc)
        except Exception as exc:
            publication_response = str(exc)

        strict = getattr(settings, "FINALIZE_STRICT_TELEGRAM", False)
        if strict and not message_sent:
            return Response(
                {
                    "detail": "Telegram publication failed. Finalization was not saved (strict mode).",
                    "telegram_response": publication_response,
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

        try:
            api_results = ExternalAPIService.send_finalized_special_prices(
                [(special_price_type, special_price_history)]
            )
            sent_count = len(api_results.get("sent", []))
            failed_count = len(api_results.get("failed", []))
            log_finalize_event(
                level="INFO" if failed_count == 0 else "WARNING",
                message=f"External rates sync for special price: {special_price_type.name}",
                details=f"Sent: {sent_count}, Failed: {failed_count}",
                user=request.user,
            )
        except Exception as exc:
            log_finalize_event(
                level="ERROR",
                message=f"External rates sync failed for special price: {special_price_type.name}",
                details=str(exc),
                user=request.user,
            )

        log_finalize_event(
            level="INFO" if message_sent else "WARNING",
            message=f"Special price finalized: {special_price_type.name}",
            details=f"Price: {special_price_history.price}. Telegram sent: {message_sent}",
            user=request.user,
        )

        return Response(
            {
                "success": True,
                "finalization_id": finalization.id,
                "message_sent": message_sent,
                "telegram_response": publication_response,
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
                category = get_object_or_404(Category, id=cat_id)
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
                    SpecialPriceHistory, id=sp_id
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
                publisher = PricePublisherService()
                message_sent = False
                image_caption = None
                publication_response = ""
                try:
                    publication = publisher.publish_special_price(
                        special_price_type=special_price_type,
                        price_history=special_price_history,
                        channel=channel,
                        notes=notes_text,
                    )
                    message_sent = publication.success
                    image_caption = publication.caption
                    publication_response = publication.response
                except PricePublicationError as exc:
                    publication_response = str(exc)
                except Exception as exc:
                    publication_response = str(exc)
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
                try:
                    ExternalAPIService.send_finalized_special_prices(
                        [(special_price_type, special_price_history)]
                    )
                except Exception:
                    pass
                log_finalize_event(
                    level="INFO" if message_sent else "WARNING",
                    message=f"Special price finalized (all): {special_price_type.name}",
                    details=f"Telegram sent: {message_sent}",
                    user=request.user,
                )
                results.append({"id": sp_id, "type": "special", "success": True})
            except Exception as exc:
                logger.exception("Finalize all: special price %s failed", sp_id)
                results.append({
                    "id": sp_id,
                    "type": "special",
                    "success": False,
                    "error": str(exc) or "Unknown error",
                })

        if is_instagram_configured() and (category_ids or special_price_history_ids):
            enqueue_post_finalize_to_instagram(
                category_ids=category_ids,
                special_price_history_ids=special_price_history_ids,
                theme="dark",
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

        try:
            ExternalAPIService.send_finalized_prices(price_items)
        except Exception as exc:
            logger.exception("Finalize all: external API failed for category %s", category.id)

        publisher = PricePublisherService()
        message_sent = False
        publication_response = ""
        try:
            publication = publisher.publish_category_prices(
                category=category,
                price_items=price_items,
                channel=channel,
                notes=notes_text,
            )
            message_sent = publication.success
            publication_response = publication.response
        except PricePublicationError as exc:
            publication_response = str(exc)
        except Exception as exc:
            publication_response = str(exc)

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
                image_caption=None,
                telegram_response=publication_response or None,
                notes=notes,
            )
            for item in pending_prices:
                FinalizedPriceHistory.objects.create(
                    finalization=finalization,
                    price_history=item["price_history"],
                )

        log_finalize_event(
            level="INFO" if message_sent else "WARNING",
            message=f"Category finalized (all): {category.name}",
            details=f"New prices: {len(pending_prices)}. Telegram sent: {message_sent}",
            user=request.user,
        )
