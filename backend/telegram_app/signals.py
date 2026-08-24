"""Keep telegram_app.BotAdmin delegation rows in sync automatically.

- Creating a TelegramBot (or reassigning its owner) reconciles that bot's
  admin set: the owner plus the owner's delegated sub-operators.
- Changing a CustomUser's ``owner`` / ``sub_role`` grants or revokes access on
  the relevant owners' bots immediately (both the previous and new owner are
  reconciled so a moved operator loses access on the old side).

The reconcile functions are idempotent, so manual/API-level calls remain safe.
"""

from __future__ import annotations

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import TelegramBot
from .services.bot_admins import (
    DELEGATED_SUB_ROLES,
    sync_bot_admins_for_bot,
    sync_bot_admins_for_owner,
)

User = get_user_model()


def _is_delegated(owner_id, sub_role) -> bool:
    return owner_id is not None and sub_role in DELEGATED_SUB_ROLES


def _sync_owner_bots(owner_id) -> None:
    owner = User.objects.filter(pk=owner_id).first()
    if owner is not None:
        sync_bot_admins_for_owner(owner)


@receiver(post_save, sender=TelegramBot)
def sync_bot_admins_on_bot_save(sender, instance, created, **kwargs):
    if instance.owner_id is not None:
        sync_bot_admins_for_bot(instance)


@receiver(pre_save, sender=User)
def capture_user_delegation_state(sender, instance, **kwargs):
    """Stash previous owner/sub_role so post_save can compute grant/revoke."""
    if not instance.pk:
        instance._pre_owner_id = None
        instance._pre_sub_role = None
        return
    try:
        old = User.objects.only("owner_id", "sub_role").get(pk=instance.pk)
    except User.DoesNotExist:
        instance._pre_owner_id = None
        instance._pre_sub_role = None
        return
    instance._pre_owner_id = old.owner_id
    instance._pre_sub_role = old.sub_role


@receiver(post_save, sender=User)
def sync_bot_admins_on_user_save(sender, instance, created, **kwargs):
    old_owner_id = getattr(instance, "_pre_owner_id", None)
    old_sub_role = getattr(instance, "_pre_sub_role", None)
    new_owner_id = instance.owner_id
    new_sub_role = instance.sub_role

    was_delegated = _is_delegated(old_owner_id, old_sub_role)
    is_delegated = _is_delegated(new_owner_id, new_sub_role)

    if not was_delegated and not is_delegated:
        return
    if was_delegated and not is_delegated:
        # Revoked: drop the user from the previous owner's bots.
        _sync_owner_bots(old_owner_id)
        return
    if was_delegated and old_owner_id != new_owner_id:
        # Moved between owners: remove from old, grant on new.
        _sync_owner_bots(old_owner_id)
    _sync_owner_bots(new_owner_id)
