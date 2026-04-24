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
        read_only_fields = ["id", "category", "slug", "created_at", "updated_at"]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        category = attrs.get("category")
        view = self.context.get("view")

        if not category and view is not None:
            category_pk = view.kwargs.get("category_pk")
            if category_pk:
                category = Category.objects.filter(pk=category_pk).first()
                if not category:
                    raise serializers.ValidationError({"category": ["Category not found."]})

        if not category:
            return attrs

        instance = getattr(self, "instance", None)
        name = attrs.get("name", getattr(instance, "name", None))
        source_currency = attrs.get("source_currency", getattr(instance, "source_currency", None))
        target_currency = attrs.get("target_currency", getattr(instance, "target_currency", None))
        trade_type = attrs.get("trade_type", getattr(instance, "trade_type", None))

        qs = PriceType.objects.filter(category=category)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)

        errors = {}
        if name and qs.filter(name=name).exists():
            errors["name"] = ["A price type with this name already exists in this category."]

        if source_currency and target_currency and trade_type and qs.filter(
            source_currency=source_currency,
            target_currency=target_currency,
            trade_type=trade_type,
        ).exists():
            errors["trade_type"] = [
                "A price type with this source/target currency and trade type already exists in this category."
            ]

        if errors:
            raise serializers.ValidationError(errors)

        return attrs


class PriceTypeExplorerSerializer(serializers.ModelSerializer):
    """Nested in Category Explorer: includes latest_price from history."""
    source_currency = CurrencySerializer(read_only=True)
    target_currency = CurrencySerializer(read_only=True)
    latest_price = serializers.SerializerMethodField()
    latest_price_at = serializers.SerializerMethodField()
    change_value = serializers.SerializerMethodField()
    change_percent = serializers.SerializerMethodField()

    class Meta:
        model = PriceType
        fields = [
            "id", "name", "slug", "source_currency", "target_currency",
            "trade_type", "is_active", "order",
            "latest_price", "latest_price_at", "change_value", "change_percent",
        ]

    def _get_recent_histories(self, obj):
        histories = getattr(obj, "_latest_histories", None)
        if histories is not None:
            return histories
        if hasattr(obj, "price_histories"):
            return list(obj.price_histories.all()[:2])
        return []

    def get_latest_price(self, obj):
        histories = self._get_recent_histories(obj)
        first = histories[0] if histories else None
        return first.price if first else None

    def get_latest_price_at(self, obj):
        histories = self._get_recent_histories(obj)
        first = histories[0] if histories else None
        return first.created_at if first else None

    def get_change_value(self, obj):
        histories = self._get_recent_histories(obj)
        if len(histories) < 2:
            return None
        latest = histories[0].price
        previous = histories[1].price
        return latest - previous

    def get_change_percent(self, obj):
        histories = self._get_recent_histories(obj)
        if len(histories) < 2:
            return None
        latest = histories[0].price
        previous = histories[1].price
        if previous == 0:
            return None
        return ((latest - previous) / previous) * 100


class CategorySerializer(serializers.ModelSerializer):
    price_types = PriceTypeSerializer(many=True, read_only=True)
    last_used_template = serializers.IntegerField(source="last_used_template_id", read_only=True)
    template_media_url = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            "id", "name", "slug", "description",
            "telegram_message_description", "telegram_media_url", "inline_buttons",
            "last_used_template", "template_media_url",
            "created_at", "updated_at", "price_types",
        ]
        read_only_fields = ["id", "slug", "created_at", "updated_at"]

    def get_template_media_url(self, obj):
        template = getattr(obj, "last_used_template", None)
        if not template or not getattr(template, "image", None):
            return ""
        try:
            return template.image.url
        except Exception:
            return ""


class CategoryListSerializer(serializers.ModelSerializer):
    price_type_count = serializers.IntegerField(read_only=True)
    last_used_template = serializers.IntegerField(source="last_used_template_id", read_only=True)
    template_media_url = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            "id", "name", "slug", "description",
            "telegram_message_description", "telegram_media_url", "inline_buttons",
            "last_used_template", "template_media_url",
            "created_at", "updated_at", "price_type_count",
        ]
        read_only_fields = fields

    def get_template_media_url(self, obj):
        template = getattr(obj, "last_used_template", None)
        if not template or not getattr(template, "image", None):
            return ""
        try:
            return template.image.url
        except Exception:
            return ""


class CategoryExplorerSerializer(serializers.ModelSerializer):
    """List with nested price_types and latest_price for Explorer UI."""
    price_types = PriceTypeExplorerSerializer(many=True, read_only=True)
    price_type_count = serializers.SerializerMethodField()
    last_used_template = serializers.IntegerField(source="last_used_template_id", read_only=True)
    template_media_url = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            "id", "name", "slug", "description",
            "telegram_message_description", "telegram_media_url", "inline_buttons",
            "last_used_template", "template_media_url",
            "created_at", "updated_at", "price_type_count", "price_types",
        ]
        read_only_fields = fields

    def get_price_type_count(self, obj):
        pts = getattr(obj, "price_types", None)
        if pts is not None and hasattr(pts, "__len__"):
            return len(pts)
        return getattr(obj, "price_type_count", 0)

    def get_template_media_url(self, obj):
        template = getattr(obj, "last_used_template", None)
        if not template or not getattr(template, "image", None):
            return ""
        try:
            return template.image.url
        except Exception:
            return ""
