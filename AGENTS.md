# MrExchange — Agent Notes

> Full architecture: [docs/PROJECT_OVERVIEW.md](docs/PROJECT_OVERVIEW.md)  
> Onboarding a paying customer: [docs/CUSTOMER_SERVER_ONBOARDING.md](docs/CUSTOMER_SERVER_ONBOARDING.md)

---

## One-line orientation

Exchange ops panel for MrExchange (`mrexchange.co.uk`). Operators update prices → managers finalize → Celery renders branded images → publishes to Telegram (mandatory) + Instagram.

**Two products in this repo — do not cross-import:**

| Product | Root | Notes |
|---------|------|-------|
| **MrExchange Panel** | `backend/` (all apps except below) + `frontend/` | This is what you work on |
| **Iraniu** | `backend/Request-Manage-System/` | Separate Django project, own DB, own bots |

---

## Delivery model

Two tiers, one codebase. `DEPLOYMENT_MODE` picks which one a process is running as.

| Tier | Where it runs | Isolation |
|------|---------------|-----------|
| **Trial** (`cloud`) | Our VPS, one Docker Compose stack per signup at `trial-<slug>.mrexchange.co.uk` | Own DB file, own volumes, own subdomain |
| **Customer server** (`customer_server`) | The customer's VPS and domain | Everything. Installs share no data and no credentials — ever |

`backend/fleet/` owns both sides: trial provisioning and teardown, license keys
(`MREX-XXXX-XXXX-XXXX-XXXX`), and `POST /api/fleet/checkin/`, the one unauthenticated
endpoint a customer-server install calls home on. It accepts a license key, an app
version and an uptime number, and rejects anything else — never prices, never customer
data. Keep it that way.

Onboarding a paying customer: [docs/CUSTOMER_SERVER_ONBOARDING.md](docs/CUSTOMER_SERVER_ONBOARDING.md).

---

## Boot

### Docker (recommended)
```bash
# .env.docker is committed with working local-testing defaults.
# For a real deployment copy .env.example instead and fill it in.
docker compose up --build
```
- Frontend: `http://localhost:5250`
- Backend API: `http://localhost:18000`

### Local dev
System packages first (not installed by pip/npm):
`python3-venv`, `python3-dev`, `build-essential`, `redis-server`.
Start Redis before Celery: `redis-server --daemonize yes --save "" --appendonly no`
(verify with `redis-cli ping`).

```bash
# Backend
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py ensure_default_admin
python manage.py runserver   # :8000

# Celery (separate terminals)
celery -A MrExchangePanel worker --loglevel=INFO
celery -A MrExchangePanel beat --loglevel=INFO

# Frontend
cd frontend
npm install && npm run dev   # :3000, proxies /api + /media → :8000
```

### Quick verify after any change
```bash
cd backend && python manage.py check
cd backend && python manage.py test --parallel 4   # 169 tests, all green
cd frontend && npm run build
```

`npm run build` writes into `backend/static/vue/` with `emptyOutDir: true` and then
runs `collectstatic`. Those bundles are tracked, so a build shows up in `git status`
whenever the frontend actually changed — commit them with the source change.

---

## Task → directory map

| Task | Directory |
|------|-----------|
| Auth, users, JWT, RBAC, force-logout | `backend/accounts/` |
| Currencies, Categories, PriceTypes | `backend/category/` |
| Regular prices + history | `backend/change_price/` |
| Special (VIP) prices + history | `backend/special_price/` |
| Finalize pipeline | `backend/finalize/` |
| Publish service, Celery tasks, template models | `backend/price_publisher/` |
| Telegram bots, channels, auto-post | `backend/telegram_app/` |
| Site settings singleton, Logs | `backend/setting/` |
| Analytics dashboard + pricing API | `backend/analysis/` |
| Instagram OAuth + image gen + publish | `backend/instagram_hub/` |
| Visual template editor (backend) | `backend/template_editor/` |
| Public prices API, webhooks, utils | `backend/core/` |
| Trial stacks, license keys, fleet check-in | `backend/fleet/` |
| WhatsApp channel + Telegram Mini App order form | `backend/bot_gateway/` |
| Order intake queue behind the bot gateway | `backend/orders/` |
| Vue SPA (all views, stores, services) | `frontend/src/` |
| Iraniu ad-request system ONLY | `backend/Request-Manage-System/` |

---

## Core publish pipeline

```
update prices (change_price / special_price)
  → finalize/ (Celery task dispatched, wait FINALIZE_TASK_WAIT_TIMEOUT)
    → price_publisher/ PricePublisherService
      → render image from template_editor config_json
      → POST to Telegram channel (FINALIZE_STRICT_TELEGRAM controls 503-on-fail)
      → on success: persist Finalization + FinalizedPriceHistory
        → on_commit: push GBP/USDT rates to WordPress WP-JSON API
        → on_commit: optional Instagram feed + story (never raises)
```

---

## Key env vars (`.env.docker` / `.env.example`)

| Variable | Effect |
|----------|--------|
| `FINALIZE_STRICT_TELEGRAM` | `true` → Telegram failure returns 503 and skips persisting finalization |
| `FINALIZE_TASK_WAIT_TIMEOUT` | Seconds to wait for Celery publish task before timing out |
| `DJANGO_DEBUG` | `False` in production |
| `DEFAULT_ADMIN_SYNC_PASSWORD` | `false` in production (disables auto-reset of admin password) |
| `UPLOAD_STORAGE_LIMIT_GB` | Max temp upload storage (default 10 GB) |

---

## Frontend patterns

**API service** — all calls go through `frontend/src/services/api.js` (427 lines):
- Exports: `authApi`, `dashboardApi`, `categoryApi`, `priceTypeApi`, `priceApi`, `specialPriceApi`, `finalizeApi`, `instagramHubApi`, `settingsApi`, `analysisApi`, `telegramApi`, `templateApi`, `templateEditorApi`, `fleetApi`, `botGatewayApi`, `ordersApi`
- Auto-injects Bearer token, single-flight JWT refresh + replay, CSRF from cookie
- Error format: `{ error: true, message: "...", code: "validation_error" }`

**Pinia stores**: `auth`, `siteSettings`, `templatesEditor`, `currencies`, `sidebar`, `theme`

**Roles** (must match `backend/accounts/permissions.py`):
- `super_admin` — everything
- `management` — finalize, price writes, template editor, Instagram
- `employee` — + Telegram
- `developer` — read-only

**i18n**: `en` + `fa` (RTL), keys in `frontend/src/locales/`. 700+ keys. Always add both locales for new strings.

**UI conventions**: `card-luxury` / `BaseCard variant="glass"` containers, `input-luxury` fields, `btn-luxury` / `btn-luxury-outline` buttons, `animate-fade-in-up` on mount, `<Transition name="fade-slide" mode="out-in">` for tab switches.

---

## Backend patterns

**DRF error format** (always use):
```python
{"error": True, "message": "...", "code": "validation_error"}
```

**Permissions**: use `IsSuperAdmin`, `IsManagement`, `IsSuperAdminOrManagement` from `accounts/permissions.py`.

**SQLite gotchas**:
- WAL mode + 30s busy-timeout + IMMEDIATE transactions (3 concurrent processes: Django + worker + beat)
- Never open the DB file directly with external tools while the app is running

**Celery tasks**: always write idempotent tasks with duplicate-publish guards (see `price_publisher/tasks.py`).

**Logging**: use `Log` model (level/source) + `log_telegram_event` helpers; structured JSON to `logs/app.json.log`.

---

## Hot files (frequently edited)

| File | What it contains |
|------|-----------------|
| `backend/finalize/views.py` | The finalize pipeline API |
| `backend/price_publisher/services.py` | `PricePublisherService` — render + send |
| `backend/telegram_app/models.py` | `TelegramBot`, `TelegramChannel`, `AutoPostConfig` (WIP) |
| `backend/telegram_app/api_views.py` | Telegram REST endpoints |
| `backend/analysis/views.py` | Analytics dashboard API |
| `frontend/src/services/api.js` | All frontend API calls |
| `frontend/src/views/telegram/TelegramMessageView.vue` | Telegram Hub (4-tab refactor in progress) |
| `frontend/src/views/analysis/AnalyticsView.vue` | Analytics (1177 lines) |
| `frontend/src/views/SettingsView.vue` | Settings (1062 lines) |
| `frontend/src/locales/en.json` + `fa.json` | i18n strings |

---

## Telegram bots

Library: **aiogram 3** (not python-telegram-bot / Telethon / Pyrogram).

- Customer UX: **reply keyboards** only (panel under chat input)
- Channel broadcasts: inline buttons OK
- MCP: `search_aiogram_docs`, `read_aiogram_doc` via `user-aiogram-docs`

---

## Do not edit or index

- `backend/venv/`, `backend/public/`, `backend/static/vue/`, `frontend/node_modules/`
- `backend/Request-Manage-System/` (separate product)

---

## Status

The four items tracked in `tel.txt` are all shipped and covered by tests:
`UpdatePriceView` handles both the bare-list and `{ results: [...] }` shapes,
`TelegramMessageView.vue` is the 5-tab hub, `AutoPostConfig` lives in
`telegram_app/models.py` with CRUD API, and Telegram engagement is part of
`/api/analysis/dashboard/`. Treat `tel.txt` as history, not as a plan.

---

## Two customer bot stacks, and which is which

`telegram_app` owns Telegram. It is the full customer bot — aiogram, sessions,
customer profiles, exchange requests, price alerts, re-engagement — and it owns
this install's Telegram webhook.

`bot_gateway` owns WhatsApp and the order form. It came from a fork that also
had its own Telegram bot; that half was dropped on merge because two webhooks
would fight over the same updates. What is left is the WhatsApp Cloud API
channel and the customer-facing order form at `/webapp/order`, which writes
`orders.OrderIntake` rows for the panel queue at `/orders`.

Bot customers are `bot_gateway.BotCustomer`, not panel users, and authenticate
with their own short-lived token (`bot_gateway/auth.py`). Never mix that with a
staff JWT — `api.js` deliberately leaves an explicitly-set Authorization header
alone so the two cannot collide in one browser.

To give Telegram customers the same order form, have `telegram_app` send the
button built by `bot_gateway.services.dispatcher._build_order_button`; that is
the only piece the dropped Telegram half was still providing.

---

## Rendering a template: two engines

`SiteSettings.use_playwright_for_template_render` picks between them, and
`PricePublisher._render_template_editor_image` is the only place that decides:

- **Pillow** (default) — `template_editor/render.py`, approximates the editor.
- **Playwright** — loads the SPA's `/headless-render/<id>` in Chromium and
  screenshots it, so output matches the editor exactly. Any engine error falls
  back to Pillow, so a missing browser never blocks a publish.

Both read the same canvas helpers from
`frontend/src/pages/templates/templateEditorCanvasUtils.js`. Keep it that way —
the editor and the headless page have to agree pixel for pixel.
