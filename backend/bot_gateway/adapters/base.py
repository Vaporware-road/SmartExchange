from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class InboundMessage:
    platform: str
    sender_id: str
    text: str
    update_id: str
    chat_id: Optional[str] = None
    display_name: str = ""
    username: str = ""
    raw: Dict[str, Any] = field(default_factory=dict)


@dataclass
class OutboundReply:
    text: str
    buttons: Optional[List[List[Dict[str, Any]]]] = None
    parse_mode: str = "HTML"
