"""Instagram Hub models: InstagramConfig for OAuth and publish."""

from django.db import models
from django.utils import timezone

from instagram_hub.encryption import decrypt_token, encrypt_token


class InstagramConfig(models.Model):
    """
    Instagram (Meta Graph API) credentials. Token and app secret encrypted at rest.
    Single active config used for posting; OAuth flow populates token and ig_user_id.
    """

    name = models.CharField(max_length=128, default="Default", help_text="Config label")
    app_id = models.CharField(max_length=64, blank=True, help_text="Facebook App ID")
    app_secret_encrypted = models.TextField(blank=True, help_text="Facebook App Secret (encrypted)")
    ig_user_id = models.CharField(max_length=64, blank=True, help_text="Instagram Business Account ID")
    access_token_encrypted = models.TextField(blank=True, help_text="Long-lived access token (encrypted)")
    token_expires_at = models.DateTimeField(null=True, blank=True, help_text="When the token expires")
    oauth_state = models.CharField(max_length=128, blank=True, help_text="CSRF state for OAuth")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Instagram Config"
        verbose_name_plural = "Instagram Configs"
        ordering = ["-is_active", "name"]

    def __str__(self):
        return f"{self.name} (active={self.is_active})"

    def get_decrypted_token(self) -> str:
        return decrypt_token(self.access_token_encrypted)

    def set_access_token(self, plain_token: str) -> None:
        self.access_token_encrypted = encrypt_token((plain_token or "").strip())

    def get_app_secret(self) -> str:
        return decrypt_token(self.app_secret_encrypted)

    def set_app_secret(self, plain: str) -> None:
        self.app_secret_encrypted = encrypt_token((plain or "").strip())
