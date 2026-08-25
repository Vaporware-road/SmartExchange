# Admin Panel Analytics V1

Full specification for the in-bot Telegram admin analytics dashboard, customer analysis, re-engagement campaigns, PostgreSQL persistence, and webapp integration.

See also: [adminPanelTelegrambot.md](./adminPanelTelegrambot.md) (original in-bot admin slice).

---

## Overview

Admin Panel Analytics V1 adds:

1. **Analytics Dashboard** — daily bot usage, channel member snapshots, top currencies, exchange request filters, dual new-member metrics
2. **Customer Analysis** — returned/inactive users, peak hours, VIP vs ordinary request ratio
3. **Re-engagement** — audience targeting, periodic campaigns, offer templates
4. **PostgreSQL persistence** — snapshot and campaign tables shared by bot + web hub + programmer profile
5. **Web integration** — Telegram Hub admin panels + programmer user profile **Bot analytics** tab

---

## In-bot admin menu tree

```
Admin panel (/start or /admin as staff)
├── Pending requests
├── Recent requests
├── Analytics Dashboard
│   ├── [message] Summary (30d usage, channel members, top currencies)
│   ├── Exchange Requests
│   │   ├── Successful Requests (status=notified)
│   │   └── Pending Requests (status=pending)
│   └── New members
│       ├── Last month
│       ├── Last 3 months
│       ├── Last 9 months
│       └── Last year
├── Customer Analysis
│   └── [message] Returned, inactive, peak hour, VIP ratio
├── Re-engagement
│   ├── Audience: Global / VIP / Special currencies / Inactive → type message → send now
│   ├── Periodic Campaigns → audience → message → daily/weekly/monthly schedule
│   └── Offer Creation → audience → title → body → save
├── Bot stats
└── Customer menu
```

**Implementation:** [`backend/telegram_app/services/admin_conversation.py`](../backend/telegram_app/services/admin_conversation.py)

---

## Metric definitions

| Metric | Source | Notes |
|--------|--------|-------|
| Daily bot usage | `BotDailyUsageSnapshot` or `BotSession.last_activity` | Distinct users per day (30d window) |
| Channel members | `ChannelMemberSnapshot` via `getChatMemberCount` | Requires bot as channel admin |
| Channel post views | N/A | **Not available** via Telegram Bot API |
| Publish activity | `Finalization` + `SpecialPriceFinalization` | Proxy for channel activity |
| Most requested currencies | `ExchangeRequest` source/target counts | Top 10 |
| Successful requests | `status=notified` | Matches web hub |
| Pending requests | `status=pending` | Strict pending only |
| New members (channel) | Current member count − snapshot at period start | Admin-verified channels only |
| New members (bot DM) | `BotCustomerGrowthSnapshot` or new `BotSession` | First session on bot |
| Returned users | Active in 30d, session created before 30d ago | Re-engaged after idle period |
| Inactive users | No `BotSession.last_activity` in 30d | |
| Peak hours | Hour histogram of `ExchangeRequest.created_at` | Server timezone |
| VIP ratio | Avg requests per VIP ÷ avg per global customer | |

---

## PostgreSQL setup

Set either `DATABASE_URL` or individual `POSTGRES_*` variables:

```bash
export POSTGRES_DB=sarraf
export POSTGRES_USER=sarraf
export POSTGRES_PASSWORD=secret
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432
```

Or:

```bash
export DATABASE_URL=postgresql://user:pass@host:5432/dbname
```

Without these, the app falls back to SQLite (development).

Install the Postgres driver (included in `requirements.txt`):

```bash
pip install 'psycopg[binary]>=3.1'
```

Run migrations:

```bash
cd MrExchange/backend
python manage.py migrate telegram_app
```

**Required:** `telegram_app.0010_admin_analytics_foundation` must be applied. If it is missing, `GET /api/telegram/admin/dashboard/` returns **500** (schema drift — snapshot/campaign tables do not exist). After deploy, run `python manage.py migrate` before using the hub analytics panels.

---

## Database models

| Table | Model | Purpose |
|-------|-------|---------|
| `telegram_app_botdailyusagesnapshot` | `BotDailyUsageSnapshot` | Daily active users per bot |
| `telegram_app_channelmembersnapshot` | `ChannelMemberSnapshot` | Channel subscriber history |
| `telegram_app_botcustomergrowthsnapshot` | `BotCustomerGrowthSnapshot` | New bot DM users per day |
| `telegram_app_reengagecampaign` | `ReengageCampaign` | Scheduled audience DMs |
| `telegram_app_reengageoffer` | `ReengageOffer` | Offer templates |
| `telegram_app_campaigndeliverylog` | `CampaignDeliveryLog` | Send audit trail |

Migration: `telegram_app/migrations/0010_admin_analytics_foundation.py`

---

## Celery beat schedule

| Task | Default interval | Env override |
|------|------------------|--------------|
| `telegram_app.snapshot_daily_bot_usage` | 86400s (daily) | `TELEGRAM_SNAPSHOT_DAILY_SECONDS` |
| `telegram_app.snapshot_customer_growth` | 86400s | `TELEGRAM_SNAPSHOT_GROWTH_SECONDS` |
| `telegram_app.snapshot_channel_members` | 86400s | `TELEGRAM_SNAPSHOT_CHANNEL_SECONDS` |
| `telegram_app.run_due_reengage_campaigns` | 3600s | `TELEGRAM_CAMPAIGN_CHECK_SECONDS` |

Requires `celery-worker` and `celery-beat` processes (see `docker-compose.yml`).

---

## API reference

Base path: `/api/telegram/admin/`

| Method | Path | Description |
|--------|------|-------------|
| GET | `/dashboard/?bot_id=` | Full dashboard payload (reads snapshots first) |
| GET | `/snapshots/channel-members/?bot_id=&months=` | Channel growth + snapshot history |
| POST | `/reengage/` | One-shot audience DM (batch cap 100) |
| GET/POST | `/campaigns/` | List / create periodic campaigns |
| PATCH/DELETE | `/campaigns/<id>/` | Update / delete campaign |
| GET/POST | `/offers/` | List / create offers (`send_now` optional) |
| POST | `/offers/<id>/` | Send existing offer now |
| PATCH/DELETE | `/offers/<id>/` | Update / delete offer |

Programmer profile payload includes `telegram_analytics[]` per owned bot via `GET /api/auth/programmer/users/<id>/`.

Hub exchange table (live, not snapshot): `GET /api/telegram/exchange-requests/?bot_id=` (optional; omitted = owned bots for management, all bots for super_admin).

---

## Web UI

| Location | Component | Features |
|----------|-----------|----------|
| Telegram Hub | `TelegramHubAdminPanels.vue` | Analytics, exchange filters, campaigns, offers |
| Programmer profile | `ProgrammerUserDetailView.vue` | **Bot analytics** tab (read-only) |

### Web hub refresh (V1.1)

- **Verify once per browser tab.** `POST /api/telegram/admin/verify-bot/` is cached in Pinia + `sessionStorage` (`telegramHubSession`, 8h TTL). Leaving `/telegram/send` and returning via the sidebar does **not** show the full-screen verify gate.
- **Dashboard refresh.** Opening Customers Status, Notifications, Exchange Requests, Reports, Analytics, or Customer Analysis re-fetches `GET /api/telegram/admin/dashboard/?bot_id=`. Exchange Requests also has a **Refresh** button and loads the table from `GET /api/telegram/exchange-requests/?bot_id=` (falls back to the dashboard snapshot while loading). The last admin section is restored after leaving the hub.
- **Bot picker.** Multi-bot owners can switch the scoped bot in the hub header; lists and counts reload for that `bot_id`.
- Logout (and login / impersonation / expired JWT) clears the hub session cache.
- Dashboard HTTP 500 (for example missing migration `0010`) stays on the hub with an inline error — it does not redirect to the global 500 page.

---

## Known limitations

1. **Channel post view counts** — not exposed by Telegram Bot API; member count + publish activity shown instead.
2. **Channel snapshots** — bot must be channel administrator; non-admin channels excluded from channel growth.
3. **Re-engage batch cap** — 100 messages per run to respect Telegram rate limits.
4. **Periodic campaigns** — process in batches across scheduled runs.

---

## Key files

| File | Role |
|------|------|
| `backend/telegram_app/services/analytics_service.py` | Shared metrics + snapshot writers |
| `backend/telegram_app/services/reengage_service.py` | Audience send + campaign runner |
| `backend/telegram_app/services/admin_conversation.py` | In-bot menus |
| `backend/telegram_app/admin_api.py` | REST endpoints |
| `backend/telegram_app/tasks.py` | Celery snapshot + campaign tasks |
| `backend/accounts/api_views.py` | Programmer profile analytics payload |
| `frontend/src/views/telegram/TelegramHubAdminPanels.vue` | Hub admin UI |
| `frontend/src/stores/telegramHub.js` | Session-scoped verify cache + selected bot |
| `frontend/src/views/programmer/ProgrammerUserDetailView.vue` | Profile analytics tab |
