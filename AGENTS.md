# MrExchange — Agent Notes

> Full architecture: [docs/PROJECT_OVERVIEW.md](docs/PROJECT_OVERVIEW.md)  
> Parent workspace notes: [../AGENTS.md](../AGENTS.md)  
> Roadmap / WIP plan: [tel.txt](tel.txt) (Telegram Hub refactor, Analytics Telegram section, AutoPostConfig, UpdatePriceView bug)

---

## One-line orientation

Exchange ops panel for MrExchange (`mrexchange.co.uk`). Operators update prices → managers finalize → Celery renders branded images → publishes to Telegram (mandatory) + Instagram.

**Two products in this repo — do not cross-import:**

| Product | Root | Notes |
|---------|------|-------|
| **MrExchange Panel** | `backend/` (all apps except below) + `frontend/` | This is what you work on |
| **Iraniu** | `backend/Request-Manage-System/` | Separate Django project, own DB, own bots |

---

## Boot

### Docker (recommended)
```bash
cp .env.docker.example .env.docker   # first time only
docker compose up --build
```
- Frontend: `http://localhost:5250`
- Backend API: `http://localhost:18000`

### Local dev
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
cd frontend && npm run build
```

---

## Task → directory map

| Task | Directory |
|------|-----------|
| Auth, users, JWT, RBAC, force-logout | `backend/accounts/` |
| Currencies, Categories, PriceTypes | `backend/category/` |
| Regular prices + history | `backend/change_price/` |
| Special (VIP) prices + history | `backend/special_price/` |
| Finalize pipeline, external WordPress sync | `backend/finalize/` |
| Publish service, Celery tasks, template models | `backend/price_publisher/` |
| Telegram bots, channels, auto-post | `backend/telegram_app/` |
| Site settings singleton, Logs | `backend/setting/` |
| Analytics dashboard + pricing API | `backend/analysis/` |
| Instagram OAuth + image gen + publish | `backend/instagram_hub/` |
| Visual template editor (backend) | `backend/template_editor/` |
| Public prices API, webhooks, utils | `backend/core/` |
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
- Exports: `authApi`, `dashboardApi`, `categoryApi`, `priceTypeApi`, `priceApi`, `specialPriceApi`, `finalizeApi`, `instagramHubApi`, `settingsApi`, `analysisApi`, `telegramApi`, `templateApi`, `templateEditorApi`
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

For any `telegram_app` work: read `.cursor/skills/TelegramLibrarySkill/SKILL.md` first.
- Customer UX: **reply keyboards** only (panel under chat input)
- Channel broadcasts: inline buttons OK
- MCP: `search_aiogram_docs`, `read_aiogram_doc` via `user-aiogram-docs`

---

## Do not edit or index

- `backend/venv/`, `backend/public/`, `backend/static/vue/`, `frontend/node_modules/`
- `.cursor/skills/TelegramLibrarySkill/reference/` (use search/MCP instead)
- `backend/Request-Manage-System/` (separate product)

---

## Work in progress (see `tel.txt` for full spec)

1. **Fix `UpdatePriceView` loading bug** — handles `data` but not `{ results: [...] }` paginated shape
2. **Telegram Management Hub** — refactor `TelegramMessageView.vue` into 4 tabs: Messenger, Bot Setup, Channels, Automation
3. **AutoPostConfig model** — new `telegram_app` model + CRUD API (config-only, no scheduler yet)
4. **Telegram Engagement analytics** — move channel analytics into `AnalyticsView.vue`, extend `/api/analysis/dashboard/`
