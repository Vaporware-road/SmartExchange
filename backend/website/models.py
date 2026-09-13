"""The customer-facing website: one per exchange desk.

Deliberately split so a desk can redesign without retyping anything:

* :class:`WebsiteSite` holds *which* design and theme, plus branding and SEO.
* :class:`WebsiteSection` holds *content*, keyed by section **type** rather than
  by layout. Switching layout therefore changes which variant draws a section,
  never the words inside it.
* :class:`WebsitePublication` is a frozen resolved copy. The public page reads
  only the newest one, so an unfinished draft can never reach a visitor and a
  rollback is a row lookup rather than an undo stack.

Prices are never frozen into a publication — they are fetched live, because a
stale rate on a public page is worse than no page at all.
"""
from django.db import models
from django.utils import timezone

from accounts.scoping import AccountScopedModel, RelatedScopedManager
from accounts.storage import AccountUploadPath

from . import catalog


class WebsiteSite(AccountScopedModel):
    """One desk's website configuration. Created on first visit to the builder."""

    STATUS_DRAFT = "draft"
    STATUS_PUBLISHED = "published"
    STATUS_CHOICES = ((STATUS_DRAFT, "Draft"), (STATUS_PUBLISHED, "Published"))

    slug = models.SlugField(
        max_length=120,
        blank=True,
        help_text="Public path segment. Defaults to the account slug.",
    )
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=STATUS_DRAFT)

    layout_slug = models.CharField(max_length=60, default=catalog.DEFAULT_LAYOUT)
    theme_slug = models.CharField(max_length=60, blank=True)
    theme_overrides = models.JSONField(
        default=dict,
        blank=True,
        help_text="Owner choices layered over the theme: button/card/background style, "
        "corner, density, font pair, brand colour.",
    )

    primary_locale = models.CharField(max_length=8, default=catalog.DEFAULT_LOCALE)
    locales = models.JSONField(default=list, blank=True)

    # Branding. Blank fields fall back to setting.SiteSettings so a desk that
    # already filled in the panel does not fill the same boxes twice.
    inherit_panel_branding = models.BooleanField(default=True)
    business_name = models.JSONField(default=dict, blank=True)
    tagline = models.JSONField(default=dict, blank=True)
    logo = models.ImageField(upload_to=AccountUploadPath("website"), null=True, blank=True)
    favicon = models.ImageField(upload_to=AccountUploadPath("website"), null=True, blank=True)

    seo = models.JSONField(default=dict, blank=True)

    published_at = models.DateTimeField(null=True, blank=True)
    published_version = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Website"
        verbose_name_plural = "Websites"

    def __str__(self):
        return f"Website<{self.slug or self.account_id}>"

    def save(self, *args, **kwargs):
        if not self.theme_slug:
            self.theme_slug = catalog.layout(self.layout_slug)["default_theme"]
        if not self.locales:
            self.locales = [self.primary_locale]
        elif self.primary_locale not in self.locales:
            self.locales = [self.primary_locale, *self.locales]
        super().save(*args, **kwargs)

    @property
    def is_published(self):
        return self.status == self.STATUS_PUBLISHED and self.published_version > 0

    def latest_publication(self):
        return self.publications.order_by("-version").first()


class WebsiteSection(models.Model):
    """One block of the page. ``content`` leaves are ``{locale: value}`` maps."""

    site = models.ForeignKey(WebsiteSite, on_delete=models.CASCADE, related_name="sections")
    section_type = models.CharField(max_length=40)
    # Lets a layout carry two of the same type (two CTA bands, say) without the
    # content of one clobbering the other when the layout changes.
    key = models.CharField(max_length=40, blank=True, default="")
    order = models.PositiveSmallIntegerField(default=0)
    is_enabled = models.BooleanField(default=True)
    # Blank means "whatever the current layout draws this type with", which is
    # what keeps a layout switch visible instead of silently pinned to the old look.
    variant = models.CharField(max_length=60, blank=True, default="")
    content = models.JSONField(default=dict, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = RelatedScopedManager("site__account_id")
    all_objects = models.Manager()

    class Meta:
        ordering = ["order", "id"]
        unique_together = (("site", "section_type", "key"),)
        indexes = [models.Index(fields=["site", "order"])]

    def __str__(self):
        return f"{self.section_type}:{self.key or '-'}"

    def resolved_variant(self, layout_slug):
        if self.variant and self.variant in catalog.variants_for(self.section_type):
            return self.variant
        return catalog.default_variant(layout_slug, self.section_type)


class WebsiteAsset(models.Model):
    """An image the owner uploaded for their site."""

    ROLE_CHOICES = (
        ("image", "Image"),
        ("logo", "Logo"),
        ("hero", "Hero"),
        ("gallery", "Gallery"),
        ("og", "Social preview"),
    )

    site = models.ForeignKey(WebsiteSite, on_delete=models.CASCADE, related_name="assets")
    image = models.ImageField(upload_to=AccountUploadPath("website"))
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="image")
    alt = models.JSONField(default=dict, blank=True)
    width = models.PositiveIntegerField(default=0)
    height = models.PositiveIntegerField(default=0)
    size_bytes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = RelatedScopedManager("site__account_id")
    all_objects = models.Manager()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.image.name

    @property
    def account_id(self):
        """The owning account, for :class:`~accounts.storage.AccountUploadPath`.

        Child rows carry no ``account`` column — they are reached through their
        parent — but the upload path callable looks for one, and without it every
        desk's images would share a single guessable ``accounts/shared/`` folder.
        """
        return self.site.account_id


class WebsitePublication(models.Model):
    """A frozen, fully resolved copy of the site as published."""

    site = models.ForeignKey(WebsiteSite, on_delete=models.CASCADE, related_name="publications")
    version = models.PositiveIntegerField()
    snapshot = models.JSONField()
    published_by = models.ForeignKey(
        "accounts.CustomUser",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="website_publications",
    )
    published_at = models.DateTimeField(default=timezone.now)
    note = models.CharField(max_length=200, blank=True, default="")

    objects = RelatedScopedManager("site__account_id")
    all_objects = models.Manager()

    class Meta:
        ordering = ["-version"]
        unique_together = (("site", "version"),)

    def __str__(self):
        return f"v{self.version} of {self.site_id}"
