# Customer-Server Onboarding Runbook

How a MrExchange customer moves from the free 14-day trial on our VPS to a
dedicated install on their own server. Work top to bottom; every step has a
check you can point at before moving on.

`docs/DEPLOYMENT_FOR_MODELS.md` is the generic deployment guide — this runbook
is the commercial path around it, and defers to it for anything about running
the stack itself.

The rule that governs all of it: **installs share nothing.** No database, no
media, no secret, no Telegram token crosses from one customer to another or
from our VPS to theirs. The only thing that ever flows back to us is the fleet
check-in, and that carries a license key, an app version and an uptime number.

---

## 0. Where the customer starts

Signing up on the marketing site creates the account, starts a 14-day trial
(`INDIVIDUAL_TRIAL_DAYS`) and — when `TRIAL_PROVISIONING_ENABLED=true` — queues
an isolated Compose stack at `https://trial-<slug>.<TRIAL_BASE_DOMAIN>`. Nothing
in this runbook happens until they decide to buy.

Watch the trial in the owner panel at **/programmer/fleet → Trial customers**.
Three days before expiry (`TRIAL_REMINDER_DAYS`) staff get a Telegram nudge;
seven days after expiry (`TRIAL_GRACE_DAYS`) the account deactivates and the
stack is torn down, so a conversation that is still live needs an **Extend**
click before that window closes.

---

## 1. Collect what you need from the customer

Do not start until you have all of it — a half-collected onboarding stalls with
their DNS pointed at nothing.

- [ ] **Domain** they want the panel on, e.g. `panel.customer.example`.
- [ ] **VPS access**: host, SSH user, and either their key added or an account
      created for you. 2 GB RAM and several GB of disk, per the deployment guide.
- [ ] **Who controls DNS** for that domain, and how you reach them to change it.
- [ ] **Plan and term** (bronze / silver / gold …), and the renewal date they
      are agreeing to — this becomes `renews_at` on the deployment record.
- [ ] **Integration credentials they will use on their own install**: Telegram
      bot token, Instagram credentials. Theirs, not the trial's.

State plainly that the trial's secrets do not travel. Their install gets a fresh
`DJANGO_SECRET_KEY` and its own bot token even if the trial worked perfectly.

---

## 2. Export the trial and issue the license

Run **on the trial host**, from the backend directory. This stops the trial
stack briefly so SQLite is copied clean, writes one bundle, ends the trial and
prints the license key:

```bash
python manage.py convert_trial trial-acme --domain panel.customer.example --plan gold
```

Useful flags: `--term-days` (defaults to `LICENSE_TERM_DAYS=365`),
`--output-dir` (defaults to `TRIAL_ARCHIVE_ROOT`), and `--keep-running`, which
skips the stop and therefore risks a torn database — only for a trial with no
data worth keeping.

If the customer never used the trial for real work, skip the bundle entirely and
use **Convert** in the owner panel instead: it issues the license and records the
deployment without exporting anything.

- [ ] Bundle path noted.
- [ ] License key recorded and kept somewhere you can hand to the customer.
- [ ] `/programmer/fleet → Licensed customers` now lists the domain, plan and
      renewal date. Last check-in will read *Never checked in* until step 6.

---

## 3. Deploy the stack on their server

Follow `docs/DEPLOYMENT_FOR_MODELS.md` sections 3–6 on their VPS, with these
customer-server specifics:

```dotenv
DEPLOYMENT_MODE=customer_server
DJANGO_SECRET_KEY=<freshly generated, unique to this install>
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=panel.customer.example
DJANGO_CSRF_TRUSTED_ORIGINS=https://panel.customer.example
DEFAULT_ADMIN_USERNAME=<their admin>
DEFAULT_ADMIN_PASSWORD=<strong, one-time>
DEFAULT_ADMIN_SYNC_PASSWORD=false
```

The tracked `.env.example` fallback secret is in Git history — treat it as
compromised and never let it reach a customer host.

- [ ] `docker compose config --quiet` passes.
- [ ] `docker compose up --build -d` brings up `app`, `celery-worker`,
      `celery-beat`, `redis`.
- [ ] Redis is **not** published to the internet.

---

## 4. Restore their data (only when converting a used trial)

Copy the bundle across and restore it inside their app container, before the
first real use of the install:

```bash
scp /srv/mrexchange/trial-archives/trial-acme-bundle-<stamp>.tar.gz customer-host:/tmp/
# on the customer host, inside the app container:
python manage.py restore_trial_bundle /tmp/trial-acme-bundle-<stamp>.tar.gz
python manage.py migrate --noinput
```

`restore_trial_bundle` refuses to overwrite a database that already holds data
unless you pass `--force`. If it refuses, stop and work out why that install has
data — do not reach for the flag.

- [ ] Restore reported the database and media paths it wrote.
- [ ] Migrations ran clean.
- [ ] **Their** Telegram/Instagram credentials are set — the restored database
      carries the trial's configuration, and it must be replaced, not reused.

---

## 5. DNS and TLS

- [ ] `A`/`AAAA` record for the domain points at their VPS.
- [ ] Reverse proxy terminates HTTPS with a valid certificate.
- [ ] `http://` redirects to `https://`.
- [ ] The domain matches `DJANGO_ALLOWED_HOSTS` and
      `DJANGO_CSRF_TRUSTED_ORIGINS` exactly, subdomain included.

---

## 6. Turn on the fleet check-in

This is what makes the install visible in the owner panel. In their `.env`:

```dotenv
FLEET_CHECKIN_URL=https://mrexchange.co.uk/api/fleet/checkin/
FLEET_LICENSE_KEY=MREX-XXXX-XXXX-XXXX-XXXX
FLEET_CHECKIN_SECONDS=86400
APP_VERSION=<release you deployed>
```

Restart the worker and Beat so the schedule picks the values up. The daily task
POSTs the license key, the app version and process uptime — nothing else. Leaving
`FLEET_LICENSE_KEY` empty is a supported choice: the install simply stays dark in
the fleet view.

- [ ] `/programmer/fleet → Licensed customers` shows a recent check-in and the
      right version within a day (force it sooner by restarting Beat).

---

## 7. Smoke test before handover

- [ ] Log in at `https://panel.customer.example/` with the admin account.
- [ ] Prices load; a price edit saves and survives a reload.
- [ ] A finalize run completes and writes a log entry.
- [ ] Telegram send reaches their channel with their bot.
- [ ] A template renders and exports.
- [ ] `docker compose exec -T app sh -c 'cd /app/backend && python manage.py check'`
      reports no issues.

---

## 8. Handover

- [ ] Admin password changed by the customer; `DEFAULT_ADMIN_SYNC_PASSWORD=false`
      confirmed.
- [ ] License key and renewal date given to them in writing.
- [ ] Backups arranged for the SQLite database and the media volume, and a
      restore actually tested once.
- [ ] They know how to reach you, and what an upgrade will involve.
- [ ] Invoice raised for the plan and term recorded in step 1.

---

## 9. After the sale

- **Renewals.** `renews_at` in the fleet view is the reminder. Renewing is a
  commercial act — update the date on the deployment record; the key does not
  need to change.
- **A leaked license key.** Use **Reissue** in the fleet view, then put the new
  key in their `.env` and restart. The old key stops being accepted immediately.
- **A stale check-in.** The fleet view turns the timestamp amber after 48 hours.
  That means their Beat is down, their outbound network is blocked, or the
  install is off — it is not by itself a licensing problem, and the panel keeps
  working regardless.
- **Upgrades.** Their server, their maintenance window. Pull the new image,
  `docker compose up --build -d`, migrate, and bump `APP_VERSION` so the fleet
  view reflects what they are actually running.
