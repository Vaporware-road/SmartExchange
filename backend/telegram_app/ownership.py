"""Ownership helpers for Telegram hub admin APIs."""

from __future__ import annotations

from accounts.permissions import _normalize_role

from .models import TelegramBot


def user_is_super_admin(user) -> bool:
    if not user or not getattr(user, "is_authenticated", False):
        return False
    if getattr(user, "is_superuser", False):
        return True
    return _normalize_role(getattr(user, "role", None)) == "super_admin"


def user_is_management(user) -> bool:
    if not user or not getattr(user, "is_authenticated", False):
        return False
    return _normalize_role(getattr(user, "role", None)) == "management"


def owned_bots_qs(user):
    """Bots owned by the given user."""
    return TelegramBot.objects.filter(owner=user)


def primary_owned_bot(user):
    """
    Prefer latest active owned bot; fall back to latest owned bot.

    Matches the spirit of ``telegram_bot_token_masked`` on ``/auth/me``.
    """
    qs = owned_bots_qs(user).order_by("-created_at")
    return qs.filter(is_active=True).first() or qs.first()


def bots_queryset_for_user(user):
    """
    Scope bot lists for hub APIs.

    - super_admin: all bots (global view)
    - management: owned bots only
    - others (employee): all bots (operational messenger/channels)
    """
    if user_is_super_admin(user):
        return TelegramBot.objects.all()
    if user_is_management(user):
        return owned_bots_qs(user)
    return TelegramBot.objects.all()


def resolve_bot_for_user(user, bot_id=None):
    """
    Resolve a TelegramBot the user may administer.

    Returns (bot, error_code, error_message).
    error_code is None on success.
    """
    if bot_id is not None:
        try:
            bot_id = int(bot_id)
        except (TypeError, ValueError):
            return None, "invalid_bot_id", "Invalid bot_id."
        try:
            bot = TelegramBot.objects.get(pk=bot_id)
        except TelegramBot.DoesNotExist:
            return None, "bot_not_found", "Bot not found."
        if user_is_super_admin(user):
            return bot, None, None
        if bot.owner_id == getattr(user, "id", None):
            return bot, None, None
        return None, "bot_forbidden", "You do not own this bot."

    bot = primary_owned_bot(user)
    if bot is not None:
        return bot, None, None

    if user_is_super_admin(user):
        bot = (
            TelegramBot.objects.filter(is_active=True).order_by("-created_at").first()
            or TelegramBot.objects.order_by("-created_at").first()
        )
        if bot is not None:
            return bot, None, None

    return None, "no_bot", "No bot token configured for this account."
