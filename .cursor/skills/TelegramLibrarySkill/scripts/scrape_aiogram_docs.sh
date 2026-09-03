#!/usr/bin/env bash
# Mirror every page of https://docs.aiogram.dev/ into reference/aiogram/
#
# Strategy (offline-friendly, avoids RTD rate limits):
#   1. Clone aiogram @ tag matching docs
#   2. sphinx-build HTML (identical to the published site)
#   3. Convert each HTML page → Markdown for the skill
# Fallback: MODE=live polite crawl, or MODE=zip RTD htmlzip
set -euo pipefail

SKILL_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SCRAPER="${SKILL_ROOT}/scripts/aiogram_docs_scraper"
VENV="${SCRAPER}/.venv"
REF="${SKILL_ROOT}/reference"
PINNED_TAG="${AIOGRAM_TAG:-v3.30.0}"
MODE="${MODE:-local}"  # local | zip | live
WORK="${SCRAPER}/.build"

PYTHON_BIN="${PYTHON_BIN:-}"
if [[ -z "$PYTHON_BIN" ]]; then
  for candidate in python3.12 python3.11 python3.14 python3; do
    if command -v "$candidate" >/dev/null 2>&1; then
      PYTHON_BIN="$candidate"
      break
    fi
  done
fi
if [[ -z "$PYTHON_BIN" ]]; then
  echo "No python3 found" >&2
  exit 1
fi

echo "Using $PYTHON_BIN (mode=${MODE}, tag=${PINNED_TAG})"
if [[ ! -d "$VENV" ]]; then
  "$PYTHON_BIN" -m venv "$VENV"
fi
# shellcheck disable=SC1091
source "${VENV}/bin/activate"
pip install -q --upgrade pip
pip install -q -r "${SCRAPER}/requirements.txt"

export REF
mkdir -p "$WORK"

run_local() {
  SRC="${WORK}/aiogram"
  if [[ ! -d "$SRC/.git" ]]; then
    rm -rf "$SRC"
    git clone --depth 1 --branch "$PINNED_TAG" https://github.com/aiogram/aiogram.git "$SRC"
  else
    git -C "$SRC" fetch --depth 1 origin "refs/tags/${PINNED_TAG}:refs/tags/${PINNED_TAG}" 2>/dev/null || true
    git -C "$SRC" checkout -f "$PINNED_TAG"
  fi

  echo "Installing aiogram[docs] for Sphinx..."
  pip install -q -e "${SRC}[docs]"

  echo "Building HTML with sphinx-build (same content as docs.aiogram.dev)..."
  rm -rf "${SRC}/docs/_build/html"
  sphinx-build -b html -q -d "${SRC}/docs/_build/doctrees" \
    "${SRC}/docs" "${SRC}/docs/_build/html"

  python "${SCRAPER}/scrape.py" --out "$REF" --html-dir "${SRC}/docs/_build/html"

  rm -rf "${REF}/aiogram-examples"
  mkdir -p "${REF}/aiogram-examples"
  cp -R "${SRC}/examples/." "${REF}/aiogram-examples/"
}

run_zip_or_live() {
  if [[ "${1:-}" == "--limit" ]]; then
    python "${SCRAPER}/scrape.py" --out "$REF" --mode live --limit "${2:?}"
  else
    python "${SCRAPER}/scrape.py" --out "$REF" --mode "$MODE"
  fi
  VERSION="$(python - <<'PY'
import json, os
from pathlib import Path
m = Path(os.environ["REF"]) / "manifest.json"
print((json.loads(m.read_text()).get("version") if m.exists() else None) or "3.30.0")
PY
)"
  TAG="${AIOGRAM_TAG:-v${VERSION}}"
  TMP="$(mktemp -d)"
  if git clone --depth 1 --branch "$TAG" https://github.com/aiogram/aiogram.git "$TMP/aiogram" 2>/dev/null; then
    rm -rf "${REF}/aiogram-examples"
    mkdir -p "${REF}/aiogram-examples"
    cp -R "$TMP/aiogram/examples/." "${REF}/aiogram-examples/"
  fi
  rm -rf "$TMP"
}

if [[ "$MODE" == "local" ]]; then
  run_local
else
  run_zip_or_live "$@"
fi

echo "Search smoke test:"
python "${SCRAPER}/search.py" webhook FSM --limit 5
echo "Done. Docs at ${REF}/aiogram"
