"""Outgoing SMS, behind a provider seam.

Only the mock provider ships: real delivery needs credentials this install does
not have yet, and a code that silently goes nowhere is worse than one that says
so. ``SMS_PROVIDER`` picks the implementation, matching the workspace-wide
``SMS_PROVIDER=mock`` convention.
"""
import logging

from django.conf import settings

logger = logging.getLogger(__name__)


class MockSmsProvider:
    """Logs the message instead of sending it. Development and CI only."""

    name = "mock"

    def send(self, phone, message):
        logger.info("sms[mock] to=%s message=%s", phone, message)
        return True


class DisabledSmsProvider:
    """Refuses every send, so a missing provider surfaces instead of hiding."""

    name = "disabled"

    def send(self, phone, message):
        logger.warning("sms: no provider configured; not sending to %s", phone)
        return False


_PROVIDERS = {"mock": MockSmsProvider, "disabled": DisabledSmsProvider}


def get_sms_provider():
    name = (getattr(settings, "SMS_PROVIDER", "") or "disabled").strip().lower()
    return _PROVIDERS.get(name, DisabledSmsProvider)()


def send_sms(phone, message):
    """True when the provider accepted the message."""
    if not phone:
        return False
    try:
        return bool(get_sms_provider().send(phone, message))
    except Exception:
        logger.exception("sms: provider raised while sending to %s", phone)
        return False
