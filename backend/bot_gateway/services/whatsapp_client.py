"""
WhatsApp Cloud API client for outbound replies.
"""
from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

import requests
from django.conf import settings

from bot_gateway.models import WhatsAppConfig

logger = logging.getLogger(__name__)

GRAPH_API_BASE = "https://graph.facebook.com/v21.0"
REQUEST_TIMEOUT = 15


def get_active_config() -> Optional[WhatsAppConfig]:
    return WhatsAppConfig.objects.filter(is_active=True).first()


def send_text_message(
    phone: str,
    text: str,
    *,
    config: Optional[WhatsAppConfig] = None,
    cta_url: Optional[str] = None,
    cta_text: Optional[str] = None,
) -> tuple[bool, str]:
    cfg = config or get_active_config()
    if not cfg:
        return False, "No active WhatsApp config"
    token = cfg.get_access_token()
    phone_number_id = (cfg.phone_number_id or "").strip()
    if not token or not phone_number_id:
        return False, "WhatsApp credentials incomplete"

    if cta_url and cta_text:
        payload = {
            "messaging_product": "whatsapp",
            "to": phone,
            "type": "interactive",
            "interactive": {
                "type": "cta_url",
                "body": {"text": text[:1024]},
                "action": {
                    "name": "cta_url",
                    "parameters": {
                        "display_text": cta_text[:20],
                        "url": cta_url,
                    },
                },
            },
        }
    else:
        payload = {
            "messaging_product": "whatsapp",
            "to": phone,
            "type": "text",
            "text": {"body": text[:4096]},
        }

    url = f"{GRAPH_API_BASE}/{phone_number_id}/messages"
    try:
        resp = requests.post(
            url,
            json=payload,
            headers={"Authorization": f"Bearer {token}"},
            timeout=REQUEST_TIMEOUT,
        )
        if resp.ok:
            return True, "sent"
        return False, resp.text[:500]
    except requests.RequestException as exc:
        logger.warning("WhatsApp send failed: %s", exc)
        return False, str(exc)


def verify_webhook_signature(body: bytes, signature_header: str, app_secret: str) -> bool:
    if not signature_header or not app_secret:
        return False
    import hashlib
    import hmac

    expected_prefix = "sha256="
    if not signature_header.startswith(expected_prefix):
        return False
    received = signature_header[len(expected_prefix) :]
    digest = hmac.new(
        app_secret.encode("utf-8"), body, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(digest, received)
