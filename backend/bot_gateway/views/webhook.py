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

from accounts.scoping import act_as_account, unscoped
from bot_gateway.adapters.whatsapp import parse_whatsapp_webhook, webhook_phone_number_ids
from bot_gateway.services.dispatcher import process_inbound_whatsapp
from bot_gateway.services.whatsapp_client import (
    config_for_phone_number_id,
    verify_webhook_signature,
)
from bot_gateway.models import WhatsAppConfig

logger = logging.getLogger(__name__)


@method_decorator(csrf_exempt, name="dispatch")
class WhatsAppWebhookView(View):
    """GET/POST /api/bot-gateway/webhook/whatsapp/"""

    def get(self, request):
        """Meta's subscription handshake.

        Every desk points its number at this one URL and the handshake carries
        no number, so the verify token itself has to identify the desk: match it
        against all of them and accept if exactly one owns it.
        """
        mode = request.GET.get("hub.mode")
        token = (request.GET.get("hub.verify_token") or "").strip()
        challenge = request.GET.get("hub.challenge")
        if mode != "subscribe" or not token:
            return HttpResponse(status=403)
        with unscoped():
            matched = WhatsAppConfig.objects.filter(
                is_active=True, verify_token=token
            ).exists()
        if not matched:
            return HttpResponse(status=403)
        return HttpResponse(challenge or "", content_type="text/plain")

    def post(self, request):
        try:
            body = json.loads(request.body)
        except (json.JSONDecodeError, TypeError):
            return HttpResponse(status=400)

        # The number the batch was addressed to is the tenant key; signature
        # verification then runs against that desk's own app secret, so one
        # customer's credentials can never validate another's traffic.
        phone_number_ids = webhook_phone_number_ids(body)
        cfg = None
        for phone_number_id in phone_number_ids:
            cfg = config_for_phone_number_id(phone_number_id)
            if cfg is not None:
                break
        if cfg is None:
            return HttpResponse(status=404)

        app_secret = cfg.get_app_secret()
        signature = request.headers.get("X-Hub-Signature-256", "")
        if app_secret and not verify_webhook_signature(request.body, signature, app_secret):
            logger.warning("WhatsApp webhook signature mismatch")
            return HttpResponse(status=403)

        with act_as_account(cfg.account_id):
            for msg in parse_whatsapp_webhook(body):
                try:
                    process_inbound_whatsapp(msg, config=cfg)
                except Exception:
                    logger.exception("WhatsApp webhook processing failed")

        return HttpResponse(status=200)
