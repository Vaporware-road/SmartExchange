"""Package a trial install for hand-off to the customer's own VPS.

Run on the trial host. The command quiesces the stack, copies the SQLite
database and the media directory out of its volumes into one bundle, issues
the license, and prints the two commands the operator runs next. It never
reaches the customer's machine itself — those credentials belong to them, and
the deployment guide's rule is that installs share nothing.
"""

from __future__ import annotations

import subprocess
import tarfile
import tempfile
from datetime import datetime, timedelta, timezone as dt_timezone
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from fleet.models import CustomerDeployment
from fleet.provisioning import (
    COMPOSE_FILENAME,
    ProvisioningDisabled,
    ProvisioningError,
    archive,
    stack_dir,
)
from fleet.services import convert_to_licensed

DB_PATH_IN_CONTAINER = "/app/backend/data/db.sqlite3"
MEDIA_PATH_IN_CONTAINER = "/app/backend/public/media"
COPY_TIMEOUT_SECONDS = 600


class Command(BaseCommand):
    help = "Export a trial install as a portable bundle and issue its license."

    def add_arguments(self, parser):
        parser.add_argument("slug", help="Trial stack slug, e.g. trial-acme")
        parser.add_argument(
            "--domain",
            required=True,
            help="The customer's own domain for the licensed install.",
        )
        parser.add_argument("--plan", default=None, help="Plan for the licensed install.")
        parser.add_argument(
            "--term-days",
            type=int,
            default=None,
            help=f"License term (default LICENSE_TERM_DAYS={settings.LICENSE_TERM_DAYS}).",
        )
        parser.add_argument(
            "--output-dir",
            default=None,
            help="Where to write the bundle (default TRIAL_ARCHIVE_ROOT).",
        )
        parser.add_argument(
            "--keep-stack",
            action="store_true",
            help="Leave the trial stack up after converting, instead of tearing it down.",
        )
        parser.add_argument(
            "--keep-running",
            action="store_true",
            help="Do not stop the trial stack before copying. Risks a torn SQLite file.",
        )

    def handle(self, *args, **options):
        slug = options["slug"]
        trial = CustomerDeployment.objects.filter(
            slug=slug, deployment_type=CustomerDeployment.TYPE_TRIAL
        ).select_related("customer").first()
        if trial is None:
            raise CommandError(f"No trial deployment with slug {slug!r}.")

        renews_at = None
        if options["term_days"]:
            renews_at = timezone.now() + timedelta(days=options["term_days"])

        bundle = self._export_bundle(trial, options)

        licensed = convert_to_licensed(
            trial,
            domain=options["domain"],
            plan=options["plan"],
            renews_at=renews_at,
            notes=f"Converted from {trial.slug}; bundle {bundle}",
        )

        torn_down = self._retire_stack(licensed, trial, options)

        self.stdout.write(self.style.SUCCESS(f"Bundle written: {bundle}"))
        self.stdout.write(self.style.SUCCESS(f"License key:   {licensed.license_key}"))
        self.stdout.write(
            f"Renews:        {licensed.renews_at:%Y-%m-%d}" if licensed.renews_at else ""
        )
        self.stdout.write(
            self.style.SUCCESS(f"Trial stack:   torn down ({trial.domain} no longer serves)")
            if torn_down
            else self.style.WARNING(f"Trial stack:   still up at {trial.domain}")
        )
        self.stdout.write("")
        self.stdout.write("Next, on the customer's VPS:")
        self.stdout.write(f"  scp {bundle} <customer-host>:/tmp/")
        self.stdout.write(
            f"  python manage.py restore_trial_bundle /tmp/{Path(bundle).name}"
        )
        self.stdout.write("")
        self.stdout.write(
            "Set FLEET_LICENSE_KEY and FLEET_CHECKIN_URL in their .env so the "
            "install appears in the fleet view, then point their DNS at it."
        )

    def _retire_stack(self, licensed, trial, options):
        """Cut the trial subdomain over by taking its stack down.

        The record is already retired by `convert_to_licensed`; this is the
        Docker half, and its failure must not lose the license we just issued.
        """
        if options["keep_stack"]:
            return False
        try:
            archive_path = archive(trial, keep_data=True)
        except ProvisioningDisabled:
            return False
        except ProvisioningError as exc:
            self.stderr.write(
                self.style.WARNING(
                    f"License {licensed.license_key} was issued, but tearing the "
                    f"trial stack down failed: {exc}. Take it down by hand."
                )
            )
            return False
        if archive_path:
            self.stdout.write(f"Stack archive: {archive_path}")
        return True

    def _export_bundle(self, trial, options):
        output_dir = Path(options["output_dir"] or settings.TRIAL_ARCHIVE_ROOT)
        output_dir.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(dt_timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        bundle_path = output_dir / f"{trial.slug}-bundle-{stamp}.tar.gz"

        if not options["keep_running"]:
            self._compose(trial, "stop", "app", "celery-worker", "celery-beat")
        try:
            with tempfile.TemporaryDirectory() as staging_name:
                staging = Path(staging_name)
                container = self._container_id(trial, "app")
                self._docker_cp(f"{container}:{DB_PATH_IN_CONTAINER}", staging / "db.sqlite3")
                self._docker_cp(f"{container}:{MEDIA_PATH_IN_CONTAINER}", staging / "media")
                with tarfile.open(bundle_path, "w:gz") as bundle:
                    for entry in sorted(staging.iterdir()):
                        bundle.add(entry, arcname=entry.name)
        finally:
            if not options["keep_running"]:
                self._compose(trial, "start", "app", "celery-worker", "celery-beat")

        return str(bundle_path)

    def _compose(self, trial, *args):
        directory = stack_dir(trial.slug)
        cmd = [
            *settings.DOCKER_COMPOSE_COMMAND,
            "--project-name", trial.slug,
            "--project-directory", str(directory),
            "--file", str(directory / COMPOSE_FILENAME),
            *args,
        ]
        self._run(cmd)

    def _container_id(self, trial, service):
        directory = stack_dir(trial.slug)
        cmd = [
            *settings.DOCKER_COMPOSE_COMMAND,
            "--project-name", trial.slug,
            "--project-directory", str(directory),
            "--file", str(directory / COMPOSE_FILENAME),
            "ps", "--quiet", service,
        ]
        container = self._run(cmd).strip().splitlines()
        if not container:
            raise CommandError(f"Service {service!r} of {trial.slug} has no container.")
        return container[0]

    def _docker_cp(self, source, destination):
        self._run(["docker", "cp", str(source), str(destination)])

    @staticmethod
    def _run(cmd):
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=COPY_TIMEOUT_SECONDS
        )
        if result.returncode != 0:
            raise CommandError(
                f"`{' '.join(cmd)}` failed (exit {result.returncode}): "
                f"{result.stderr.strip()[:2000]}"
            )
        return result.stdout
