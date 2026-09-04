from django.core.management.base import BaseCommand

from instagram_hub.services.instagram_config import get_instagram_readiness
from instagram_hub.services.image_generator import generate_price_images


class Command(BaseCommand):
    help = "Simulate Instagram pipeline readiness (config, images, publish prerequisites)"

    def add_arguments(self, parser):
        parser.add_argument(
            "--skip-images",
            action="store_true",
            help="Skip Pillow image generation test",
        )

    def handle(self, *args, **options):
        readiness = get_instagram_readiness()
        self.stdout.write("Instagram pipeline simulator")
        self.stdout.write("-" * 40)

        checks = [
            ("App ID configured", readiness["has_app_id"]),
            ("Token + IG user ID", readiness["has_token"]),
            ("Public INSTAGRAM_BASE_URL", readiness["public_base_url_configured"]),
            ("Ready for publish", readiness["ready_for_publish"]),
        ]
        for label, ok in checks:
            style = self.style.SUCCESS if ok else self.style.WARNING
            mark = "OK" if ok else "FAIL"
            self.stdout.write(style(f"  [{mark}] {label}"))

        if readiness["public_base_url"]:
            self.stdout.write(f"  Base URL: {readiness['public_base_url']}")
        else:
            self.stdout.write(self.style.WARNING("  Base URL: (not set)"))

        if readiness["token_expired"]:
            self.stdout.write(self.style.ERROR("  Token: EXPIRED — reconnect from Settings"))
        elif readiness["token_expiring_soon"]:
            days = readiness["days_until_token_expiry"]
            self.stdout.write(self.style.WARNING(f"  Token: expires in {days} day(s) — reconnect soon"))
        elif readiness["days_until_token_expiry"] is not None:
            self.stdout.write(f"  Token: {readiness['days_until_token_expiry']} day(s) remaining")

        for code in readiness["warnings"]:
            self.stdout.write(self.style.WARNING(f"  Warning: {code}"))

        if not options["skip_images"]:
            self.stdout.write("")
            self.stdout.write("Image generation test...")
            result = generate_price_images(
                price_entries=[{"title": "Test", "price": "12345"}],
                theme="dark",
                category_title="Simulator",
            )
            if result and result.get("post_path") and result.get("story_path"):
                self.stdout.write(self.style.SUCCESS(f"  [OK] Post: {result['post_path']}"))
                self.stdout.write(self.style.SUCCESS(f"  [OK] Story: {result['story_path']}"))
            else:
                self.stdout.write(self.style.ERROR("  [FAIL] Image generation failed"))

        self.stdout.write("")
        if readiness["ready_for_publish"]:
            self.stdout.write(self.style.SUCCESS("Instagram is ready for automated publish after finalize."))
        else:
            self.stdout.write(self.style.WARNING("Instagram is NOT fully ready — fix warnings above."))
