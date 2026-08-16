"""Parse customer-typed TTL strings into minutes."""

from __future__ import annotations

import re

_TTL_RE = re.compile(
    r"^\s*(\d+(?:\.\d+)?)\s*(m|min|mins|minutes|h|hr|hrs|hours|d|day|days)?\s*$",
    re.IGNORECASE,
)


def parse_ttl_minutes(raw: str) -> int | None:
    """
    Accept ``30``, ``30m``, ``1h``, ``2d``, etc. Returns positive minutes or None.
    Bare numbers are treated as minutes.
    """
    if raw is None:
        return None
    match = _TTL_RE.match(str(raw))
    if not match:
        return None
    try:
        value = float(match.group(1))
    except (TypeError, ValueError):
        return None
    if value <= 0:
        return None
    unit = (match.group(2) or "m").lower()
    if unit in ("h", "hr", "hrs", "hours"):
        minutes = int(value * 60)
    elif unit in ("d", "day", "days"):
        minutes = int(value * 1440)
    else:
        minutes = int(value)
    return minutes if minutes > 0 else None
