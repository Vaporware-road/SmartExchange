from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional
from uuid import UUID

import jwt
from django.conf import settings

from bot_gateway.models import BotCustomer


def _lifetime_minutes() -> int:
    return int(getattr(settings, "BOT_CUSTOMER_JWT_LIFETIME_MINUTES", 60))


def issue_customer_token(
    customer: BotCustomer,
    *,
    bot_id: Optional[int] = None,
    extra: Optional[Dict[str, Any]] = None,
) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": str(customer.uuid),
        "typ": "bot_customer",
        "platform": customer.platform,
        "iat": now,
        "exp": now + timedelta(minutes=_lifetime_minutes()),
    }
    if customer.telegram_chat_id is not None:
        payload["chat_id"] = customer.telegram_chat_id
    if customer.whatsapp_phone:
        payload["phone"] = customer.whatsapp_phone
    if bot_id is not None:
        payload["bot_id"] = bot_id
    if extra:
        payload.update(extra)
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")


def decode_customer_token(token: str) -> Optional[Dict[str, Any]]:
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    except jwt.PyJWTError:
        return None


def get_customer_from_token(token: str) -> Optional[BotCustomer]:
    payload = decode_customer_token(token)
    if not payload or payload.get("typ") != "bot_customer":
        return None
    sub = payload.get("sub")
    if not sub:
        return None
    try:
        return BotCustomer.objects.filter(uuid=UUID(str(sub))).first()
    except (ValueError, TypeError):
        return None


def build_webapp_url(auth_token: str) -> str:
    base = getattr(settings, "BOT_GATEWAY_FRONTEND_URL", "http://localhost:3000").rstrip("/")
    return f"{base}/webapp/order?auth_token={auth_token}"
