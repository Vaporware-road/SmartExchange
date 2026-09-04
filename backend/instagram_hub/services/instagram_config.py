"""Instagram configuration helpers. Reads from InstagramConfig model."""

from __future__ import annotations

import os
from datetime import timedelta

from django.conf import settings
from django.utils import timezone

_LOCAL_BASES = frozenset({
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "http://127.0.0.1:5250",
    "http://localhost:5250",
    "http://127.0.0.1:5173",
    "http://localhost:5173",
})

TOKEN_EXPIRY_WARN_DAYS = 14


def normalize_instagram_base_url(raw: str) -> str:
    """Strip trailing slashes and accidental /media suffix from INSTAGRAM_BASE_URL."""
    base = (raw or "").strip().rstrip("/")
    if base.lower().endswith("/media"):
        base = base[: -len("/media")].rstrip("/")
    return base


def get_instagram_base_url() -> str:
    raw = (
        (getattr(settings, "INSTAGRAM_BASE_URL", None) or "").strip()
        or os.environ.get("INSTAGRAM_BASE_URL", "").strip()
    )
    return normalize_instagram_base_url(raw)


def is_public_base_url_configured() -> bool:
    """True when a non-local public base URL is set (Meta can fetch /media/...)."""
    base = get_instagram_base_url()
    if not base:
        return False
    if base in _LOCAL_BASES:
        return False
    return base.startswith("http://") or base.startswith("https://")


def get_active_instagram_config():
    from instagram_hub.models import InstagramConfig

    return InstagramConfig.objects.filter(is_active=True).order_by("pk").first()


def is_instagram_configured() -> bool:
    """Return True if an active InstagramConfig has token and ig_user_id set."""
    try:
        config = get_active_instagram_config()
        if not config:
            return False
        token = config.get_decrypted_token()
        ig_id = (config.ig_user_id or "").strip()
        return bool(token and ig_id)
    except Exception:
        return False


def get_token_status(config=None) -> dict:
    """
    Token expiry snapshot for UI and maintenance tasks.
    Returns: expired, expiring_soon, days_remaining (None if unknown).
    """
    if config is None:
        config = get_active_instagram_config()
    if not config or not config.token_expires_at:
        return {
            "expired": False,
            "expiring_soon": False,
            "days_remaining": None,
        }
    now = timezone.now()
    delta = config.token_expires_at - now
    if delta.total_seconds() <= 0:
        return {"expired": True, "expiring_soon": False, "days_remaining": 0}
    days = delta.days
    return {
        "expired": False,
        "expiring_soon": days <= TOKEN_EXPIRY_WARN_DAYS,
        "days_remaining": days,
    }


def is_ready_for_publish() -> bool:
    """Credentials + public image base URL (required for Meta to fetch PNGs)."""
    return is_instagram_configured() and is_public_base_url_configured()


def get_instagram_readiness() -> dict:
    """Full readiness report for API / simulator."""
    config = get_active_instagram_config()
    token_status = get_token_status(config)
    base_url = get_instagram_base_url()
    has_token = False
    has_app_id = False
    if config:
        has_app_id = bool((config.app_id or "").strip())
        has_token = bool(config.get_decrypted_token() and (config.ig_user_id or "").strip())

    warnings: list[str] = []
    if not has_app_id:
        warnings.append("missing_app_id")
    if not has_token:
        warnings.append("missing_token")
    if token_status["expired"]:
        warnings.append("token_expired")
    elif token_status["expiring_soon"]:
        warnings.append("token_expiring_soon")
    if not base_url:
        warnings.append("missing_public_base_url")
    elif base_url in _LOCAL_BASES:
        warnings.append("local_base_url_not_reachable_by_meta")
    elif not is_public_base_url_configured():
        warnings.append("invalid_public_base_url")

    return {
        "configured": is_instagram_configured(),
        "ready_for_publish": is_ready_for_publish(),
        "has_app_id": has_app_id,
        "has_token": has_token,
        "public_base_url": base_url or None,
        "public_base_url_configured": is_public_base_url_configured(),
        "token_expired": token_status["expired"],
        "token_expiring_soon": token_status["expiring_soon"],
        "days_until_token_expiry": token_status["days_remaining"],
        "warnings": warnings,
    }
