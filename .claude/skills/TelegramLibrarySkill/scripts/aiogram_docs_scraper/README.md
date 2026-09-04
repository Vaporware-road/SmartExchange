# aiogram docs scraper

Mirrors **every** page of [docs.aiogram.dev](https://docs.aiogram.dev/en/latest/) as Markdown for TelegramLibrarySkill.

## Quick start

```bash
# From repo root (default: local Sphinx build = same HTML as the site)
.cursor/skills/TelegramLibrarySkill/scripts/scrape_aiogram_docs.sh
```

Creates `.venv/`, builds aiogram docs with Sphinx, converts ~670 HTML pages → `../reference/aiogram/`, copies `examples/`, writes `manifest.json` + `INDEX.md`.

### Modes

| Mode | Env | Behavior |
|------|-----|----------|
| **local** (default) | `MODE=local` | Clone tag → `sphinx-build` → Markdown (recommended) |
| zip | `MODE=zip` | Download RTD htmlzip (often singlehtml; not ideal) |
| live | `MODE=live` | Crawl each live URL (rate-limits easily) |

```bash
AIOGRAM_TAG=v3.30.0 MODE=local .cursor/skills/TelegramLibrarySkill/scripts/scrape_aiogram_docs.sh
MODE=live .cursor/skills/TelegramLibrarySkill/scripts/scrape_aiogram_docs.sh --limit 20
```

## Search (for agents)

```bash
.venv/bin/python search.py "Router webhook"
.venv/bin/python search.py FSM storage --json --limit 8
```

## Optional MCP server

```bash
.venv/bin/pip install mcp
```

Add to Cursor MCP config (absolute paths):

```json
{
  "mcpServers": {
    "aiogram-docs": {
      "command": "/ABS/sarraf/.cursor/skills/TelegramLibrarySkill/scripts/aiogram_docs_scraper/.venv/bin/python",
      "args": [
        "/ABS/sarraf/.cursor/skills/TelegramLibrarySkill/scripts/aiogram_docs_scraper/mcp_server.py"
      ]
    }
  }
}
```

Tools: `search_aiogram_docs`, `read_aiogram_doc`.

## Layout

| File | Role |
|------|------|
| `scrape.py` | Zip / live crawl / local HTML → Markdown |
| `search.py` | Local full-text search CLI |
| `mcp_server.py` | Optional MCP wrapper |
| `../scrape_aiogram_docs.sh` | One-shot refresh entrypoint |
| `.build/` | Cached aiogram clone + Sphinx HTML (gitignored) |
