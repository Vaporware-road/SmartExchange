"""Django admin for Instagram Hub — set App ID and App Secret for OAuth."""

from django import forms
from django.contrib import admin
from django.utils.html import format_html

from .models import InstagramConfig


class InstagramConfigAdminForm(forms.ModelForm):
    """Form with optional plain App secret field; encrypted field is not edited directly."""

    app_secret_plain = forms.CharField(
        required=False,
        strip=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Leave blank to keep current secret"}),
        help_text="Meta App Secret. Leave blank to keep the existing value.",
    )

    class Meta:
        model = InstagramConfig
        fields = [
            "name",
            "is_active",
            "app_id",
            "ig_user_id",
            "access_token_encrypted",
            "token_expires_at",
            "oauth_state",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Don't show raw encrypted value
        if "access_token_encrypted" in self.fields:
            self.fields["access_token_encrypted"].widget.attrs["readonly"] = True

    def save(self, commit=True):
        instance = super().save(commit=False)
        plain = (self.cleaned_data.get("app_secret_plain") or "").strip()
        if plain:
            instance.set_app_secret(plain)
        if commit:
            instance.save()
        return instance


@admin.register(InstagramConfig)
class InstagramConfigAdmin(admin.ModelAdmin):
    form = InstagramConfigAdminForm
    list_display = ("name", "app_id_display", "has_token", "is_active", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("name", "app_id")
    readonly_fields = ("token_expires_at", "oauth_state", "created_at", "updated_at")
    fieldsets = (
        (None, {"fields": ("name", "is_active")}),
        (
            "Meta / Facebook App (required for OAuth)",
            {
                "fields": ("app_id", "app_secret_plain"),
                "description": "App ID and App Secret from your Meta App (developers.facebook.com). "
                "App Secret is stored encrypted. Leave App Secret blank to keep the existing value.",
            },
        ),
        (
            "OAuth / Token (filled by Connect flow)",
            {
                "fields": ("ig_user_id", "access_token_encrypted", "token_expires_at", "oauth_state"),
            },
        ),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

    def app_id_display(self, obj):
        if not (obj.app_id or "").strip():
            return format_html('<span style="color: #999;">—</span>')
        return (obj.app_id or "")[:16] + "…" if len(obj.app_id or "") > 16 else (obj.app_id or "")

    app_id_display.short_description = "App ID"

    def has_token(self, obj):
        return bool(obj.get_decrypted_token() and (obj.ig_user_id or "").strip())

    has_token.boolean = True
    has_token.short_description = "Has token"
