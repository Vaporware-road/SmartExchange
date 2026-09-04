from __future__ import annotations

from typing import Any, Dict, List, Optional

from bot_gateway.adapters.base import InboundMessage
from bot_gateway.models import Platform


def parse_whatsapp_webhook(payload: Dict[str, Any]) -> List[InboundMessage]:
    """Parse Meta WhatsApp Cloud API webhook payload into inbound messages."""
    results: List[InboundMessage] = []
    for entry in payload.get("entry") or []:
        for change in entry.get("changes") or []:
            value = change.get("value") or {}
            messages = value.get("messages") or []
            contacts = {c.get("wa_id"): c for c in (value.get("contacts") or [])}
            for msg in messages:
                if msg.get("type") != "text":
                    continue
                text = (msg.get("text") or {}).get("body", "").strip()
                if not text:
                    continue
                phone = msg.get("from", "")
                contact = contacts.get(phone) or {}
                profile = contact.get("profile") or {}
                results.append(
                    InboundMessage(
                        platform=Platform.WHATSAPP,
                        sender_id=phone,
                        chat_id=phone,
                        text=text,
                        update_id=msg.get("id", ""),
                        display_name=profile.get("name", ""),
                        username="",
                        raw=msg,
                    )
                )
    return results
