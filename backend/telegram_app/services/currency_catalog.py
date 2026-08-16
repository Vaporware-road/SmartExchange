"""Worldwide ISO 4217 currency catalog for Telegram pickers."""

from __future__ import annotations

import difflib
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Iterable

from django.core.cache import cache
from django.db.models import Count

DEFAULT_PAGE_SIZE = 8
MIN_PAGE_SIZE = 8
MAX_PAGE_SIZE = 10
TOP_EXCHANGE_LIMIT = 10
TOP_EXCHANGE_CACHE_KEY = "tg_top_exchange_currencies_v1"
TOP_EXCHANGE_CACHE_TTL = 120

# Fallback when there is little/no exchange history yet.
DEFAULT_TOP_CODES = (
    "USD",
    "EUR",
    "GBP",
    "AED",
    "IRR",
    "TRY",
    "CNY",
    "RUB",
    "CHF",
    "JPY",
)

# callback_data tokens kept short for Telegram's 64-byte limit
CALLBACK_PREFIX = "cc"
CALLBACK_PAGE = "p"
CALLBACK_SELECT = "s"


@dataclass(frozen=True)
class Currency:
    code: str
    name: str

    @property
    def label(self) -> str:
        return f"{self.code} — {self.name}"


def _catalog_path() -> Path:
    return Path(__file__).resolve().parent.parent / "data" / "allCurrencies.txt"


def _parse_lines(lines: Iterable[str]) -> list[Currency]:
    currencies: list[Currency] = []
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "|" not in line:
            continue
        code, name = line.split("|", 1)
        code = code.strip().upper()
        name = name.strip()
        if not code or not name:
            continue
        currencies.append(Currency(code=code, name=name))
    return currencies


@lru_cache(maxsize=1)
def load_currencies() -> tuple[Currency, ...]:
    """Load and cache the catalog from allCurrencies.txt."""
    path = _catalog_path()
    text = path.read_text(encoding="utf-8")
    return tuple(_parse_lines(text.splitlines()))


@lru_cache(maxsize=1)
def _currency_by_code() -> dict[str, Currency]:
    return {c.code: c for c in load_currencies()}


@lru_cache(maxsize=1)
def _name_index() -> list[tuple[str, Currency]]:
    """Lowercased names for fuzzy / substring matching."""
    return [(c.name.lower(), c) for c in load_currencies()]


def clear_currency_cache() -> None:
    """Clear the in-memory catalog cache (tests / hot-reload)."""
    load_currencies.cache_clear()
    _currency_by_code.cache_clear()
    _name_index.cache_clear()
    cache.delete(TOP_EXCHANGE_CACHE_KEY)
    for n in range(1, 21):
        cache.delete(f"{TOP_EXCHANGE_CACHE_KEY}:{n}")


def get_currency(code: str) -> Currency | None:
    """Lookup a currency by ISO code (case-insensitive)."""
    needle = (code or "").strip().upper()
    if not needle:
        return None
    return _currency_by_code().get(needle)


def guess_currency(raw: str) -> Currency | None:
    """
    Resolve a typed currency: exact code, name substring, then fuzzy code/name.

    Examples: ``usd``, ``US Doller``, ``euro``, ``dolr``.
    """
    q = (raw or "").strip()
    if not q:
        return None

    exact = get_currency(q)
    if exact:
        return exact

    q_lower = q.lower()
    name_hits = [c for name, c in _name_index() if q_lower in name]
    if len(name_hits) == 1:
        return name_hits[0]
    if name_hits:
        name_hits.sort(key=lambda c: len(c.name))
        return name_hits[0]

    codes = list(_currency_by_code().keys())
    close_codes = difflib.get_close_matches(q.upper(), codes, n=1, cutoff=0.72)
    if close_codes:
        return get_currency(close_codes[0])

    names = [name for name, _ in _name_index()]
    close_names = difflib.get_close_matches(q_lower, names, n=1, cutoff=0.68)
    if close_names:
        for name, currency in _name_index():
            if name == close_names[0]:
                return currency

    # Token-level fuzzy (catches short typos like "dolr" → Dollar / USD).
    best: Currency | None = None
    best_score = 0.0
    default_rank = {code: i for i, code in enumerate(DEFAULT_TOP_CODES)}
    for currency in load_currencies():
        candidates = {currency.code.lower(), currency.name.lower()}
        candidates.update(
            word for word in currency.name.lower().replace("-", " ").split() if len(word) >= 3
        )
        for candidate in candidates:
            score = difflib.SequenceMatcher(None, q_lower, candidate).ratio()
            if score < 0.72:
                continue
            if best is None or score > best_score:
                best_score = score
                best = currency
            elif score == best_score and best is not None:
                # Prefer common exchange currencies on ties (USD over AUD for "dolr").
                if default_rank.get(currency.code, 999) < default_rank.get(best.code, 999):
                    best = currency
    if best is not None:
        return best
    return None


def top_exchanged_currencies(limit: int = TOP_EXCHANGE_LIMIT) -> list[Currency]:
    """
    Return up to ``limit`` currencies ranked by how often they appear in
    ExchangeRequest source/target pairs (global). Falls back to defaults.
    """
    cache_key = f"{TOP_EXCHANGE_CACHE_KEY}:{limit}"
    cached = cache.get(cache_key)
    if cached is not None:
        return list(cached)

    from telegram_app.models import ExchangeRequest

    tallies: dict[str, int] = {}
    for field in ("source_currency", "target_currency"):
        rows = (
            ExchangeRequest.objects.values(field)
            .annotate(c=Count("id"))
            .order_by("-c")[:50]
        )
        for row in rows:
            code = (row.get(field) or "").strip().upper()
            if not code:
                continue
            tallies[code] = tallies.get(code, 0) + int(row["c"])

    ranked = sorted(tallies.items(), key=lambda item: (-item[1], item[0]))
    result: list[Currency] = []
    for code, _count in ranked:
        cur = get_currency(code)
        if cur and cur not in result:
            result.append(cur)
        if len(result) >= limit:
            break

    if len(result) < limit:
        for code in DEFAULT_TOP_CODES:
            cur = get_currency(code)
            if cur and cur not in result:
                result.append(cur)
            if len(result) >= limit:
                break

    cache.set(cache_key, result, TOP_EXCHANGE_CACHE_TTL)
    return result


def normalize_page_size(page_size: int | None = None) -> int:
    size = DEFAULT_PAGE_SIZE if page_size is None else int(page_size)
    return max(MIN_PAGE_SIZE, min(MAX_PAGE_SIZE, size))


def page_count(page_size: int | None = None) -> int:
    size = normalize_page_size(page_size)
    total = len(load_currencies())
    if total == 0:
        return 0
    return (total + size - 1) // size


def paginate(
    page: int = 0,
    page_size: int | None = None,
) -> tuple[list[Currency], int, bool, bool]:
    """
    Return (items, page_index, has_prev, has_next) for Telegram keyboards.

    page is 0-based and clamped to a valid range.
    """
    size = normalize_page_size(page_size)
    all_currencies = load_currencies()
    total_pages = page_count(size)
    if total_pages == 0:
        return [], 0, False, False

    page_index = max(0, min(int(page), total_pages - 1))
    start = page_index * size
    end = start + size
    items = list(all_currencies[start:end])
    return items, page_index, page_index > 0, page_index < total_pages - 1


def encode_page_callback(page: int, *, prefix: str = CALLBACK_PREFIX) -> str:
    """Callback token for navigating to a catalog page (0-based)."""
    return f"{prefix}:{CALLBACK_PAGE}:{int(page)}"


def encode_select_callback(code: str, *, prefix: str = CALLBACK_PREFIX) -> str:
    """Callback token for selecting a currency code."""
    return f"{prefix}:{CALLBACK_SELECT}:{code.strip().upper()}"


def encode_prev_callback(current_page: int, *, prefix: str = CALLBACK_PREFIX) -> str:
    """Callback token for the Previous button (targets current_page - 1)."""
    return encode_page_callback(max(0, int(current_page) - 1), prefix=prefix)


def encode_next_callback(current_page: int, *, prefix: str = CALLBACK_PREFIX) -> str:
    """Callback token for the Next button (targets current_page + 1)."""
    return encode_page_callback(int(current_page) + 1, prefix=prefix)


@dataclass(frozen=True)
class CatalogCallback:
    kind: str  # "page" | "select"
    page: int | None = None
    code: str | None = None


def decode_catalog_callback(
    token: str,
    *,
    prefix: str = CALLBACK_PREFIX,
) -> CatalogCallback | None:
    """Parse a page/select callback token produced by this module."""
    if not token:
        return None
    parts = token.split(":")
    if len(parts) != 3 or parts[0] != prefix:
        return None
    _, action, payload = parts
    if action == CALLBACK_PAGE:
        try:
            return CatalogCallback(kind="page", page=int(payload))
        except ValueError:
            return None
    if action == CALLBACK_SELECT:
        code = payload.strip().upper()
        if not code:
            return None
        return CatalogCallback(kind="select", code=code)
    return None
