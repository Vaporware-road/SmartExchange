# SmartExchange Panel

A full-stack **price management and publishing system** for currency exchange operations. Manage exchange rates, track history, generate branded price images, and publish them to Telegram channels—with an optional **landing page** and a separate **Request Management System (Iraniu)** in the same repository.

---

## Table of Contents

- [What This Project Is](#what-this-project-is)
- [Features](#features)
- [Architecture & Tech Stack](#architecture--tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running the Application](#running-the-application)
- [Configuration](#configuration)
- [Usage Overview](#usage-overview)
- [API Reference](#api-reference)
- [Security](#security)
- [Troubleshooting](#troubleshooting)
- [Related Documentation](#related-documentation)
- [License & Support](#license--support)

---

## What This Project Is

**SmartExchange Panel** provides:

1. **Price management** — Categories, price types (currency pairs, buy/sell), regular and special prices, full history.
2. **Finalization workflow** — Review and finalize prices before publication, with approval tracking.
3. **Image rendering** — Generate branded price images from configurable templates (backgrounds, logos, watermarks).
4. **Telegram publishing** — Publish price updates to one or more Telegram channels via configured bots.
5. **Analytics** — Dashboards, charts, trends, top movers, finalization stats.
6. **Template editor** — Visual drag-and-drop editor for price templates (and a standalone template-editor app under `/template-editor/`).
7. **Landing page** — Marketing site at `/landingpage/` (mr. sarafi | آقای صرافی) with EN/FA and RTL.
8. **Instagram Hub** — OAuth and publishing integration for Instagram (optional).

The repository also includes **Request-Manage-System (Iraniu)**, a separate Django application for ad request management (AI moderation, Telegram notifications). It has its own README under `backend/Request-Manage-System/README.md`.

---

## Features

### Core

- **Category-based price management** — Organize currency pairs and price types into categories.
- **Dual price system** — Regular (category) prices and special/promotional prices.
- **Price history** — Full audit trail of changes with timestamps and notes.
- **Currency pairs** — Multiple currencies with buy/sell trade types.
- **Finalization workflow** — Review, approve, and finalize before publishing.

### Publishing & Automation

- **Telegram publishing** — Publish to multiple channels; multiple bots supported.
- **Custom image rendering** — Branded images from templates (Pillow-based).
- **Templates** — Default, category-specific, and special-price templates; backgrounds, logos, watermarks.
- **Visual template editor** — Drag-and-drop layout and styling.
- **Multi-channel** — Manage several Telegram bots and channels.

### Analytics & Reporting

- **Analytics dashboard** — Real-time charts, trends, volatility, category summaries, top movers, finalization stats.
- **Historical data** — e.g. 30-day price history.
- **Performance** — Publication success and channel activity.

### User & Security

- **Roles** — Management, Employee, Developer (and super_admin for users/settings).
- **Auth** — Custom user model, JWT + session auth, login required for panel.
- **Activity & audit** — Logging and who finalized what and when.

### Other

- **Settings** — Centralized site/config management.
- **Log viewer** — Filter logs by level and source.
- **Persian calendar** — jdatetime support.
- **Responsive UI** — Vue 3 SPA with Tailwind; PWA support.

---

## Architecture & Tech Stack

| Layer        | Technology |
|-------------|------------|
| **Frontend** | Vue 3, Vite, Vue Router, Pinia, Tailwind CSS, Chart.js, vue-i18n, PWA (vite-plugin-pwa) |
| **Backend**  | Django 5.2+, Django REST Framework, Simple JWT |
| **Database** | SQLite (default; PostgreSQL-ready) |
| **Image**    | Pillow (PIL) |
| **Telegram** | python-telegram-bot, Pyrogram (as used by apps) |
| **API**      | REST under `/api/`; JSON; session + JWT |

The **frontend** is a single-page application (SPA). All non-API routes are served by Django with the same `index.html`; the Vue app handles routing. The frontend can be developed with Vite's dev server (proxying `/api` and `/media` to Django) or served after building into `backend/static/vue/`.

---

## Project Structure

```
SmartExchangePanel/
├── README.md                    # This file
├── frontend/                    # Vue 3 SPA
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js           # Builds to ../backend/static/vue/
│   └── src/
│       ├── assets/
│       ├── components/          # layout/, ui/
│       ├── layouts/
│       ├── router/
│       ├── services/            # API client
│       ├── stores/              # Pinia: auth, theme, siteSettings
│       └── views/               # auth, dashboard, prices, finalize, categories, settings, analysis, telegram, templates, instagram
│
└── backend/                     # Django project root
    ├── manage.py                # DJANGO_SETTINGS_MODULE=SarafiPardis.settings
    ├── requirements.txt
    ├── SarafiPardis/            # Main Django project
    │   ├── settings.py
    │   ├── urls.py              # API, landing, template-editor, instagram-hub, SPA catch-all
    │   ├── api_urls.py          # Mounts all app APIs under /api/
    │   └── views.py             # SPAView, 404, favicon
    ├── core/                    # Shared utilities (e.g. DRF exception handler)
    │   └── exceptions.py
    ├── accounts/                # Auth, users, roles, JWT, activity log
    ├── category/                # Currency, Category, PriceType
    ├── change_price/            # Price updates, bulk update, PriceHistory
    ├── special_price/           # SpecialPriceType, SpecialPriceHistory
    ├── finalize/                # Finalization, SpecialPriceFinalization, publishing
    ├── price_publisher/         # Templates, image rendering, Telegram publishing
    ├── template_editor/         # Visual template editor (standalone + API)
    ├── analysis/                # Dashboard API, pricing API, charts
    ├── telegram_app/            # Bots, channels, sending
    ├── setting/                 # Site settings, logs
    ├── dashboard/               # Dashboard API
    ├── landing/                 # Landing page (mr. sarafi)
    ├── instagram_hub/           # Instagram OAuth & hub
    ├── static/                  # Static assets (fonts, etc.); Vue build output → static/vue/
    ├── templates/               # Django templates (e.g. 404)
    └── public/
        ├── staticfiles/         # collectstatic output
        └── media/               # Uploaded files
    └── Request-Manage-System/   # Separate app (Iraniu) — see its README
```

---

## Prerequisites

- **Python 3.10–3.12** (recommended; use a **venv** and `pip install -r backend/requirements.txt`. Avoid running `manage.py` with a random global `python` that does not have project dependencies — you will see errors like `No module named 'pytz'`.)
- **Node.js 18+** (for frontend dev and build)
- **pip** and a **virtual environment** (required for local backend commands)
- **Docker + Docker Compose** (recommended for easiest setup)

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd SmartExchangePanel
```

### 2. Backend: virtualenv and dependencies

```bash
cd backend
python -m venv venv
# Windows:
#   venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

**Windows (PowerShell):** from repo root, `cd backend` only once (not `backend\backend`). After `venv` exists, prefer the venv interpreter explicitly:

```powershell
cd C:\Work\Project\SmartExchangePanel\backend
.\venv\Scripts\python.exe manage.py migrate
.\venv\Scripts\python.exe manage.py ensure_default_admin
```

Or from repo root:

```powershell
.\scripts\ensure-default-admin.ps1
```

### 3. Backend: environment (optional but recommended)

Create a `.env` in `backend/` or set:

- **`DJANGO_SECRET_KEY`** — Secret key (e.g. generate with `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`).
- **`DJANGO_DEBUG`** — `True` for dev, `False` in production.
- **`DJANGO_ALLOWED_HOSTS`** — Comma-separated hosts (e.g. `localhost,127.0.0.1,panel.example.com`).
- **`FINALIZE_STRICT_TELEGRAM`** — If `True`, finalization is rolled back when Telegram publish fails.
- **`EXTERNAL_API_URL`** / **`EXTERNAL_API_KEY`** — If you use the external rates API.
- **`INSTAGRAM_BASE_URL`** — Public base URL for media (for Instagram).

Settings read these via `os.environ.get(...)`.

### 4. Backend: database and superuser

```bash
# From backend/
python manage.py migrate
python manage.py createsuperuser
```

### 5. Backend: static files (for production-style serving)

```bash
python manage.py collectstatic --noinput
```

### 6. Frontend: dependencies and build

```bash
cd ../frontend
npm install
npm run build
```

This writes the SPA into `backend/static/vue/` so Django can serve it.

---

## Running the Application

### Option 0: Docker (single container + hot reload)

From repository root:

```bash
docker compose up --build
```

Then open:

- **http://localhost:5173** (frontend with HMR)
- **http://localhost:8000** (backend API/Admin)

Useful commands:

```bash
# View logs
docker compose logs -f app

# Stop containers
docker compose down

# Stop and remove Docker volumes (media + collected static; SQLite file lives on disk under backend/data/)
docker compose down -v
```

Default login (created automatically on backend startup in Docker):

- **Username:** `admin`
- **Password:** `admin`
- **Role:** `super_admin` (full panel access, including user management and site settings)

To create another superuser manually:

```bash
docker compose exec app python manage.py createsuperuser
```

To seed the same default user without Docker (from `backend/` after migrate), use the venv’s Python (not a global interpreter):

```bash
# Linux/macOS (venv activated)
python manage.py ensure_default_admin
```

```powershell
# Windows (explicit venv path)
.\venv\Scripts\python.exe manage.py ensure_default_admin
```

Optional env vars: `DEFAULT_ADMIN_USERNAME`, `DEFAULT_ADMIN_PASSWORD`, `DEFAULT_ADMIN_SYNC_PASSWORD` (when `true`, existing default user’s password is reset on each `ensure_default_admin` run — enabled in `docker-compose` for local dev).

Notes for Docker mode:

- A single `app` container runs both Django (`:8000`) and Vite (`:5173`) from one entrypoint script (no extra process manager package).
- Frontend runs with Vite HMR inside Docker (`CHOKIDAR_USEPOLLING` / `WATCHPACK_POLLING` help file watching on Windows).
- Backend runs with Django `runserver` auto-reload; code is bind-mounted from `./backend`.
- `migrate` and default admin seed (`ensure_default_admin`) run automatically at startup.
- SQLite remains SQLite. The database file is stored at **`backend/data/db.sqlite3` on your machine** (bind-mounted into the container via `SQLITE_PATH=/app/backend/data/db.sqlite3`), so panel changes are written to that file directly.
- Uploaded media and collected static files stay in Docker volumes (`media_data`, `static_data`).

### Option A: Backend only (serves built SPA)

After building the frontend once:

```bash
cd backend
source venv/bin/activate   # or venv\Scripts\activate on Windows
python manage.py runserver
```

Open **http://127.0.0.1:8000**. The SPA is served for all non-API routes.

### Option B: Frontend dev server + backend (recommended for development)

**Terminal 1 — Django:**

```bash
cd backend
source venv/bin/activate
python manage.py runserver
```

**Terminal 2 — Vite:**

```bash
cd frontend
npm run dev
```

Vite runs on **http://localhost:3000** (see `vite.config.js`) and proxies `/api` and `/media` to `http://127.0.0.1:8000`. Use the Vite URL for development.

### CORS

Backend allows credentials and origins for `http://localhost:5173`, `http://127.0.0.1:5173`, `http://localhost:3000`, `http://127.0.0.1:3000`. Adjust `CORS_ALLOWED_ORIGINS` in `SarafiPardis/settings.py` if you use another origin.

---

## Configuration

### Telegram

1. Create bots via [@BotFather](https://t.me/botfather).
2. In the panel: **Telegram** (or admin) → add bots and channels.
3. Configure which channels receive which finalizations.

### Templates

1. Upload backgrounds/logos/watermarks via admin or settings.
2. Create category-specific or special-price templates.
3. Use **Template editor** (UI or `/template-editor/`) for layout and styling.

### User roles

- **Management** — Full access (including finalize, settings).
- **Employee** — Standard operations.
- **Developer** — Technical access.
- **Super admin** — User management and sensitive settings.

---

## Usage Overview

### Price workflow

1. **Categories & price types** — Create categories and define price types (currency pairs, buy/sell).
2. **Update prices** — Use "Price hub" / bulk update by category or single price updates.
3. **Finalize** — In **Finalize**, select prices, choose channel, add notes, and finalize.
4. **Publish** — System renders the image and publishes to the selected Telegram channel(s).

### Special prices

- Define special price types independently.
- Update and finalize them separately; they can use their own templates.

### Analytics

- Open **Analysis** for trends, category summaries, top movers, finalization stats, and historical data.

### Template editing

- Use the **Template editor** to position and style text/image elements and preview before saving.

---

## API Reference

All panel APIs are under **`/api/`** and use the same REST conventions. Authentication: **Session** or **JWT** (e.g. `Authorization: Bearer <access_token>`). Login: `POST /api/auth/login/`; refresh: `POST /api/auth/token/refresh/`.

### Main API prefixes (under `/api/`)

| Prefix | Purpose |
|--------|--------|
| `auth/` | Login, logout, me, token refresh, users, activity |
| `dashboard/` | Dashboard data |
| `categories/` | Categories and price types |
| `prices/` | Price list, detail, update, bulk update, history |
| `special-prices/` | Special price types and updates |
| `finalize/` | Finalization actions |
| `telegram/` | Bots and channels |
| `settings/` | Site settings |
| `analysis/` | Analytics dashboard and **pricing data** |
| `templates/` | Price templates (publisher) |
| `template-editor/` | Template editor API |
| `instagram-hub/` | Instagram hub |

### Public pricing data (read-only)

Suitable for dashboards, bots, or external systems:

- **URL:** `GET /api/analysis/pricing/`
- **Auth:** Configurable (often unauthenticated for public feed).
- **Response:** JSON with `generated_at` and `categories`. Each category has `id`, `name`, `slug`, `description`, and `items`. Regular items include `latest_price`, `latest_price_timestamp`; special-price items include `latest_special_price`, `latest_special_price_timestamp`. Special prices only include items updated in the last 6 hours.

Example response shape:

```json
{
  "generated_at": "2025-01-01T12:00:00Z",
  "categories": [
    {
      "id": 1,
      "name": "Cash",
      "slug": "cash",
      "description": "Cash exchange prices",
      "items": [
        {
          "id": 10,
          "name": "USD / IRR Buy",
          "pair": "USD/IRR",
          "trade_type": "Buy",
          "latest_price": "123456.78",
          "latest_price_timestamp": "2025-01-01T11:55:00Z"
        }
      ]
    },
    {
      "id": null,
      "name": "Special Prices",
      "slug": "special-prices",
      "items": []
    }
  ]
}
```

### Error format

API errors use a common shape: `{ "error": true, "message": "...", "code": "..." }` (e.g. `validation_error`, `permission_denied`, `authentication_failed`, `not_found`, `server_error`).

---

## Security

- **Authentication** — All panel views require login (enforced by middleware); public routes (e.g. login, landing) are excluded.
- **Authorization** — Role-based access; finalize and settings restricted to appropriate roles.
- **CSRF** — Enabled for browser requests.
- **CORS** — Configured for known frontend origins.
- **Production** — Use `DEBUG=False`, strong `SECRET_KEY`, correct `ALLOWED_HOSTS`, and HTTPS (settings enable secure cookies and HSTS when not DEBUG).
- **Secrets** — Prefer environment variables or a secrets manager; do not commit real keys.

---

## Troubleshooting

### "Vue app not built"

- Run `cd frontend && npm run build`. Ensure `backend/static/vue/index.html` exists.

### Telegram publishing fails

- Check bot token and that the bot can post in the channel; verify channel/chat IDs.

### Image rendering errors

- Ensure template assets (backgrounds, fonts) exist and paths in settings are correct (e.g. `TEMPLATE_EDITOR_DEFAULT_FONT`, `PRICE_RENDERER_FONT_ROOT`). Check Pillow is installed.

### Database errors

- Run `python manage.py migrate` from `backend/`. If you use PostgreSQL, set `DATABASES` in settings accordingly.

### 401/403 on API from frontend

- Confirm credentials (session cookie or JWT) and that the user has the required role; check CORS and `credentials: true` if using a separate dev origin.

---

## Related Documentation

- **Frontend:** `frontend/README.md` — Vue app structure and scripts.
- **Landing:** `backend/landing/README.md` — Landing page structure and Django integration.
- **Template editor:** `backend/template_editor/README.md` — Template manager and visual editor usage.
- **Request-Manage-System (Iraniu):** `backend/Request-Manage-System/README.md` — Ad request flow, AI moderation, Telegram bots, runbots, and configuration.

---

## License & Support

- **License:** See repository or project license file.
- **Support:** Configure contact details under **Settings → Site Settings** (e.g. support phone, email). Production and admin URLs are configured in deployment settings.

---

**SmartExchange Panel** — Price management, finalization, and Telegram publishing for currency exchange operations.
