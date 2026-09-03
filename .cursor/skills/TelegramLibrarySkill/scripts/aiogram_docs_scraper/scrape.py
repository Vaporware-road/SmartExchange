#!/usr/bin/env python3
"""
Mirror every page of https://docs.aiogram.dev/ as Markdown.

Primary strategy: download ReadTheDocs HTML zip (one request, all pages).
Fallback: polite live crawl via Sphinx searchindex.js.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
import shutil
import sys
import tempfile
import time
import zipfile
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urljoin, urlparse

import httpx
from bs4 import BeautifulSoup
from markdownify import markdownify as html_to_md

BASE = "https://docs.aiogram.dev/en/latest/"
HTMLZIP_URL = "https://docs.aiogram.dev/_/downloads/en/latest/htmlzip/"
USER_AGENT = "SmartExchange-aiogram-docs-scraper/1.2 (+local skill mirror)"
SKIP_NAMES = {"search", "genindex", "py-modindex", "404"}
CONTENT_SELECTORS = (
    "div[role='main']",
    "article",
    "#furo-main-content",
    "main",
    "div.document",
)


@dataclass
class PageRecord:
    docname: str
    title: str
    url: str
    path: str
    bytes: int
    status: int


class RateLimiter:
    def __init__(self, min_interval: float) -> None:
        self.min_interval = min_interval
        self._lock = asyncio.Lock()
        self._next = 0.0

    async def wait(self) -> None:
        async with self._lock:
            now = time.monotonic()
            delay = self._next - now
            if delay > 0:
                await asyncio.sleep(delay)
            self._next = time.monotonic() + self.min_interval


def skill_reference_dir(explicit: Path | None) -> Path:
    if explicit is not None:
        return explicit.resolve()
    return Path(__file__).resolve().parents[2] / "reference"


def clean_doc_text(text: str) -> str:
    text = text.replace("¶", "").replace("\xa0", " ")
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text.strip()


def extract_title(soup: BeautifulSoup, fallback: str) -> str:
    heading = soup.select_one("h1")
    if heading:
        text = clean_doc_text(heading.get_text(" ", strip=True))
        text = re.sub(r"\s*#\s*$", "", text).strip()
        if text:
            return text
    if soup.title and soup.title.string:
        return clean_doc_text(
            soup.title.string.replace(" — aiogram", "").replace(" documentation", "")
        )
    return fallback


def extract_main_html(soup: BeautifulSoup) -> str:
    for selector in CONTENT_SELECTORS:
        node = soup.select_one(selector)
        if node is not None:
            for junk in node.select(
                "nav, .headerlink, .viewcode-link, script, style, "
                ".related, .sphinxsidebar, footer, .page-info"
            ):
                junk.decompose()
            return str(node)
    body = soup.body
    return str(body) if body else str(soup)


def to_markdown(html: str, source_url: str, title: str) -> str:
    md = html_to_md(
        html,
        heading_style="ATX",
        bullets="-",
        strip=["img"],
    )
    md = clean_doc_text(md)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    md = re.sub(r"\\_", "_", md)
    header = f"# {title}\n\n> Source: [{source_url}]({source_url})\n\n"
    body = re.sub(rf"^#\s+{re.escape(title)}\s*\n+", "", md, count=1)
    return header + body + "\n"


def html_path_to_docname(rel: Path) -> str | None:
    parts = rel.parts
    # zip usually: docs-aiogram-dev-en-latest/en/latest/....html
    if "latest" in parts:
        idx = parts.index("latest")
        rel = Path(*parts[idx + 1 :])
    elif "en" in parts:
        idx = parts.index("en")
        rest = parts[idx + 1 :]
        if rest and rest[0] == "latest":
            rest = rest[1:]
        rel = Path(*rest)
    if rel.suffix != ".html":
        return None
    stem = rel.with_suffix("").as_posix()
    if stem in SKIP_NAMES or stem.startswith("_"):
        return None
    return stem


def convert_html_file(html_path: Path, docname: str, out_root: Path) -> PageRecord:
    url = urljoin(BASE, f"{docname}.html")
    rel = "index.md" if docname == "index" else f"{docname}.md"
    out_path = out_root / "aiogram" / rel
    html = html_path.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, "lxml")
    title = extract_title(soup, docname)
    markdown = to_markdown(extract_main_html(soup), url, title)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(markdown, encoding="utf-8")
    return PageRecord(docname, title, url, rel, len(markdown.encode()), 200)


def write_index(ref: Path, version: str, records: list[PageRecord], mode: str) -> None:
    fetched = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    ok = sum(1 for r in records if r.status == 200)
    lines = [
        f"# aiogram docs mirror ({mode})",
        "",
        f"- **Docs version:** `{version}`",
        f"- **Fetched:** {fetched}",
        f"- **Upstream:** {BASE}",
        f"- **Pages:** {ok}/{len(records)} OK",
        f"- **Manifest:** `manifest.json`",
        "",
        "## How agents should use this",
        "",
        "Do **not** load the entire tree. Open `INDEX.md`, then only the files needed.",
        "Search locally:",
        "",
        "```bash",
        "python .cursor/skills/TelegramLibrarySkill/scripts/aiogram_docs_scraper/search.py \"webhook FSM\"",
        "```",
        "",
        "## High-value paths",
        "",
        "| Topic | Path |",
        "|-------|------|",
        "| Install | `aiogram/install.md` |",
        "| Migration 2→3 | `aiogram/migration_2_to_3.md` |",
        "| Dispatcher | `aiogram/dispatcher/index.md` |",
        "| Router | `aiogram/dispatcher/router.md` |",
        "| FSM | `aiogram/dispatcher/finite_state_machine/index.md` |",
        "| Filters | `aiogram/dispatcher/filters/index.md` |",
        "| Middleware | `aiogram/dispatcher/middlewares.md` |",
        "| Webhook | `aiogram/dispatcher/webhook.md` |",
        "| Bot API client | `aiogram/api/bot.md` |",
        "| Types index | `aiogram/api/types/index.md` |",
        "| Methods index | `aiogram/api/methods/index.md` |",
        "| Keyboards | `aiogram/utils/keyboard.md` |",
        "| Examples | `aiogram-examples/` |",
        "",
        "## Full page list",
        "",
    ]
    for record in sorted(records, key=lambda r: r.docname):
        mark = "OK" if record.status == 200 else f"HTTP {record.status}"
        lines.append(f"- [{record.title}](aiogram/{record.path}) — `{record.docname}` ({mark})")
    lines.append("")
    (ref / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")
    manifest = {
        "base": BASE,
        "version": version,
        "fetched": fetched,
        "mode": mode,
        "page_count": len(records),
        "ok_count": ok,
        "pages": [asdict(r) for r in sorted(records, key=lambda r: r.docname)],
    }
    (ref / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def detect_version_from_html(html_root: Path) -> str:
    for candidate in html_root.rglob("documentation_options.js"):
        text = candidate.read_text(encoding="utf-8", errors="ignore")
        match = re.search(r"VERSION:\s*'([^']+)'", text)
        if match:
            return match.group(1)
    return "unknown"


def scrape_from_zip(out_dir: Path, zip_path: Path) -> tuple[str, list[PageRecord]]:
    extract_dir = Path(tempfile.mkdtemp(prefix="aiogram-docs-"))
    try:
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(extract_dir)
        version = detect_version_from_html(extract_dir)
        aiogram_out = out_dir / "aiogram"
        if aiogram_out.exists():
            shutil.rmtree(aiogram_out)
        aiogram_out.mkdir(parents=True, exist_ok=True)

        records: list[PageRecord] = []
        for html_path in extract_dir.rglob("*.html"):
            rel = html_path.relative_to(extract_dir)
            docname = html_path_to_docname(rel)
            if not docname:
                continue
            try:
                records.append(convert_html_file(html_path, docname, out_dir))
            except Exception as exc:
                print(f"  skip {docname}: {exc}", file=sys.stderr)
        return version, records
    finally:
        shutil.rmtree(extract_dir, ignore_errors=True)


async def download_htmlzip(client: httpx.AsyncClient, dest: Path) -> None:
    print(f"Downloading HTML zip from {HTMLZIP_URL} ...")
    async with client.stream("GET", HTMLZIP_URL, follow_redirects=True) as response:
        response.raise_for_status()
        with dest.open("wb") as fh:
            async for chunk in response.aiter_bytes():
                fh.write(chunk)
    print(f"  saved {dest.stat().st_size} bytes")


# --- live crawl fallback -------------------------------------------------


def parse_search_index(raw: str) -> tuple[list[str], list[str]]:
    match = re.search(r"Search\.setIndex\((\{.*\})\)\s*;?\s*$", raw, re.S)
    if not match:
        raise RuntimeError("Could not parse Sphinx searchindex.js")
    data: dict[str, Any] = json.loads(match.group(1))
    return list(data["docnames"]), list(data["titles"])


def docname_to_url(docname: str) -> str:
    return urljoin(BASE, f"{docname}.html")


def should_skip_url(url: str) -> bool:
    path = unquote(urlparse(url).path)
    if not path.startswith("/en/latest/"):
        return True
    rel = path[len("/en/latest/") :]
    return rel.startswith("_") or rel.split("/")[0].replace(".html", "") in SKIP_NAMES


async def fetch_text(
    client: httpx.AsyncClient,
    url: str,
    limiter: RateLimiter,
    retries: int = 8,
) -> tuple[int, str]:
    delay = 1.0
    last_exc: Exception | None = None
    for _ in range(retries):
        await limiter.wait()
        try:
            response = await client.get(url, follow_redirects=True)
            if response.status_code == 429:
                retry_after = response.headers.get("Retry-After")
                sleep_for = float(retry_after) if retry_after and retry_after.isdigit() else delay
                sleep_for = max(sleep_for, delay)
                print(f"  rate-limited; sleeping {sleep_for:.1f}s", flush=True)
                await asyncio.sleep(sleep_for)
                delay = min(delay * 2, 60.0)
                continue
            return response.status_code, response.text
        except (httpx.HTTPError, httpx.TransportError) as exc:
            last_exc = exc
            await asyncio.sleep(delay)
            delay = min(delay * 2, 30.0)
    if last_exc:
        raise RuntimeError(f"fetch failed for {url}: {last_exc}") from last_exc
    return 429, ""


async def scrape_page_live(
    client: httpx.AsyncClient,
    semaphore: asyncio.Semaphore,
    limiter: RateLimiter,
    docname: str,
    title_hint: str,
    out_root: Path,
) -> PageRecord:
    url = docname_to_url(docname)
    rel = "index.md" if docname == "index" else f"{docname}.md"
    out_path = out_root / "aiogram" / rel
    async with semaphore:
        status, html = await fetch_text(client, url, limiter)
    if status != 200 or not html:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        body = f"# {title_hint}\n\n> Failed to fetch {url} (HTTP {status})\n"
        out_path.write_text(body, encoding="utf-8")
        return PageRecord(docname, title_hint, url, rel, len(body.encode()), status)
    soup = BeautifulSoup(html, "lxml")
    title = extract_title(soup, title_hint)
    markdown = to_markdown(extract_main_html(soup), url, title)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(markdown, encoding="utf-8")
    return PageRecord(docname, title, url, rel, len(markdown.encode()), 200)


async def run_live(out_dir: Path, concurrency: int, interval: float, limit: int | None) -> int:
    headers = {"User-Agent": USER_AGENT}
    limiter = RateLimiter(interval)
    async with httpx.AsyncClient(timeout=60.0, headers=headers) as client:
        status, options_js = await fetch_text(
            client, urljoin(BASE, "_static/documentation_options.js"), limiter
        )
        version = "unknown"
        if status == 200:
            vm = re.search(r"VERSION:\s*'([^']+)'", options_js)
            if vm:
                version = vm.group(1)
        status, index_js = await fetch_text(client, urljoin(BASE, "searchindex.js"), limiter)
        if status != 200:
            print(f"Failed searchindex.js: HTTP {status}", file=sys.stderr)
            return 1
        docnames, titles = parse_search_index(index_js)
        pairs = [(d, t) for d, t in zip(docnames, titles) if not should_skip_url(docname_to_url(d))]
        if limit is not None:
            pairs = pairs[:limit]
        print(f"Live-crawling {len(pairs)} pages...")
        (out_dir / "aiogram").mkdir(parents=True, exist_ok=True)
        sem = asyncio.Semaphore(concurrency)
        tasks = [scrape_page_live(client, sem, limiter, d, t, out_dir) for d, t in pairs]
        records = []
        done = 0
        for coro in asyncio.as_completed(tasks):
            rec = await coro
            records.append(rec)
            done += 1
            if done % 25 == 0 or done == len(tasks):
                print(f"  {done}/{len(tasks)} … {rec.docname} ({rec.status})")
    write_index(out_dir, version, records, "live crawl")
    failed = [r for r in records if r.status != 200]
    print(f"Done live crawl: {len(records) - len(failed)} OK")
    return 0 if not failed else 2


def scrape_from_html_dir(out_dir: Path, html_root: Path) -> tuple[str, list[PageRecord]]:
    """Convert a local Sphinx HTML build (same structure as docs.aiogram.dev)."""
    version = detect_version_from_html(html_root)
    # Prefer .../html as root; also accept nested en/latest
    roots = [html_root]
    for candidate in (html_root / "en" / "latest", html_root / "latest"):
        if candidate.is_dir():
            roots.insert(0, candidate)

    aiogram_out = out_dir / "aiogram"
    if aiogram_out.exists():
        shutil.rmtree(aiogram_out)
    aiogram_out.mkdir(parents=True, exist_ok=True)

    records: list[PageRecord] = []
    seen: set[str] = set()
    for root in roots:
        for html_path in root.rglob("*.html"):
            try:
                rel = html_path.relative_to(root)
            except ValueError:
                continue
            if any(part.startswith("_") for part in rel.parts):
                continue
            docname = html_path_to_docname(rel)
            if not docname or docname in seen:
                continue
            seen.add(docname)
            try:
                records.append(convert_html_file(html_path, docname, out_dir))
            except Exception as exc:
                print(f"  skip {docname}: {exc}", file=sys.stderr)
        if records:
            break
    return version, records


async def run_zip(out_dir: Path, zip_file: Path | None = None) -> int:
    if zip_file is not None:
        version, records = scrape_from_zip(out_dir, zip_file)
        # RTD "htmlzip" may be singlehtml — split is lossy; warn if tiny page count
        if len(records) < 50:
            print(
                f"Zip only yielded {len(records)} page(s) (often singlehtml). "
                "Prefer --html-dir from a local sphinx-build or --mode live.",
                file=sys.stderr,
            )
    else:
        headers = {"User-Agent": USER_AGENT}
        async with httpx.AsyncClient(timeout=120.0, headers=headers) as client:
            with tempfile.NamedTemporaryFile(suffix=".zip", delete=False) as tmp:
                zip_path = Path(tmp.name)
            try:
                await download_htmlzip(client, zip_path)
                version, records = scrape_from_zip(out_dir, zip_path)
            finally:
                zip_path.unlink(missing_ok=True)
            if len(records) < 50:
                print(
                    f"Zip only yielded {len(records)} page(s). Falling back to live crawl.",
                    file=sys.stderr,
                )
                return await run_live(out_dir, concurrency=2, interval=0.5, limit=None)
    if not records:
        print("HTML zip produced 0 pages", file=sys.stderr)
        return 1
    write_index(out_dir, version, records, "RTD HTML zip")
    print(f"Done. Converted {len(records)} pages (aiogram {version}) → {out_dir / 'aiogram'}")
    return 0


async def run(
    mode: str,
    out_dir: Path,
    concurrency: int,
    interval: float,
    limit: int | None,
    zip_file: Path | None,
    html_dir: Path | None,
) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    if html_dir is not None:
        version, records = scrape_from_html_dir(out_dir, html_dir)
        if not records:
            print(f"No HTML pages found under {html_dir}", file=sys.stderr)
            return 1
        write_index(out_dir, version, records, "local Sphinx HTML")
        print(f"Done. Converted {len(records)} pages (aiogram {version}) → {out_dir / 'aiogram'}")
        return 0
    if mode == "zip":
        try:
            return await run_zip(out_dir, zip_file)
        except Exception as exc:
            print(f"HTML zip failed ({exc}); falling back to live crawl", file=sys.stderr)
            return await run_live(out_dir, concurrency, interval, limit)
    if mode == "live":
        return await run_live(out_dir, concurrency, interval, limit)
    raise SystemExit(f"unknown mode: {mode}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=None)
    parser.add_argument(
        "--mode",
        choices=("zip", "live"),
        default="zip",
        help="zip = download full RTD HTML archive (default); live = crawl each page",
    )
    parser.add_argument(
        "--zip-file",
        type=Path,
        default=None,
        help="Use a local RTD htmlzip instead of downloading",
    )
    parser.add_argument(
        "--html-dir",
        type=Path,
        default=None,
        help="Convert a local Sphinx HTML build directory (recommended offline path)",
    )
    parser.add_argument("--concurrency", type=int, default=2)
    parser.add_argument("--interval", type=float, default=0.5)
    parser.add_argument("--limit", type=int, default=None, help="live mode only")
    args = parser.parse_args()
    out = skill_reference_dir(args.out)
    raise SystemExit(
        asyncio.run(
            run(
                args.mode,
                out,
                args.concurrency,
                args.interval,
                args.limit,
                args.zip_file,
                args.html_dir,
            )
        )
    )


if __name__ == "__main__":
    main()
