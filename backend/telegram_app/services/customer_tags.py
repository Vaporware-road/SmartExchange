"""Customer tag rules: staff are Admin and that tag is not stored or editable."""

from __future__ import annotations

from django.db.models import Count, QuerySet

from ..models import BotSession, CustomerProfile, TelegramBot
from .staff_access import resolve_staff_user

DISPLAY_ADMIN_TAG = "admin"


class AdminTagImmutable(Exception):
    """Raised when a staff customer's tag would be overwritten."""


def is_admin_customer(telegram_user_id) -> bool:
    return resolve_staff_user(telegram_user_id) is not None


def effective_tag(profile: CustomerProfile) -> str:
    if is_admin_customer(profile.telegram_user_id):
        return DISPLAY_ADMIN_TAG
    return profile.tag


def display_name(profile: CustomerProfile) -> str:
    return (profile.username or profile.first_name or "").strip()


def telegram_display_name(profile: CustomerProfile) -> str:
    """Returns the Telegram display name (first_name or username fallback)."""
    return (profile.first_name or profile.username or "").strip()


def telegram_username(profile: CustomerProfile) -> str:
    """Returns the Telegram username."""
    return (profile.username or "").strip()


def set_customer_tag(profile: CustomerProfile, tag: str) -> CustomerProfile:
    allowed = set(CustomerProfile.Tag.values)
    if tag not in allowed:
        raise ValueError(f"Invalid tag: {tag}")
    if is_admin_customer(profile.telegram_user_id):
        raise AdminTagImmutable("Admin tag cannot be changed.")
    profile.tag = tag
    profile.save(update_fields=["tag", "updated_at"])
    return profile


def customers_ranked_for_bot(bot: TelegramBot) -> QuerySet[CustomerProfile]:
    user_ids = BotSession.objects.filter(bot=bot).values("telegram_user_id")
    return (
        CustomerProfile.objects.filter(telegram_user_id__in=user_ids)
        .annotate(request_count=Count("exchange_requests"))
        .order_by("-request_count", "telegram_user_id")
    )
