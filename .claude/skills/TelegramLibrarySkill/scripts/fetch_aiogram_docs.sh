#!/usr/bin/env bash
# Refresh mirrored aiogram docs into reference/aiogram/
set -euo pipefail

SKILL_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REF="${SKILL_ROOT}/reference"
PINNED_TAG="${AIOGRAM_TAG:-v3.30.0}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "Fetching aiogram ${PINNED_TAG} docs..."
git clone --depth 1 --branch "$PINNED_TAG" https://github.com/aiogram/aiogram.git "$TMP/aiogram"

rm -rf "${REF}/aiogram"
mkdir -p "${REF}/aiogram"

# Prefer pandoc RST→Markdown; fall back to copying RST.
if command -v pandoc >/dev/null 2>&1; then
  echo "Converting RST → Markdown with pandoc..."
  while IFS= read -r -d '' f; do
    rel="${f#"$TMP/aiogram/docs/"}"
    out="${REF}/aiogram/${rel%.rst}.md"
    mkdir -p "$(dirname "$out")"
    pandoc -f rst -t gfm -o "$out" "$f" 2>/dev/null || cp "$f" "${out%.md}.rst"
  done < <(find "$TMP/aiogram/docs" -name '*.rst' -print0)
else
  echo "pandoc not found; copying RST sources..."
  cp -R "$TMP/aiogram/docs/." "${REF}/aiogram/"
fi

# Copy examples for agent reference (small).
if [[ -d "$TMP/aiogram/examples" ]]; then
  rm -rf "${REF}/aiogram-examples"
  mkdir -p "${REF}/aiogram-examples"
  cp -R "$TMP/aiogram/examples/." "${REF}/aiogram-examples/"
fi

FETCH_DATE="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
cat > "${REF}/INDEX.md" <<EOF
# aiogram docs mirror

- **Pinned tag:** \`${PINNED_TAG}\`
- **Fetched:** ${FETCH_DATE}
- **Upstream:** https://docs.aiogram.dev/en/latest/
- **Source:** https://github.com/aiogram/aiogram/tree/${PINNED_TAG}/docs

## How agents should use this

Do **not** load the entire tree. Open \`INDEX.md\` then only the files needed for the current task.

## High-value paths

| Topic | Path |
|-------|------|
| Install | \`aiogram/install.md\` |
| Migration 2→3 | \`aiogram/migration_2_to_3.md\` |
| Dispatcher | \`aiogram/dispatcher/index.md\` |
| Router | \`aiogram/dispatcher/router.md\` |
| FSM | \`aiogram/dispatcher/finite_state_machine/index.md\` |
| Filters | \`aiogram/dispatcher/filters/index.md\` |
| Middleware | \`aiogram/dispatcher/middlewares.md\` |
| Webhook | \`aiogram/dispatcher/webhook.md\` |
| Bot API client | \`aiogram/api/bot.md\` |
| Types index | \`aiogram/api/types/index.md\` |
| Methods index | \`aiogram/api/methods/index.md\` |
| Keyboards | \`aiogram/utils/keyboard.md\` |
| Examples | \`aiogram-examples/\` |

Official HTML docs remain authoritative if a mirrored page is incomplete: https://docs.aiogram.dev/en/latest/
EOF

echo "Done. Docs at ${REF}/aiogram"
