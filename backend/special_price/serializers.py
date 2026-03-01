from rest_framework import serializers

from category.serializers import CurrencySerializer
from .models import SpecialPriceHistory, SpecialPriceType


class SpecialPriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialPriceHistory
        fields = ["id", "special_price_type", "price", "created_at", "updated_at", "notes"]
        read_only_fields = ["id", "special_price_type", "created_at", "updated_at"]


class SpecialPriceTypeSerializer(serializers.ModelSerializer):
    source_currency = CurrencySerializer(read_only=True)
    target_currency = CurrencySerializer(read_only=True)
    source_currency_id = serializers.PrimaryKeyRelatedField(
        queryset=SpecialPriceType.source_currency.field.related_model.objects.all(),
        source="source_currency",
        write_only=True,
    )
    target_currency_id = serializers.PrimaryKeyRelatedField(
        queryset=SpecialPriceType.target_currency.field.related_model.objects.all(),
        source="target_currency",
        write_only=True,
    )
    latest_price = serializers.SerializerMethodField()

    class Meta:
        model = SpecialPriceType
        fields = [
            "id", "name", "slug", "icon",
            "source_currency", "target_currency",
            "source_currency_id", "target_currency_id",
            "trade_type", "description",
            "created_at", "updated_at",
            "latest_price",
        ]
        read_only_fields = ["id", "slug", "created_at", "updated_at"]

    def get_latest_price(self, obj):
        latest = obj.special_price_histories.order_by("-created_at").first()
        if latest:
            return {
                "id": latest.id,
                "price": str(latest.price),
                "created_at": latest.created_at,
            }
        return None


class SpecialPriceUpdateSerializer(serializers.Serializer):
    price = serializers.DecimalField(max_digits=20, decimal_places=2, min_value=0)
    notes = serializers.CharField(required=False, allow_blank=True, default="")
