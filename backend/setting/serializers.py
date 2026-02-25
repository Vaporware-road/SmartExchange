from rest_framework import serializers

from .models import SiteSettings, Log
from telegram_app.models import TelegramBot, TelegramChannel


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = [
            "site_name",
            "tagline",
            "logo",
            "favicon",
            "support_phone",
            "support_phone_2",
            "support_phone_3",
            "support_email",
            "address",
            "office_map_url",
            "business_hours",
            "telegram_link",
            "instagram_link",
            "twitter_link",
            "linkedin_link",
        ]


class TelegramBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramBot
        fields = ["id", "name", "token", "is_active", "created_at", "updated_at"]


class TelegramChannelSerializer(serializers.ModelSerializer):
    bot_name = serializers.CharField(source="bot.name", read_only=True)

    class Meta:
        model = TelegramChannel
        fields = [
            "id",
            "bot",
            "bot_name",
            "name",
            "chat_id",
            "is_active",
            "created_at",
            "updated_at",
        ]


class LogSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True, default=None)

    class Meta:
        model = Log
        fields = [
            "id",
            "level",
            "source",
            "message",
            "details",
            "created_at",
            "user",
            "username",
        ]
