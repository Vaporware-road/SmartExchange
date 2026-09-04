# SmartExchange Panel

SmartExchange Panel is a full-stack exchange operations platform:

- Manage regular and special prices
- Review/finalize changes before publishing
- Render branded images
- Publish to Telegram channels
- Analyze activity and trends
- Manage templates, settings, users, and optional Instagram integration

This repository also contains another Django app at `backend/Request-Manage-System/`. That app is separate and has its own documentation.

---

## Table of Contents

- [Current Architecture](#current-architecture)
- [Tech Stack](#tech-stack)
- [Repository Layout](#repository-layout)
- [Quick Start (Docker)](#quick-start-docker)
- [Quick Start (Local Development)](#quick-start-local-development)
- [Environment Variables](#environment-variables)
- [Main Functional Areas](#main-functional-areas)
- [API Overview](#api-overview)
- [Production Notes](#production-notes)
- [Troubleshooting](#troubleshooting)
- [Related Docs](#related-docs)

---

## Current Architecture

The project runs as:

- **Frontend:** Vue 3 SPA in `frontend/`
- **Backend:** Django API + SPA host in `backend/`
- **Database:** SQLite by default (`backend/data/db.sqlite3` in Docker mode)
- **Queue/Broker:** Celery workers with Redis broker/result backend
- **Static/Media:** Django static + media folders/volumes

Frontend behavior:

- In local dev, Vite serves the app and proxies `/api` and `/media` to Django.
- In production-style mode, `npm run build` outputs to `backend/static/vue/`, and Django serves the built SPA.

---

## Tech Stack

- **Frontend:** Vue 3, Vite 6, Vue Router, Pinia, vue-i18n, Tailwind, Chart.js
- **Backend:** Django 5.2+, DRF, SimpleJWT
- **Image rendering:** Pillow
- **Messaging:** Telegram integrations (bot/channel management and publishing)
- **Optional integrations:** Instagram Hub

---

## Repository Layout

```text
SmartExchangePanel/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── layouts/
│   │   ├── router/
│   │   ├── services/
│   │   ├── stores/
│   │   └── views/
│   ├── package.json
│   └── vite.config.js
├── backend/
│   ├── SmartExchangePanel/        # Django project settings/urls
│   ├── accounts/
│   ├── analysis/
│   ├── category/
│   ├── change_price/
│   ├── dashboard/
│   ├── finalize/
│   ├── instagram_hub/
│   ├── price_publisher/
│   ├── setting/
│   ├── special_price/
│   ├── telegram_app/
│   ├── template_editor/
│   ├── manage.py
│   └── requirements.txt
├── scripts/
│   └── ensure-default-admin.ps1
├── docker-compose.yml
└── .env.docker.example
```

---

## Quick Start (Docker)

Recommended for fastest setup.

### 1) Configure env

```bash
cp .env.docker.example .env.docker
```

Edit `.env.docker` for your host/domain when needed.

### 2) Start

```bash
docker compose up --build
```

Current port mapping from `docker-compose.yml`:

- **Frontend (Vite in container):** `http://localhost:5250`
- **Backend (Django in container):** `http://localhost:18000`
- **Redis broker:** `redis://localhost:6379`

### 3) Default admin

Container startup runs migrations and seeds/updates default admin:

- Username: `admin`
- Password: `admin`

Stop commands:

```bash
docker compose down
docker compose down -v
```

---

## Quick Start (Local Development)

Use this if you do not want Docker.

## Backend

```bash
cd backend
python -m venv venv
```

Activate venv:

- Windows PowerShell: `.\venv\Scripts\activate`
- Linux/macOS: `source venv/bin/activate`

Install deps and run:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py ensure_default_admin
python manage.py runserver
```

Backend URL: `http://127.0.0.1:8000`

In additional terminals (required for finalize/telegram background execution):

```bash
celery -A SmartExchangePanel worker --loglevel=INFO
celery -A SmartExchangePanel beat --loglevel=INFO
```

## Frontend

In a second terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend dev URL (from `vite.config.js`): `http://localhost:3000`

Proxy target defaults to `http://127.0.0.1:8000` unless `VITE_API_PROXY_TARGET` is set.

---

## Environment Variables

## Docker env file (`.env.docker`)

Key values used in deployment:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_USE_HTTP_BEHIND_PROXY`
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_CSRF_TRUSTED_ORIGINS`
- `FINALIZE_STRICT_TELEGRAM`
- `INSTAGRAM_BASE_URL`
- `EXTERNAL_API_URL`
- `EXTERNAL_API_KEY`
- `CELERY_BROKER_URL`
- `CELERY_RESULT_BACKEND`
- `CELERY_TASK_TIME_LIMIT`
- `CELERY_TASK_SOFT_TIME_LIMIT`
- `FINALIZE_TASK_WAIT_TIMEOUT`
- `REDIS_CACHE_URL` (Django cache DB index for bot gateway live rates)
- `BOT_GATEWAY_FRONTEND_URL` (public Vue URL for Telegram Web App order button)
- `BOT_GATEWAY_RATES_CACHE_TTL` (seconds, default `15`)
- `BOT_CUSTOMER_JWT_LIFETIME_MINUTES` (default `60`)
- `BOT_GATEWAY_RATE_LIMIT` / `BOT_GATEWAY_RATE_WINDOW` (per-customer message throttle)
- `DEFAULT_ADMIN_USERNAME`
- `DEFAULT_ADMIN_PASSWORD`
- `DEFAULT_ADMIN_SYNC_PASSWORD` (optional; avoid `true` in production)

See `.env.docker.example` for a template.

## Runtime env used by compose

`docker-compose.yml` also sets:

- `SQLITE_PATH=/app/backend/data/db.sqlite3`
- `VITE_API_PROXY_TARGET=http://127.0.0.1:8000`
- `PLAYWRIGHT_FRONTEND_BASE_URL=http://app:5173` (Celery worker → Vite in `app` container)
- `PLAYWRIGHT_MAX_CONCURRENT=2`, `SCREENSHOT_CACHE_TTL=300`
- polling options for file-watch stability on Windows
- dedicated `celery-worker` and `celery-beat` services

---

## Main Functional Areas

- **Bot Gateway:** inbound Telegram/WhatsApp auto-replies with Redis-cached rates, Web App order intake, admin orders queue
- **Auth & User management:** login/logout/me, role-based access, activity logs
- **Price management:** categories, price types, regular prices, history
- **Special prices:** separate flow and history
- **Finalize pipeline:** confirm and publish final values
- **Telegram:** bots/channels, manual sending, automation settings
- **Template editor:** visual configuration and media tools; optional **Playwright headless render** for Telegram boards (Site Settings → `use_playwright_for_template_render`, falls back to Pillow)
- **Settings:** site branding/settings, logs, upload policy
- **Analysis:** dashboard + pricing endpoints
- **Instagram Hub (optional):** config/status/preview flow

---

## API Overview

Base prefix: `/api/`

Common groups:

- `/api/auth/`
- `/api/dashboard/`
- `/api/categories/`
- `/api/prices/`
- `/api/special-prices/`
- `/api/finalize/`
- `/api/telegram/`
- `/api/settings/`
- `/api/analysis/`
- `/api/templates/`
- `/api/template-editor/`
- `/api/instagram-hub/`
- `/api/bot-gateway/` (Telegram/WhatsApp webhooks, bot customer auth, order submit)
- `/api/orders/` (staff order queue review)

Bot gateway setup:

1. Enable `gateway_enabled` on a Telegram bot (API or Django admin).
2. Register webhook: `python manage.py setup_bot_webhook --bot-id=N --base-url=https://your-domain`
3. Configure `BOT_GATEWAY_FRONTEND_URL` to the public Vue origin (e.g. `https://panel.example.com` or dev port `5250`).
4. For WhatsApp: create `WhatsAppConfig` in Django admin with Meta Cloud API credentials and subscribe webhook to `/api/bot-gateway/webhook/whatsapp/`.

Auth model:

- Login: `POST /api/auth/login/`
- Me: `GET /api/auth/me/`
- Logout: `POST /api/auth/logout/`
- JWT refresh: `POST /api/auth/token/refresh/`

Error format:

```json
{
  "error": true,
  "message": "Human readable message",
  "code": "validation_error"
}
```

---

## Production Notes

- Set `DJANGO_DEBUG=False`
- Set strict `DJANGO_ALLOWED_HOSTS`
- Set correct `DJANGO_CSRF_TRUSTED_ORIGINS`
- Use strong `DJANGO_SECRET_KEY`
- Disable automatic password re-sync for default admin (`DEFAULT_ADMIN_SYNC_PASSWORD=false`)
- Serve behind HTTPS in real deployments

Frontend build note:

- `npm run build` uses `vite-plugin-pwa`.
- If build fails with Workbox max-size errors, reduce icon asset sizes (`pwa-192x192.png`, `pwa-512x512.png`, `apple-touch-icon.png`) or adjust PWA workbox config.

---

## Troubleshooting

## `ERR_CONNECTION_REFUSED` on frontend URL

No server is listening on that port. Start the frontend process:

- Docker mode: `docker compose up`
- Local mode: `cd frontend && npm run dev`

## Frontend says port 3000 but not reachable

Check if Vite is actually running and if another process already occupies 3000.

## Login shows generic 500 page

Check backend/container logs immediately:

```bash
docker logs --tail 300 smart-exchange-app-1
```

Also test API directly:

```bash
curl -i http://localhost:18000/api/settings/site/
curl -i http://localhost:18000/api/auth/me/
```

## UI language does not switch to Persian

- Ensure frontend is rebuilt/restarted after i18n changes.
- Hard refresh browser (and clear service worker cache if needed).

## API proxy errors like `ECONNREFUSED 127.0.0.1:8000`

Backend is not running or proxy target is wrong.

- Local: start Django on `127.0.0.1:8000`
- Docker: make sure compose app is healthy and mapped ports are used correctly

## Build fails due to PWA icon size

Optimize oversized PNG icons or update Vite PWA Workbox limits.

---

## Related Docs

- `frontend/README.md`
- `backend/template_editor/README.md`
- `backend/landing/README.md`
- `backend/Request-Manage-System/README.md`

---

If you want, this README can also be split into:

- `README.md` (quick start + operations)
- `docs/deployment.md` (prod-specific guide)
- `docs/dev.md` (contributor workflow)
