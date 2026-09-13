"""Serving a published customer website.

The page itself is Vue. What happens here is the part Vue cannot do: putting
real ``<title>``, description, Open Graph and JSON-LD into the HTML *before*
hydration, because a crawler indexing an exchange desk never runs the bundle.
"""
import html
import json

from django.http import HttpResponse
from django.utils.html import escape

from accounts.scoping import act_as_account, resolve_public_account_id, unscoped
from MrExchangePanel.views import spa_with_head

from .models import WebsiteSite

_FALLBACK_TITLE = "Exchange rates"


def _localized(value, locale, fallback_locale):
    """One string out of a ``{locale: text}`` map, preferring ``locale``."""
    if isinstance(value, str):
        return value
    if not isinstance(value, dict) or not value:
        return ""
    for candidate in (locale, fallback_locale, ""):
        text = value.get(candidate)
        if text:
            return text
    return next((text for text in value.values() if text), "")


def _seo_head(snapshot, request):
    locale = snapshot.get("primary_locale") or "en"
    branding = snapshot.get("branding") or {}
    seo = snapshot.get("seo") or {}

    name = _localized(branding.get("business_name"), locale, locale) or _FALLBACK_TITLE
    title = _localized(seo.get("title"), locale, locale) or name
    description = _localized(seo.get("description"), locale, locale) or _localized(
        branding.get("tagline"), locale, locale
    )
    image = seo.get("og_image") or branding.get("logo") or ""
    if image and image.startswith("/"):
        image = request.build_absolute_uri(image)
    canonical = request.build_absolute_uri(request.path)

    contact = branding.get("contact") or {}
    structured = {
        "@context": "https://schema.org",
        "@type": "CurrencyConversionService",
        "name": name,
        "url": canonical,
    }
    if description:
        structured["description"] = description
    if image:
        structured["image"] = image
    if contact.get("phone"):
        structured["telephone"] = contact["phone"]
    if contact.get("address"):
        structured["address"] = contact["address"]

    parts = [
        f"<title>{escape(title)}</title>",
        f'<link rel="canonical" href="{escape(canonical)}">',
        f'<meta name="description" content="{escape(description)}">',
        f'<meta property="og:type" content="website">',
        f'<meta property="og:title" content="{escape(title)}">',
        f'<meta property="og:description" content="{escape(description)}">',
        f'<meta property="og:url" content="{escape(canonical)}">',
        f'<meta name="twitter:card" content="summary_large_image">',
    ]
    if image:
        parts.append(f'<meta property="og:image" content="{escape(image)}">')
    if seo.get("keywords"):
        parts.append(f'<meta name="keywords" content="{escape(seo["keywords"])}">')
    if branding.get("favicon"):
        parts.append(f'<link rel="icon" href="{escape(branding["favicon"])}">')
    parts.append(
        '<script type="application/ld+json">%s</script>'
        % html.escape(json.dumps(structured, ensure_ascii=False), quote=False)
    )
    return "\n".join(parts)


def public_site(request, slug=None):
    """``/site/`` and ``/site/<slug>/`` — a desk's published website."""
    with unscoped():
        account_id = resolve_public_account_id(slug)
    if account_id is None:
        return _not_found()

    with act_as_account(account_id):
        site = WebsiteSite.objects.first()
        if site is None or not site.is_published:
            return _not_found()
        publication = site.latest_publication()
    if publication is None:
        return _not_found()

    return spa_with_head(_seo_head(publication.snapshot, request))


def _not_found():
    return HttpResponse(
        "<h1>404</h1><p>No published website here.</p>",
        status=404,
        content_type="text/html",
    )
