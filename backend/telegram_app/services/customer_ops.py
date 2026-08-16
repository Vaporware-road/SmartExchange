"""Customer profile upsert from Telegram update payloads."""

from __future__ import annotations

from telegram_app.models import CustomerProfile


def _from_user(body: dict) -> dict:
    return (
        (body.get("message") or {}).get("from")
        or (body.get("edited_message") or {}).get("from")
        or (body.get("callback_query") or {}).get("from")
        or {}
    )


def upsert_customer_profile(update_dict: dict) -> CustomerProfile | None:
    user = _from_user(update_dict)
    try:
        telegram_user_id = int(user.get("id", 0))
    except (TypeError, ValueError):
        return None
    if not telegram_user_id:
        return None

    defaults = {
        "username": (user.get("username") or "")[:255],
        "first_name": (user.get("first_name") or "")[:255],
        "last_name": (user.get("last_name") or "")[:255],
        "language": (user.get("language_code") or "")[:16],
    }
    profile, _ = CustomerProfile.objects.update_or_create(
        telegram_user_id=telegram_user_id,
        defaults=defaults,
    )
    return profile
