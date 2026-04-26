from rest_framework import serializers

from core.utils import validate_uploaded_image, MAX_IMAGE_SIZE
from .models import SiteSettings, Log
from telegram_app.models import TelegramBot, TelegramChannel

CANONICAL_BASE_CURRENCIES = {
    "USD", "USDT", "BTC", "ETH", "BNB", "EUR", "GBP", "AUD", "CAD", "CHF", "CNY", "TRY",
    "IRR", "IRT", "AED", "JPY", "RUB", "IQD", "XAU",
}
UPLOAD_FORMAT_CHOICES = {"PNG", "JPG", "SVG", "GIF", "WEBP", "JPEG"}


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
            "base_currency_code",
            "support_email",
            "address",
            "office_map_url",
            "business_hours",
            "telegram_link",
            "instagram_link",
            "twitter_link",
            "linkedin_link",
            "auto_post_on_update",
            "use_template_editor_for_boards",
        ]

    def validate_base_currency_code(self, value):
        code = str(value or "").upper().strip()
        if code not in CANONICAL_BASE_CURRENCIES:
            raise serializers.ValidationError("Unsupported base currency code.")
        return code

    def validate_logo(self, value):
        if value and hasattr(value, "read"):
            try:
                validate_uploaded_image(value, max_size=MAX_IMAGE_SIZE)
            except ValueError as e:
                raise serializers.ValidationError(str(e))
        return value

    def validate_favicon(self, value):
        if value and hasattr(value, "read"):
            try:
                validate_uploaded_image(value, max_size=MAX_IMAGE_SIZE)
            except ValueError as e:
                raise serializers.ValidationError(str(e))
        return value


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


class UploadPolicySerializer(serializers.Serializer):
    max_file_size_mb = serializers.IntegerField(min_value=1, max_value=50)
    allowed_formats = serializers.ListField(
        child=serializers.CharField(max_length=10),
        allow_empty=False,
    )

    def validate_allowed_formats(self, value):
        normalized = []
        for fmt in value:
            key = str(fmt or "").strip().upper()
            if key == "JPEG":
                key = "JPG"
            if key not in UPLOAD_FORMAT_CHOICES:
                raise serializers.ValidationError(f"Unsupported format: {fmt}")
            if key not in normalized:
                normalized.append(key)
        if not normalized:
            raise serializers.ValidationError("At least one format must be selected.")
        return normalized
