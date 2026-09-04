from django.core.management.base import BaseCommand

from bot_gateway.services.rates_cache import refresh_live_rates_cache


class Command(BaseCommand):
    help = "Force refresh bot gateway live rates Redis cache"

    def handle(self, *args, **options):
        refresh_live_rates_cache("management_command")
        self.stdout.write(self.style.SUCCESS("Bot rates cache refreshed"))
