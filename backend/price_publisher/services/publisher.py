"""High-level price publishing utilities for Telegram image posts."""

from __future__ import annotations

import io
import logging
import re
from dataclasses import dataclass
from typing import Iterable, List, Optional

from django.db import transaction
from django.utils import timezone
import jdatetime

from PIL import Image

from accounts.models import CustomUser
from accounts.plans import allowed_plans_for, user_plan
from price_publisher.models import PriceTemplate
from price_publisher.services.image_renderer import (
    PriceEntry,
    PriceImageRenderer,
    PriceImageRenderingError,
    RenderedPriceImage,
    TemplateAssets,
)
from price_publisher.services.tether_renderer import supports_tether_category
from price_publisher.services.special_offer_renderer import (
    SPECIAL_GBP_TEMPLATES,
    normalize_identifier,
    render_special_offer_board,
    resolve_special_offer_template,
    supports_special_offer_type,
)
from core.utils import format_price_display
from setting.models import SiteSettings
from telegram_app.services.telegram_client import TelegramService

from template_editor.constants import CATEGORY_BOARD, TETHER_BOARD, SPECIAL_OFFER
from template_editor.dynamic_data import (
    build_dynamic_data_for_category_board,
    build_dynamic_data_for_tether_board,
    build_dynamic_data_for_special_offer,
)
from template_editor.render import render_price_template
from template_editor.services.screenshot_engine import (
    ScreenshotEngineError,
    generate_template_screenshot,
)

logger = logging.getLogger(__name__)


def _safe_last_used_template_id(instance) -> Optional[int]:
    """Read ``last_used_template_id`` without crashing if the DB column is missing (pre-migrate)."""
    if instance is None:
        return None
    try:
        rid = instance.last_used_template_id
    except Exception:
        return None
    return rid if rid is not None else None


class PricePublicationError(RuntimeError):
    """Raised when the price publishing pipeline fails."""


# ----------------------------------------------------------------------
# Constants for special GBP template detection
# ----------------------------------------------------------------------
SPECIAL_GBP_KEYWORDS = {
    # Buy cash keywords
    "خریدنقدیپوندویژه", "خریدویژهنقدیپوند", "خریدویژهنقدی",
    "buycashpoundspecial", "specialbuycashgbp", "special_buy_cash_gbp",
    "buycashgbpspecial", "buycashspecial", "specialcashpurchase",
    # Buy account keywords
    "خریدویژهازحساب",
    "buyaccountspecial", "specialbuyaccountgbp", "special_buy_account_gbp", "buyaccountgbpspecial",
    # Sell cash keywords
    "فروشویژهنقدی",
    "sellcashspecial", "specialselcashgbp", "special_sell_cash_gbp", "sellcashgbpspecial",
    # Sell account keywords
    "فروشویژهازحساب",
    "sellaccountspecial", "specialselaccountgbp", "special_sell_account_gbp", "sellaccountgbpspecial",
}

BUY_ACCOUNT_KEYWORDS = {
    "خریدویژهازحساب", "buyaccountspecial", "specialbuyaccountgbp",
    "special_buy_account_gbp", "buyaccountgbpspecial",
}

SELL_CASH_KEYWORDS = {
    "فروشویژهنقدی", "sellcashspecial", "specialselcashgbp",
    "special_sell_cash_gbp", "sellcashgbpspecial",
}

SELL_ACCOUNT_KEYWORDS = {
    "فروشویژهازحساب", "sellaccountspecial", "specialselaccountgbp",
    "special_sell_account_gbp", "sellaccountgbpspecial",
}

# Template to type mapping
TEMPLATE_TYPE_MAP = {
    "special_buy_account_GBP.jpg": (True, False),   # (is_account, is_sell)
    "special_sell_cash_GBP.jpg": (False, True),
    "special_sell_account_GBP.jpg": (True, True),
}

# Persian date constants
FARSI_MONTHS = [
    "", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
    "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"
]

FARSI_WEEKDAYS = {
    "Saturday": "شنبه",
    "Sunday": "یکشنبه",
    "Monday": "دوشنبه",
    "Tuesday": "سه‌شنبه",
    "Wednesday": "چهارشنبه",
    "Thursday": "پنجشنبه",
    "Friday": "جمعه",
}

PERSIAN_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")

# ----------------------------------------------------------------------
# Legacy Telegram message metadata - built dynamically from SiteSettings
# ----------------------------------------------------------------------


def _get_site_settings():
    """Load SiteSettings (cached)."""
    return SiteSettings.load()


def _build_legacy_final_message() -> str:
    """Build legacy caption from SiteSettings (support_phone, address, office_map_url, business_hours)."""
    s = _get_site_settings()
    contact = ""
    if s.support_phone:
        clean_phone = s.support_phone.replace("+", "").replace(" ", "")
        contact = f"📱 <a href=\"https://wa.me/{clean_phone}\">{s.support_phone}</a>\n\n"
    office = ""
    if s.address:
        url = s.office_map_url or "#"
        office = f"📍 <b>آدرس دفتر:</b>\n<a href=\"{url}\">{s.address.replace(chr(10), ' ')}</a>\n\n"
    hours = s.business_hours or "دوشنبه تا شنبه: 9:30 صبح تا ۱۷\nیکشنبه ها: تعطیل"
    return (
        f"💷 <b>خرید فروش تتر و پوند نقدی و حسابی</b>\n\n"
        f"{contact}"
        f"{office}"
        f"🕐 <b>ساعات کاری:</b>\n{hours}"
    )


class _SafeFormatDict(dict):
    """Missing keys in caption templates render as {key} instead of raising."""

    def __missing__(self, key):
        return "{" + str(key) + "}"


def _safe_format_caption(template_str: str, dynamic_data: dict) -> str:
    if not template_str or not str(template_str).strip():
        return ""
    try:
        normalized = re.sub(r"\{\{\s*([^{}]+?)\s*\}\}", r"{\1}", str(template_str).strip())
        return normalized.format_map(_SafeFormatDict(dynamic_data))
    except (ValueError, KeyError, IndexError):
        return str(template_str).strip()


def _normalize_inline_keyboard(raw) -> list:
    """Build Telegram inline_keyboard rows: [[{text, url}, ...], ...]."""
    if not raw or not isinstance(raw, list):
        return []
    rows: List[list] = []
    for item in raw:
        if isinstance(item, list):
            row = []
            for b in item:
                if isinstance(b, dict):
                    t = b.get("text") or b.get("label")
                    u = b.get("url")
                    if t and u:
                        row.append({"text": str(t), "url": str(u)})
            if row:
                rows.append(row)
        elif isinstance(item, dict):
            t = item.get("text") or item.get("label")
            u = item.get("url")
            if t and u:
                rows.append([{"text": str(t), "url": str(u)}])
    return rows


def _build_legacy_final_buttons() -> list:
    """Build legacy inline buttons from SiteSettings support_phone fields."""
    s = _get_site_settings()
    buttons = []
    if s.support_phone:
        clean = s.support_phone.replace("+", "").replace(" ", "")
        buttons.append([{"text": "ارتباط با امور مشتریان ۱", "url": f"https://wa.me/{clean}"}])
    if s.support_phone_2:
        clean = s.support_phone_2.replace("+", "").replace(" ", "")
        buttons.append([{"text": "ارتباط با امور مشتریان ۲", "url": f"https://wa.me/{clean}"}])
    if s.support_phone_3:
        clean = s.support_phone_3.replace("+", "").replace(" ", "")
        buttons.append([{"text": "مدیر مالی", "url": f"https://wa.me/{clean}"}])
    if s.telegram_link or s.instagram_link:
        row = []
        if s.telegram_link:
            row.append({"text": "کانال تلگرام ما", "url": s.telegram_link})
        if s.instagram_link:
            row.append({"text": "اینستاگرام", "url": s.instagram_link})
        if row:
            buttons.append(row)
    return buttons if buttons else []


@dataclass(frozen=True)
class PublicationResult:
    """Outcome of a Telegram publication request."""

    success: bool
    response: str
    caption: Optional[str]
    template_id: Optional[int] = None
    publish_path: str = "unknown"
    render_fallback_reason: Optional[str] = None


class PricePublisherService:
    """Coordinates rendering price cards and sending them to Telegram."""

    def __init__(
        self,
        renderer: Optional[PriceImageRenderer] = None,
        acting_user: Optional[CustomUser] = None,
    ) -> None:
        self._renderer = renderer or PriceImageRenderer()
        self._acting_user = acting_user

    def _plan_filter(self):
        if not self._acting_user:
            return {}
        return {"plan__in": allowed_plans_for(user_plan(self._acting_user))}

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def publish_category_prices(
        self,
        *,
        category,
        price_items: Iterable[tuple],
        channel,
        notes: Optional[str] = None,
    ) -> PublicationResult:
        """Render and post category prices to Telegram.

        Args:
            category: `category.models.Category` instance the prices belong to.
            price_items: Iterable of `(price_type, price_history)` tuples.
            channel: `telegram_app.models.TelegramChannel` destination.
            notes: Optional additional text to show on the image footer.
        """

        entries = []
        latest_timestamp = None

        for price_type, price_history in price_items:
            subtitle = self._build_pricetype_subtitle(price_type)
            meta = self._build_price_meta(price_history)
            entries.append(
                PriceEntry(
                    title=price_type.name,
                    price=self._format_price(price_history.price),
                    subtitle=subtitle,
                    meta=meta,
                )
            )

            history_timestamp = self._get_history_timestamp(price_history)
            if latest_timestamp is None or history_timestamp > latest_timestamp:
                latest_timestamp = history_timestamp

        if not entries:
            raise PricePublicationError("No price entries were provided for publication.")

        template = self._get_template_for_category(category)
        template_assets = self._build_template_assets(template)

        image, te_template_used, publish_path, fallback_reason = self._render_category_image(
            category=category,
            price_items=price_items,
            category_name=category.name,
            entries=entries,
            notes=notes,
            timestamp=latest_timestamp,
            template_assets=template_assets,
        )

        caption = self._build_category_publish_caption(
            category, price_items, latest_timestamp, te_template_used
        )
        buttons = self._build_category_publish_buttons(category, te_template_used)

        return self._send_photo(
            channel=channel,
            image=image,
            caption=caption,
            buttons=buttons,
            template_id=getattr(te_template_used, "id", None),
            publish_path=publish_path,
            render_fallback_reason=fallback_reason,
        )

    def publish_special_price(
        self,
        *,
        special_price_type,
        price_history,
        channel,
        notes: Optional[str] = None,
    ) -> PublicationResult:
        """Render and post a special price to Telegram."""

        custom_offer = supports_special_offer_type(special_price_type)
        te_template, matched_category_price_type = self._select_next_template_editor_for_special(
            special_price_type
        )
        try:
            if te_template and self._template_editor_eligible(te_template):
                dynamic_data = build_dynamic_data_for_special_offer(
                    special_price_type, price_history, matched_category_price_type
                )
                image = self._render_template_editor_image(
                    te_template, SPECIAL_OFFER, dynamic_data
                )
                if getattr(te_template, "is_active", True):
                    self._mark_category_template_used(
                        getattr(matched_category_price_type, "category", None), te_template
                    )
                caption = self._build_special_publish_caption(
                    special_price_type, price_history, dynamic_data, te_template, custom_offer=True
                )
                buttons = self._build_special_publish_buttons(te_template)
                return self._send_photo(
                    channel=channel,
                    image=image,
                    caption=caption,
                    buttons=buttons,
                    template_id=getattr(te_template, "id", None),
                    publish_path="special_template_editor",
                )
            if not te_template:
                logger.warning(
                    "template_editor special fallback: no template special_price_type_id=%s",
                    getattr(special_price_type, "id", None),
                )
            else:
                logger.warning(
                    "template_editor special fallback: ineligible template_id=%s special_price_type_id=%s",
                    getattr(te_template, "id", None),
                    getattr(special_price_type, "id", None),
                )
        except Exception:
            logger.exception(
                "template_editor special fallback: render failed special_price_type_id=%s template_id=%s",
                getattr(special_price_type, "id", None),
                getattr(te_template, "id", None) if te_template else None,
            )

        if custom_offer:
            try:
                image = render_special_offer_board(
                    special_price_type=special_price_type,
                    price_history=price_history,
                )
            except FileNotFoundError as exc:
                raise PricePublicationError(str(exc)) from exc
        else:
            subtitle = self._build_pricetype_subtitle(special_price_type)
            entry = PriceEntry(
                title=special_price_type.name,
                price=self._format_price(price_history.price),
                subtitle=subtitle,
                meta=self._build_price_meta(price_history),
            )

            template = self._get_template_for_special(special_price_type)
            template_assets = self._build_template_assets(template)

            image = self._render_special_price_image(
                title=f"Special Price: {special_price_type.name}",
                entry=entry,
                notes=notes or price_history.notes,
                timestamp=self._get_history_timestamp(price_history),
                template_assets=template_assets,
            )

        caption = self._build_special_price_caption(
            special_price_type, price_history, custom_offer
        )
        return self._send_photo(
            channel=channel,
            image=image,
            caption=caption,
            buttons=_build_legacy_final_buttons(),
            publish_path="special_legacy_renderer" if custom_offer else "special_default_renderer",
        )

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _template_editor_eligible(self, te_template) -> bool:
        if not te_template:
            return False
        cfg = te_template.config if isinstance(getattr(te_template, "config", None), dict) else {}
        if cfg.get("themes"):
            return True
        cj = te_template.config_json if isinstance(te_template.config_json, dict) else {}
        ws = cj.get("widgets")
        if isinstance(ws, list) and len(ws) > 0:
            return True
        fields = cfg.get("fields")
        if isinstance(fields, dict) and len(fields) > 0:
            return bool(te_template.image)
        return bool(te_template.image)

    def _select_next_template_editor_for_category(self, category):
        """Pick category template with priority: pinned on category -> active round-robin -> latest for category."""
        from template_editor.models import Template

        if not category:
            return None

        # Honor pinned template only when it belongs to the same category.
        pinned_id = _safe_last_used_template_id(category)
        if pinned_id:
            pinned = Template.objects.filter(
                pk=pinned_id, category=category, **self._plan_filter()
            ).first()
            if pinned:
                return pinned
            logger.warning(
                "Ignoring pinned template that does not belong to category "
                "(category_id=%s, pinned_template_id=%s)",
                getattr(category, "id", None),
                pinned_id,
            )

        active = list(
            Template.objects.filter(
                category=category, is_active=True, **self._plan_filter()
            ).order_by(
                "publish_order", "id"
            )
        )
        if not active:
            return None
        # Prefer templates that have PixelCast widgets so finalize does not pick an
        # empty placeholder row and fall back to the generic PriceImageRenderer card.
        with_widgets = [t for t in active if self._template_widget_count(t) > 0]
        pool = with_widgets if with_widgets else active
        ids = [t.pk for t in pool]
        last_id = _safe_last_used_template_id(category)
        if last_id not in ids:
            return pool[0]
        idx = ids.index(last_id)
        return pool[(idx + 1) % len(pool)]

    @staticmethod
    def _template_widget_count(te_template) -> int:
        cj = getattr(te_template, "config_json", None)
        if not isinstance(cj, dict):
            return 0
        w = cj.get("widgets")
        return len(w) if isinstance(w, list) else 0

    def _mark_category_template_used(self, category, te_template) -> None:
        if not category or not te_template:
            return
        if getattr(te_template, "category_id", None) != getattr(category, "pk", None):
            return
        try:
            from category.models import Category

            with transaction.atomic():
                cat = Category.objects.select_for_update().get(pk=category.pk)
                cat.last_used_template = te_template
                cat.save(update_fields=["last_used_template", "updated_at"])
        except Exception:
            logger.exception("Failed to update category.last_used_template")

    def _mark_special_price_template_used(self, special_price_type, te_template) -> None:
        if not special_price_type or not te_template:
            return
        if getattr(te_template, "special_price_type_id", None) != getattr(
            special_price_type, "pk", None
        ):
            return
        try:
            from special_price.models import SpecialPriceType

            with transaction.atomic():
                spt = SpecialPriceType.objects.select_for_update().get(pk=special_price_type.pk)
                spt.last_used_template = te_template
                spt.save(update_fields=["last_used_template", "updated_at"])
        except Exception:
            logger.exception("Failed to update special_price_type.last_used_template")

    def _build_category_publish_caption(self, category, price_items, timestamp, te_template):
        usage_tether = supports_tether_category(category)
        dynamic_data = (
            build_dynamic_data_for_tether_board(category, price_items, timestamp)
            if usage_tether
            else build_dynamic_data_for_category_board(category, price_items, timestamp)
        )
        if te_template and getattr(te_template, "telegram_caption_template", "").strip():
            return _safe_format_caption(te_template.telegram_caption_template, dynamic_data)
        if category and (category.telegram_message_description or "").strip():
            return _safe_format_caption(category.telegram_message_description, dynamic_data)
        return ""

    def _build_category_publish_buttons(self, category, te_template):
        if te_template and isinstance(te_template.telegram_buttons_json, list):
            norm = _normalize_inline_keyboard(te_template.telegram_buttons_json)
            if norm:
                return norm
        if category and category.inline_buttons:
            norm = _normalize_inline_keyboard(category.inline_buttons)
            if norm:
                return norm
        return []

    def _build_special_publish_caption(
        self, special_price_type, price_history, dynamic_data, te_template, custom_offer: bool
    ):
        if te_template and getattr(te_template, "telegram_caption_template", "").strip():
            return _safe_format_caption(te_template.telegram_caption_template, dynamic_data)
        return ""

    def _build_special_publish_buttons(self, te_template):
        if te_template and isinstance(te_template.telegram_buttons_json, list):
            norm = _normalize_inline_keyboard(te_template.telegram_buttons_json)
            if norm:
                return norm
        return []

    def _render_category_image(
        self,
        *,
        category,
        price_items,
        category_name: str,
        entries: list[PriceEntry],
        notes: Optional[str],
        timestamp,
        template_assets: Optional[TemplateAssets],
    ) -> tuple[RenderedPriceImage, object | None, str, str | None]:
        """Returns (RenderedPriceImage, template_editor.Template | None, publish_path, fallback_reason)."""
        # Always prefer template_editor Template for finalize publication.
        te_template = self._select_next_template_editor_for_category(category)
        try:
            if te_template and self._template_editor_eligible(te_template):
                usage_type = (
                    TETHER_BOARD if supports_tether_category(category) else CATEGORY_BOARD
                )
                dynamic_data = (
                    build_dynamic_data_for_tether_board(category, price_items, timestamp)
                    if usage_type == TETHER_BOARD
                    else build_dynamic_data_for_category_board(category, price_items, timestamp)
                )
                image = self._render_template_editor_image(
                    te_template, usage_type, dynamic_data, price_items=price_items
                )
                if getattr(te_template, "is_active", True):
                    self._mark_category_template_used(category, te_template)
                return image, te_template, "category_template_editor", None
            if not te_template:
                logger.warning(
                    "template_editor category fallback: no template category_id=%s",
                    getattr(category, "id", None),
                )
                fallback_reason = "no_template"
            else:
                logger.warning(
                    "template_editor category fallback: ineligible template_id=%s category_id=%s",
                    getattr(te_template, "id", None),
                    getattr(category, "id", None),
                )
                fallback_reason = "ineligible_template"
        except Exception:
            logger.exception(
                "template_editor category fallback: render failed category_id=%s template_id=%s",
                getattr(category, "id", None),
                getattr(te_template, "id", None) if te_template else None,
            )
            fallback_reason = "template_render_failed"
        raise PricePublicationError(
            f"Template contract violation for category_id={getattr(category, 'id', None)}: {fallback_reason}"
        )

    def _select_next_template_editor_for_special(self, special_price_type):
        """
        Resolve special-price rendering template via category price contract.
        Returns (template, matched_category_price_type) or (None, None).
        """
        from category.models import PriceType

        if not special_price_type:
            return None, None

        matched_price_type = (
            PriceType.objects.select_related("category")
            .filter(
                source_currency_id=getattr(special_price_type, "source_currency_id", None),
                target_currency_id=getattr(special_price_type, "target_currency_id", None),
                trade_type=getattr(special_price_type, "trade_type", None),
                is_active=True,
            )
            .order_by("category_id", "order", "id")
            .first()
        )
        if not matched_price_type:
            return None, None

        template = self._select_next_template_editor_for_category(matched_price_type.category)
        if not template:
            return None, None
        return template, matched_price_type

    def _render_template_editor_image(
        self, te_template, usage_type: str, dynamic_data: dict, price_items=None
    ) -> RenderedPriceImage:
        """Render a template_editor Template, headless first when it is switched on.

        Playwright reproduces the editor pixel for pixel; Pillow approximates it.
        A browser that is missing, slow or crashing must never stop a publish,
        so any engine error falls through to the Pillow renderer.
        """
        if getattr(SiteSettings.load(), "use_playwright_for_template_render", False):
            try:
                png_bytes = generate_template_screenshot(
                    template_id=te_template.id,
                    dynamic_data=dynamic_data,
                    price_items=price_items,
                )
                return self._bytes_to_rendered(png_bytes)
            except ScreenshotEngineError:
                logger.exception(
                    "Playwright render failed; falling back to Pillow template_id=%s",
                    getattr(te_template, "id", None),
                )
        return self._pil_image_to_rendered(
            render_price_template(te_template, usage_type, dynamic_data)
        )

    @staticmethod
    def _bytes_to_rendered(png_bytes: bytes) -> RenderedPriceImage:
        from PIL import Image

        buf = io.BytesIO(png_bytes)
        buf.name = "prices.png"
        with Image.open(io.BytesIO(png_bytes)) as probe:
            width, height = probe.size
        buf.seek(0)
        return RenderedPriceImage(stream=buf, width=width, height=height)

    @staticmethod
    def _pil_image_to_rendered(pil_image) -> RenderedPriceImage:
        """Convert PIL Image to RenderedPriceImage."""
        buf = io.BytesIO()
        buf.name = "prices.png"
        pil_image.convert("RGB").save(buf, format="PNG")
        buf.seek(0)
        return RenderedPriceImage(stream=buf, width=pil_image.width, height=pil_image.height)

    def _render_special_price_image(
        self,
        *,
        title: str,
        entry: PriceEntry,
        notes: Optional[str],
        timestamp,
        template_assets: Optional[TemplateAssets],
    ) -> RenderedPriceImage:
        try:
            return self._renderer.render_special_price(
                title=title,
                price_entry=entry,
                notes=notes,
                timestamp=timestamp,
                template_assets=template_assets,
            )
        except PriceImageRenderingError as exc:  # pragma: no cover - delegated
            raise PricePublicationError(str(exc)) from exc

    def _send_photo(
        self,
        *,
        channel,
        image: RenderedPriceImage,
        caption: Optional[str],
        buttons: Optional[list[list[dict]]] = None,
        template_id: Optional[int] = None,
        publish_path: str = "unknown",
        render_fallback_reason: Optional[str] = None,
    ) -> PublicationResult:
        stream = self._prepare_stream(image.stream, fallback_name="prices.png")

        service = TelegramService(channel.bot.get_plain_token())
        success, response = service.send_photo(
            channel.chat_id,
            stream,
            caption=caption,
            buttons=buttons,
        )

        return PublicationResult(
            success=success,
            response=response,
            caption=caption,
            template_id=template_id,
            publish_path=publish_path,
            render_fallback_reason=render_fallback_reason,
        )

    @staticmethod
    def _build_pricetype_subtitle(price_type) -> str:
        source_code = getattr(price_type.source_currency, "code", "-")
        target_code = getattr(price_type.target_currency, "code", "-")
        trade_display = getattr(price_type, "get_trade_type_display", None)
        if callable(trade_display):
            trade_label = trade_display()
        else:
            trade_label = getattr(price_type, "trade_type", "")

        normalized_trade = trade_label.capitalize() if isinstance(trade_label, str) else ""
        pair = f"{source_code}/{target_code}"
        return f"{pair} • {normalized_trade}".strip(" •")

    @staticmethod
    def _build_price_meta(price_history) -> Optional[str]:
        pieces = []

        updated_at = getattr(price_history, "updated_at", None) or getattr(
            price_history, "created_at", None
        )
        if updated_at:
            localized = timezone.localtime(updated_at)
            pieces.append(localized.strftime("Updated %Y-%m-%d %H:%M"))

        notes = getattr(price_history, "notes", None)
        if notes:
            pieces.append(notes)

        return " • ".join(pieces) if pieces else None

    @staticmethod
    def _format_price(price) -> str:
        return format_price_display(price)

    @staticmethod
    def _prepare_stream(stream: io.BytesIO, fallback_name: str) -> io.BytesIO:
        if not getattr(stream, "name", None):
            stream.name = fallback_name
        stream.seek(0)
        return stream

    @staticmethod
    def _get_history_timestamp(price_history):
        timestamp = getattr(price_history, "updated_at", None) or getattr(
            price_history, "created_at", None
        )
        return timestamp or timezone.now()

    # ------------------------------------------------------------------
    # Template helpers
    # ------------------------------------------------------------------
    def _get_template_for_category(self, category):
        if not category:
            return self._get_default_template()

        template = (
            PriceTemplate.objects.filter(
                template_type=PriceTemplate.TemplateType.CATEGORY,
                category=category,
                is_active=True,
                **self._plan_filter(),
            )
            .select_related("category")
            .first()
        )

        if template:
            return template

        return self._get_default_template()

    def _get_template_for_special(self, special_price_type):
        if not special_price_type:
            return self._get_default_template()

        template = (
            PriceTemplate.objects.filter(
                template_type=PriceTemplate.TemplateType.SPECIAL,
                special_price_type=special_price_type,
                is_active=True,
                **self._plan_filter(),
            )
            .select_related("special_price_type")
            .first()
        )

        if template:
            return template

        return self._get_default_template()

    def _get_default_template(self):
        return (
            PriceTemplate.objects.filter(
                template_type=PriceTemplate.TemplateType.DEFAULT,
                is_active=True,
                **self._plan_filter(),
            )
            .order_by("name")
            .first()
        )

    def _build_template_assets(self, template: Optional[PriceTemplate]) -> Optional[TemplateAssets]:
        if not template:
            return None

        background_image = self._open_image_field(template.background_image)
        if background_image is None:
            return None

        logo_image = self._open_image_field(template.logo_image)
        watermark_image = self._open_image_field(template.watermark_image)

        return TemplateAssets(
            background=background_image,
            logo=logo_image,
            watermark=watermark_image,
        )

    def _open_image_field(self, field) -> Optional[Image.Image]:
        if not field:
            return None

        try:
            with field.open("rb") as file_obj:
                image = Image.open(file_obj)
                converted = image.convert("RGBA")
                converted.load()
                return converted
        except FileNotFoundError:
            return None
        except Exception as exc:  # pragma: no cover - defensive
            raise PricePublicationError(f"Failed to load template image: {exc}") from exc

    def _build_special_price_caption(self, special_price_type, price_history, custom_offer: bool) -> str:
        """Build caption for special price offers, detecting if it's a special GBP template."""
        special_price_name = getattr(special_price_type, "name", "")
        normalized_name = normalize_identifier(special_price_name)
        
        # Check if it's a special GBP template
        template = resolve_special_offer_template(special_price_type) if custom_offer else None
        is_special_gbp = (
            template is not None 
            and template.background in SPECIAL_GBP_TEMPLATES
        ) or any(keyword in normalized_name for keyword in SPECIAL_GBP_KEYWORDS)
        
        if not is_special_gbp:
            return _build_legacy_final_message()
        
        # Determine template type (account/sell flags)
        is_account, is_sell = self._detect_template_type(template, normalized_name)
        
        timestamp = self._get_history_timestamp(price_history)
        return self._build_special_pound_caption(timestamp, is_account=is_account, is_sell=is_sell)
    
    def _detect_template_type(self, template, normalized_name: str) -> tuple[bool, bool]:
        """Detect if template is account-based and/or sell type. Returns (is_account, is_sell)."""
        # First check template background
        if template and template.background in TEMPLATE_TYPE_MAP:
            return TEMPLATE_TYPE_MAP[template.background]
        
        # Fallback to keyword matching
        if any(keyword in normalized_name for keyword in SELL_ACCOUNT_KEYWORDS):
            return (True, True)  # Sell account
        if any(keyword in normalized_name for keyword in BUY_ACCOUNT_KEYWORDS):
            return (True, False)  # Buy account
        if any(keyword in normalized_name for keyword in SELL_CASH_KEYWORDS):
            return (False, True)  # Sell cash
        
        return (False, False)  # Default: Buy cash
    
    @staticmethod
    def _format_dates(timestamp) -> tuple[str, str, str, str]:
        """Format Persian and English dates from timestamp. Returns (farsi_date, farsi_weekday, english_date, english_weekday)."""
        now = timezone.localtime(timestamp) if timestamp else timezone.localtime()
        jalali = jdatetime.datetime.fromgregorian(datetime=now)
        
        farsi_date = f"{jalali.day} {FARSI_MONTHS[jalali.month]} {jalali.year}"
        farsi_weekday = FARSI_WEEKDAYS.get(now.strftime("%A"), "")
        # Format English date with zero-padded day: "December 04, 2025"
        english_date = now.strftime("%B %d, %Y")
        english_weekday = now.strftime("%A")
        
        # Convert English digits to Persian
        farsi_date = farsi_date.translate(PERSIAN_DIGITS)
        
        return farsi_date, farsi_weekday, english_date, english_weekday
    
    @staticmethod
    def _build_contact_section() -> str:
        """Build the contact information section from SiteSettings.support_phone."""
        s = _get_site_settings()
        if not s.support_phone:
            return ""
        clean = s.support_phone.replace("+", "").replace(" ", "")
        return f"📱 <a href=\"https://wa.me/{clean}\">{s.support_phone}</a>"
    
    @staticmethod
    def _build_common_description(title: str) -> str:
        """Build common description section from SiteSettings (address, office_map_url, business_hours)."""
        s = _get_site_settings()
        contact_section = PricePublisherService._build_contact_section()
        office_url = s.office_map_url or "#"
        office_text = s.address or "—"
        hours = s.business_hours or "دوشنبه تا شنبه: 9:30 صبح تا ۱۷\nیکشنبه ها: تعطیل"
        addr_line = f"📍 <b>آدرس دفتر:</b>\n<a href=\"{office_url}\">{office_text.replace(chr(10), ' ')}</a>\n\n"
        hours_line = f"🕐 <b>ساعات کاری:</b>\n{hours}"
        if title:
            mid = f"\n\n{contact_section}\n\n" if contact_section else "\n\n"
            return f"💷 <b>{title}</b>{mid}{addr_line}{hours_line}"
        return f"{contact_section}\n\n{addr_line}{hours_line}" if contact_section else f"{addr_line}{hours_line}"
    
    @staticmethod
    def _build_tether_caption(timestamp) -> str:
        """Build caption for Tether prices from SiteSettings (support_phone, address, office_map_url, business_hours)."""
        s = _get_site_settings()
        farsi_date, farsi_weekday, english_date, english_weekday = PricePublisherService._format_dates(timestamp)
        office_url = s.office_map_url or "#"
        office_text = s.address or "—"
        hours = s.business_hours or "دوشنبه تا شنبه از ۹:۳۰ صبح تا ۵ عصر (به وقت لندن)\nیکشنبه‌ها تعطیل است"
        site_name = s.site_name or "MrExchange"
        contact_lines = []
        if s.support_phone:
            c = s.support_phone.replace("+", "").replace(" ", "")
            contact_lines.append(f"1️⃣ تماس ۱\n📱 <a href=\"https://wa.me/{c}\">{s.support_phone}</a>")
        if s.support_phone_2:
            c = s.support_phone_2.replace("+", "").replace(" ", "")
            contact_lines.append(f"2️⃣ تماس ۲\n📱 <a href=\"https://wa.me/{c}\">{s.support_phone_2}</a>")
        if s.support_phone_3:
            c = s.support_phone_3.replace("+", "").replace(" ", "")
            contact_lines.append(f"👤 مدیر مالی\n📱 <a href=\"https://wa.me/{c}\">{s.support_phone_3}</a>")
        contact_block = "\n".join(contact_lines) + "\n\n" if contact_lines else ""
        return (
            f"📅 <b>تاریخ:</b>\n\n"
            f"🇮🇷 {farsi_weekday} {farsi_date}\n\n"
            f"🇬🇧 {english_weekday}, {english_date}\n\n"
            f"━━━━━━\n\n"
            "💷 خرید فروش تتر\n\n"
            "━━━━━━━━━━━\n"
            "💬 کارشناسان ما همواره پاسخ‌گوی شما هستند.\n"
            "📞 تماس با ما:\n"
            f"{contact_block}"
            "📍 آدرس دفتر:\n"
            f"🏢 <a href=\"{office_url}\">{office_text.replace(chr(10), ' ')}</a>\n\n"
            "━━━━━━━━━━━\n"
            f"🕐 ساعات کاری:\n{hours}\n"
            "━━━━━━━━━━━\n"
            f"{site_name}، همراهی مطمئن در تمامی امور ارزی شما\n"
            "🌍 خدمات در لندن و لیدز"
        )
    
    @staticmethod
    def _build_gbp_category_caption(timestamp) -> str:
        """Build caption for GBP category from SiteSettings."""
        s = _get_site_settings()
        office_url = s.office_map_url or "#"
        office_text = s.address or "—"
        hours = s.business_hours or "دوشنبه تا شنبه از ۹:۳۰ صبح تا ۵ عصر (به وقت لندن)\nیکشنبه‌ها تعطیل است"
        site_name = s.site_name or "MrExchange"
        contact_lines = []
        if s.support_phone:
            c = s.support_phone.replace("+", "").replace(" ", "")
            contact_lines.append(f"1️⃣ تماس ۱\n📱 <a href=\"https://wa.me/{c}\">{s.support_phone}</a>")
        if s.support_phone_2:
            c = s.support_phone_2.replace("+", "").replace(" ", "")
            contact_lines.append(f"2️⃣ تماس ۲\n📱 <a href=\"https://wa.me/{c}\">{s.support_phone_2}</a>")
        if s.support_phone_3:
            c = s.support_phone_3.replace("+", "").replace(" ", "")
            contact_lines.append(f"👤 مدیر مالی\n📱 <a href=\"https://wa.me/{c}\">{s.support_phone_3}</a>")
        contact_block = "\n".join(contact_lines) + "\n\n" if contact_lines else ""
        return (
            "💷 خرید و فروش پوند (GBP) | لیر | درهم\n"
            "💰 نقدی و حسابی\n\n"
            "━━━━━━━━━━━\n"
            "💬 کارشناسان ما همواره پاسخ‌گوی شما هستند.\n"
            "📞 تماس با ما:\n"
            f"{contact_block}"
            "📍 آدرس دفتر:\n"
            f"🏢 <a href=\"{office_url}\">{office_text.replace(chr(10), ' ')}</a>\n\n"
            "━━━━━━━━━━━\n"
            f"🕐 ساعات کاری:\n{hours}\n"
            "━━━━━━━━━━━\n"
            f"{site_name}، همراهی مطمئن در تمامی امور ارزی شما\n"
            "🌍 خدمات در لندن و لیدز"
        )

    @staticmethod
    def _get_special_pound_title(is_account: bool, is_sell: bool) -> str:
        """Get the title for special pound caption based on type."""
        if is_sell and is_account:
            return "💷 <b>فروش ویژه از حساب پوند</b>"
        elif is_sell:
            return "💷 <b>فروش ویژه نقدی پوند</b>"
        elif is_account:
            return "💷 <b>خرید ویژه از حساب پوند</b>"
        else:
            return "💷 <b>خرید ویژه نقدی پوند</b>"
    
    @staticmethod
    def _build_special_pound_caption(timestamp, is_account: bool = False, is_sell: bool = False) -> str:
        """Build a professional and attractive caption for Special Pound prices without dates."""
        title = PricePublisherService._get_special_pound_title(is_account, is_sell)
        
        # Get description without title
        description = PricePublisherService._build_common_description('')
        
        caption = (
            f"{title}\n\n"
            f"{description}"
        )
        
        return caption



