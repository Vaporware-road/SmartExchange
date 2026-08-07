from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="InstagramConfig",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(default="Default", help_text="Config label", max_length=128)),
                ("app_id", models.CharField(blank=True, help_text="Facebook App ID", max_length=64)),
                ("app_secret_encrypted", models.TextField(blank=True, help_text="Facebook App Secret (encrypted)")),
                ("ig_user_id", models.CharField(blank=True, help_text="Instagram Business Account ID", max_length=64)),
                ("access_token_encrypted", models.TextField(blank=True, help_text="Long-lived access token (encrypted)")),
                ("token_expires_at", models.DateTimeField(blank=True, help_text="When the token expires", null=True)),
                ("oauth_state", models.CharField(blank=True, help_text="CSRF state for OAuth", max_length=128)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(default=timezone.now)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Instagram Config",
                "verbose_name_plural": "Instagram Configs",
                "ordering": ["-is_active", "name"],
            },
        ),
    ]
