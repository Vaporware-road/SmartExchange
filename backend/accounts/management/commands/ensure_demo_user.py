import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = (
        "Create the demo account (role=management, unusable password) used by the "
        "public demo-login endpoint. Idempotent: on an existing user it fixes "
        "role/is_active/staff/superuser to demo settings without touching the password."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--username",
            default=os.environ.get("DEMO_USERNAME", "demo"),
        )

    def handle(self, *args, **options):
        # Strip CR/LF/spaces from env-file values (Windows CRLF often breaks matching).
        username = (str(options["username"] or "")).strip().replace("\r", "")
        if not username:
            username = "demo"

        user = User.objects.filter(username=username).first()
        if user:
            updated = False
            if not user.is_active:
                user.is_active = True
                updated = True
            if user.role != User.ROLE_MANAGEMENT:
                user.role = User.ROLE_MANAGEMENT
                updated = True
            if user.is_staff:
                user.is_staff = False
                updated = True
            if user.is_superuser:
                user.is_superuser = False
                updated = True
            if updated:
                user.save()
                self.stdout.write(
                    self.style.WARNING(
                        f'User "{username}" already existed; fixed role/is_active/staff to demo (management, active, non-staff).'
                    )
                )
            else:
                self.stdout.write(
                    self.style.NOTICE(
                        f'User "{username}" already exists as the demo account; no changes needed.'
                    )
                )
            return

        # password=None -> set_password(None) -> unusable password, so the account can
        # only be entered through the demo-login endpoint (no password guessing).
        User.objects.create_user(
            username=username,
            password=None,
            role=User.ROLE_MANAGEMENT,
            full_name="Demo User",
            is_active=True,
        )
        self.stdout.write(
            self.style.SUCCESS(
                f'Created demo user "{username}" (role=management, unusable password). '
                f"Access via the demo-login endpoint."
            )
        )
