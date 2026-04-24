from rest_framework import serializers

from core.utils import validate_uploaded_image, MAX_ASSET_SIZE
from .canvas_sync import sync_template_dimensions_from_background
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
            "config_json",
            "canvas_width",
            "canvas_height",
            "orientation",
            "is_active",
            "publish_order",
            "telegram_caption_template",
            "telegram_buttons_json",
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

    def create(self, validated_data):
        instance = super().create(validated_data)
        if sync_template_dimensions_from_background(instance):
            instance.save(
                update_fields=["canvas_width", "canvas_height", "config", "updated_at"]
            )
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        if "image" in validated_data and validated_data.get("image"):
            if sync_template_dimensions_from_background(instance):
                instance.save(
                    update_fields=["canvas_width", "canvas_height", "config", "updated_at"]
                )
        return instance
