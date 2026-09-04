import os
import sys

import django

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SmartExchangePanel.settings")
django.setup()

from bot_gateway.models import BotCustomer, Platform
from bot_gateway.services.auth_tokens import issue_customer_token

c, _ = BotCustomer.objects.get_or_create(
    platform=Platform.TELEGRAM,
    telegram_chat_id=123456789,
    defaults={"display_name": "Test User", "username": "testuser"},
)
print(issue_customer_token(c, bot_id=1))
