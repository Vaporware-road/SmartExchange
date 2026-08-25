# MrExchange Deployment Guide for Coding Agents

Use this guide to run MrExchange locally or deploy it on a Docker host. The repository contains a separate `backend/Request-Manage-System/` product; deploy only the main MrExchange stack unless explicitly asked otherwise.

## 1. What runs

The main product is a Vue 3 frontend, Django/DRF backend, SQLite database, Celery worker, Celery Beat scheduler, and Redis broker. Docker Compose starts four services:

- `app`: Django plus Vite development server under Supervisor
- `celery-worker`: asynchronous publishing and automation tasks
- `celery-beat`: scheduled task dispatcher
- `redis`: Celery broker/result backend

## 2. Delivery modes

Use `DEPLOYMENT_MODE=cloud` for the hosted SaaS service: one deployment on your infrastructure with individually managed customer accounts and server-side trial enforcement.

Use `DEPLOYMENT_MODE=customer_server` for a dedicated installation: deploy the same stack on the customer’s server with customer-specific secrets, database/media volumes, domain, backups, and integrations. Never share data or credentials between installations.

The application code is shared; infrastructure ownership and account data are isolated.

On our own infrastructure each trial signup gets its own isolated stack rather than a shared multi-tenant database; the `fleet` app provisions it. For the commercial path that takes a customer from a trial to their own server — access, license, data migration, DNS, smoke test, handover — follow `CUSTOMER_SERVER_ONBOARDING.md`.

## 3. Prerequisites

- Docker Engine with Compose v2
- At least 2 GB free memory and several GB of disk space for the image/build cache
- A copy of the repository

Check the tools:

```bash
docker --version
docker compose version
```

## 4. Configure secrets before deployment

Create the runtime env file from the tracked template:

```bash
cp .env.example .env.docker
```

Set at minimum:

```dotenv
DJANGO_SECRET_KEY=<long-random-secret>
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=your-domain.example,www.your-domain.example
DJANGO_CSRF_TRUSTED_ORIGINS=https://your-domain.example,https://www.your-domain.example
DEFAULT_ADMIN_USERNAME=admin
DEFAULT_ADMIN_PASSWORD=<strong-password>
DEFAULT_ADMIN_SYNC_PASSWORD=false
```

For a local-only demo, `DJANGO_ALLOWED_HOSTS` may include `localhost,127.0.0.1`, but never ship `admin/admin` or a known secret to production. Keep `.env.docker` private; it is ignored by Git in normal project setup.

Optional integrations are configured with the remaining variables in `.env.example`, including Telegram, Instagram, and Celery settings.

## 5. Choose free host ports

The default production-style Compose file maps:

- Frontend: host `5250` → container `5173`
- Backend API: host `18000` → container `8000`
- Redis: host `16379` → container `6379`

Check availability:

```bash
for p in 5250 18000 16379; do
  ss -ltn "sport = :$p" | grep -q LISTEN && echo "busy: $p" || echo "free: $p"
done
```

If any port is busy, edit only the host side of the relevant mapping in `docker-compose.yml`. Keep the container side unchanged. Also update `VITE_HMR_CLIENT_PORT`, `VITE_DEV_ORIGIN`, and any allowed-origin settings when changing the frontend port.

Example alternate mappings:

```yaml
ports:
  - "15250:5173"
  - "19000:8000"
  - "17379:6379"
```

Do not expose Redis publicly on an internet-facing host. For production, remove its host `ports` mapping and let Compose networking handle it.

## 6. Validate and start

Validate the rendered Compose configuration first:

```bash
docker compose config --quiet
```

Build and start the stack:

```bash
docker compose up --build -d
```

The first build can take several minutes because it installs Python and Node dependencies. Subsequent starts can use:

```bash
docker compose up -d
```

Startup automatically runs database migrations, collects static files, and ensures the configured admin/demo accounts exist.

## 7. Verify the deployment

Check all containers:

```bash
docker compose ps
```

Expected state: `app`, `celery-worker`, `celery-beat`, and `redis` are running; Redis should show `healthy`.

Check logs:

```bash
docker compose logs --tail=100 app celery-worker celery-beat redis
```

Check the services from the host, replacing ports if customized:

```bash
curl -i http://127.0.0.1:5250/
curl -i http://127.0.0.1:18000/api/settings/site/
docker compose exec -T redis redis-cli ping
```

Success criteria:

- Frontend returns HTTP `200`
- Backend endpoint returns HTTP `200` or an expected authenticated/permission response
- Redis prints `PONG`
- Celery worker logs `ready`
- Celery Beat logs `beat: Starting`

Run Django checks inside the app container:

```bash
docker compose exec -T app sh -c 'cd /app/backend && python manage.py check'
```

## 8. Open the application

Default URLs:

- Panel: `http://localhost:5250/`
- API: `http://localhost:18000/`
- Admin: `http://localhost:18000/admin/`

The default credentials come from `.env.docker`; use a strong password and disable `DEFAULT_ADMIN_SYNC_PASSWORD` after the first bootstrap.

## 9. Operations

Follow logs:

```bash
docker compose logs -f --tail=100 app celery-worker celery-beat
```

Restart without rebuilding:

```bash
docker compose restart
```

Rebuild after dependency or image changes:

```bash
docker compose up --build -d
```

Stop while preserving named volumes:

```bash
docker compose down
```

`docker compose down -v` deletes named volumes, including persistent media/static data and any database data stored in Compose volumes. Use it only when intentionally resetting the environment.

## 10. Production checklist

1. Set a unique strong `DJANGO_SECRET_KEY`.
2. Set `DJANGO_DEBUG=False`.
3. Set exact `DJANGO_ALLOWED_HOSTS` and `DJANGO_CSRF_TRUSTED_ORIGINS`.
4. Set a strong admin password and `DEFAULT_ADMIN_SYNC_PASSWORD=false`.
5. Configure Telegram/Instagram credentials only through environment or the application’s encrypted configuration flow.
6. Put the app behind HTTPS and a reverse proxy.
7. Do not publish Redis directly.
8. Back up the SQLite database and media volume.
9. Run migrations before declaring a new release healthy.
10. Confirm frontend, API, worker, Beat, and Redis health after rollout.
11. Have a rollback and database-backup plan before changing production data.

## 11. Common failures

### Port already allocated

Find the process/container using the port, then select another host port in `docker-compose.yml`. Do not change the container port unless the Supervisor/Vite configuration is changed too.

### Frontend is reachable but API calls fail

Check that the app container is running and inspect:

```bash
docker compose logs --tail=200 app
```

Confirm the browser-visible frontend port and Vite proxy target match the Compose environment.

### Containers start but requests reset/refuse

Wait for migrations and Supervisor startup, then retry. Verify with:

```bash
docker compose ps
docker compose logs --tail=200 app
```

### Celery tasks fail on Telegram

A running worker does not mean external Telegram credentials are valid. Check bot tokens/channels in application settings and inspect worker logs for authentication errors.

### Build fails during dependency download

Retry after checking Docker DNS/network access. The Compose file includes static package-index host mappings for reproducible builds; those mappings may need maintenance if upstream CDN addresses change.

## 12. Handoff format for another model

When handing this deployment to another coding model, report:

```text
Compose file: docker-compose.yml
Stack command: docker compose up --build -d
Frontend URL: http://localhost:<host-frontend-port>/
Backend URL: http://localhost:<host-backend-port>/
Redis check: docker compose exec -T redis redis-cli ping
Health result: <containers + HTTP statuses>
Known warnings: <non-blocking log warnings>
```
