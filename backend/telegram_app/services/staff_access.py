"""Resolve whether a Telegram user may use the in-bot admin panel for a bot."""

from __future__ import annotations

from django.contrib.auth import get_user_model

from accounts.models import CustomUser
from accounts.permissions import _normalize_role

from ..models import TelegramBot

User = get_user_model()

STAFF_ROLES = (CustomUser.ROLE_SUPER_ADMIN, CustomUser.ROLE_MANAGEMENT)


def normalize_telegram_id(value) -> str:
    raw = str(value or "").strip()
    return "".join(ch for ch in raw if ch.isdigit())


def resolve_staff_user(telegram_user_id: int | str) -> CustomUser | None:
    """Active panel user whose telegram_id matches the Telegram from.id."""
    tid = normalize_telegram_id(telegram_user_id)
    if not tid:
        return None
    return (
        User.objects.filter(is_active=True, telegram_id=tid, role__in=STAFF_ROLES)
        .order_by("id")
        .first()
    )


def staff_telegram_id_set() -> set[str]:
    ids: set[str] = set()
    for user in User.objects.filter(is_active=True, role__in=STAFF_ROLES).only(
        "telegram_id"
    ):
        tid = normalize_telegram_id(user.telegram_id)
        if tid:
            ids.add(tid)
    return ids


def is_bot_admin(telegram_user_id: int | str, bot: TelegramBot) -> CustomUser | None:
    """
    Staff may open the in-bot admin panel with no login button.

    - ``super_admin``: any bot
    - ``management``: only bots they own (or any bot if they own none yet — still
      allow when they are the notify recipient for this bot's owner org; ownership
      is the strict rule)
    """
    user = resolve_staff_user(telegram_user_id)
    if user is None or bot is None:
        return None
    role = _normalize_role(getattr(user, "role", None))
    if getattr(user, "is_superuser", False) or role == CustomUser.ROLE_SUPER_ADMIN:
        return user
    if role == CustomUser.ROLE_MANAGEMENT and bot.owner_id == user.id:
        return user
    return None
