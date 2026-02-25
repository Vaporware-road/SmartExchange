from rest_framework import serializers

from .models import PriceTemplate


class PriceTemplateSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True, default=None)
    special_price_type_name = serializers.CharField(
        source="special_price_type.name", read_only=True, default=None
    )

    class Meta:
        model = PriceTemplate
        fields = [
            "id",
            "name",
            "template_type",
            "category",
            "category_name",
            "special_price_type",
            "special_price_type_name",
            "background_image",
            "logo_image",
            "watermark_image",
            "is_active",
            "notes",
            "created_at",
            "updated_at",
        ]
