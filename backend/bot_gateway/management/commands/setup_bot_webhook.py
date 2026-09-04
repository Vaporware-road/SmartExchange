"""
Register Telegram webhook URL for a gateway-enabled bot.
"""
import requests
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from telegram_app.models import TelegramBot


class Command(BaseCommand):
    help = "Set Telegram webhook for a gateway-enabled bot"

    def add_arguments(self, parser):
        parser.add_argument("--bot-id", type=int, required=True)
        parser.add_argument(
            "--base-url",
            type=str,
            default="",
            help="Public base URL (e.g. https://panel.example.com). Defaults to first ALLOWED_HOSTS.",
        )

    def handle(self, *args, **options):
        bot_id = options["bot_id"]
        bot = TelegramBot.objects.filter(pk=bot_id, is_active=True).first()
        if not bot:
            raise CommandError(f"Bot {bot_id} not found or inactive")
        if not bot.gateway_enabled:
            raise CommandError(f"Bot {bot_id} does not have gateway_enabled=True")

        base = (options["base_url"] or "").strip().rstrip("/")
        if not base:
            hosts = getattr(settings, "ALLOWED_HOSTS", [])
            host = next((h for h in hosts if h not in ("*", "localhost", "127.0.0.1")), None)
            if not host:
                raise CommandError("Provide --base-url or set DJANGO_ALLOWED_HOSTS")
            scheme = "https" if not settings.DEBUG else "http"
            base = f"{scheme}://{host}"

        webhook_url = (
            f"{base}/api/bot-gateway/webhook/telegram/{bot.webhook_secret_token}/"
        )
        api_url = f"https://api.telegram.org/bot{bot.token}/setWebhook"
        resp = requests.post(
            api_url,
            json={
                "url": webhook_url,
                "secret_token": str(bot.webhook_secret_token),
                "allowed_updates": ["message", "edited_message"],
            },
            timeout=15,
        )
        data = resp.json()
        if not data.get("ok"):
            raise CommandError(f"setWebhook failed: {data}")
        self.stdout.write(self.style.SUCCESS(f"Webhook set: {webhook_url}"))
