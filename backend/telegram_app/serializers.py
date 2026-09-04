from rest_framework import serializers

from .models import TelegramBot, TelegramChannel, DefaultMessageSettings, AutoPostConfig


class TelegramBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramBot
        fields = [
            "id",
            "name",
            "display_name",
            "notes",
            "is_active",
            "restrict_to_known_channels",
            "log_all_messages",
            "gateway_enabled",
            "default_category",
            "order_button_text",
            "webhook_secret_token",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "webhook_secret_token", "created_at", "updated_at"]


class TelegramBotDetailSerializer(serializers.ModelSerializer):
    """Full serializer for create/update - includes token."""

    class Meta:
        model = TelegramBot
        fields = [
            "id",
            "name",
            "token",
            "display_name",
            "notes",
            "is_active",
            "restrict_to_known_channels",
            "log_all_messages",
            "gateway_enabled",
            "default_category",
            "order_button_text",
            "webhook_secret_token",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "webhook_secret_token", "created_at", "updated_at"]
        extra_kwargs = {"token": {"write_only": True}}


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


class SendMessageSerializer(serializers.Serializer):
    bot_id = serializers.PrimaryKeyRelatedField(
        queryset=TelegramBot.objects.filter(is_active=True), write_only=True
    )
    channel_id = serializers.PrimaryKeyRelatedField(
        queryset=TelegramChannel.objects.filter(is_active=True, bot__is_active=True),
        write_only=True,
    )
    message = serializers.CharField(
        max_length=4096, trim_whitespace=False, required=False, allow_blank=True
    )
    banner_key = serializers.CharField(
        max_length=64, required=False, allow_blank=True, default=""
    )
    cash_price = serializers.DecimalField(
        max_digits=20, decimal_places=2, min_value=0, required=False, allow_null=True
    )
    account_price = serializers.DecimalField(
        max_digits=20, decimal_places=2, min_value=0, required=False, allow_null=True
    )
    price = serializers.DecimalField(
        max_digits=20, decimal_places=2, min_value=0, required=False, allow_null=True
    )

    def validate_message(self, value):
        if value is None:
            return ""
        return value or ""

    def validate(self, attrs):
        channel = attrs["channel_id"]
        bot = attrs["bot_id"]
        if channel.bot_id != bot.id:
            raise serializers.ValidationError(
                {"channel_id": "Channel does not belong to the selected bot."}
            )
        attrs["bot"] = bot
        attrs["channel"] = channel
        message = (attrs.get("message") or "").strip()
        banner_key = (attrs.get("banner_key") or "").strip()
        cash = attrs.get("cash_price")
        account = attrs.get("account_price")
        single = attrs.get("price")
        has_banner = banner_key and banner_key != "none"
        has_double = cash is not None or account is not None
        has_single = single is not None
        if not message and not has_banner and not has_double and not has_single:
            raise serializers.ValidationError(
                {"message": "Provide message text and/or banner/prices."}
            )
        return attrs


class DefaultMessageSettingsSerializer(serializers.ModelSerializer):
    bot_name = serializers.CharField(source="bot.name", read_only=True)

    class Meta:
        model = DefaultMessageSettings
        fields = [
            "id",
            "bot",
            "bot_name",
            "default_caption",
            "default_buttons",
            "active",
            "created_at",
            "updated_at",
        ]


class AutoPostConfigSerializer(serializers.ModelSerializer):
    channel_name = serializers.CharField(source="channel.name", read_only=True)
    target_type = serializers.SerializerMethodField()

    class Meta:
        model = AutoPostConfig
        fields = [
            "id",
            "channel",
            "channel_name",
            "category",
            "special_price_type",
            "time_of_day",
            "timezone",
            "enabled",
            "notes",
            "created_at",
            "updated_at",
            "target_type",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "target_type"]

    def get_target_type(self, obj):
        if obj.category_id:
            return "category"
        if obj.special_price_type_id:
            return "special"
        return "none"
