from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser, UserActivityLog
from .plans import COLLABORATION_CHOICES, PLAN_BRONZE, PLAN_CHOICES, normalize_plan
from .tokens import issue_tokens_for_user
from .trial import trial_expires_at


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
    trial_days_remaining = serializers.SerializerMethodField()

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
            "telegram_username",
            "website",
            "collaboration_type",
            "registered_by",
            "registered_by_name",
            "owner",
            "owner_name",
            "owner_username",
            "sub_role",
            "plan",
            "role",
            "trial_started_at",
            "trial_expires_at",
            "trial_expiry_notified_at",
            "trial_days_remaining",
            "is_active",
            "date_joined",
            "telegram_bot_token_masked",
        ]
        read_only_fields = fields

    registered_by_name = serializers.SerializerMethodField()
    owner_name = serializers.SerializerMethodField()
    owner_username = serializers.SerializerMethodField()

    def get_trial_days_remaining(self, obj):
        from fleet.services import days_remaining

        return days_remaining(obj)

    def get_registered_by_name(self, obj):
        staff = obj.registered_by
        if staff is None:
            return ""
        return staff.get_full_name() or staff.username

    def get_owner_name(self, obj):
        owner = obj.owner
        if owner is None:
            return ""
        return owner.get_full_name() or owner.username

    def get_owner_username(self, obj):
        owner = obj.owner
        if owner is None:
            return ""
        return owner.username

    def get_trial_days_remaining(self, obj):
        from django.utils import timezone

        if obj.trial_expires_at is None:
            return None
        return max(0, (obj.trial_expires_at - timezone.now()).days)

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
    # A BotFather token is required for client accounts (they own a customer bot).
    # Delegated operators (sub_role operator/head_operator) do not own a bot, so
    # the token is optional for them — enforced in validate().
    telegram_bot_token = serializers.CharField(write_only=True, required=False, allow_blank=True, default="")
    website = serializers.URLField(max_length=256, allow_blank=True, required=False, default="")
    collaboration_type = serializers.ChoiceField(choices=COLLABORATION_CHOICES, required=False, allow_blank=True, default="")
    plan = serializers.ChoiceField(choices=PLAN_CHOICES, default=PLAN_BRONZE, required=False)
    sub_role = serializers.ChoiceField(choices=CustomUser.SUB_ROLE_CHOICES, default=CustomUser.SUB_ROLE_ADMIN, required=False)
    owner_username = serializers.CharField(max_length=150, allow_blank=True, required=False, default="")
    telegram_username = serializers.CharField(max_length=128, allow_blank=True, required=False, default="")

    def validate_email(self, value):
        email = value.strip().lower()
        if CustomUser.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return email

    def validate(self, attrs):
        sub_role = attrs.get("sub_role") or CustomUser.SUB_ROLE_ADMIN
        delegated = sub_role in (CustomUser.SUB_ROLE_OPERATOR, CustomUser.SUB_ROLE_HEAD_OPERATOR)
        owner_username = (attrs.get("owner_username") or "").strip()
        token = (attrs.get("telegram_bot_token") or "").strip()
        if delegated:
            if not owner_username:
                raise serializers.ValidationError(
                    {"owner_username": "Owner username is required for delegated operators."}
                )
            attrs["telegram_bot_token"] = ""
        else:
            if not token:
                raise serializers.ValidationError(
                    {"telegram_bot_token": "Bot token is required for client accounts."}
                )
            attrs["owner_username"] = ""
        attrs["owner_username"] = owner_username
        return attrs

    def _resolve_owner(self, username):
        if not username:
            return None
        owner = CustomUser.objects.filter(username__iexact=username).first()
        if owner is None:
            raise serializers.ValidationError(
                {"owner_username": "No user with this username exists."}
            )
        return owner

    def create(self, validated_data):
        import secrets

        token = validated_data.pop("telegram_bot_token")
        email = validated_data["email"]
        password = secrets.token_urlsafe(12)
        username = unique_username_from_email(email)
        plan = normalize_plan(validated_data.get("plan"))
        sub_role = validated_data.get("sub_role") or CustomUser.SUB_ROLE_ADMIN
        delegated = sub_role in (CustomUser.SUB_ROLE_OPERATOR, CustomUser.SUB_ROLE_HEAD_OPERATOR)
        owner = self._resolve_owner((validated_data.get("owner_username") or "").strip())
        registered_by = validated_data.pop("registered_by", None) or getattr(self.context.get("request"), "user", None)
        from django.utils import timezone

        started_at = timezone.now()
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
            telegram_username=(validated_data.get("telegram_username") or "").strip(),
            website=(validated_data.get("website") or "").strip(),
            collaboration_type=(validated_data.get("collaboration_type") or "").strip(),
            plan=plan,
            sub_role=sub_role,
            owner=owner,
            role=CustomUser.ROLE_EMPLOYEE if delegated else CustomUser.ROLE_MANAGEMENT,
            is_active=True,
            trial_started_at=started_at,
            trial_expires_at=trial_expires_at(started_at),
        )
        user.registered_by = registered_by
        user.save(update_fields=["registered_by"])
        if not delegated:
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
    collaboration_type = serializers.ChoiceField(choices=COLLABORATION_CHOICES, required=False, allow_blank=True)
    sub_role = serializers.ChoiceField(choices=CustomUser.SUB_ROLE_CHOICES, required=False)
    # Owner is referenced by username (friendlier for admins); empty string clears it.
    owner_username = serializers.CharField(max_length=150, allow_blank=True, required=False, default="")
    telegram_username = serializers.CharField(max_length=128, allow_blank=True, required=False, default="")

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
            "telegram_username",
            "website",
            "collaboration_type",
            "sub_role",
            "owner_username",
            "plan",
            "is_active",
            "telegram_bot_token",
        ]

    def validate_owner_username(self, value):
        username = (value or "").strip()
        if not username:
            return ""
        owner = CustomUser.objects.filter(username__iexact=username).first()
        if owner is None:
            raise serializers.ValidationError("No user with this username exists.")
        if self.instance is not None and owner.id == self.instance.id:
            raise serializers.ValidationError("A user cannot be their own owner.")
        return username

    def update(self, instance, validated_data):
        token = validated_data.pop("telegram_bot_token", None)
        if "owner_username" in validated_data:
            username = validated_data.pop("owner_username")
            owner = None
            if username:
                owner = CustomUser.objects.filter(username__iexact=username).first()
                if owner is None:
                    raise serializers.ValidationError(
                        {"owner_username": "No user with this username exists."}
                    )
            validated_data["owner"] = owner
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
