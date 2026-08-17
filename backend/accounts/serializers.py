from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser, UserActivityLog
from .plans import PLAN_BRONZE, PLAN_CHOICES, normalize_plan
from .tokens import issue_tokens_for_user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = (attrs.get("username") or "").strip()
        password = attrs.get("password") or ""
        attrs["username"] = username
        request = self.context.get("request")
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if not user or not user.is_active:
            raise serializers.ValidationError("Invalid credentials.")
        attrs["user"] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    telegram_bot_token_masked = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "full_name",
            "exchange_name",
            "country",
            "email",
            "phone",
            "telegram_id",
            "plan",
            "role",
            "is_active",
            "date_joined",
            "telegram_bot_token_masked",
        ]
        read_only_fields = fields

    def get_telegram_bot_token_masked(self, obj):
        bot = obj.telegram_bots.order_by("-created_at").first()
        if bot is None:
            return ""
        token = bot.get_plain_token()
        if not token:
            return ""
        if len(token) <= 8:
            return "••••"
        return f"{token[:4]}…{token[-4:]}"


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


def unique_username_from_email(email):
    local = (email or "").split("@")[0].strip().lower()
    cleaned = "".join(ch for ch in local if ch.isalnum() or ch in "._-")[:140]
    base = cleaned or "user"
    candidate = base
    n = 1
    while CustomUser.objects.filter(username__iexact=candidate).exists():
        candidate = f"{base}{n}"
        n += 1
    return candidate


class ProgrammerRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    exchange_name = serializers.CharField(max_length=255)
    country = serializers.CharField(max_length=120)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=40)
    telegram_id = serializers.CharField(max_length=64, allow_blank=True, required=False, default="")
    telegram_bot_token = serializers.CharField(write_only=True)
    plan = serializers.ChoiceField(choices=PLAN_CHOICES, default=PLAN_BRONZE, required=False)

    def validate_email(self, value):
        email = value.strip().lower()
        if CustomUser.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return email

    def create(self, validated_data):
        import secrets

        token = validated_data.pop("telegram_bot_token")
        email = validated_data["email"]
        password = secrets.token_urlsafe(12)
        username = unique_username_from_email(email)
        plan = normalize_plan(validated_data.get("plan"))
        user = CustomUser.objects.create_user(
            username,
            password=password,
            first_name=validated_data["first_name"].strip(),
            last_name=validated_data["last_name"].strip(),
            exchange_name=validated_data["exchange_name"].strip(),
            country=validated_data["country"].strip(),
            email=email,
            phone=validated_data["phone"].strip(),
            telegram_id=(validated_data.get("telegram_id") or "").strip(),
            plan=plan,
            role=CustomUser.ROLE_MANAGEMENT,
            is_active=True,
        )
        from telegram_app.models import TelegramBot

        TelegramBot.objects.create(
            name=user.exchange_name or username,
            token=token.strip(),
            display_name=user.exchange_name or username,
            owner=user,
            is_active=True,
        )
        user._generated_password = password
        return user


class ProgrammerUserUpdateSerializer(serializers.ModelSerializer):
    telegram_bot_token = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "exchange_name",
            "country",
            "email",
            "phone",
            "telegram_id",
            "plan",
            "is_active",
            "telegram_bot_token",
        ]

    def update(self, instance, validated_data):
        token = validated_data.pop("telegram_bot_token", None)
        if validated_data.get("email"):
            validated_data["email"] = validated_data["email"].strip().lower()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if token:
            from telegram_app.models import TelegramBot

            bot = instance.telegram_bots.order_by("-created_at").first()
            if bot:
                bot.token = token.strip()
                bot.save(update_fields=["token", "updated_at"])
            else:
                TelegramBot.objects.create(
                    name=instance.exchange_name or instance.username,
                    token=token.strip(),
                    owner=instance,
                    is_active=True,
                )
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
        try:
            refresh = RefreshToken(attrs["refresh"])
            user_id = refresh.get("user_id")
            if not user_id:
                return data
            user = CustomUser.objects.filter(pk=user_id).first()
            if not user:
                return data
            impersonator = None
            impersonator_id = refresh.get("impersonator_id")
            if impersonator_id:
                impersonator = CustomUser.objects.filter(pk=impersonator_id).first()
            issued = issue_tokens_for_user(user, impersonator=impersonator)
            data["access"] = str(issued.access_token)
            data["refresh"] = str(issued)
        except Exception:
            pass
        return data
