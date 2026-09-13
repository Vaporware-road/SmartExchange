"""Serializers for the website builder.

Section content is free-form JSON on the way in, so it is validated against
``catalog/sections.json`` here — an unknown key, an over-long list or an
out-of-range number is rejected rather than stored and then silently ignored
by a renderer that has no field for it.
"""
from rest_framework import serializers

from . import catalog
from .models import WebsiteAsset, WebsitePublication, WebsiteSection, WebsiteSite

MAX_TEXT = 4000
MAX_LOCALES = 7


def _clean_localized(value, field_key):
    """A ``{locale: text}`` map, or a bare string promoted to one."""
    if value in (None, ""):
        return {}
    if isinstance(value, str):
        return {"": value[:MAX_TEXT]}
    if not isinstance(value, dict):
        raise serializers.ValidationError(f"'{field_key}' must be text or a per-locale map.")
    cleaned = {}
    for locale, text in list(value.items())[:MAX_LOCALES]:
        if not isinstance(locale, str) or len(locale) > 8:
            raise serializers.ValidationError(f"'{field_key}' has an invalid locale key.")
        if text is None:
            continue
        if not isinstance(text, str):
            raise serializers.ValidationError(f"'{field_key}' values must be text.")
        cleaned[locale] = text[:MAX_TEXT]
    return cleaned


def _clean_scalar(field, value):
    kind = field["type"]
    key = field["key"]

    if kind in ("text", "textarea"):
        if field.get("localized"):
            return _clean_localized(value, key)
        return str(value or "")[:MAX_TEXT]
    if kind in ("url", "icon"):
        return str(value or "")[:500]
    if kind == "bool":
        return bool(value)
    if kind == "number":
        try:
            number = int(value)
        except (TypeError, ValueError):
            number = field.get("default", 0)
        if "min" in field:
            number = max(number, field["min"])
        if "max" in field:
            number = min(number, field["max"])
        return number
    if kind == "select":
        options = field.get("options", [])
        return value if value in options else field.get("default", options[0] if options else "")
    if kind == "image":
        return str(value or "")[:500]
    if kind in ("category_picker", "price_type_picker"):
        if not isinstance(value, list):
            return []
        ids = []
        for item in value[:100]:
            try:
                ids.append(int(item))
            except (TypeError, ValueError):
                continue
        return ids
    raise serializers.ValidationError(f"Unsupported field type '{kind}' on '{key}'.")


def clean_content(section_type, content):
    """Content narrowed to the fields this section type actually declares."""
    spec = catalog.sections().get(section_type)
    if spec is None:
        raise serializers.ValidationError(f"Unknown section type '{section_type}'.")
    if content is None:
        content = {}
    if not isinstance(content, dict):
        raise serializers.ValidationError("Section content must be an object.")

    cleaned = {}
    for field in spec["fields"]:
        key = field["key"]
        if key not in content:
            if "default" in field:
                cleaned[key] = field["default"]
            continue
        if field["type"] == "list":
            cleaned[key] = _clean_list(field, content[key])
        else:
            cleaned[key] = _clean_scalar(field, content[key])
    return cleaned


def _clean_list(field, value):
    if not isinstance(value, list):
        return []
    limit = field.get("max", 12)
    rows = []
    for row in value[:limit]:
        if not isinstance(row, dict):
            continue
        cleaned_row = {}
        for sub in field["fields"]:
            key = sub["key"]
            if key not in row:
                continue
            if sub["type"] == "list":
                cleaned_row[key] = _clean_list(sub, row[key])
            else:
                cleaned_row[key] = _clean_scalar(sub, row[key])
        rows.append(cleaned_row)
    return rows


class WebsiteSectionSerializer(serializers.ModelSerializer):
    resolved_variant = serializers.SerializerMethodField()

    class Meta:
        model = WebsiteSection
        fields = [
            "id",
            "section_type",
            "key",
            "order",
            "is_enabled",
            "variant",
            "resolved_variant",
            "content",
            "updated_at",
        ]
        read_only_fields = ["id", "updated_at", "resolved_variant"]

    def get_resolved_variant(self, obj):
        layout_slug = self.context.get("layout_slug") or obj.site.layout_slug
        return obj.resolved_variant(layout_slug)

    def validate_section_type(self, value):
        if not catalog.is_section_type(value):
            raise serializers.ValidationError(f"Unknown section type '{value}'.")
        return value

    def validate(self, attrs):
        section_type = attrs.get("section_type") or getattr(self.instance, "section_type", None)
        variant = attrs.get("variant", None)
        if variant:
            if variant not in catalog.variants_for(section_type):
                raise serializers.ValidationError(
                    {"variant": f"'{variant}' is not a variant of '{section_type}'."}
                )
        if "content" in attrs:
            attrs["content"] = clean_content(section_type, attrs["content"])
        return attrs


class WebsiteAssetSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = WebsiteAsset
        fields = ["id", "url", "role", "alt", "width", "height", "size_bytes", "created_at"]
        read_only_fields = ["id", "url", "width", "height", "size_bytes", "created_at"]

    def get_url(self, obj):
        return obj.image.url if obj.image else None

    def validate_alt(self, value):
        return _clean_localized(value, "alt")


class WebsitePublicationSerializer(serializers.ModelSerializer):
    published_by_name = serializers.SerializerMethodField()

    class Meta:
        model = WebsitePublication
        fields = ["version", "published_at", "note", "published_by_name"]

    def get_published_by_name(self, obj):
        user = obj.published_by
        if user is None:
            return ""
        return user.full_name or user.username


class WebsiteSiteSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    favicon_url = serializers.SerializerMethodField()
    public_url = serializers.SerializerMethodField()

    class Meta:
        model = WebsiteSite
        fields = [
            "slug",
            "status",
            "layout_slug",
            "theme_slug",
            "theme_overrides",
            "primary_locale",
            "locales",
            "inherit_panel_branding",
            "business_name",
            "tagline",
            "logo",
            "logo_url",
            "favicon",
            "favicon_url",
            "seo",
            "published_at",
            "published_version",
            "public_url",
            "updated_at",
        ]
        read_only_fields = ["slug", "status", "published_at", "published_version", "updated_at"]
        extra_kwargs = {"logo": {"write_only": True}, "favicon": {"write_only": True}}

    def get_logo_url(self, obj):
        return obj.logo.url if obj.logo else None

    def get_favicon_url(self, obj):
        return obj.favicon.url if obj.favicon else None

    def get_public_url(self, obj):
        return f"/site/{obj.slug}/" if obj.slug else "/site/"

    def validate_layout_slug(self, value):
        if not catalog.is_layout(value):
            raise serializers.ValidationError(f"Unknown layout '{value}'.")
        return value

    def validate_theme_slug(self, value):
        if value and not catalog.is_theme(value):
            raise serializers.ValidationError(f"Unknown theme '{value}'.")
        return value

    def validate_theme_overrides(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError("Theme overrides must be an object.")
        style_catalog = catalog.styles()
        cleaned = {}
        for group in catalog.STYLE_GROUPS:
            if group not in value:
                continue
            choice = value[group]
            if choice in style_catalog.get(group, {}):
                cleaned[group] = choice
        brand = str(value.get("brand_color") or "").strip()
        if brand:
            if not _is_hex_color(brand):
                raise serializers.ValidationError({"brand_color": "Expected a hex colour."})
            cleaned["brand_color"] = brand
        return cleaned

    def validate_business_name(self, value):
        return _clean_localized(value, "business_name")

    def validate_tagline(self, value):
        return _clean_localized(value, "tagline")

    def validate_locales(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Locales must be a list.")
        cleaned = []
        for locale in value[:MAX_LOCALES]:
            if isinstance(locale, str) and 1 < len(locale) <= 8 and locale not in cleaned:
                cleaned.append(locale)
        return cleaned or [catalog.DEFAULT_LOCALE]

    def validate_seo(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError("SEO must be an object.")
        return {
            "title": _clean_localized(value.get("title"), "seo.title"),
            "description": _clean_localized(value.get("description"), "seo.description"),
            "keywords": str(value.get("keywords") or "")[:500],
            "og_image": str(value.get("og_image") or "")[:500],
        }


def _is_hex_color(value):
    if not value.startswith("#"):
        return False
    body = value[1:]
    return len(body) in (3, 6) and all(ch in "0123456789abcdefABCDEF" for ch in body)
