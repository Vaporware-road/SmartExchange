"""Resolve whether a Telegram user may use the in-bot admin panel for a bot."""

from __future__ import annotations

from django.contrib.auth import get_user_model
from django.db.models import Q

from accounts.models import CustomUser
from accounts.permissions import _normalize_role

from ..models import BotAdmin, TelegramBot
from .bot_admins import DELEGATED_SUB_ROLES

User = get_user_model()

STAFF_ROLES = (CustomUser.ROLE_SUPER_ADMIN, CustomUser.ROLE_MANAGEMENT)


def normalize_telegram_id(value) -> str:
    raw = str(value or "").strip()
    return "".join(ch for ch in raw if ch.isdigit())


def resolve_staff_user(
    telegram_user_id: int | str, telegram_username: str | None = None
) -> CustomUser | None:
    """Active panel user who may act as bot staff for a Telegram from.id/username.

    Matches staff roles (super_admin / management) first, then delegated
    sub-operators (employee role with a non-admin sub_role).
    """
    tid = normalize_telegram_id(telegram_user_id)
    q = Q(is_active=True)
    if tid:
        q &= Q(telegram_id=tid)
    else:
        uname = (telegram_username or "").strip().lstrip("@")
        if not uname:
            return None
        q &= Q(telegram_username__iexact=uname)
    staff = (
        User.objects.filter(q, role__in=STAFF_ROLES).order_by("id").first()
    )
    if staff is not None:
        return staff
    return (
        User.objects.filter(q, role=CustomUser.ROLE_EMPLOYEE, sub_role__in=DELEGATED_SUB_ROLES)
        .order_by("id")
        .first()
    )


def staff_telegram_id_set() -> set[str]:
    ids: set[str] = set()
    qs = User.objects.filter(
        Q(role__in=STAFF_ROLES) | Q(role=CustomUser.ROLE_EMPLOYEE, sub_role__in=DELEGATED_SUB_ROLES)
    )
    for user in qs.only("telegram_id"):
        tid = normalize_telegram_id(user.telegram_id)
        if tid:
            ids.add(tid)
    return ids


def get_effective_sub_role(staff: CustomUser | None) -> str:
    """Effective admin sub-role for menu/action policy.

    Returns ``operator`` / ``head_operator`` for delegated staff, otherwise
    ``admin`` (full access).
    """
    if staff is None:
        return CustomUser.SUB_ROLE_ADMIN
    sub = str(getattr(staff, "sub_role", "") or "").strip().lower().replace("-", "_")
    if sub in DELEGATED_SUB_ROLES:
        return sub
    return CustomUser.SUB_ROLE_ADMIN


def is_bot_admin(
    telegram_user_id: int | str,
    bot: TelegramBot,
    telegram_username: str | None = None,
) -> CustomUser | None:
    """
    Staff may open the in-bot admin panel with no login button.

    - ``super_admin``: any bot
    - ``management``: only bots they own (or any bot if they own none yet — still
      allow when they are the notify recipient for this bot's owner org; ownership
      is the strict rule)
    - delegated sub-operators (employee role): only bots they are a BotAdmin of
      (synced via ``sync_bot_admins_for_owner``)
    """
    user = resolve_staff_user(telegram_user_id, telegram_username=telegram_username)
    if user is None or bot is None:
        return None
    role = _normalize_role(getattr(user, "role", None))
    if getattr(user, "is_superuser", False) or role == CustomUser.ROLE_SUPER_ADMIN:
        return user
    if BotAdmin.objects.filter(bot=bot, user=user).exists():
        return user
    if role == CustomUser.ROLE_MANAGEMENT and bot.owner_id == user.id:
        return user
    # Delegated sub-operator whose owner is this bot's owner (works without an
    # explicit BotAdmin row; sync_bot_admins_for_owner() materialises the same set).
    if (
        role == CustomUser.ROLE_EMPLOYEE
        and getattr(user, "sub_role", None) in DELEGATED_SUB_ROLES
        and user.owner_id is not None
        and user.owner_id == bot.owner_id
    ):
        return user
    return None
