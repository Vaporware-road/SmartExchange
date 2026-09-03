# SmartExchange Telegram map

Pinned library: **aiogram 3.30.0** (see `reference/INDEX.md`).

## Layout

```text
SmartExchange/backend/telegram_app/
  bot/                      # aiogram Dispatcher, routers, middleware, FSM storage
    factory.py
    middlewares.py
    states.py
    storage.py
    keyboards.py
    handlers/               # start, menu, profile, exchange, alerts
  services/
    telegram_client.py      # sync façade over aiogram.Bot (Celery, admin, DRF)
    conversation.py         # domain FSM helpers / reply content (used by handlers)
    dispatcher.py           # webhook entry → feed_update; broadcast; setWebhook
    admin_notify.py
    alert_checker.py
    currency_catalog.py
  management/commands/poll_telegram_bots.py
```

## Invariants

1. Customer menus use the **reply keyboard panel** under the input (not inline buttons on messages).
2. Per-user debounce middleware drops overlapping updates.
3. `BotSession` + `CustomerProfile` remain the source of truth for staff UI and history.
4. Outbound channel price publishing stays on the same bots/channels; only the client library changes.
5. Poller: one asyncio loop; never `asyncio.run()` per update.
6. Channel broadcast buttons may remain inline (URLs).

## Entry points

| Path | Role |
|------|------|
| `POST /api/telegram/webhook/<bot_id>/` | Production inbound |
| `manage.py poll_telegram_bots` | Dev long-poll |
| `TelegramService.send_*` | Sync outbound from Celery / admin / API |
