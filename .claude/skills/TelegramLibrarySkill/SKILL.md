---
name: telegram-library-skill
description: >-
  Author and refactor SmartExchange Telegram bots with aiogram 3. Use when
  editing telegram_app, customer bot FSM, webhooks, polling, inline keyboards,
  callback message edits, Bot API handlers, outbound channel broadcasts,
  admin notify, or price alerts via Telegram. Includes a full local mirror of
  https://docs.aiogram.dev/ — search before coding.
---

# TelegramLibrarySkill (aiogram 3)

SmartExchange customer bots use **aiogram 3**, not python-telegram-bot or Telethon.

## Before coding

1. Read [smartexchange.md](smartexchange.md) for this repo’s layout and invariants.
2. **Search the mirrored docs** (do not load the whole tree):

```bash
.claude/skills/TelegramLibrarySkill/scripts/aiogram_docs_scraper/.venv/bin/python \
  .claude/skills/TelegramLibrarySkill/scripts/aiogram_docs_scraper/search.py "webhook FSM"
```

3. Open only the matching paths under [reference/](reference/) (see [reference/INDEX.md](reference/INDEX.md)).
4. Prefer **reply keyboards** (button panel under the chat input). Do not use
   inline message buttons for customer menus. Each tap sends the label as text
   and the bot replies with the next keyboard panel.

## Project conventions

- Package: `backend/telegram_app/bot/` (factory, routers, FSM, middleware).
- Sync Django/Celery call sites use `telegram_app.services.telegram_client.TelegramService` (aiogram under the hood).
- Customer UX: `ReplyKeyboardMarkup` (`keyboard="reply"`) — bottom panel buttons, not inline.
- Persist customer FSM in Django `BotSession` via custom storage — do not invent a second session store.
- Keep Django models, staff DRF/Vue, Celery alert math, and currency catalog behavior unless the task asks otherwise.
- Do not touch Iraniu / Request-Manage-System bots.
- Channel price broadcasts may still use **inline** URL buttons.

## Must-read docs (by task)

| Task | Open |
|------|------|
| Routers / handlers | `reference/aiogram/dispatcher/router.md` |
| FSM multi-step flows | `reference/aiogram/dispatcher/finite_state_machine/index.md` |
| Filters / callbacks | `reference/aiogram/dispatcher/filters/index.md` |
| Webhooks | `reference/aiogram/dispatcher/webhook.md` |
| Bot methods | `reference/aiogram/api/bot.md` |
| Inline keyboards | `reference/aiogram/utils/keyboard.md` |

## Anti-patterns

- Inline keyboards for customer menu navigation (use reply keyboards instead).
- Sync `asyncio.run()` per update inside a long-lived loop.
- MTProto / Telethon / Pyrogram for BotFather-token customer bots.
- Dumping the full docs mirror into chat — cite `reference/` paths or search hits instead.

## Refresh docs (full site mirror)

Rebuilds the same HTML as https://docs.aiogram.dev/ via Sphinx, then converts every page to Markdown under `reference/aiogram/` (~670 pages):

```bash
.claude/skills/TelegramLibrarySkill/scripts/scrape_aiogram_docs.sh
# AIOGRAM_TAG=v3.30.0 MODE=local ...
# MODE=live --limit 20   # polite live crawl (rate-limits easily)
```

Details: [scripts/aiogram_docs_scraper/README.md](scripts/aiogram_docs_scraper/README.md).

Legacy RST-only mirror (no autodoc expansion): `scripts/fetch_aiogram_docs.sh`.

## Optional MCP

Local search/read tools without stuffing the whole tree into context. See [scripts/aiogram_docs_scraper/README.md](scripts/aiogram_docs_scraper/README.md).

## Agent discovery

Project skill path: `.claude/skills/TelegramLibrarySkill/` (auto-discovered by Claude Code).

Also documented in repo root `AGENTS.md`. Optional: add a Cursor User Rule  
`For any SmartExchange telegram_app / Telegram bot task, use the TelegramLibrarySkill.`  
Or invoke explicitly: `use TelegramLibrarySkill`.
