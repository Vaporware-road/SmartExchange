# MrExchange Panel — current structure

Snapshot of the app **as it exists in this repo now**. Git root is `sarraf`; almost all product code lives in `MrExchange/`.

This is an operations panel for currency exchange desks. Staff update buy/sell rates, managers finalize them, the backend renders branded price images, and posts go to Telegram (and optionally Instagram).

---

## What it is

A full-stack exchange operations platform:

- Manage regular and special prices
- Review and finalize before publishing
- Render branded images (Pillow + templates)
- Publish to Telegram channels
- Optional Instagram Hub (Meta Graph)
- Analysis, logs, users, branding, template editor
- Public JSON snapshot of latest prices

UI languages: English and Persian (`frontend/src/locales/`).

---

## Who uses it

| Role | Username field | What they can do |
|------|----------------|------------------|
| `employee` | CustomUser.role | Update prices, history, most day-to-day screens |
| `management` | CustomUser.role | Same plus finalize, settings, user center |
| `super_admin` | CustomUser.role | Full access |
| `developer` | CustomUser.role | Exists on the user model |

Frontend gates: `/finalize` needs `auth.can('finalize')`; `/settings` needs `auth.can('settings')`; `/users` is limited to `super_admin` and `management`.

Auth: JWT (`SimpleJWT`) plus `token_version` for force logout. Demo login: `POST /api/auth/demo-login/` (management demo user, no password; used by marketing `?demo=1`).

---

## Core workflow

1. **Structure** — currencies, categories, price types (source/target + buy/sell).
2. **Update** — regular prices and special prices; bulk update per category.
3. **History** — every change is stored (`event_at` optional for backdated imports).
4. **Finalize** — managers confirm which rates go live and which channels get them.
5. **Render** — Pillow builds a branded image from price templates / template editor / site branding.
6. **Publish** — Celery sends to Telegram; optional Instagram feed/story.
7. **Sync (optional)** — finalize can push to `EXTERNAL_API_URL` with `EXTERNAL_API_KEY`.

---

## Tech stack (current)

| Layer | Tech |
|-------|------|
| Frontend | Vue 3, Vite 6, Vue Router, Pinia, vue-i18n, Tailwind, Chart.js, PWA |
| Backend | Django 5.2+, DRF, SimpleJWT |
| Images | Pillow |
| Jobs | Celery + Redis (worker + beat) |
| DB | SQLite default (`backend/db.sqlite3` locally, or `SQLITE_PATH` / `backend/data/db.sqlite3` in Docker) |
| Messaging | Telegram Bot API (python-telegram-bot / pyrogram in deps) |
| Optional | Instagram Hub (encrypted tokens), OpenAI only in the **separate** Iraniu app |

Dev: Vite on **http://localhost:3000**, proxies `/api` and `/media` to Django **http://127.0.0.1:8000**.

Prod-style: `npm run build` writes to `backend/static/vue/`; Django serves the SPA.

Docker (optional): `docker compose up --build` — panel `localhost:5250`, API `localhost:18000`, Redis `6379`. Needs `.env.docker` (copy from `.env.example`).

---

## Repository layout

```text
sarraf/
└── MrExchange/
    ├── README.md
    ├── معرفی-پنل.md
    ├── baseFromhub.md          # this file
    ├── docker-compose.yml
    ├── Dockerfile
    ├── .env.example
    ├── frontend/               # Vue 3 SPA
    ├── backend/                # Django API + SPA host
    ├── docker/
    ├── docs/
    ├── scripts/
    ├── landing page/           # static marketing assets
    └── backend/Request-Manage-System/   # separate Django app (Iraniu)
```

### Frontend (`frontend/src/`)

```text
src/
├── App.vue
├── main.js
├── assets/
├── components/          # layout + UI
├── composables/
├── config/
├── constants/
├── i18n / locales/      # en.json, fa.json
├── layouts/             # AppLayout
├── pages/templates/     # TemplateEditor
├── router/index.js
├── services/            # API client
├── stores/              # auth, theme, siteSettings
├── utils/
├── vendor/
└── views/
    ├── auth/            # Login, Landing
    ├── dashboard/
    ├── prices/
    ├── special-prices/
    ├── categories/
    ├── finalize/
    ├── settings/
    ├── users/
    ├── analysis/
    ├── telegram/
    ├── templates/
    ├── instagram/
    └── errors/
```

### Backend Django apps (`backend/`)

| App | Job |
|-----|-----|
| `MrExchangePanel` | Settings, Celery, root URLs, `/api/` router |
| `accounts` | CustomUser, JWT, activity logs, demo-login |
| `category` | Currency, Category, PriceType |
| `change_price` | Regular PriceHistory |
| `special_price` | SpecialPriceType, pairs, history |
| `finalize` | Finalization records + publish orchestration |
| `telegram_app` | Bots, channels, send, studio settings |
| `price_publisher` | PriceTemplate assets, render, Celery publish tasks |
| `template_editor` | Visual templates, layers, widgets |
| `setting` | SiteSettings (branding/contact), system logs |
| `dashboard` | Dashboard API |
| `analysis` | Analytics API |
| `instagram_hub` | OAuth config, feed/story publish log |
| `landing` | Landing routes/assets |
| `core` | Public prices snapshot, exception handler |
| `Request-Manage-System` | **Not** wired into the panel. Separate Iraniu project |

There is **no `orders` app** in this tree. Category delete used to import `orders.models.OrderIntake`. That import is now optional (`try/except ImportError`) so the panel starts.

---

## Frontend routes (panel)

Public: `/login`, `/landing`, `/error/404|500|403`.

Authenticated (AppLayout):

| Path | Screen |
|------|--------|
| `/` | Dashboard |
| `/update` | Price hub (regular + special) |
| `/prices/category/:id/update` | Bulk update |
| `/prices/special/:id/update` | Update special price |
| `/prices/:id/history` | Regular price history |
| `/special-prices/new` | New special type |
| `/special-prices/:id/history` | Special history |
| `/finalize` | Finalize dashboard |
| `/finalize/category/:id` | Finalize category |
| `/finalize/special-price/:id` | Finalize special |
| `/categories` | Category list |
| `/categories/new`, `/:id/edit` | Category form |
| `/categories/:id/price-types/...` | Price type form |
| `/categories/:id/telegram-studio` | Telegram studio |
| `/settings` | Site settings |
| `/settings/logs` | Logs |
| `/users` | User center |
| `/analysis` | Analytics |
| `/telegram/send` | Manual send |
| `/telegram/bots/new`, `/:id/edit` | Bot form |
| `/telegram/settings` | Telegram settings |
| `/templates` | Templates dashboard |
| `/templates/new` | New price template |
| `/templates/media` | Media library |
| `/templates/:id/editor` | Visual template editor |
| `/instagram` | Instagram Hub |

---

## API map

Base prefix: `/api/`.

Typical error JSON:

```json
{
  "error": true,
  "message": "Human readable message",
  "code": "validation_error"
}
```

| Prefix | Purpose |
|--------|---------|
| `/api/public/prices/` | Unauthenticated, throttled latest rates snapshot |
| `/api/auth/` | login, logout, me, token refresh, demo-login |
| `/api/dashboard/` | Dashboard data |
| `/api/categories/` | Categories, currencies, price types |
| `/api/prices/` | Regular prices and history |
| `/api/special-prices/` | Special types, pairs, history |
| `/api/finalize/` | Confirm and publish pipeline |
| `/api/telegram/` | Bots, channels, send, automation |
| `/api/templates/` | Price publisher templates |
| `/api/template-editor/` | Visual editor |
| `/api/instagram-hub/` | OAuth, config, publish status |
| `/api/settings/` | Site settings and logs |
| `/api/analysis/` | Analytics |

Auth endpoints: `POST /api/auth/login/`, `GET /api/auth/me/`, `POST /api/auth/logout/`, `POST /api/auth/token/refresh/`.

---

## Domain model (short)

- **Currency** — code, name, symbol
- **Category** — name, Telegram caption/media/buttons, last-used template
- **PriceType** — category, source/target currency, buy/sell, order, active
- **PriceHistory** — value, optional `event_at`
- **SpecialPriceType / SpecialPricePair / SpecialPriceHistory** — same idea outside the category tree
- **Finalization / SpecialPriceFinalization** — who published, channel, captions, Telegram response
- **TelegramBot / TelegramChannel**
- **PriceTemplate** — background, logo, watermark (default / category / special)
- **Template / Layer / Widget** — editor (clock, date, text, QR, chart, image, …)
- **SiteSettings** — singleton branding: logo, phones, address, hours, map, social, upload policy, fonts
- **InstagramConfig / InstagramPublicationLog** — tokens encrypted at rest
- **CustomUser / UserActivityLog**

---

## What the product can do

**Prices.** Currencies, categories, price types, single and bulk updates, full history.

**Special prices.** Types and pairs with their own history, templates, and finalize path.

**Telegram.** Register bots and channels; restrict targets; manual send; per-category studio; finalize posts image + caption.

**Templates.** Price-image templates and a visual editor with layers/widgets and a media library. Round-robin last-used templates on publish.

**Instagram (optional).** Meta Graph OAuth, feed/story after finalize, caption suffix and hashtags, publication log.

**Branding.** Site name, logo, favicon, contact block used in published captions.

**Control.** JWT, roles, activity logs, system logs, dashboard, analysis charts.

**Public / integrations.** `GET /api/public/prices/`; optional external rates push on finalize; marketing landing + demo autologin.

---

## Separate app: Iraniu (`backend/Request-Manage-System/`)

Not part of the MrExchange panel runtime. Own Django project, Bootstrap UI, SQLite.

Flow: ad submissions → optional OpenAI moderation → staff approve/reject → Telegram notify (edit-and-resubmit links). Config in a `SiteConfiguration` singleton.

---

## How to run locally (no Docker)

Three terminals, from `MrExchange`.

**Backend**

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py ensure_default_admin
python manage.py runserver
```

**Celery** (needed for finalize / Telegram; needs Redis)

```bash
cd backend
source venv/bin/activate
celery -A MrExchangePanel worker --loglevel=INFO
# optional:
celery -A MrExchangePanel beat --loglevel=INFO
```

**Frontend**

```bash
cd frontend
npm install
npm run dev
```

Open **http://localhost:3000**. API: **http://127.0.0.1:8000**.

Without Redis/Celery, login and price edits still work; finalize/Telegram background jobs fail.

### Docker

```bash
cd MrExchange
cp .env.example .env.docker
docker compose up --build
```

Requires Docker Desktop running. Panel `http://localhost:5250`, API `http://localhost:18000`. Compose seeds `admin` / `admin` unless you change env.

---

## Current local notes

- Default Django DB path is `backend/db.sqlite3` unless `SQLITE_PATH` is set.
- A local superuser was created on that DB: username `samadmin`, password `SarrafLocal2026!`, role `super_admin`. Change this before any real deploy.
- `orders` is referenced in category delete but the app is absent; import is optional so `runserver` works.
- `docs/MASTER_PLAN.md` describes an older rebrand (Pardis → MrExchange). Vue + DRF conversion is already the live architecture.

---

## Related files

- `README.md` — ops, env, troubleshooting
- `معرفی-پنل.md` — Persian product intro
- `frontend/README.md`
- `backend/template_editor/README.md`
- `backend/landing/README.md`
- `backend/Request-Manage-System/README.md`
