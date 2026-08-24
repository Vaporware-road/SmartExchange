from django.apps import AppConfig


class TelegramAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telegram_app'

    def ready(self):
        # Auto-sync BotAdmin delegation rows (bot owner / sub-operator changes).
        from . import signals  # noqa: F401
