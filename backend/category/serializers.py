from rest_framework import serializers

from .models import Category, Currency, PriceType


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["id", "code", "name", "symbol"]


class PriceTypeSerializer(serializers.ModelSerializer):
    source_currency = CurrencySerializer(read_only=True)
    target_currency = CurrencySerializer(read_only=True)
    source_currency_id = serializers.PrimaryKeyRelatedField(
        queryset=Currency.objects.all(), source="source_currency", write_only=True
    )
    target_currency_id = serializers.PrimaryKeyRelatedField(
        queryset=Currency.objects.all(), source="target_currency", write_only=True
    )

    class Meta:
        model = PriceType
        fields = [
            "id", "category", "name", "slug", "source_currency", "target_currency",
            "source_currency_id", "target_currency_id",
            "trade_type", "description", "is_active", "order",
            "created_at", "updated_at",
        ]
        read_only_fields = ["id", "slug", "created_at", "updated_at"]


class PriceTypeExplorerSerializer(serializers.ModelSerializer):
    """Nested in Category Explorer: includes latest_price from history."""
    source_currency = CurrencySerializer(read_only=True)
    target_currency = CurrencySerializer(read_only=True)
    latest_price = serializers.SerializerMethodField()
    latest_price_at = serializers.SerializerMethodField()

    class Meta:
        model = PriceType
        fields = [
            "id", "name", "slug", "source_currency", "target_currency",
            "trade_type", "is_active", "order",
            "latest_price", "latest_price_at",
        ]

    def get_latest_price(self, obj):
        first = getattr(obj, "_latest_history", None) or (
            obj.price_histories.first() if hasattr(obj, "price_histories") else None
        )
        return first.price if first else None

    def get_latest_price_at(self, obj):
        first = getattr(obj, "_latest_history", None) or (
            obj.price_histories.first() if hasattr(obj, "price_histories") else None
        )
        return first.created_at if first else None


class CategorySerializer(serializers.ModelSerializer):
    price_types = PriceTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            "id", "name", "slug", "description",
            "telegram_message_description", "telegram_media_url", "inline_buttons",
            "created_at", "updated_at", "price_types",
        ]
        read_only_fields = ["id", "slug", "created_at", "updated_at"]


class CategoryListSerializer(serializers.ModelSerializer):
    price_type_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = [
            "id", "name", "slug", "description",
            "telegram_message_description", "telegram_media_url", "inline_buttons",
            "created_at", "updated_at", "price_type_count",
        ]
        read_only_fields = fields


class CategoryExplorerSerializer(serializers.ModelSerializer):
    """List with nested price_types and latest_price for Explorer UI."""
    price_types = PriceTypeExplorerSerializer(many=True, read_only=True)
    price_type_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            "id", "name", "slug", "description",
            "telegram_message_description", "telegram_media_url", "inline_buttons",
            "created_at", "updated_at", "price_type_count", "price_types",
        ]
        read_only_fields = fields

    def get_price_type_count(self, obj):
        pts = getattr(obj, "price_types", None)
        if pts is not None and hasattr(pts, "__len__"):
            return len(pts)
        return getattr(obj, "price_type_count", 0)
