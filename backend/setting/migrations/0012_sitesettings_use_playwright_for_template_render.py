# Generated manually for use_playwright_for_template_render

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("setting", "0011_sitesettings_prices_webhook_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="sitesettings",
            name="use_playwright_for_template_render",
            field=models.BooleanField(
                default=False,
                help_text=(
                    "If enabled, Telegram template boards are rendered via headless Vue "
                    "screenshot (Playwright). Falls back to Pillow on error."
                ),
            ),
        ),
    ]
