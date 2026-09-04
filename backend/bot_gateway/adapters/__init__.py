from bot_gateway.adapters.base import InboundMessage, OutboundReply
from bot_gateway.adapters.telegram import parse_telegram_update
from bot_gateway.adapters.whatsapp import parse_whatsapp_webhook

__all__ = [
    "InboundMessage",
    "OutboundReply",
    "parse_telegram_update",
    "parse_whatsapp_webhook",
]
