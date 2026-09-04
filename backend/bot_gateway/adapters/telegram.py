from __future__ import annotations

from typing import Any, Dict, List, Optional

from bot_gateway.adapters.base import InboundMessage
from bot_gateway.models import Platform


def parse_telegram_update(payload: Dict[str, Any]) -> Optional[InboundMessage]:
    """Extract user text message from a Telegram Update object."""
    message = payload.get("message") or payload.get("edited_message")
    if not message:
        return None
    text = (message.get("text") or message.get("caption") or "").strip()
    if not text:
        return None
    chat = message.get("chat") or {}
    user = message.get("from") or {}
    chat_id = chat.get("id")
    if chat_id is None:
        return None
    update_id = str(payload.get("update_id", ""))
    return InboundMessage(
        platform=Platform.TELEGRAM,
        sender_id=str(chat_id),
        chat_id=str(chat_id),
        text=text,
        update_id=update_id,
        display_name=" ".join(
            filter(None, [user.get("first_name"), user.get("last_name")])
        ).strip(),
        username=user.get("username") or "",
        raw=payload,
    )
