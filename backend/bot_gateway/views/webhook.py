"""
Inbound webhook endpoint for WhatsApp.

Telegram is not served here: telegram_app owns this install's Telegram webhook
and its customer bot is the richer one (sessions, profiles, exchange requests,
price alerts). A second Telegram webhook would fight it for the same updates.
"""
from __future__ import annotations

import json
import logging

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from bot_gateway.adapters.whatsapp import parse_whatsapp_webhook
from bot_gateway.services.dispatcher import process_inbound_whatsapp
from bot_gateway.services.whatsapp_client import get_active_config, verify_webhook_signature

logger = logging.getLogger(__name__)


@method_decorator(csrf_exempt, name="dispatch")
class WhatsAppWebhookView(View):
    """GET/POST /api/bot-gateway/webhook/whatsapp/"""

    def get(self, request):
        mode = request.GET.get("hub.mode")
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")
        cfg = get_active_config()
        if not cfg:
            return HttpResponse(status=404)
        if mode == "subscribe" and token == (cfg.verify_token or "").strip():
            return HttpResponse(challenge or "", content_type="text/plain")
        return HttpResponse(status=403)

    def post(self, request):
        cfg = get_active_config()
        if not cfg:
            return HttpResponse(status=404)

        app_secret = cfg.get_app_secret()
        signature = request.headers.get("X-Hub-Signature-256", "")
        if app_secret and not verify_webhook_signature(request.body, signature, app_secret):
            logger.warning("WhatsApp webhook signature mismatch")
            return HttpResponse(status=403)

        try:
            body = json.loads(request.body)
        except (json.JSONDecodeError, TypeError):
            return HttpResponse(status=400)

        for msg in parse_whatsapp_webhook(body):
            try:
                process_inbound_whatsapp(msg, config=cfg)
            except Exception:
                logger.exception("WhatsApp webhook processing failed")

        return HttpResponse(status=200)
