from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser, UserActivityLog


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(
            username=attrs["username"],
            password=attrs["password"],
        )
        if not user or not user.is_active:
            raise serializers.ValidationError("Invalid credentials.")
        attrs["user"] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "full_name", "role", "is_active", "date_joined"]
        read_only_fields = fields


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = ["username", "password", "full_name", "role", "is_active"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        username = validated_data.pop("username")
        user = CustomUser.objects.create_user(username, password=password, **validated_data)
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, required=False)

    class Meta:
        model = CustomUser
        fields = ["full_name", "role", "is_active", "password"]

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserActivityLogSerializer(serializers.ModelSerializer):
    user_display = serializers.SerializerMethodField()

    class Meta:
        model = UserActivityLog
        fields = ["id", "user", "user_display", "action_type", "ip_address", "user_agent", "details", "created_at"]

    def get_user_display(self, obj):
        if obj.user:
            return obj.user.get_full_name() or obj.user.username
        return None


class TokenRefreshWithVersionSerializer(TokenRefreshSerializer):
    """Add token_version to the new access token when refreshing."""

    def validate(self, attrs):
        data = super().validate(attrs)
        # Re-build access token with token_version so force-logout works after refresh
        try:
            refresh = RefreshToken(attrs["refresh"])
            user_id = refresh.get("user_id")
            if not user_id:
                return data
            user = CustomUser.objects.filter(pk=user_id).first()
            if not user:
                return data
            new_refresh = RefreshToken.for_user(user)
            new_refresh.access_token["token_version"] = user.token_version
            data["access"] = str(new_refresh.access_token)
        except Exception:
            pass
        return data
