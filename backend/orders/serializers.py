from rest_framework import serializers

from bot_gateway.models import Platform
from orders.models import OrderIntake


class OrderIntakeSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source="customer.display_name", read_only=True)
    customer_uuid = serializers.UUIDField(source="customer.uuid", read_only=True)
    customer_username = serializers.CharField(source="customer.username", read_only=True)
    customer_phone = serializers.SerializerMethodField()
    contact_phone = serializers.SerializerMethodField()
    telegram_chat_id = serializers.SerializerMethodField()
    category_name = serializers.CharField(source="category.name", read_only=True)
    price_type_name = serializers.CharField(
        source="price_type.name", read_only=True, allow_null=True
    )

    class Meta:
        model = OrderIntake
        fields = [
            "uuid",
            "platform",
            "status",
            "trade_type",
            "category",
            "category_name",
            "price_type",
            "price_type_name",
            "amount",
            "currency_code",
            "customer_note",
            "admin_note",
            "customer_name",
            "customer_uuid",
            "customer_username",
            "customer_phone",
            "contact_phone",
            "telegram_chat_id",
            "source_metadata",
            "reviewed_at",
            "created_at",
        ]
        read_only_fields = fields

    def get_contact_phone(self, obj):
        meta = obj.source_metadata or {}
        if meta.get("customer_phone"):
            return str(meta["customer_phone"])
        if obj.platform in (Platform.WEB, Platform.WHATSAPP):
            return obj.customer.whatsapp_phone or ""
        return ""

    def get_telegram_chat_id(self, obj):
        if obj.platform != Platform.TELEGRAM:
            return None
        chat_id = obj.customer.telegram_chat_id
        if chat_id is None:
            meta = obj.source_metadata or {}
            chat_id = meta.get("telegram_chat_id")
        return chat_id

    def get_customer_phone(self, obj):
        """Backward-compatible: contact phone, not Telegram chat id."""
        return self.get_contact_phone(obj)


class OrderIntakeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderIntake
        fields = [
            "trade_type",
            "category",
            "price_type",
            "amount",
            "currency_code",
            "customer_note",
        ]

    def create(self, validated_data):
        customer = self.context["customer"]
        request = self.context.get("request")
        metadata = {"source": "bot_webapp"}
        if customer.display_name:
            metadata["customer_name"] = customer.display_name
        if customer.username:
            metadata["telegram_username"] = customer.username
        if customer.telegram_chat_id is not None:
            metadata["telegram_chat_id"] = customer.telegram_chat_id
        if request:
            metadata["user_agent"] = request.headers.get("User-Agent", "")[:500]
        return OrderIntake.objects.create(
            customer=customer,
            platform=customer.platform,
            source_metadata=metadata,
            **validated_data,
        )


class OrderIntakeReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderIntake
        fields = ["status", "admin_note"]

    def validate_status(self, value):
        allowed = {
            OrderIntake.Status.APPROVED,
            OrderIntake.Status.REJECTED,
            OrderIntake.Status.CANCELLED,
        }
        if value not in allowed:
            raise serializers.ValidationError("Invalid review status")
        return value
