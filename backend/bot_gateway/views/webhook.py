"""
Inbound webhook endpoints for Telegram and WhatsApp.
"""
from __future__ import annotations

import json
import logging

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from bot_gateway.adapters.telegram import parse_telegram_update
from bot_gateway.adapters.whatsapp import parse_whatsapp_webhook
from bot_gateway.services.dispatcher import process_inbound_telegram, process_inbound_whatsapp
from bot_gateway.services.whatsapp_client import get_active_config, verify_webhook_signature
from telegram_app.models import TelegramBot

logger = logging.getLogger(__name__)


@method_decorator(csrf_exempt, name="dispatch")
@method_decorator(require_http_methods(["POST"]), name="dispatch")
class TelegramWebhookView(View):
    """POST /api/bot-gateway/webhook/telegram/<uuid:secret>/"""

    def post(self, request, secret):
        bot = TelegramBot.objects.filter(
            webhook_secret_token=secret,
            is_active=True,
            gateway_enabled=True,
        ).first()
        if not bot:
            logger.warning("Telegram webhook: secret not found or gateway disabled")
            return HttpResponse(status=404)

        secret_header = request.headers.get("X-Telegram-Bot-Api-Secret-Token", "").strip()
        if secret_header and str(secret) != secret_header:
            return HttpResponse(status=403)

        try:
            body = json.loads(request.body)
        except (json.JSONDecodeError, TypeError):
            return HttpResponse(status=400)

        msg = parse_telegram_update(body)
        if msg:
            try:
                process_inbound_telegram(bot, msg)
            except Exception:
                logger.exception("Telegram webhook processing failed bot=%s", bot.pk)

        return HttpResponse(status=200)


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
