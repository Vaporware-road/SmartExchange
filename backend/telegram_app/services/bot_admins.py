"""Delegate in-bot admin access for a bot owner's Telegram bots.

A bot owner (management user) can grant employee-role staff access to the
in-bot admin panel of their bots. Those delegated staff carry a ``sub_role``
(operator / head_operator) that limits which admin actions they may use
(see ``telegram_app.services.admin_conversation``).

Rows are kept in sync automatically by ``telegram_app.signals`` whenever a bot
is created/assigned or a user's ``owner``/``sub_role`` changes; the functions
here are idempotent so manual calls (tests, admin actions) are safe.
"""

from __future__ import annotations

import logging

from django.contrib.auth import get_user_model

from accounts.models import CustomUser

from ..models import BotAdmin, TelegramBot

logger = logging.getLogger(__name__)

User = get_user_model()

DELEGATED_SUB_ROLES = (
    CustomUser.SUB_ROLE_OPERATOR,
    CustomUser.SUB_ROLE_HEAD_OPERATOR,
)


def _delegated_members_for_owner(owner_id: int | None) -> list[CustomUser]:
    """The admin set for a bot owned by ``owner_id``: owner + delegated sub-ops."""
    if not owner_id:
        return []
    members = list(
        User.objects.filter(
            owner_id=owner_id,
            role=CustomUser.ROLE_EMPLOYEE,
            sub_role__in=DELEGATED_SUB_ROLES,
        )
    )
    owner = User.objects.filter(pk=owner_id).first()
    if owner is not None:
        members.append(owner)
    return members


def sync_bot_admins_for_bot(bot: TelegramBot) -> int:
    """Reconcile BotAdmin rows for one bot against its owner's delegation set.

    Creates missing rows, drops rows whose user is no longer a member, and
    leaves untouched rows intact (no delete-and-recreate churn).

    Returns the number of BotAdmin rows created.
    """
    if bot is None or bot.owner_id is None:
        return 0
    members = _delegated_members_for_owner(bot.owner_id)
    member_ids = {m.id for m in members}

    existing = {ba.user_id: ba for ba in BotAdmin.objects.filter(bot=bot)}

    created = 0
    for uid in member_ids - existing.keys():
        BotAdmin.objects.create(bot=bot, user_id=uid)
        created += 1

    stale = [ba for uid, ba in existing.items() if uid not in member_ids]
    if stale:
        BotAdmin.objects.filter(pk__in=[ba.pk for ba in stale]).delete()
    return created


def sync_bot_admins_for_owner(owner: CustomUser | None) -> int:
    """Reconcile BotAdmin rows for every bot owned by ``owner``.

    Returns the number of BotAdmin rows created.
    """
    if owner is None:
        return 0
    total = 0
    for bot in TelegramBot.objects.filter(owner=owner):
        total += sync_bot_admins_for_bot(bot)
    return total
