"""
Notify panel staff on Telegram when a customer confirms an exchange request.

Recipients: active CustomUser with role super_admin or management and a
non-empty telegram_id. Failures are logged; callers must not crash the customer flow.

The request stays ``new`` until an operator changes state. Notify is a side effect.
"""

from __future__ import annotations

import logging

from django.contrib.auth import get_user_model

from accounts.models import CustomUser
from ..models import ExchangeRequest, TelegramBot
from .staff_access import normalize_telegram_id
from .telegram_client import TelegramService

logger = logging.getLogger(__name__)

User = get_user_model()

STAFF_ROLES = (
    CustomUser.ROLE_SUPER_ADMIN,
    CustomUser.ROLE_DEVELOPER,
    CustomUser.ROLE_MANAGEMENT,
)


def staff_notify_recipients():
    """Active staff with a telegram_id set."""
    return (
        User.objects.filter(is_active=True, role__in=STAFF_ROLES)
        .exclude(telegram_id__isnull=True)
        .exclude(telegram_id__exact="")
    )


def _format_request_message(req: ExchangeRequest) -> str:
    customer = req.customer
    tag = customer.get_tag_display() if hasattr(customer, "get_tag_display") else customer.tag
    who = customer.username or customer.first_name or str(customer.telegram_user_id)
    price_display = (
        str(req.price_at_request) if req.price_at_request is not None else "N/A"
    )
    return (
        "🎉 New exchange request!\n"
        f"👤 Customer: {who} (tg:{customer.telegram_user_id})\n"
        f"🏷 Tag: {tag}\n"
        f"💱 Pair: {req.source_currency} → {req.target_currency}\n"
        f"💵 Amount: {req.amount}\n"
        f"💰 Price at request: {price_display}\n"
        f"⏱ TTL: {req.ttl_minutes} min\n"
        f"🆔 Request id: {req.pk}\n\n"
        "🛠 Open admin panel in this bot: /admin\n"
        "Then Pending requests to change state or hold TTL. You've got this! ✨"
    )


def notify_staff_of_exchange_request(
    req: ExchangeRequest,
    *,
    bot: TelegramBot | None = None,
) -> dict:
    """
    Fan-out DMs to staff. Returns ``{sent: int, failed: int, recipients: int}``.

    Uses ``bot`` (or ``req.bot``) for sending. Does not raise.
    """
    send_bot = bot or req.bot
    if send_bot is None:
        logger.warning("admin_notify: no bot for request_id=%s", req.pk)
        return {"sent": 0, "failed": 0, "recipients": 0}

    try:
        client = TelegramService(send_bot.get_plain_token())
    except Exception:
        logger.exception("admin_notify: TelegramService init failed request_id=%s", req.pk)
        return {"sent": 0, "failed": 0, "recipients": 0}

    recipients = list(staff_notify_recipients())
    if not recipients:
        logger.info("admin_notify: no staff recipients for request_id=%s", req.pk)
        return {"sent": 0, "failed": 0, "recipients": 0}

    text = _format_request_message(req)
    sent = 0
    failed = 0
    last_error = ""
    for user in recipients:
        chat_id = normalize_telegram_id(user.telegram_id)
        if not chat_id:
            failed += 1
            continue
        try:
            ok, detail, _ = client.send_message(
                chat_id=chat_id, text=text, parse_mode=None
            )
        except Exception as exc:
            ok, detail = False, str(exc)
        if ok:
            sent += 1
        else:
            failed += 1
            last_error = str(detail or "")
            logger.warning(
                "admin_notify: send failed user_id=%s chat_id=%s detail=%s",
                user.pk,
                chat_id,
                detail,
            )

    result = {"sent": sent, "failed": failed, "recipients": len(recipients)}
    if last_error:
        result["last_error"] = last_error
    return result
