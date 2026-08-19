# AGENTS.md

## Cursor Cloud specific instructions

### What this repo is
`SmartExchange Panel` is a full-stack exchange operations panel:
- **Backend** (`backend/`): Django 5.2+ (installs Django 6.x) REST API + SPA host. SQLite DB.
- **Frontend** (`frontend/`): Vue 3 + Vite 6 SPA (dev server on port `3000`).
- **Async** : Celery worker + Celery beat, brokered by **Redis**. Needed only for the finalize/publish/telegram background pipeline; login + price/category management work without them.
- `backend/Request-Manage-System/` is a **separate** Django project with its own docs — not part of this panel's dev loop.

Standard setup/run commands live in `README.md` (Quick Start Local Development). Only the non-obvious deltas are captured below.

### System packages (not handled by the update script)
The update script only refreshes language deps (`backend/venv` + pip, and `frontend` npm). These OS packages must be present in the base image/snapshot (install once with apt if a fresh pod lacks them):
- `python3-venv`, `python3-dev`, `build-essential` (needed to create the venv / build wheels)
- `redis-server` (Celery broker/result backend)

Start Redis before Celery: `redis-server --daemonize yes --save "" --appendonly no` (verify with `redis-cli ping`).

### KNOWN BLOCKER — backend does not boot as-committed
`backend/category/api.py` does `from orders.models import OrderIntake`, but there is **no `orders` app** anywhere in the repo (and it is not in `INSTALLED_APPS`). This breaks the whole URLconf, so `runserver`/`migrate`/`check` all fail with `ModuleNotFoundError: No module named 'orders'`. `OrderIntake` is used only as a category-delete guard (`OrderIntake.objects.filter(category=...).count()`).
To run the backend you must first restore the missing `orders` app (a model with a `category` FK) or otherwise resolve that import. This is a code defect, not an environment problem.

### Ports & the committed proxy gotcha
- `frontend/.env.local` is committed and sets `VITE_API_PROXY_TARGET=http://127.0.0.1:18000` (the Docker host port), which **overrides** the vite.config default of `8000`. So for in-VM local dev, run Django on **18000** to match it: `./venv/bin/python manage.py runserver 127.0.0.1:18000`. (Alternatively point the proxy at 8000, but do not commit that.) Vite dev serves the browser on `3000` and proxies `/api`, `/media`, `/static` to the backend.

### Run the dev services (from `backend/` unless noted, venv activated or via `./venv/bin/`)
- Backend: `python manage.py runserver 127.0.0.1:18000`
- Frontend (from `frontend/`): `npm run dev`  → http://localhost:3000
- Celery worker: `celery -A SmartExchangePanel worker --loglevel=INFO --concurrency=2`
- Celery beat: `celery -A SmartExchangePanel beat --loglevel=INFO`
- First-time DB seed: `python manage.py migrate` then `python manage.py ensure_default_admin --username admin --password admin`, `python manage.py ensure_demo_user`, and (optional demo content) `python manage.py seed_demo_data`. Default panel login is `admin` / `admin`.

### Lint / test / build
- Tests: `python manage.py test` (Django test runner; ~106 tests). 2 tests in `template_editor/tests.py` about font resolution (`InterVF.ttf` vs `VazirmatnVF.ttf`) fail on `main` independent of environment — treat as pre-existing.
- Lint: there is no dedicated Python linter or frontend ESLint config. `python manage.py check` is the closest static check.
- Build: `npm run build` (from `frontend/`) writes to `backend/static/vue/` with `emptyOutDir: true`, which **wipes committed assets** there — avoid running it unless you intend to regenerate those tracked files. Development uses `npm run dev`, not a build.
