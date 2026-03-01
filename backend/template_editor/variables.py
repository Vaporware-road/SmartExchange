"""
Variable catalog for template-based price banners.
Defines standard variable keys with type and description for the editor and for building dynamic_data.
"""

from typing import Any, Callable, Dict, List, Optional

# Variable types for UI and validation
VAR_TYPE_TEXT = "text"
VAR_TYPE_NUMBER = "number"
VAR_TYPE_IMAGE = "image"

# Canonical variable keys and metadata. Used by API and by publisher when building dynamic_data.
VARIABLE_CATALOG: List[Dict[str, Any]] = [
    # Prices - category/GBP
    {"key": "price_cash_buy", "type": VAR_TYPE_NUMBER, "description": "Cash buy price", "group": "prices"},
    {"key": "price_cash_sell", "type": VAR_TYPE_NUMBER, "description": "Cash sell price", "group": "prices"},
    {"key": "price_account_buy", "type": VAR_TYPE_NUMBER, "description": "Account buy price", "group": "prices"},
    {"key": "price_account_sell", "type": VAR_TYPE_NUMBER, "description": "Account sell price", "group": "prices"},
    {"key": "price_official_sell", "type": VAR_TYPE_NUMBER, "description": "Official sell price", "group": "prices"},
    {"key": "price_lira", "type": VAR_TYPE_NUMBER, "description": "Lira price", "group": "prices"},
    {"key": "price_dirham", "type": VAR_TYPE_NUMBER, "description": "Dirham price", "group": "prices"},
    # Prices - tether
    {"key": "tether_buy_irr", "type": VAR_TYPE_NUMBER, "description": "Tether buy (IRR)", "group": "prices"},
    {"key": "tether_sell_irr", "type": VAR_TYPE_NUMBER, "description": "Tether sell (IRR)", "group": "prices"},
    {"key": "tether_buy_gbp", "type": VAR_TYPE_NUMBER, "description": "Tether buy (GBP)", "group": "prices"},
    {"key": "tether_sell_gbp", "type": VAR_TYPE_NUMBER, "description": "Tether sell (GBP)", "group": "prices"},
    # Prices - special (single price)
    {"key": "price", "type": VAR_TYPE_NUMBER, "description": "Single price (special)", "group": "prices"},
    {"key": "special_buy_cash_gbp_price", "type": VAR_TYPE_NUMBER, "description": "Special buy cash GBP", "group": "prices"},
    {"key": "special_buy_account_gbp_price", "type": VAR_TYPE_NUMBER, "description": "Special buy account GBP", "group": "prices"},
    {"key": "special_sell_cash_gbp_price", "type": VAR_TYPE_NUMBER, "description": "Special sell cash GBP", "group": "prices"},
    {"key": "special_sell_account_gbp_price", "type": VAR_TYPE_NUMBER, "description": "Special sell account GBP", "group": "prices"},
    # Date / time
    {"key": "date_fa", "type": VAR_TYPE_TEXT, "description": "Date (Persian)", "group": "dates"},
    {"key": "date_en", "type": VAR_TYPE_TEXT, "description": "Date (English)", "group": "dates"},
    {"key": "farsi_date", "type": VAR_TYPE_TEXT, "description": "Farsi date", "group": "dates"},
    {"key": "farsi_weekday", "type": VAR_TYPE_TEXT, "description": "Farsi weekday", "group": "dates"},
    {"key": "english_date", "type": VAR_TYPE_TEXT, "description": "English date", "group": "dates"},
    {"key": "english_weekday", "type": VAR_TYPE_TEXT, "description": "English weekday", "group": "dates"},
    {"key": "tether_date", "type": VAR_TYPE_TEXT, "description": "Tether date (e.g. 14 dec)", "group": "dates"},
    {"key": "tether_year", "type": VAR_TYPE_TEXT, "description": "Tether year", "group": "dates"},
    {"key": "time", "type": VAR_TYPE_TEXT, "description": "Time", "group": "dates"},
    # Branding / meta
    {"key": "pair_name", "type": VAR_TYPE_TEXT, "description": "Pair/category name", "group": "branding"},
    {"key": "channel_username", "type": VAR_TYPE_TEXT, "description": "Channel username", "group": "branding"},
    {"key": "website", "type": VAR_TYPE_TEXT, "description": "Website URL", "group": "branding"},
    {"key": "phone", "type": VAR_TYPE_TEXT, "description": "Phone number", "group": "branding"},
    {"key": "working_hours", "type": VAR_TYPE_TEXT, "description": "Working hours text", "group": "branding"},
    {"key": "logo", "type": VAR_TYPE_IMAGE, "description": "Logo image (path or URL)", "group": "branding"},
]

# Keys only, for quick lookup
VARIABLE_KEYS = [v["key"] for v in VARIABLE_CATALOG]


def get_variable_catalog() -> List[Dict[str, Any]]:
    """Return the full variable catalog for API/UI."""
    return list(VARIABLE_CATALOG)


def get_default_sample_value(key: str) -> str:
    """Return a sample string for preview when no dynamic_data is provided."""
    for v in VARIABLE_CATALOG:
        if v["key"] == key:
            if v["type"] == VAR_TYPE_NUMBER:
                return "1,234.56"
            if v["type"] == VAR_TYPE_IMAGE:
                return ""
            return key.replace("_", " ").title()
    return key.replace("_", " ").title()
