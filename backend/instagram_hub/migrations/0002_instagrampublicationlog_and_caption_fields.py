# Generated manually for Instagram Hub parity plan

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instagram_hub", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="instagramconfig",
            name="feed_caption_suffix",
            field=models.TextField(
                blank=True,
                default="",
                help_text="Optional text appended to feed captions after finalize (e.g. contact line). Max length enforced at publish time.",
            ),
        ),
        migrations.AddField(
            model_name="instagramconfig",
            name="feed_hashtags",
            field=models.TextField(
                blank=True,
                default="",
                help_text="Optional hashtags for feed posts (plain text, e.g. #exchange #rates). Appended after caption suffix.",
            ),
        ),
        migrations.CreateModel(
            name="InstagramPublicationLog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("kind", models.CharField(choices=[("feed", "Feed"), ("story", "Story")], db_index=True, max_length=16)),
                ("success", models.BooleanField(db_index=True, default=False)),
                ("error_message", models.TextField(blank=True, default="")),
                ("media_id", models.CharField(blank=True, default="", max_length=128)),
                ("container_id", models.CharField(blank=True, default="", max_length=128)),
                ("category_ids", models.JSONField(blank=True, default=list)),
                ("special_price_history_ids", models.JSONField(blank=True, default=list)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                "verbose_name": "Instagram publication log",
                "verbose_name_plural": "Instagram publication logs",
                "ordering": ["-created_at"],
            },
        ),
    ]
