# Agent notes (sarraf / SmartExchange)

> **Working inside the SmartExchange workspace?** Start from [SmartExchange/AGENTS.md](SmartExchange/AGENTS.md) — it has everything in one place including env vars, hot files, frontend patterns, and the current WIP plan.

Start here for the two-product overview. For architecture depth, read [SmartExchange/docs/PROJECT_OVERVIEW.md](SmartExchange/docs/PROJECT_OVERVIEW.md).

## Two products in one tree

| Product | Path | Notes |
|---------|------|-------|
| **SmartExchange Panel** | `SmartExchange/backend/` (except below) | Exchange ops: prices, finalize, publish, Telegram channels, Vue SPA |
| **Iraniu (Request-Manage-System)** | `SmartExchange/backend/Request-Manage-System/` | Separate Django app — own docs, models, bots. Do not cross-import. |

All paths below are relative to `SmartExchange/` unless noted.

## Boot and verify

### Docker (recommended)

```bash
cd SmartExchange
cp .env.docker.example .env.docker   # if needed
docker compose up --build
```

- Frontend: `http://localhost:5250`
- Backend: `http://localhost:18000`

### Local dev

Backend (`SmartExchange/backend/`):

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py ensure_default_admin
python manage.py runserver
```

Also run Celery worker + beat (finalize, Telegram background tasks):

```bash
celery -A SmartExchangePanel worker --loglevel=INFO
celery -A SmartExchangePanel beat --loglevel=INFO
```

Frontend (`SmartExchange/frontend/`):

```bash
npm install && npm run dev
```

Dev URL: `http://localhost:3000` (proxies `/api` and `/media` to Django `:8000`).

### Quick checks after a change

```bash
# Backend
cd SmartExchange/backend && python manage.py check

# Frontend
cd SmartExchange/frontend && npm run build
```

## Where to edit (task → directory)

| Task | Directory |
|------|-----------|
| Auth, users, JWT, RBAC | `backend/accounts/` |
| Currencies, categories, price types | `backend/category/` |
| Regular prices | `backend/change_price/` |
| Special (VIP) prices | `backend/special_price/` |
| Finalize pipeline, external API sync | `backend/finalize/` |
| Publish service, Celery tasks, templates | `backend/price_publisher/` |
| Customer bots, channels, webhooks | `backend/telegram_app/` → see Telegram section |
| Site settings, logs | `backend/setting/` |
| Analytics | `backend/analysis/` |
| Instagram integration | `backend/instagram_hub/` |
| Template editor backend | `backend/template_editor/` |
| Vue SPA | `frontend/src/` |
| Iraniu ad-request system | `backend/Request-Manage-System/` only |

Core publish flow: **update prices** → **finalize** (`finalize/`) → **Celery** (`price_publisher/`) → Telegram / Instagram / external WordPress API.

## Stack (short)

- **Frontend:** Vue 3, Vite, Pinia, Vue Router, vue-i18n, Tailwind
- **Backend:** Django 5.2+, DRF, SimpleJWT, Celery + Redis
- **DB:** SQLite (`backend/data/db.sqlite3` in Docker)
- **Telegram (customer bots):** aiogram 3 — not python-telegram-bot / Telethon

## Do not index or grep

These paths are excluded via `.cursorignore` (build artifacts, venv, static output):

- `backend/venv/`, `backend/public/`, `backend/static/vue/`, `frontend/node_modules/`
- `.cursor/skills/TelegramLibrarySkill/reference/` — use search or MCP instead (see Telegram section)

## Telegram bots

Customer bot work (webhooks, polling, reply-keyboard menus, alerts, outbound channel sends in `telegram_app`): **read and follow** [`.cursor/skills/TelegramLibrarySkill/SKILL.md`](.cursor/skills/TelegramLibrarySkill/SKILL.md).

- Library: **aiogram 3** (not python-telegram-bot / Telethon / Pyrogram).
- Repo map: `.cursor/skills/TelegramLibrarySkill/smartexchange.md`
- Search mirrored docs: `.cursor/skills/TelegramLibrarySkill/scripts/aiogram_docs_scraper/search.py`
- MCP (when configured): `search_aiogram_docs`, `read_aiogram_doc` via `user-aiogram-docs`
- Refresh mirror: `.cursor/skills/TelegramLibrarySkill/scripts/scrape_aiogram_docs.sh`
- Customer UX uses **reply keyboards** (panel under chat input). Inline buttons are for channel broadcasts only.

### How to make agents load this skill

1. **Automatic (project skill):** keep the skill under `.cursor/skills/TelegramLibrarySkill/` — Cursor injects its description into agent context.
2. **This file:** agents reading `AGENTS.md` are pointed at the skill (you are here).
3. **Optional user rule:** add  
   `For any SmartExchange telegram_app / Telegram bot task, use the TelegramLibrarySkill.`  
   in Cursor User Rules.
4. **Explicit invoke:** in chat, say `use TelegramLibrarySkill` or `/telegram-library-skill`.
5. **Do not** install the skill under `~/.cursor/skills-cursor/` (Cursor-managed). Personal copy only under `~/.cursor/skills/` if you want it in every project.

## Related docs

- [SmartExchange/AGENTS.md](SmartExchange/AGENTS.md) — **local agent notes** (env vars, hot files, patterns, WIP)
- [SmartExchange/README.md](SmartExchange/README.md) — human-oriented setup and env vars
- [SmartExchange/docs/PROJECT_OVERVIEW.md](SmartExchange/docs/PROJECT_OVERVIEW.md) — full architecture and API map
- [SmartExchange/docs/MASTER_PLAN.md](SmartExchange/docs/MASTER_PLAN.md) — phased roadmap
- [SmartExchange/tel.txt](SmartExchange/tel.txt) — current WIP task list (Telegram Hub, AutoPostConfig, analytics, price bug fix)
