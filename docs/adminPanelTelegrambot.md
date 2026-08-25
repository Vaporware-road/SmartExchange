# In-bot Telegram admin panel

Summary of work completed for the MrExchange customer bot admin experience (no login button).

## Source plan

Derived from the earlier research thread on “4 admins, different panel than customers, no login”:

- Telegram already identifies users via `from.id`
- Staff are a whitelist of numeric IDs on panel `CustomUser.telegram_id`
- On `/start` (or `/admin`), branch: staff → admin keyboard; everyone else → customer keyboard
- Authorize every admin action server-side (not UI-only)

This is **separate** from the web Telegram Hub admin UI (`/telegram/send` token-gated hub).

## What existed before

- Staff with `super_admin` / `management` + `telegram_id` only received **DM notifications** when a customer confirmed an exchange request (`admin_notify.py`)
- `/start` always opened the **customer** main menu for everyone

## What was built

### Access rules (`telegram_app/services/staff_access.py`)

A Telegram user is a bot admin when:

1. An active `CustomUser` has matching `telegram_id` (digits only), and
2. Role is `super_admin` (any bot), or `management` **and** they **own** that `TelegramBot`

No password / Login button in the bot.

### Admin FSM (`telegram_app/services/admin_conversation.py`)

Reply-keyboard panel (same UX convention as the customer bot). Admin home includes: Pending requests, Recent requests, Analytics Dashboard, Customer Analysis, Re-engagement, Bot stats, Customer menu.

See [AdminPanelV1.md](./AdminPanelV1.md) for analytics, snapshots, campaigns, and web hub integration.

| Action | Behavior |
|--------|----------|
| `/start` or `/admin` (as staff) | Admin home |
| Analytics Dashboard | Daily usage, channel members, top currencies, exchange filters, new members |
| Customer Analysis | Returned/inactive users, peak hours, VIP ratio |
| Re-engagement | Audience send, periodic campaigns, offer creation |
| Pending requests | Live `pending` / `notified` requests for this bot |
| Recent requests | Last 10 requests |
| Bot stats | Session customers + status counts |
| Open `Req #…` | Detail: pair, amount, tag, TTL, etc. |
| Close request | Sets status `closed` |
| Set customer tag | Global / VIP / Special |
| Customer menu | Switch to normal customer main menu |

Session states added: `ADMIN_MENU`, `ADMIN_REQUEST_LIST`, `ADMIN_REQUEST_DETAIL`, `ADMIN_SET_TAG`, plus analytics/re-engage states (`ADMIN_ANALYTICS`, `ADMIN_REENGAGE_*`, `ADMIN_OFFER_CREATE`, etc.).

### Wiring (`conversation.py`)

- `/start` → admin menu if staff, else customer menu
- `/admin` → admin menu, or a clear “not registered” message
- Admin reply labels mapped before customer label mapping
- Staff “Back to menu” from customer flows can return to admin home

### Notify copy (`admin_notify.py`)

Staff DMs for new exchange requests now include: `Open admin panel in this bot: /admin`.

### Web hub (V1.1)

The in-bot pending/recent lists are **live ORM reads**. The web hub at `/telegram/send` used to show a one-shot dashboard snapshot after token verify, so new customer exchanges could appear in-bot but not on the web Exchange Requests table.

Web hub behavior now:

- Verify (`getMe`) once per browser tab (Pinia + `sessionStorage`, 8h TTL); sidebar re-entry does not show the full-screen gate
- Opening Exchange Requests / Reports / Analytics refreshes `GET /api/telegram/admin/dashboard/?bot_id=`
- Exchange Requests table also loads `GET /api/telegram/exchange-requests/?bot_id=` (Refresh button)
- Bot picker on the hub header if the owner has multiple bots
- Run `python manage.py migrate` after deploy (`telegram_app.0010_admin_analytics_foundation`); a missing migration 500s the dashboard

See [AdminPanelV1.md](./AdminPanelV1.md) for the full web hub + analytics spec.

### Tests (`telegram_app.tests.InBotAdminPanelTests`)

- Admin `/start` → admin panel
- Customer `/start` → customer menu
- List + close pending request
- Non-owner management user denied on `/admin`

## Local ops notes

- Active bot in this DB was **id=2** (`Vroad`), not `1`
- Poll with: `python manage.py poll_telegram_bots --bot-id 2`
- Staff ID used for testing: `6296044948` on `samadmin` (`super_admin`)

## Key files

| File | Role |
|------|------|
| `backend/telegram_app/services/staff_access.py` | Whitelist / ownership check |
| `backend/telegram_app/services/admin_conversation.py` | Admin menus + actions |
| `backend/telegram_app/services/conversation.py` | `/start` / `/admin` branch |
| `backend/telegram_app/services/admin_notify.py` | Staff DM + `/admin` hint |
| `backend/telegram_app/models.py` | Admin session states |
| `backend/telegram_app/bot/states.py` | aiogram state mirrors |
| `backend/telegram_app/tests.py` | `InBotAdminPanelTests` |

## Explicitly not in this slice

- Web Telegram Hub category admin (verify-bot / dashboard / re-engage) — see [AdminPanelV1.md](./AdminPanelV1.md) and **Web hub (V1.1)** above
- Iraniu / Request-Manage-System `AdminProfile` bot
- Mini App / login button for admins
