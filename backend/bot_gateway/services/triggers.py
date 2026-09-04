from __future__ import annotations

import re
from typing import Optional, Tuple

from category.models import Category
from template_editor.dynamic_data import _normalize

from bot_gateway.models import TriggerType

PRICE_KEYWORDS = {
    "/start",
    "start",
    "قیمت",
    "price",
    "نرخ",
    "rates",
    "hello",
    "سلام",
}


def _build_currency_aliases() -> dict:
    aliases = {}
    for cat in Category.objects.all():
        for token in filter(
            None,
            [
                cat.name,
                cat.slug,
                getattr(cat, "name_fa", None),
            ],
        ):
            aliases[_normalize(str(token))] = cat
    tether_tokens = ("تتر", "tether", "usdt", "تترتومان")
    tether_cat = Category.objects.filter(slug__icontains="tether").first()
    if not tether_cat:
        tether_cat = Category.objects.filter(name__icontains="تتر").first()
    if tether_cat:
        for t in tether_tokens:
            aliases[_normalize(t)] = tether_cat
    return aliases


def match_trigger(text: str) -> Tuple[str, Optional[Category]]:
    """
    Return (trigger_type, matched_category).
    matched_category is None for generic price requests.
    """
    normalized = (text or "").strip()
    lower = normalized.lower()
    if lower.startswith("/start") or lower in PRICE_KEYWORDS:
        return TriggerType.START if lower.startswith("/start") else TriggerType.PRICE_KEYWORD, None

    norm = _normalize(normalized)
    aliases = _build_currency_aliases()
    if norm in aliases:
        return TriggerType.CURRENCY_MATCH, aliases[norm]

    for key, cat in aliases.items():
        if key and key in norm:
            return TriggerType.CURRENCY_MATCH, cat

    return TriggerType.OTHER, None
