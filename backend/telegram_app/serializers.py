from rest_framework import serializers

from .models import TelegramBot, TelegramChannel, DefaultMessageSettings


class TelegramBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramBot
        fields = ["id", "name", "is_active", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class TelegramBotDetailSerializer(serializers.ModelSerializer):
    """Full serializer for create/update - includes token."""

    class Meta:
        model = TelegramBot
        fields = ["id", "name", "token", "is_active", "created_at", "updated_at"]
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
    message = serializers.CharField(max_length=4096, trim_whitespace=False)

    def validate_message(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Message cannot be empty.")
        return value

    def validate(self, attrs):
        channel = attrs["channel_id"]
        bot = attrs["bot_id"]
        if channel.bot_id != bot.id:
            raise serializers.ValidationError(
                {"channel_id": "Channel does not belong to the selected bot."}
            )
        attrs["bot"] = bot
        attrs["channel"] = channel
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
