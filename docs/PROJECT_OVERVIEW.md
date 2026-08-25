# MrExchange Panel — Project Overview

A full-stack exchange (صرافی) operations platform for **MrExchange** (`mrexchange.co.uk`). It lets an exchange team manage currency prices, review and finalize changes, render branded price-board images, and auto-publish them to Telegram (and optionally Instagram and an external WordPress website).

> Note: the repo also bundles a second, unrelated Django app at `backend/Request-Manage-System/` ("Iraniu" — an ad-request management system). It is separate and has its own documentation.

---

## 1. High-Level Purpose

The product answers one core workflow:

1. **Update prices** (regular + special) in a web panel.
2. **Review/finalize** the changes with management oversight.
3. **Render branded images** (price boards / cards) from editable templates.
4. **Publish** to Telegram channels, Instagram feed/story, and an external website API.
5. **Track everything** — history, logs, analytics, user activity.

---

## 2. Architecture

| Layer | Technology | Location |
|-------|-----------|----------|
| Frontend | Vue 3 SPA, Vite 6, Pinia, Vue Router, vue-i18n, Tailwind, Chart.js, PWA | `frontend/` |
| Backend | Django 5.2, Django REST Framework, SimpleJWT | `backend/` |
| Database | SQLite (WAL, busy-timeout 30s, IMMEDIATE transactions) | `backend/data/db.sqlite3` |
| Queue | Celery worker + beat with Redis broker | `docker-compose.yml` |
| Image rendering | Pillow | `backend/` |
| Integrations | Telegram Bot API, Meta Graph API v18 (Instagram), external WordPress WP-JSON API | `backend/` |
| Deployment | Docker Compose (app + celery-worker + celery-beat + redis), supervisord in container, HTTP-behind-proxy (Dokploy-style) | `Dockerfile`, `docker/` |

- In **local dev**, Vite serves the SPA on `:3000` and proxies `/api` + `/media` to Django (`:8000`).
- In **production**, `npm run build` outputs to `backend/static/vue/` and Django serves the SPA via a catch-all `SPAView`.

---

## 3. Repo Layout

```text
MrExchange/
├── backend/
│   ├── MrExchangePanel/   # Django project (settings, urls, celery, middleware, SPAView)
│   ├── accounts/             # Users, roles, JWT auth, activity logs
│   ├── analysis/             # Analytics dashboard + pricing API
│   ├── category/             # Currencies, Categories, PriceTypes
│   ├── change_price/         # Regular prices + PriceHistory
│   ├── core/                 # Public prices API, exceptions, webhook, utils
│   ├── dashboard/            # HTML dashboard views + API
│   ├── finalize/             # Finalization pipeline + external API sync
│   ├── instagram_hub/        # Instagram OAuth, image gen, publishing
│   ├── landing/              # Marketing landing page render
│   ├── price_publisher/      # Publish service + Celery tasks + template models
│   ├── setting/              # SiteSettings singleton, Logs, upload policy
│   ├── special_price/        # Special prices + history
│   ├── telegram_app/         # Telegram bots, channels, auto-post config
│   ├── template_editor/      # Visual template editor backend
│   ├── Request-Manage-System/# SEPARATE app: "Iraniu" ad-request manager
│   └── data/, public/, static/, logs/
├── frontend/                 # Vue 3 SPA
├── landing page/             # Static marketing page (fa, RTL) + Demo.mp4
├── docker/                   # entrypoint, supervisord, dev Dockerfiles
├── docs/                     # MASTER_PLAN.md, PROJECT_OVERVIEW.md
├── scripts/                  # PowerShell helpers (default admin, font download)
├── docker-compose.yml
├── Dockerfile
└── README.md
```

---

## 4. Backend Apps (domain-by-domain)

### accounts — auth & users
- `CustomUser` (role, `token_version` for force-logout), `UserActivityLog`.
- JWT auth with a token-version check (`JWTAuthenticationWithTokenVersion`); refresh rotates the token version.
- RBAC permissions: `IsSuperAdmin`, `IsManagement`, `IsSuperAdminOrManagement`.
- Endpoints: `login`, `logout`, `me`, `token/refresh`, `demo-login`, users CRUD, force-logout, activity.

### category — market structure
- Models: `Currency` (19 seeded on migrate), `Category` (includes Telegram caption/media/buttons, `last_used_template`), `PriceType` (buy/sell, source→target currency, ordering).
- ViewSet API + `CategoryExplorerAPIView`; templates resolved at serialization time for previews.

### change_price — regular prices
- `PriceHistory` (each change recorded with `event_at`).
- Endpoints: list / detail / update / bulk-update per category / history. Persian-aware sort helpers for GBP and Tether price types.

### special_price — special (VIP) prices
- `SpecialPriceType`, `SpecialPricePair` (enforces buy + sell rows), `SpecialPriceHistory`.
- Separate flow and history from regular prices, same finalize/publish pipeline downstream.

### finalize — the publish pipeline
- Models: `Finalization`, `FinalizedPriceHistory`, `SpecialPriceFinalization`.
- API: dashboard, `finalize-category`, `finalize-special-price`, `finalize-all` (channel + category/special selection).
- Flow per finalize: run **Celery publish task** → wait up to `FINALIZE_TASK_WAIT_TIMEOUT` → honor `FINALIZE_STRICT_TELEGRAM` (503 if Telegram fails) → persist finalization **only on success** → then on-commit queue **external API sync** and optional **Instagram post**.

### price_publisher — publish service
- `PricePublisherService` (`publish_category_prices`, `publish_special_price`) returns a `PublicationResult` (success, response, caption, template id, render fallback reason).
- Celery tasks with idempotent duplicate-publish guards.
- Legacy template admin/forms + `PriceTemplateViewSet` + dashboard API.

### template_editor — visual template designer
- Models: `Template` (name, category, legacy `config` + `config_json`, 1920×1080 canvas, orientation, round-robin `publish_order`, Telegram caption + buttons), `Widget`, `Layer`, `TemplateWidgetBinding`.
- Rendering from `config_json` (percentage coordinates, price-key heuristics) plus legacy `render_template`.
- Variable catalog with Persian price slots; fonts (Vazirmatn/Inter/Kalameh); admin import/export/zip; full HTML frontend (list/create/edit/delete/preview) + signed font-face URLs.

### telegram_app — messaging
- `TelegramBot` (encrypted token, webhook/polling, `restrict_to_known_channels`, `log_all_messages`), `TelegramChannel`, `DefaultMessageSettings` (one active per bot; caption + JSON buttons), `AutoPostConfig` (scheduler config: channel + category/special + time-of-day).
- Routers for bots/channels/auto-post-config; `SendMessageAPIView`; `TelegramService` client.

### setting — site config & logs
- Singleton `SiteSettings` (branding, socials, business hours, upload policy, `prices_webhook_url`, UI fonts) with no-cache `.load()`.
- `Log` model (level/source); structured JSON logging to `logs/app.json.log`.
- API: public site settings (GET public, PUT superadmin), bots/channels ViewSets, paginated logs, upload policy + temp-storage usage + clear-temp endpoint (`UPLOAD_STORAGE_LIMIT_GB` default 10).

### analysis — dashboards & trends
- `AnalyticsDashboardView` (server HTML with Chart.js: timelines, volatility + linear-regression trend stats, finalization stats, Telegram engagement, last-updated-price trend); its `get_analytics_data()` powers `AnalysisDashboardAPIView`.
- `PricingDataAPIView`: public read-only pricing incl. synthetic "Special Prices" filtered to last 6h.
- Query params: `start/end/category_id/price_type_ids`, max span 366 days.

### instagram_hub — optional Instagram
- `InstagramConfig` (Fernet-encrypted secrets, caption suffix/hashtags, OAuth state) + `InstagramPublicationLog`.
- OAuth connect/callback (short-lived → long-lived tokens); Meta Graph API v18.0 client (`create_media_container`, `media_publish`, caption max 2200).
- Pillow image generator: 1080×1080 post + 1080×1920 story, dark-gold/light-blue themes.
- Celery task chain after finalize (render → publish feed + story; never raises, always logs).

### fleet — delivery tiers, licensing, fleet visibility
- `CustomerDeployment` — one row per trial stack or customer-server install: type, slug, domain, license key, plan, status (pending → provisioning → active → expired/suspended/archived/failed), installed version, last check-in, renewal date. Partial unique constraints keep license keys unique and allow only one live trial per customer.
- `provisioning.py` — renders `docker/trial-stack.compose.yml` into a per-trial stack directory with its own `.env` (fresh secret key, own volumes, own Traefik-routed subdomain), then `docker compose up`. Every Docker path is inert unless `TRIAL_PROVISIONING_ENABLED`.
- `licensing.py` — `MREX-XXXX-XXXX-XXXX-XXXX` keys over a Crockford-style alphabet. A bearer identifier for support and renewals, not a secret protecting customer data.
- Celery beat: pre-expiry reminders to staff (`TRIAL_REMINDER_DAYS`), teardown of trials past `TRIAL_GRACE_DAYS`, and the install's own daily check-in.
- `POST /api/fleet/checkin/` — the single unauthenticated endpoint, throttled at 60/h. Accepts license key, app version and uptime and **rejects any other field**; unknown and archived keys get an identical 403 so a probe learns nothing.
- Management commands `convert_trial` (export a trial as a bundle, issue the license) and `restore_trial_bundle` (restore it on the customer's own server, refusing to overwrite live data without `--force`).

### dashboard / landing / core
- `dashboard`: classic + `dashboard2` HTML views (24h top-10 trends, category averages, recent updates timeline, histogram, 7-day frequency) + dashboard API.
- `core`: public prices API (`AllowAny` + throttle), `prices_webhook.py` (daemon-thread POST of price snapshot), image magic-byte validation, price-formatting / Persian-digit utils.
- `landing`: renders the marketing page at `/landingpage/`.

---

## 5. Frontend SPA

### Stack & key libraries
Vue 3.5, Vite 6, Pinia, Vue Router 4, vue-i18n v12-alpha (`legacy: true`), Tailwind 3.4, Chart.js (vue-chartjs), vue3-moveable + vue-draggable-plus (template editor drag/resize), date-fns-jalali, xlsx (Excel import/export in Analytics), vite-plugin-pwa (installable app).

### Router & views (routes under the authed `AppLayout`)
- **auth:** `/login`, `/landing`; **errors:** `/error/{404,500,403}`.
- **dashboard:** `/` — 8 stat cards, live clock, skeleton loaders.
- **prices:** `/update`, `/prices`, bulk update per category.
- **categories:** list, category form, price-type form, Telegram Studio (per-category Telegram caption/media/buttons setup).
- **special-prices:** form, history, update, Telegram/template redirects.
- **finalize:** dashboard, per-category, per-special, and a `FinalizeAllModal` (preflight destinations icons, channel select, results per category).
- **settings:** `SettingsView` (1062 lines) with mobile/desktop tabs, live font preview; `LogsView`.
- **analysis:** `AnalyticsView` (1177 lines) with charts, filters, Excel import/export.
- **telegram:** messenger + bot setup (1038 lines), settings, bot form.
- **templates:** dashboard, form, media library.
- **instagram:** hub status/config/preview.
- **users:** user management + activity (432 lines).
- **fleet:** `/programmer/fleet` — trial customers with days remaining and extend/convert/provision actions; licensed installs with domain, plan, renewal, last check-in (amber past 48h) and license reissue.
- **template editor:** `pages/templates/TemplateEditor.vue` (881 lines) + `WidgetLibraryPanel` + `TemplateInspectorPanel` — full-screen canvas editor with moveable widgets, text/date/clock/weekday/image preview widgets.

### Data layer
- `src/services/api.js` (427 lines): axios instance with Bearer token injection, **single-flight JWT refresh + replay**, CSRF (`csrftoken` cookie / `X-CSRFToken`), silent-mode toasts, standardized error parsing (DRF + project `{error, message, code}` payloads), and exported API groups: `authApi`, `dashboardApi`, `categoryApi`, `priceTypeApi`, `priceApi`, `specialPriceApi`, `finalizeApi`, `instagramHubApi`, `settingsApi`, `analysisApi`, `telegramApi`, `templateApi`, `templateEditorApi`, `fleetApi`.
- Pinia stores: `auth` (roles/permissions via `src/config/permissions.js`), `siteSettings` (branding, dynamic fonts), `templatesEditor`, `currencies`, `sidebar`, `theme`.
- i18n: `en`, `fa`, `ar`, `de`, `es`, `fr`, `tr` with identical key structures; `fa` → RTL; locale/theme persisted in localStorage (`mrexchange-*` / `smartexchange-*` fallbacks).

### Roles/permissions (must match backend `accounts/permissions.py`)
- `super_admin`: everything (settings, admin management).
- `management`: finalize, price writes, template editor, Instagram.
- `employee`: + Telegram.
- `developer`: read-only authenticated endpoints.

---

## 6. Key End-to-End Workflows

### 6.1 Update → Finalize → Publish
1. Operator updates regular/special prices (single or bulk) → `PriceHistory` / `SpecialPriceHistory` rows created.
2. A manager opens Finalize, picks a channel + categories/specials.
3. Backend dispatches Celery task: builds the price board via `PricePublisherService`, renders the image from the template (`render_template` or `render_template_from_config_json`), publishes to the chosen Telegram channel, and (strict mode) fails loudly if Telegram rejects.
4. On success, `Finalization` + `FinalizedPriceHistory` are committed; then a Celery on-commit chain pushes rates to the external WordPress API and optionally posts the rendered image to Instagram (feed + story).

### 6.2 Template editor
Design a 1920×1080 canvas with moveable widgets → `config_json` (percentage coordinates) saved via `PUT /api/templates/:id/` → widgets synced to DB (`_sync_widgets_from_config`) → used by renderer for board images.

### 6.3 Telegram automation
`AutoPostConfig` defines scheduled posts (channel + category/special + time-of-day); bots/channels are managed via API/HTML; `SendMessageAPIView` sends one-off messages.

---

## 7. API Surface (prefix `/api/`)

Groups: `auth`, `dashboard`, `categories`, `prices`, `special-prices`, `finalize`, `telegram`, `settings`, `analysis`, `templates`, `template-editor`, `instagram-hub`, `fleet`, plus public `api/public/prices/`.

Error format (standard): `{ "error": true, "message": "...", "code": "validation_error" }`.

Throttles: anon 100/h, user 1000/h, finalize 60/h, settings 200/h, public prices 2000/h, fleet check-in 60/h.

---

## 8. Deployment & Ops

- **Docker Compose:** `app` (Django + supervisord, runs migrate/collectstatic/ensure_default_admin/ensure_demo_user at start), `celery-worker` (concurrency 2), `celery-beat`, `redis:7-alpine`. Ports: backend `18000`, frontend Vite `5250`, redis `6379`.
- **Env:** `.env.docker` / `.env.example` — Django secret/debug/hosts, Celery broker/limits, finalize timeouts/strict mode, Instagram base URL, trial/provisioning and fleet check-in settings, default admin credentials.
- **Production checklist** (from README): `DJANGO_DEBUG=False`, strict allowed hosts + CSRF origins, strong secret key, `DEFAULT_ADMIN_SYNC_PASSWORD=false`, HTTPS behind proxy.
- **Known build note:** `vite-plugin-pwa` can fail on oversized PWA icons (Workbox max-size) — reduce `pwa-*.png` sizes.
- **SQLite tuning** targets exactly 3 concurrent processes (Django + worker + beat) — WAL, 30s busy-timeout, IMMEDIATE transactions.

- **Delivery tiers:** `DEPLOYMENT_MODE=cloud` is the hosted service, where each 14-day trial gets its own isolated Compose stack on our VPS; `DEPLOYMENT_MODE=customer_server` is a dedicated install on the customer's VPS and domain. Installs share no data and no credentials. Onboarding runbook: [CUSTOMER_SERVER_ONBOARDING.md](CUSTOMER_SERVER_ONBOARDING.md).

---

## 9. Bundled-but-Separate Apps

- **`backend/Request-Manage-System/` ("Iraniu")** — standalone Django 5.0.1 project: human-in-the-loop ad-request management with OpenAI moderation pre-scan, staff approve/reject, Telegram notifications with "Edit & Resubmit", Bootstrap 5 dark theme. Own settings, DB, docs.
- **`landing page/`** — static Persian marketing page for MrExchange (with `Demo.mp4`, sitemap, robots.txt), separate from the `backend/landing` Django view which also renders a landing page.

---

## 10. Development Notes / Current State

- Both README (frontend) and docs/MASTER_PLAN.md describe an ongoing **migration from server-rendered Django templates to the Vue SPA** (phases: rebrand ✅ → backend API conversion → Vue frontend → deprecate old templates). The codebase currently has both HTML views and DRF APIs.
- `tel.txt` contains a task list ("Telegram Management Hub" 4-tab refactor, Analytics Telegram engagement, AutoPostConfig, UpdatePriceView bug fix) — a work-in-progress agenda.
- Scripts: `scripts/ensure-default-admin.ps1`, `scripts/download_template_fonts.ps1`.
