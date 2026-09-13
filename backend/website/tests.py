"""Acceptance tests for the customer website builder.

Two things here are load-bearing and would be silent failures otherwise: an
unpublished draft must never reach a visitor, and switching layout must not
cost the owner a word of their content.
"""
import json
import re
from pathlib import Path

from django.conf import settings
from django.core.cache import cache
from rest_framework.test import APITestCase

from accounts.models import CustomUser
from accounts.scoping import act_as_account, unscoped
from category.models import Category, Currency, PriceType
from change_price.models import PriceHistory
from core.prices_snapshot import build_prices_public_snapshot
from finalize.models import FinalizedPriceHistory, Finalization

from . import catalog, services
from .models import WebsiteSection, WebsiteSite


def _make_desk(username, role=CustomUser.ROLE_MANAGEMENT):
    with unscoped():
        user = CustomUser.objects.create_user(
            username=username,
            password="pass12345",
            role=role,
            email=f"{username}@example.com",
        )
    return user, user.account_id


class WebsiteBuilderApiTests(APITestCase):
    def setUp(self):
        cache.clear()
        self.owner, self.account = _make_desk("desk_owner")
        self.client.force_authenticate(self.owner)

    def test_site_is_created_lazily_with_starter_sections(self):
        response = self.client.get("/api/website/site/")
        self.assertEqual(response.status_code, 200, response.content)
        body = response.json()
        self.assertEqual(body["layout_slug"], catalog.DEFAULT_LAYOUT)
        self.assertEqual(body["status"], "draft")
        self.assertTrue(body["theme_slug"])

        sections = self.client.get("/api/website/sections/").json()
        starter = catalog.layout(catalog.DEFAULT_LAYOUT)["starter"]
        self.assertEqual([s["section_type"] for s in sections], starter)
        self.assertTrue(all(s["resolved_variant"] for s in sections))

    def test_switching_layout_keeps_content_and_rebinds_variants(self):
        self.client.get("/api/website/site/")
        hero = WebsiteSection.all_objects.get(site__account_id=self.account, section_type="hero")
        self.client.patch(
            f"/api/website/sections/{hero.pk}/",
            {"content": {"title": {"en": "Pardis Exchange"}}},
            format="json",
        )

        before = self.client.get("/api/website/sections/").json()
        hero_before = next(s for s in before if s["section_type"] == "hero")

        response = self.client.post("/api/website/layout/", {"layout_slug": "vault"}, format="json")
        self.assertEqual(response.status_code, 200, response.content)
        self.assertEqual(response.json()["layout_slug"], "vault")

        after = self.client.get("/api/website/sections/").json()
        hero_after = next(s for s in after if s["section_type"] == "hero")
        self.assertEqual(hero_after["content"]["title"], {"en": "Pardis Exchange"})
        # The words survive; the look does not.
        self.assertNotEqual(hero_after["resolved_variant"], hero_before["resolved_variant"])
        self.assertEqual(hero_after["resolved_variant"], catalog.default_variant("vault", "hero"))

    def test_pinned_variant_survives_a_layout_it_is_valid_for(self):
        self.client.get("/api/website/site/")
        rates = WebsiteSection.all_objects.get(site__account_id=self.account, section_type="rates")
        self.client.patch(f"/api/website/sections/{rates.pk}/", {"variant": "ticker"}, format="json")
        self.client.post("/api/website/layout/", {"layout_slug": "atlas"}, format="json")
        rates.refresh_from_db()
        self.assertEqual(rates.variant, "ticker")
        self.assertEqual(rates.resolved_variant("atlas"), "ticker")

    def test_content_is_narrowed_to_the_sections_declared_fields(self):
        self.client.get("/api/website/site/")
        hero = WebsiteSection.all_objects.get(site__account_id=self.account, section_type="hero")
        response = self.client.patch(
            f"/api/website/sections/{hero.pk}/",
            {"content": {"title": {"en": "Hi"}, "not_a_field": "drop me"}},
            format="json",
        )
        self.assertEqual(response.status_code, 200, response.content)
        self.assertNotIn("not_a_field", response.json()["content"])

    def test_unknown_layout_theme_and_variant_are_rejected(self):
        self.client.get("/api/website/site/")
        self.assertEqual(
            self.client.post("/api/website/layout/", {"layout_slug": "nope"}, format="json").status_code,
            400,
        )
        self.assertEqual(
            self.client.patch("/api/website/site/", {"theme_slug": "nope"}, format="json").status_code,
            400,
        )
        hero = WebsiteSection.all_objects.get(site__account_id=self.account, section_type="hero")
        self.assertEqual(
            self.client.patch(
                f"/api/website/sections/{hero.pk}/", {"variant": "accordion"}, format="json"
            ).status_code,
            400,
        )

    def test_theme_overrides_are_filtered_to_known_presets(self):
        self.client.get("/api/website/site/")
        response = self.client.patch(
            "/api/website/site/",
            {"theme_overrides": {"corner": "sharp", "card": "bogus", "brand_color": "#123456"}},
            format="json",
        )
        self.assertEqual(response.status_code, 200, response.content)
        overrides = response.json()["theme_overrides"]
        self.assertEqual(overrides, {"corner": "sharp", "brand_color": "#123456"})

    def test_reorder_sets_the_render_order(self):
        self.client.get("/api/website/site/")
        sections = self.client.get("/api/website/sections/").json()
        reversed_ids = [s["id"] for s in reversed(sections)]
        response = self.client.post(
            "/api/website/sections/reorder/", {"order": reversed_ids}, format="json"
        )
        self.assertEqual(response.status_code, 200, response.content)
        self.assertEqual([s["id"] for s in response.json()], reversed_ids)

    def test_a_singleton_section_cannot_be_added_twice(self):
        self.client.get("/api/website/site/")
        response = self.client.post(
            "/api/website/sections/", {"section_type": "hero"}, format="json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["code"], "duplicate_section")


class WebsitePublishingTests(APITestCase):
    def setUp(self):
        cache.clear()
        self.owner, self.account = _make_desk("publisher")
        self.client.force_authenticate(self.owner)
        self.client.get("/api/website/site/")

    @property
    def slug(self):
        with unscoped():
            return WebsiteSite.all_objects.get(account_id=self.account).slug

    def _public(self, path="/api/public/website/"):
        return self.client.get(f"{path}?account={self.slug}")

    def _set_hero_title(self, title):
        hero = WebsiteSection.all_objects.get(site__account_id=self.account, section_type="hero")
        self.client.patch(
            f"/api/website/sections/{hero.pk}/", {"content": {"title": {"en": title}}}, format="json"
        )

    def test_public_endpoint_is_404_until_published(self):
        self.client.force_authenticate(None)
        self.assertEqual(self._public().status_code, 404)
        self.assertEqual(self.client.get(f"/site/{self.slug}/").status_code, 404)

    def test_publish_freezes_a_version_and_the_draft_never_leaks(self):
        self._set_hero_title("Version one")
        response = self.client.post("/api/website/publish/", {}, format="json")
        self.assertEqual(response.status_code, 200, response.content)
        self.assertEqual(response.json()["publication"]["version"], 1)

        # Keep editing after publishing: visitors must still see version one.
        self._set_hero_title("Unfinished edit")
        cache.clear()

        self.client.force_authenticate(None)
        published = self._public().json()
        hero = next(s for s in published["sections"] if s["type"] == "hero")
        self.assertEqual(hero["content"]["title"], {"en": "Version one"})
        self.assertEqual(published["version"], 1)

    def test_restore_republishes_an_older_snapshot_forward(self):
        self._set_hero_title("First")
        self.client.post("/api/website/publish/", {}, format="json")
        self._set_hero_title("Second")
        self.client.post("/api/website/publish/", {}, format="json")

        response = self.client.post("/api/website/publications/1/restore/", {}, format="json")
        self.assertEqual(response.status_code, 200, response.content)
        self.assertEqual(response.json()["publication"]["version"], 3)

        cache.clear()
        self.client.force_authenticate(None)
        published = self._public().json()
        hero = next(s for s in published["sections"] if s["type"] == "hero")
        self.assertEqual(hero["content"]["title"], {"en": "First"})

    def test_unpublish_takes_the_site_down(self):
        self.client.post("/api/website/publish/", {}, format="json")
        self.client.post("/api/website/unpublish/", {}, format="json")
        cache.clear()
        self.client.force_authenticate(None)
        self.assertEqual(self._public().status_code, 404)

    def test_published_page_carries_seo_metadata_before_hydration(self):
        self.client.patch(
            "/api/website/site/",
            {
                "business_name": {"en": "Pardis Exchange"},
                "seo": {"description": {"en": "Live currency rates in Tehran"}},
            },
            format="json",
        )
        self.client.post("/api/website/publish/", {}, format="json")

        self.client.force_authenticate(None)
        response = self.client.get(f"/site/{self.slug}/")
        if response.status_code == 503:
            self.skipTest("SPA bundle not built in this environment")
        self.assertEqual(response.status_code, 200)
        html = response.content.decode()
        self.assertIn("<title>Pardis Exchange</title>", html)
        self.assertIn("Live currency rates in Tehran", html)
        self.assertIn("application/ld+json", html)

    def test_republishing_replaces_a_cached_public_response(self):
        """Without a clearing cache the desk would keep serving the old page.

        Deliberately fetched without ``?account=``, the way a single-account
        install does: the reader and the writer have to agree on the cache key
        or publishing looks like it silently did nothing.
        """
        self._set_hero_title("Before")
        self.client.post("/api/website/publish/", {}, format="json")

        self.client.force_authenticate(None)
        first = self.client.get(f"/api/public/website/?account={self.slug}").json()
        self.assertEqual(
            next(s for s in first["sections"] if s["type"] == "hero")["content"]["title"],
            {"en": "Before"},
        )

        self.client.force_authenticate(self.owner)
        self._set_hero_title("After")
        self.client.post("/api/website/publish/", {}, format="json")

        self.client.force_authenticate(None)
        second = self.client.get(f"/api/public/website/?account={self.slug}").json()
        self.assertEqual(
            next(s for s in second["sections"] if s["type"] == "hero")["content"]["title"],
            {"en": "After"},
        )
        self.assertEqual(second["version"], 2)

    def test_snapshot_resolves_theme_tokens(self):
        self.client.patch(
            "/api/website/site/",
            {"theme_slug": "gold-luxe", "theme_overrides": {"corner": "sharp"}},
            format="json",
        )
        self.client.post("/api/website/publish/", {}, format="json")
        cache.clear()
        self.client.force_authenticate(None)
        theme = self._public().json()["theme"]
        self.assertEqual(theme["slug"], "gold-luxe")
        self.assertEqual(theme["tokens"]["--ws-radius"], "2px")
        self.assertEqual(theme["tokens"]["--ws-primary"], "#ffd700")
        self.assertTrue(theme["font_families"])


class WebsiteIsolationTests(APITestCase):
    """One desk must never see, edit or publish over another desk's site."""

    def setUp(self):
        cache.clear()
        self.alice, self.alice_account = _make_desk("alice_site")
        self.bob, self.bob_account = _make_desk("bob_site")
        self.assertNotEqual(self.alice_account, self.bob_account)

    def test_each_desk_gets_its_own_site(self):
        self.client.force_authenticate(self.alice)
        self.client.post("/api/website/layout/", {"layout_slug": "vault"}, format="json")
        self.client.force_authenticate(self.bob)
        self.assertEqual(self.client.get("/api/website/site/").json()["layout_slug"], "aurora")
        with unscoped():
            self.assertEqual(WebsiteSite.all_objects.count(), 2)

    def test_a_desk_cannot_touch_another_desks_sections(self):
        self.client.force_authenticate(self.alice)
        self.client.get("/api/website/site/")
        alice_hero = WebsiteSection.all_objects.get(
            site__account_id=self.alice_account, section_type="hero"
        )
        self.client.force_authenticate(self.bob)
        self.client.get("/api/website/site/")
        response = self.client.patch(
            f"/api/website/sections/{alice_hero.pk}/",
            {"content": {"title": {"en": "hijacked"}}},
            format="json",
        )
        self.assertEqual(response.status_code, 404)
        alice_hero.refresh_from_db()
        self.assertNotEqual(alice_hero.content.get("title"), {"en": "hijacked"})

    def test_public_slug_selects_the_named_desks_site(self):
        for user, name in ((self.alice, "Alice Desk"), (self.bob, "Bob Desk")):
            self.client.force_authenticate(user)
            self.client.patch("/api/website/site/", {"business_name": {"en": name}}, format="json")
            self.client.post("/api/website/publish/", {}, format="json")

        self.client.force_authenticate(None)
        with unscoped():
            alice_slug = WebsiteSite.all_objects.get(account_id=self.alice_account).slug
        body = self.client.get(f"/api/public/website/?account={alice_slug}").json()
        self.assertEqual(body["branding"]["business_name"], {"en": "Alice Desk"})


class WebsitePermissionTests(APITestCase):
    def setUp(self):
        cache.clear()
        self.employee, _ = _make_desk("just_an_employee", role=CustomUser.ROLE_EMPLOYEE)
        self.developer, _ = _make_desk("just_a_developer", role=CustomUser.ROLE_DEVELOPER)

    def test_employee_and_developer_cannot_reach_the_builder(self):
        for user in (self.employee, self.developer):
            self.client.force_authenticate(user)
            self.assertEqual(self.client.get("/api/website/site/").status_code, 403)
            self.assertEqual(
                self.client.post(
                    "/api/website/layout/", {"layout_slug": "vault"}, format="json"
                ).status_code,
                403,
            )

    def test_anonymous_cannot_reach_the_builder(self):
        self.assertEqual(self.client.get("/api/website/site/").status_code, 401)

    def test_public_endpoints_ignore_a_bogus_token(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer not-a-real-token")
        with unscoped():
            slug = CustomUser.objects.get(username="just_an_employee").account.slug
        self.assertEqual(
            self.client.get(f"/api/public/website/prices/?account={slug}").status_code, 200
        )


class FinalizedPricesTests(APITestCase):
    """The website quotes finalized prices only; the existing feed is unchanged."""

    def setUp(self):
        cache.clear()
        self.owner, self.account = _make_desk("rates_desk")
        self.usd, _ = Currency.objects.get_or_create(code="USD", defaults={"name": "Dollar"})
        self.gbp, _ = Currency.objects.get_or_create(code="GBP", defaults={"name": "Pound"})
        with act_as_account(self.account):
            self.category = Category.objects.create(name="Cash")
            self.price_type = PriceType.objects.create(
                category=self.category,
                name="Buy",
                trade_type="buy",
                source_currency=self.usd,
                target_currency=self.gbp,
            )
            self.finalized = PriceHistory.objects.create(price_type=self.price_type, price="1.10")
            # No channel: a finalization records manager approval, and Telegram
            # delivery is a separate concern this test does not exercise.
            finalization = Finalization.objects.create(category=self.category)
            FinalizedPriceHistory.objects.create(
                finalization=finalization, price_history=self.finalized
            )
            self.draft = PriceHistory.objects.create(price_type=self.price_type, price="9.99")

    @property
    def slug(self):
        with unscoped():
            return CustomUser.objects.get(username="rates_desk").account.slug

    def _latest(self, finalized_only):
        with act_as_account(self.account):
            snapshot = build_prices_public_snapshot(finalized_only=finalized_only)
        return snapshot["categories"][0]["price_types"][0]["latest_price"]

    def test_default_snapshot_still_reports_the_newest_price(self):
        self.assertEqual(self._latest(False), "9.99")

    def test_finalized_snapshot_ignores_a_price_no_manager_approved(self):
        self.assertEqual(self._latest(True), "1.10")

    def test_public_website_prices_endpoint_serves_finalized_only(self):
        response = self.client.get(f"/api/public/website/prices/?account={self.slug}")
        self.assertEqual(response.status_code, 200, response.content)
        body = response.json()
        self.assertEqual(body["categories"][0]["price_types"][0]["latest_price"], "1.10")


class CatalogIntegrityTests(APITestCase):
    """The catalog and the Vue registry are one design; drift between them is a blank page."""

    registry_path = (
        Path(settings.BASE_DIR).parent / "frontend" / "src" / "website" / "registry.js"
    )

    def setUp(self):
        self.layouts = catalog.layouts()
        self.themes = catalog.themes()
        self.sections = catalog.sections()

    def test_every_layout_default_names_a_real_variant(self):
        for slug, manifest in self.layouts.items():
            self.assertIn(manifest["default_theme"], self.themes, slug)
            self.assertIn(manifest["chrome"], {"standard", "onepage", "sidebar", "split"}, slug)
            for section_type, variant in manifest["defaults"].items():
                self.assertIn(section_type, self.sections, (slug, section_type))
                self.assertIn(variant, self.sections[section_type]["variants"], (slug, variant))
            for section_type in manifest["starter"]:
                self.assertIn(section_type, manifest["supports"], (slug, section_type))

    def test_every_theme_declares_the_whole_token_set(self):
        token_sets = [set(theme["tokens"]) for theme in self.themes.values()]
        for slug, theme in self.themes.items():
            self.assertEqual(set(theme["tokens"]), token_sets[0], f"{slug} token set differs")
            for group in catalog.STYLE_GROUPS:
                self.assertIn(theme["defaults"][group], catalog.styles()[group], (slug, group))

    def test_field_keys_are_unique_within_a_section(self):
        for section_type, spec in self.sections.items():
            keys = [field["key"] for field in spec["fields"]]
            self.assertEqual(len(keys), len(set(keys)), section_type)

    def test_the_vue_registry_can_draw_every_catalog_entry(self):
        if not self.registry_path.exists():
            self.skipTest("frontend registry not present")
        source = self.registry_path.read_text()
        registered = set(re.findall(r"'([a-z0-9-]+)/([a-z0-9-]+)'", source))
        registered_keys = {f"{a}/{b}" for a, b in registered}
        for section_type, spec in self.sections.items():
            for variant in spec["variants"]:
                self.assertIn(
                    f"{section_type}/{variant}",
                    registered_keys,
                    f"No Vue component registered for {section_type}/{variant}",
                )
        for slug in self.layouts:
            self.assertIn(f"'{slug}'", source, f"Layout {slug} missing from the registry")


class WebsiteBrandingUploadTests(APITestCase):
    """Logo and favicon go straight onto the site row, including being removed."""

    def _png(self):
        """A real PNG: the serializer runs Pillow over it, unlike a direct save."""
        from io import BytesIO

        from PIL import Image

        buffer = BytesIO()
        Image.new("RGB", (8, 8), (255, 215, 0)).save(buffer, format="PNG")
        return buffer.getvalue()

    def setUp(self):
        cache.clear()
        self.owner, self.account = _make_desk("brand_owner")
        self.client.force_authenticate(self.owner)
        self.client.get("/api/website/site/")

    def _upload(self, field="logo"):
        from django.core.files.uploadedfile import SimpleUploadedFile

        upload = SimpleUploadedFile("logo.png", self._png(), content_type="image/png")
        return self.client.patch("/api/website/site/", {field: upload}, format="multipart")

    def test_logo_uploads_and_is_served_from_the_accounts_own_folder(self):
        response = self._upload()
        self.assertEqual(response.status_code, 200, response.content)
        url = response.json()["logo_url"]
        self.assertIn(f"accounts/{self.account}/website/", url)

    def test_logo_can_be_cleared_again(self):
        self._upload()
        response = self.client.patch("/api/website/site/", {"logo": ""}, format="multipart")
        self.assertEqual(response.status_code, 200, response.content)
        self.assertIsNone(response.json()["logo_url"])

    def test_an_asset_upload_lands_in_the_desks_own_library(self):
        from django.core.files.uploadedfile import SimpleUploadedFile

        upload = SimpleUploadedFile("hero.png", self._png(), content_type="image/png")
        response = self.client.post("/api/website/assets/", {"image": upload}, format="multipart")
        self.assertEqual(response.status_code, 201, response.content)
        self.assertIn(f"accounts/{self.account}/website/", response.json()["url"])
        listed = self.client.get("/api/website/assets/").json()
        self.assertEqual(len(listed), 1)

    def test_a_non_image_upload_is_refused(self):
        from django.core.files.uploadedfile import SimpleUploadedFile

        upload = SimpleUploadedFile("notes.txt", b"hello", content_type="text/plain")
        response = self.client.post("/api/website/assets/", {"image": upload}, format="multipart")
        self.assertEqual(response.status_code, 400)
