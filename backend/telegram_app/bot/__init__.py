"""aiogram customer-bot package for SmartExchange telegram_app."""

from .factory import build_bot_and_dispatcher, feed_customer_update

__all__ = [
    "build_bot_and_dispatcher",
    "feed_customer_update",
]
