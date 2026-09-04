"""
Flatten category price types into an order-intake catalog (only priced, active items).
"""
from __future__ import annotations

from typing import Any, Dict, List


def build_price_catalog(snapshot: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Return price types that have a latest_price, with parent category metadata."""
    catalog: List[Dict[str, Any]] = []
    for cat in snapshot.get("categories") or []:
        cat_id = cat.get("id")
        cat_name = cat.get("name") or ""
        for pt in cat.get("price_types") or []:
            if pt.get("is_active") is False:
                continue
            price = pt.get("latest_price")
            if price is None or str(price).strip() == "":
                continue
            target = pt.get("target_currency") or {}
            source = pt.get("source_currency") or {}
            catalog.append(
                {
                    "id": pt.get("id"),
                    "name": pt.get("name") or "",
                    "slug": pt.get("slug") or "",
                    "trade_type": pt.get("trade_type") or "",
                    "latest_price": price,
                    "category_id": cat_id,
                    "category_name": cat_name,
                    "category_slug": cat.get("slug") or "",
                    "source_currency": source,
                    "target_currency": target,
                    "currency_code": target.get("code") or source.get("code") or "",
                }
            )
    return catalog
