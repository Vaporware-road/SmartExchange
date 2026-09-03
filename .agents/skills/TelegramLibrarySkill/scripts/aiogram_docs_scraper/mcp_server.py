#!/usr/bin/env python3
"""
Minimal MCP server: search local aiogram docs mirror.

Configure in Cursor MCP settings:

{
  "mcpServers": {
    "aiogram-docs": {
      "command": "/absolute/path/to/.cursor/skills/TelegramLibrarySkill/scripts/aiogram_docs_scraper/.venv/bin/python",
      "args": [
        "/absolute/path/to/.cursor/skills/TelegramLibrarySkill/scripts/aiogram_docs_scraper/mcp_server.py"
      ]
    }
  }
}

Requires: pip install 'mcp>=1.2,<2' (in the scraper venv). Skill+search.py works without MCP.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from search import search

try:
    from mcp.server.fastmcp import FastMCP
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "Install mcp in the scraper venv: pip install 'mcp>=1.2,<2'\n"
        "Or use search.py without MCP."
    ) from exc

mcp = FastMCP("aiogram-docs")


@mcp.tool()
def search_aiogram_docs(query: str, limit: int = 12) -> str:
    """Search mirrored https://docs.aiogram.dev/ pages. Returns paths under reference/."""
    results = search(query, limit)
    return json.dumps(results, indent=2, ensure_ascii=False)


@mcp.tool()
def read_aiogram_doc(path: str) -> str:
    """
    Read one mirrored doc page. Path is relative to reference/, e.g.
    aiogram/dispatcher/webhook.md
    """
    ref = Path(__file__).resolve().parents[2] / "reference"
    target = (ref / path).resolve()
    if not str(target).startswith(str(ref.resolve())):
        return json.dumps({"error": "path escapes reference/"})
    if not target.is_file():
        return json.dumps({"error": f"not found: {path}"})
    text = target.read_text(encoding="utf-8", errors="ignore")
    if len(text) > 80_000:
        text = text[:80_000] + "\n\n… truncated …\n"
    return text


if __name__ == "__main__":
    mcp.run()
