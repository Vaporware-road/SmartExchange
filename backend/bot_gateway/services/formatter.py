"""
Format live price captions for bot replies using template_editor dynamic_data.
"""
from __future__ import annotations

from typing import Dict

from django.db.models import Prefetch
from django.utils import timezone

from category.models import Category, PriceType
from change_price.prefetch_helpers import prefetch_price_histories_latest
from price_publisher.services.publisher import _safe_format_caption
from price_publisher.services.tether_renderer import supports_tether_category
from template_editor.dynamic_data import (
    build_dynamic_data_for_category_board,
    build_dynamic_data_for_tether_board,
)
from template_editor.models import Template


class _SafeFormatDict(dict):
    def __missing__(self, key):
        return "{" + str(key) + "}"


def safe_format_caption(template_str: str, dynamic_data: dict) -> str:
    return _safe_format_caption(template_str, dynamic_data)


def _resolve_template(category: Category) -> Template | None:
    if getattr(category, "last_used_template_id", None):
        tpl = Template.objects.filter(pk=category.last_used_template_id, is_active=True).first()
        if tpl:
            return tpl
    usage = "tether_board" if supports_tether_category(category) else "category_board"
    return (
        Template.objects.filter(category=category, usage_type=usage, is_active=True)
        .order_by("publish_order", "id")
        .first()
    )


def _price_items_for_category(category: Category):
    price_types = (
        PriceType.objects.filter(category=category, is_active=True)
        .order_by("order", "id")
        .prefetch_related(prefetch_price_histories_latest())
    )
    items = []
    for pt in price_types:
        latest = pt.price_histories.first()
        if latest:
            items.append((pt, latest))
    return items


def build_category_caption(category: Category) -> str:
    """Build formatted caption text for one category board."""
    if not category:
        return ""
    price_items = _price_items_for_category(category)
    timestamp = timezone.now()
    te_template = _resolve_template(category)
    usage_tether = supports_tether_category(category)
    dynamic_data = (
        build_dynamic_data_for_tether_board(category, price_items, timestamp)
        if usage_tether
        else build_dynamic_data_for_category_board(category, price_items, timestamp)
    )
    if te_template and getattr(te_template, "telegram_caption_template", "").strip():
        return safe_format_caption(te_template.telegram_caption_template, dynamic_data)
    if (category.telegram_message_description or "").strip():
        return safe_format_caption(category.telegram_message_description, dynamic_data)
    lines = [f"📊 {category.name}"]
    for pt, ph in price_items:
        price = getattr(ph, "price", None)
        if price is not None:
            lines.append(f"• {pt.name}: {price}")
    return "\n".join(lines)


def build_all_formatted_captions() -> Dict[str, str]:
    """Pre-build captions for all categories (stored in Redis)."""
    result: Dict[str, str] = {}
    for cat in Category.objects.all().order_by("name"):
        try:
            result[str(cat.pk)] = build_category_caption(cat)
        except Exception:
            result[str(cat.pk)] = f"📊 {cat.name}"
    return result


def build_reply_text(category: Category, trigger_type: str) -> str:
    """Primary reply: cached caption or live build."""
    from bot_gateway.services.rates_cache import get_cached_caption

    if category:
        cached = get_cached_caption(category.pk)
        if cached:
            return cached
        return build_category_caption(category)

    from bot_gateway.services.rates_cache import get_cached_live_rates

    snapshot = get_cached_live_rates()
    lines = ["📊 نرخ‌های لحظه‌ای", ""]
    for cat in snapshot.get("categories") or []:
        lines.append(f"▫️ {cat.get('name', '')}")
        for pt in cat.get("price_types") or []:
            price = pt.get("latest_price")
            if price:
                lines.append(f"  • {pt.get('name')}: {price}")
        lines.append("")
    return "\n".join(lines).strip()
