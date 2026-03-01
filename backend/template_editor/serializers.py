from rest_framework import serializers

from core.utils import validate_uploaded_image, MAX_ASSET_SIZE
from .models import Template


class TemplateSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True, default=None)
    special_price_type_name = serializers.CharField(
        source="special_price_type.name", read_only=True, default=None
    )

    class Meta:
        model = Template
        fields = [
            "id",
            "name",
            "category",
            "category_name",
            "special_price_type",
            "special_price_type_name",
            "image",
            "config",
            "created_at",
            "updated_at",
        ]

    def validate_image(self, value):
        if value and hasattr(value, "read"):
            try:
                validate_uploaded_image(value, max_size=MAX_ASSET_SIZE)
            except ValueError as e:
                raise serializers.ValidationError(str(e))
        return value
