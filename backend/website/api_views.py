"""Builder and public APIs for the customer website.

Two audiences with opposite needs share this module. The builder endpoints are
authenticated, scoped to the signed-in desk and read the *draft*. The public
endpoints are unauthenticated, name their desk with ``?account=<slug>`` like the
rest of the public surface, and read only the newest publication.
"""
import logging

from django.core.cache import cache
from django.db import transaction
from rest_framework import status
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView

from accounts.permissions import IsSuperAdminOrManagement
from accounts.scoping import act_as_account, resolve_public_account_id, unscoped
from core.prices_snapshot import build_prices_public_snapshot

from . import catalog, services
from .models import WebsiteAsset, WebsiteSection, WebsiteSite
from .serializers import (
    WebsiteAssetSerializer,
    WebsitePublicationSerializer,
    WebsiteSectionSerializer,
    WebsiteSiteSerializer,
)

logger = logging.getLogger(__name__)

PUBLIC_SITE_TTL = 60
PUBLIC_PRICES_TTL = 30
MAX_ASSET_BYTES = 6 * 1024 * 1024
ALLOWED_ASSET_TYPES = ("image/png", "image/jpeg", "image/webp", "image/svg+xml", "image/gif")


def _error(message, code="validation_error", http_status=status.HTTP_400_BAD_REQUEST):
    return Response({"error": True, "message": message, "code": code}, status=http_status)


class BuilderView(APIView):
    """Shared base: every builder endpoint works on the caller's own site."""

    permission_classes = [IsSuperAdminOrManagement]

    def get_site(self):
        return services.get_or_create_site()

    def site_payload(self, site):
        return WebsiteSiteSerializer(site).data


class WebsiteSiteAPIView(BuilderView):
    """``GET``/``PATCH /api/website/site/`` — the desk's one site."""

    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get(self, request):
        site = self.get_site()
        return Response(self.site_payload(site))

    def patch(self, request):
        site = self.get_site()
        serializer = WebsiteSiteSerializer(site, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        services.invalidate_public_cache(site.account_id)
        return Response(self.site_payload(serializer.instance))


class WebsiteLayoutAPIView(BuilderView):
    """``POST /api/website/layout/`` — switch design without losing content."""

    def post(self, request):
        layout_slug = str(request.data.get("layout_slug") or "")
        if not catalog.is_layout(layout_slug):
            return _error(f"Unknown layout '{layout_slug}'.")
        site = self.get_site()
        services.apply_layout(site, layout_slug)
        services.invalidate_public_cache(site.account_id)
        return Response(self.site_payload(site))


class WebsiteSectionListAPIView(BuilderView):
    def get(self, request):
        site = self.get_site()
        sections = site.sections.all()
        return Response(
            WebsiteSectionSerializer(
                sections, many=True, context={"layout_slug": site.layout_slug}
            ).data
        )

    def post(self, request):
        site = self.get_site()
        serializer = WebsiteSectionSerializer(
            data=request.data, context={"layout_slug": site.layout_slug}
        )
        serializer.is_valid(raise_exception=True)
        section_type = serializer.validated_data["section_type"]
        spec = catalog.sections()[section_type]
        key = serializer.validated_data.get("key", "")
        if spec.get("singleton") and site.sections.filter(section_type=section_type).exists():
            return _error(f"'{section_type}' can only appear once.", code="duplicate_section")
        if site.sections.filter(section_type=section_type, key=key).exists():
            return _error("That section already exists.", code="duplicate_section")
        content = serializer.validated_data.get("content") or catalog.field_defaults(section_type)
        serializer.save(
            site=site,
            content=content,
            order=site.sections.count(),
        )
        services.invalidate_public_cache(site.account_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class WebsiteSectionDetailAPIView(BuilderView):
    def get_object(self, site, pk):
        return site.sections.filter(pk=pk).first()

    def patch(self, request, pk):
        site = self.get_site()
        section = self.get_object(site, pk)
        if section is None:
            return _error("Section not found.", code="not_found", http_status=status.HTTP_404_NOT_FOUND)
        serializer = WebsiteSectionSerializer(
            section, data=request.data, partial=True, context={"layout_slug": site.layout_slug}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        services.invalidate_public_cache(site.account_id)
        return Response(serializer.data)

    def delete(self, request, pk):
        site = self.get_site()
        section = self.get_object(site, pk)
        if section is None:
            return _error("Section not found.", code="not_found", http_status=status.HTTP_404_NOT_FOUND)
        section.delete()
        services.invalidate_public_cache(site.account_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class WebsiteSectionReorderAPIView(BuilderView):
    """``POST /api/website/sections/reorder/`` with ``{"order": [id, id, ...]}``."""

    def post(self, request):
        ids = request.data.get("order")
        if not isinstance(ids, list):
            return _error("Expected an 'order' list of section ids.")
        site = self.get_site()
        sections = {s.id: s for s in site.sections.all()}
        updated = []
        for position, raw_id in enumerate(ids):
            section = sections.get(raw_id if isinstance(raw_id, int) else _to_int(raw_id))
            if section is None:
                continue
            section.order = position
            updated.append(section)
        with transaction.atomic():
            for section in updated:
                section.save(update_fields=["order"])
        services.invalidate_public_cache(site.account_id)
        return Response(
            WebsiteSectionSerializer(
                site.sections.all(), many=True, context={"layout_slug": site.layout_slug}
            ).data
        )


def _to_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


class WebsiteAssetAPIView(BuilderView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get(self, request):
        site = self.get_site()
        return Response(WebsiteAssetSerializer(site.assets.all(), many=True).data)

    def post(self, request):
        site = self.get_site()
        upload = request.FILES.get("image")
        if upload is None:
            return _error("No image supplied.")
        if upload.size > MAX_ASSET_BYTES:
            return _error("Image is larger than 6 MB.", code="file_too_large")
        content_type = getattr(upload, "content_type", "")
        if content_type and content_type not in ALLOWED_ASSET_TYPES:
            return _error("Unsupported image type.", code="unsupported_media_type")

        asset = WebsiteAsset(
            site=site,
            image=upload,
            role=request.data.get("role") or "image",
            size_bytes=upload.size,
        )
        asset.save()
        # Dimensions are a nicety for the picker; a format Pillow will not open
        # (SVG, most often) is still a perfectly good asset.
        try:
            asset.width, asset.height = asset.image.width, asset.image.height
            asset.save(update_fields=["width", "height"])
        except Exception:
            logger.debug("Could not read dimensions for website asset %s", asset.pk)
        return Response(WebsiteAssetSerializer(asset).data, status=status.HTTP_201_CREATED)


class WebsiteAssetDetailAPIView(BuilderView):
    def delete(self, request, pk):
        site = self.get_site()
        asset = site.assets.filter(pk=pk).first()
        if asset is None:
            return _error("Asset not found.", code="not_found", http_status=status.HTTP_404_NOT_FOUND)
        asset.image.delete(save=False)
        asset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WebsitePreviewAPIView(BuilderView):
    """The resolved **draft** — what the builder canvas draws."""

    def get(self, request):
        site = self.get_site()
        return Response(services.build_site_snapshot(site))


class WebsitePublishAPIView(BuilderView):
    def post(self, request):
        site = self.get_site()
        publication = services.publish(site, request.user, str(request.data.get("note") or ""))
        return Response(
            {
                "site": self.site_payload(site),
                "publication": WebsitePublicationSerializer(publication).data,
            }
        )


class WebsiteUnpublishAPIView(BuilderView):
    def post(self, request):
        site = self.get_site()
        services.unpublish(site)
        return Response(self.site_payload(site))


class WebsitePublicationListAPIView(BuilderView):
    def get(self, request):
        site = self.get_site()
        return Response(WebsitePublicationSerializer(site.publications.all()[:50], many=True).data)


class WebsitePublicationRestoreAPIView(BuilderView):
    def post(self, request, version):
        site = self.get_site()
        try:
            publication = services.restore(site, version, request.user)
        except ValueError as exc:
            return _error(str(exc), code="not_found", http_status=status.HTTP_404_NOT_FOUND)
        return Response(
            {
                "site": self.site_payload(site),
                "publication": WebsitePublicationSerializer(publication).data,
            }
        )


class PublicWebsiteAPIView(APIView):
    """``GET /api/public/website/?account=<slug>`` — the published site.

    Reads the frozen publication, never the draft, so an owner mid-edit never
    leaks a half-written page to visitors.
    """

    permission_classes = [AllowAny]
    authentication_classes = []
    throttle_scope = "public_site"
    throttle_classes = [ScopedRateThrottle]

    def get(self, request):
        slug = request.query_params.get("account")
        with unscoped():
            account_id = resolve_public_account_id(slug)
        if account_id is None:
            return _error("No such website.", code="not_found", http_status=status.HTTP_404_NOT_FOUND)

        cache_key = services.public_cache_key(account_id)
        # Every cache touch runs as the desk, because the key function
        # namespaces by the account in context and the builder invalidates from
        # a signed-in request. Read and write have to agree on that namespace.
        with act_as_account(account_id):
            cached = cache.get(cache_key)
            if cached is not None:
                return Response(cached)

            site = WebsiteSite.objects.first()
            if site is None or not site.is_published:
                return _error(
                    "This website is not published yet.",
                    code="not_found",
                    http_status=status.HTTP_404_NOT_FOUND,
                )
            publication = site.latest_publication()
            if publication is None:
                return _error(
                    "This website is not published yet.",
                    code="not_found",
                    http_status=status.HTTP_404_NOT_FOUND,
                )

            payload = {
                "version": publication.version,
                "published_at": publication.published_at,
                **publication.snapshot,
            }
            cache.set(cache_key, payload, PUBLIC_SITE_TTL)
        return Response(payload)


class PublicWebsitePricesAPIView(APIView):
    """``GET /api/public/website/prices/?account=<slug>`` — finalized rates only."""

    permission_classes = [AllowAny]
    authentication_classes = []
    throttle_scope = "public_prices"
    throttle_classes = [ScopedRateThrottle]

    def get(self, request):
        slug = request.query_params.get("account")
        with unscoped():
            account_id = resolve_public_account_id(slug)
        if account_id is None:
            return Response({"generated_at": None, "categories": [], "special_prices": []})

        cache_key = f"website:prices:{account_id}"
        with act_as_account(account_id):
            cached = cache.get(cache_key)
            if cached is not None:
                return Response(cached)

            payload = build_prices_public_snapshot(finalized_only=True)
            cache.set(cache_key, payload, PUBLIC_PRICES_TTL)
        return Response(payload)
