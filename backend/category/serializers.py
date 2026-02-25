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
            "trade_type", "description", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "slug", "created_at", "updated_at"]


class CategorySerializer(serializers.ModelSerializer):
    price_types = PriceTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            "id", "name", "slug", "description",
            "created_at", "updated_at", "price_types",
        ]
        read_only_fields = ["id", "slug", "created_at", "updated_at"]


class CategoryListSerializer(serializers.ModelSerializer):
    price_type_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "description", "created_at", "updated_at", "price_type_count"]
        read_only_fields = fields
