import re

from rest_framework import serializers

from bot_gateway.models import BotCustomer, Platform
from category.models import Category, PriceType
from orders.models import OrderIntake
from orders.serializers import OrderIntakeSerializer


def _normalize_phone(value: str) -> str:
    return re.sub(r"[^\d+]", "", (value or "").strip())


class PublicOrderIntakeCreateSerializer(serializers.Serializer):
    customer_name = serializers.CharField(max_length=255)
    customer_phone = serializers.CharField(max_length=32)
    trade_type = serializers.ChoiceField(choices=OrderIntake.TradeType.choices)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    price_type = serializers.PrimaryKeyRelatedField(
        queryset=PriceType.objects.filter(is_active=True),
        required=False,
        allow_null=True,
    )
    amount = serializers.DecimalField(max_digits=18, decimal_places=4, min_value=0)
    currency_code = serializers.CharField(max_length=16, required=False, allow_blank=True)
    customer_note = serializers.CharField(required=False, allow_blank=True)

    def validate_customer_phone(self, value):
        phone = _normalize_phone(value)
        if len(phone) < 8:
            raise serializers.ValidationError("Enter a valid phone number.")
        return phone

    def validate(self, attrs):
        price_type = attrs.get("price_type")
        category = attrs["category"]
        trade_type = attrs["trade_type"]
        if price_type:
            if price_type.category_id != category.id:
                raise serializers.ValidationError(
                    {"price_type": "Price type does not belong to the selected category."}
                )
            if price_type.trade_type != trade_type:
                raise serializers.ValidationError(
                    {"price_type": "Price type does not match the selected trade direction."}
                )
        return attrs

    def _upsert_customer(self, name: str, phone: str) -> BotCustomer:
        from django.utils import timezone

        customer, _ = BotCustomer.objects.get_or_create(
            platform=Platform.WEB,
            whatsapp_phone=phone,
            defaults={"display_name": name},
        )
        update_fields = ["last_seen_at"]
        customer.last_seen_at = timezone.now()
        if name and customer.display_name != name:
            customer.display_name = name
            update_fields.append("display_name")
        customer.save(update_fields=update_fields)
        return customer

    def create(self, validated_data):
        request = self.context.get("request")
        name = validated_data.pop("customer_name").strip()
        phone = validated_data.pop("customer_phone")
        customer = self._upsert_customer(name, phone)
        metadata = {
            "source": "public_web",
            "customer_name": name,
            "customer_phone": phone,
        }
        if request:
            metadata["user_agent"] = request.headers.get("User-Agent", "")[:500]
        order = OrderIntake.objects.create(
            customer=customer,
            platform=Platform.WEB,
            source_metadata=metadata,
            **validated_data,
        )
        return order

    def to_representation(self, instance):
        return OrderIntakeSerializer(instance).data
