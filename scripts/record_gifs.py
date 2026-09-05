#!/usr/bin/env python3
"""Record the tutorial GIFs by driving the running dev app.

These four clips are what the landing page shows instead of the 42 MB demo
video that used to sit there, so size discipline is the point: Playwright
records WebM, ffmpeg palettes it down to a GIF no wider than 900 px, and each
flow is trimmed to the seconds that actually show something.

Run against a dev stack that is already up (``./dev.sh up``) and seeded::

    python scripts/record_gifs.py --password 'Tutorial!2026'
    python scripts/record_gifs.py --only publish-prices

Playwright and ffmpeg live on the host, not in the container — install once
with ``pip install playwright && playwright install chromium``.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from playwright.sync_api import Page, sync_playwright

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "backend" / "static" / "landing" / "gifs"

BASE_URL = "http://localhost:5252"
VIEWPORT = {"width": 1440, "height": 900}
GIF_WIDTH = 900
GIF_FPS = 8

DEFAULT_USER = "demo.owner"


def _settle(page: Page, seconds: float = 1.2) -> None:
    """Hold the frame. Playback needs the pause to be readable."""
    page.wait_for_timeout(int(seconds * 1000))


def _click_nav(page: Page, href: str) -> None:
    """Follow a sidebar link, then let the view finish painting."""
    page.click(f'a[href="{href}"]')
    page.wait_for_load_state("networkidle")
    _settle(page)


def login(page: Page, username: str, password: str) -> None:
    page.goto(f"{BASE_URL}/login", wait_until="networkidle")
    page.fill('input[autocomplete="username"]', username)
    page.fill('input[type="password"]', password)
    page.click('button[type="submit"]')
    page.wait_for_url(f"{BASE_URL}/**", timeout=30_000)
    page.wait_for_load_state("networkidle")
    _settle(page, 2)
    _dismiss_chrome(page)
    _dismiss_tour(page)


def _dismiss_chrome(page: Page) -> None:
    """Close the PWA install prompt, which otherwise sits over every clip."""
    later = page.get_by_role("button", name="Later")
    if later.count():
        later.first.click()
        _settle(page, 0.6)


def _dismiss_tour(page: Page) -> None:
    """Close the onboarding tour if this account has not seen it.

    It opens over the panel on a first sign-in, which is exactly what the
    signup clip is for and exactly what the other three must not show.
    """
    close = page.locator(".onboarding-tour__close")
    if close.count():
        close.first.click()
        _settle(page, 1)


def flow_publish_prices(page: Page) -> None:
    """Update prices -> finalize -> publish."""
    _click_nav(page, "/update")
    _settle(page, 2)

    for value, field in zip(("66500", "67200"), page.locator('input[type="number"]').all()[:2]):
        field.click()
        field.fill(value)
        _settle(page, 0.8)

    _click_nav(page, "/finalize")
    _settle(page, 3)


def flow_template_editor(page: Page) -> None:
    """Template editor: open a template and work the canvas."""
    _click_nav(page, "/templates")
    _settle(page, 2.5)

    card = page.locator('a[href^="/templates/"][href$="/editor"]')
    if not card.count():
        raise RuntimeError("No template to record. Create one in the panel first.")
    card.first.click()
    page.wait_for_load_state("networkidle")
    _settle(page, 3)

    # The widget library is the left rail; adding from it is the whole point of
    # the clip, so give each addition room to land on the canvas.
    library = page.locator('aside:has-text("Widget library")').first
    for widget in library.locator("button").all()[:3]:
        widget.click()
        _settle(page, 1.4)
    _settle(page, 2)


def flow_telegram_bot(page: Page) -> None:
    """Telegram: the bot and channel the panel publishes through."""
    _click_nav(page, "/telegram/send")
    _settle(page, 3)
    page.mouse.wheel(0, 500)
    _settle(page, 2)


def flow_signup_tour(page: Page, username: str, password: str) -> None:
    """Signup form -> the confirmation code screen -> the first-login tour.

    The form is shown but not submitted: a real submission would burn a
    one-time code and leave a junk account behind on every re-record. The tour
    is replayed from the header instead, which is the same component a new
    customer meets.
    """
    page.goto(f"{BASE_URL}/signup", wait_until="networkidle")
    _settle(page, 2.5)
    page.mouse.wheel(0, 300)
    _settle(page, 2)

    page.goto(f"{BASE_URL}/confirm", wait_until="networkidle")
    _settle(page, 3)

    login(page, username, password)
    page.click('button[aria-label*="tour" i], button[title*="tour" i]')
    _settle(page, 2.5)
    for _ in range(3):
        page.click(".onboarding-tour__btn--primary")
        _settle(page, 2)


FLOWS = {
    "publish-prices": (flow_publish_prices, True),
    "template-editor": (flow_template_editor, True),
    "telegram-bot": (flow_telegram_bot, True),
    "signup-tour": (flow_signup_tour, False),
}


def to_gif(webm: Path, gif: Path) -> None:
    """WebM -> palette-optimised GIF.

    Two passes: ffmpeg builds a palette from the whole clip first, because a
    per-frame palette is what makes screen recordings band and dither.
    """
    with tempfile.TemporaryDirectory() as tmp:
        palette = Path(tmp) / "palette.png"
        scale = f"fps={GIF_FPS},scale={GIF_WIDTH}:-1:flags=lanczos"
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-i", str(webm),
             "-vf", f"{scale},palettegen=stats_mode=diff", str(palette)],
            check=True,
        )
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-i", str(webm), "-i", str(palette),
             "-lavfi", f"{scale}[x];[x][1:v]paletteuse=dither=bayer:bayer_scale=3",
             "-loop", "0", str(gif)],
            check=True,
        )


def record(name: str, needs_login: bool, username: str, password: str) -> None:
    flow, _ = FLOWS[name]
    with tempfile.TemporaryDirectory() as tmp, sync_playwright() as pw:
        browser = pw.chromium.launch()
        context = browser.new_context(
            viewport=VIEWPORT,
            record_video_dir=tmp,
            record_video_size=VIEWPORT,
        )
        page = context.new_page()
        try:
            if needs_login:
                login(page, username, password)
                flow(page)
            else:
                flow(page, username, password)
            _settle(page, 1.5)
        finally:
            video = page.video
            context.close()
            browser.close()

        webm = Path(video.path())
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        gif = OUTPUT_DIR / f"{name}.gif"
        to_gif(webm, gif)
        size_mb = gif.stat().st_size / 1_048_576
        print(f"{gif.relative_to(REPO_ROOT)} — {size_mb:.1f} MB")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--user", default=DEFAULT_USER, help="Panel account to record with")
    parser.add_argument("--password", required=True, help="Its password")
    parser.add_argument("--only", action="append", choices=sorted(FLOWS), help="Record just this flow")
    args = parser.parse_args()

    if shutil.which("ffmpeg") is None:
        print("ffmpeg is not on PATH.", file=sys.stderr)
        return 1

    for name in args.only or sorted(FLOWS):
        _, needs_login = FLOWS[name]
        record(name, needs_login, args.user, args.password)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
