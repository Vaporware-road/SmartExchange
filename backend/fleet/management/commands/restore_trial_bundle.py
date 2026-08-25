"""Restore a trial bundle onto a customer-server install.

Run on the customer's own VPS, inside their app container, before the first
start of the licensed stack. It refuses to overwrite an install that already
holds data unless --force is given, so a mistyped host cannot destroy a live
customer's database.
"""

from __future__ import annotations

import shutil
import tarfile
import tempfile
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

EXPECTED_MEMBERS = {"db.sqlite3", "media"}


class Command(BaseCommand):
    help = "Restore a database and media bundle produced by `convert_trial`."

    def add_arguments(self, parser):
        parser.add_argument("bundle", help="Path to the .tar.gz produced by convert_trial.")
        parser.add_argument(
            "--force",
            action="store_true",
            help="Overwrite an existing database and media directory.",
        )

    def handle(self, *args, **options):
        bundle_path = Path(options["bundle"])
        if not bundle_path.is_file():
            raise CommandError(f"No bundle at {bundle_path}.")

        db_path = Path(settings.DATABASES["default"]["NAME"])
        media_root = Path(settings.MEDIA_ROOT)

        if not options["force"] and db_path.exists() and db_path.stat().st_size > 0:
            raise CommandError(
                f"{db_path} already exists and is not empty. Re-run with --force "
                "only if you are certain this install has no data of its own."
            )

        with tempfile.TemporaryDirectory() as staging_name:
            staging = Path(staging_name)
            with tarfile.open(bundle_path, "r:gz") as bundle:
                members = {Path(m.name).parts[0] for m in bundle.getmembers()}
                unexpected = members - EXPECTED_MEMBERS
                if unexpected:
                    raise CommandError(
                        f"Bundle contains unexpected entries: {', '.join(sorted(unexpected))}"
                    )
                bundle.extractall(staging, filter="data")

            staged_db = staging / "db.sqlite3"
            if not staged_db.is_file():
                raise CommandError("Bundle has no db.sqlite3.")
            db_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(staged_db, db_path)

            staged_media = staging / "media"
            if staged_media.is_dir():
                media_root.mkdir(parents=True, exist_ok=True)
                shutil.copytree(staged_media, media_root, dirs_exist_ok=True)

        self.stdout.write(self.style.SUCCESS(f"Database restored to {db_path}"))
        self.stdout.write(self.style.SUCCESS(f"Media restored to {media_root}"))
        self.stdout.write("")
        self.stdout.write("Now run: python manage.py migrate --noinput")
        self.stdout.write(
            "Then rotate this install's own secrets — its DJANGO_SECRET_KEY and "
            "Telegram/Instagram credentials must not be the trial's."
        )
