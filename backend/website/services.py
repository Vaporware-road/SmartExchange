"""Site provisioning, layout switching, and publishing.

The rules that make "change the design without losing your content" true live
here rather than in the views, because the builder, the seeder and the tests all
need the same answers.
"""
from django.db import transaction
from django.utils import timezone
from django.utils.text import slugify

from accounts.models import Account
from accounts.scoping import UNSCOPED, act_as_account, get_current_account_id
from setting.models import SiteSettings

from . import catalog
from .models import WebsitePublication, WebsiteSection, WebsiteSite


def current_account_id():
    account_id = get_current_account_id()
    if account_id in (None, UNSCOPED):
        return None
    return account_id


@transaction.atomic
def get_or_create_site(account_id=None):
    """The account's site, seeded with its layout's starter sections.

    Created lazily on first use instead of by a signal on signup: most desks
    never open the builder, and an empty row per account would be a migration
    to write and a row to keep in step for no gain.
    """
    account_id = account_id or current_account_id()
    if account_id is None:
        raise ValueError("No account in context; cannot resolve a website.")

    site = WebsiteSite.all_objects.filter(account_id=account_id).first()
    if site is not None:
        return site

    account = Account.objects.filter(pk=account_id).first()
    settings_row = SiteSettings.load(account_id)
    site = WebsiteSite(
        account_id=account_id,
        slug=(account.slug if account else "") or slugify(str(account_id)),
        layout_slug=catalog.DEFAULT_LAYOUT,
    )
    if settings_row.site_name:
        site.business_name = {site.primary_locale: settings_row.site_name}
    if settings_row.tagline:
        site.tagline = {site.primary_locale: settings_row.tagline}
    site.save()
    seed_sections(site)
    return site


def seed_sections(site):
    """Create any starter section the layout expects and the site lacks."""
    manifest = catalog.layout(site.layout_slug)
    existing = {s.section_type for s in site.sections.all()}
    order = site.sections.count()
    created = []
    for section_type in manifest["starter"]:
        if section_type in existing:
            continue
        created.append(
            WebsiteSection(
                site=site,
                section_type=section_type,
                order=order,
                is_enabled=True,
                content=catalog.field_defaults(section_type),
            )
        )
        order += 1
    if created:
        WebsiteSection.objects.bulk_create(created)
        normalize_order(site)
    return created


def normalize_order(site):
    """Keep the header first and the footer last, whatever else moved.

    Sections seeded by a layout switch are appended, which would otherwise drop
    a new block below the footer in the builder's list — technically harmless,
    since the chrome pulls those two out anyway, but it reads as a bug.
    """
    rank = {"header": -1, "footer": 1}
    ordered = sorted(
        site.sections.all(),
        key=lambda section: (rank.get(section.section_type, 0), section.order, section.id),
    )
    for position, section in enumerate(ordered):
        if section.order != position:
            section.order = position
            section.save(update_fields=["order"])


@transaction.atomic
def apply_layout(site, layout_slug):
    """Switch design, keeping every word the owner has written.

    Three things happen, and only these three: the layout slug changes, the
    theme follows *only* if the owner never chose one, and any variant pinned
    to a look the new layout cannot draw is released back to the layout's
    default. Content is never touched.
    """
    if not catalog.is_layout(layout_slug):
        raise ValueError(f"Unknown layout: {layout_slug}")

    previous = catalog.layout(site.layout_slug)
    site.layout_slug = layout_slug
    manifest = catalog.layout(layout_slug)

    # A theme the owner never moved off is the previous layout's suggestion,
    # not a choice, so the new layout gets to make its own suggestion.
    if site.theme_slug == previous["default_theme"]:
        site.theme_slug = manifest["default_theme"]
    site.save()

    supported = set(manifest["supports"])
    for section in site.sections.all():
        if section.section_type not in supported and section.is_enabled:
            # Kept, not deleted: switching back must bring it and its content home.
            section.is_enabled = False
            section.save(update_fields=["is_enabled"])
        elif section.variant and section.variant not in catalog.variants_for(section.section_type):
            section.variant = ""
            section.save(update_fields=["variant"])

    seed_sections(site)
    return site


def resolve_branding(site):
    """Site branding, falling back to the panel's own settings where blank."""
    settings_row = SiteSettings.load(site.account_id)
    inherit = site.inherit_panel_branding

    def pick(localized, fallback):
        if localized:
            return localized
        return {site.primary_locale: fallback} if (inherit and fallback) else {}

    logo = site.logo.url if site.logo else None
    if logo is None and inherit and settings_row.logo:
        logo = settings_row.logo.url
    favicon = site.favicon.url if site.favicon else None
    if favicon is None and inherit and settings_row.favicon:
        favicon = settings_row.favicon.url

    return {
        "business_name": pick(site.business_name, settings_row.site_name),
        "tagline": pick(site.tagline, settings_row.tagline),
        "logo": logo,
        "favicon": favicon,
        "contact": {
            "phone": settings_row.support_phone if inherit else "",
            "phone_2": settings_row.support_phone_2 if inherit else "",
            "phone_3": settings_row.support_phone_3 if inherit else "",
            "email": settings_row.support_email if inherit else "",
            "address": settings_row.address if inherit else "",
            "map_url": settings_row.office_map_url if inherit else "",
            "hours": settings_row.business_hours if inherit else "",
        },
        "socials": {
            "telegram": settings_row.telegram_link,
            "instagram": settings_row.instagram_link,
            "twitter": settings_row.twitter_link,
            "linkedin": settings_row.linkedin_link,
        },
    }


def build_site_snapshot(site):
    """The resolved site the renderer draws, draft or published alike.

    Content stays in its ``{locale: value}`` form rather than being flattened to
    one language: a publication then serves every locale the owner enabled, so
    a visitor switching language costs nothing and the cache stays a single entry.
    """
    manifest = catalog.layout(site.layout_slug)
    theme = catalog.resolve_tokens(site.theme_slug, site.theme_overrides)

    sections = []
    for section in site.sections.all():
        if not section.is_enabled or section.section_type not in manifest["supports"]:
            continue
        sections.append(
            {
                "id": section.id,
                "type": section.section_type,
                "key": section.key,
                "variant": section.resolved_variant(site.layout_slug),
                "content": section.content or {},
            }
        )

    return {
        "slug": site.slug,
        "layout": site.layout_slug,
        "chrome": manifest["chrome"],
        "theme": {"slug": site.theme_slug, **theme},
        "primary_locale": site.primary_locale,
        "locales": site.locales or [site.primary_locale],
        "branding": resolve_branding(site),
        "seo": site.seo or {},
        "sections": sections,
        "generated_at": timezone.now().isoformat(),
    }


@transaction.atomic
def publish(site, user=None, note=""):
    """Freeze the draft as a new numbered publication and go live."""
    version = site.published_version + 1
    publication = WebsitePublication.objects.create(
        site=site,
        version=version,
        snapshot=build_site_snapshot(site),
        published_by=user if getattr(user, "pk", None) else None,
        note=note[:200],
    )
    site.status = WebsiteSite.STATUS_PUBLISHED
    site.published_version = version
    site.published_at = publication.published_at
    site.save(update_fields=["status", "published_version", "published_at", "updated_at"])
    invalidate_public_cache(site.account_id)
    return publication


@transaction.atomic
def unpublish(site):
    site.status = WebsiteSite.STATUS_DRAFT
    site.save(update_fields=["status", "updated_at"])
    invalidate_public_cache(site.account_id)
    return site


@transaction.atomic
def restore(site, version, user=None):
    """Re-publish an older snapshot as a new version.

    Forward-only: the history stays append-only, so "what was live at 4pm" has
    one answer even after someone rolls back.
    """
    source = site.publications.filter(version=version).first()
    if source is None:
        raise ValueError(f"No publication v{version}")
    new_version = site.published_version + 1
    publication = WebsitePublication.objects.create(
        site=site,
        version=new_version,
        snapshot=source.snapshot,
        published_by=user if getattr(user, "pk", None) else None,
        note=f"restored from v{version}",
    )
    site.status = WebsiteSite.STATUS_PUBLISHED
    site.published_version = new_version
    site.published_at = publication.published_at
    site.save(update_fields=["status", "published_version", "published_at", "updated_at"])
    invalidate_public_cache(site.account_id)
    return publication


def public_cache_key(account_id):
    return f"website:public:{account_id}"


def invalidate_public_cache(account_id):
    """Drop a desk's cached public page.

    Pinned to the account on purpose: ``settings.CACHES`` namespaces every key
    by whoever is in context (``accounts.cache.account_scoped_key``), so a
    delete issued from the signed-in builder would land in the *staff*
    namespace and quietly miss the entry an anonymous visitor's request wrote.
    """
    from django.core.cache import cache

    with act_as_account(account_id):
        cache.delete(public_cache_key(account_id))
