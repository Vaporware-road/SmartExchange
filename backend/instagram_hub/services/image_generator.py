"""
Instagram Hub — image generator for price posts and stories.

Uses Pillow for compositing; arabic_reshaper + bidi for Persian text.
Outputs: Post 1080x1080 (1:1), Story 1080x1920 (9:16) with blur canvas.
Themes: DARK_GOLD (default, charcoal + gold), LIGHT_BLUE (slate-50 + blue).
"""

from __future__ import annotations

import logging
import os
import uuid
from pathlib import Path
from typing import Any

from django.conf import settings

logger = logging.getLogger(__name__)

# Format dimensions (Instagram)
# Post: 1:1 (1080x1080) for feed; Story: 9:16 (1080x1920) with blur canvas.
POST_WIDTH, POST_HEIGHT = 1080, 1080
STORY_WIDTH, STORY_HEIGHT = 1080, 1920
STORY_SAFE_TOP = 250
STORY_SAFE_BOTTOM = 250

# Theme RGB (aligned with frontend main.css / Tailwind)
# Dark: bg-base #0f172a, bg-card #1e293b, primary #ffd700, text #e2e8f0, secondary #94a3b8
DARK_GOLD_THEME = {
    "background": (15, 23, 42),
    "card": (30, 41, 59),
    "card_highlight": (71, 85, 105),
    "text_primary": (226, 232, 240),
    "text_secondary": (148, 163, 184),
    "accent": (255, 215, 0),
    "accent_dark": (184, 134, 11),
}
# Light: bg #f8fafc, card #ffffff, primary #2563eb, text #1e293b, secondary #64748b
LIGHT_BLUE_THEME = {
    "background": (248, 250, 252),
    "card": (255, 255, 255),
    "card_highlight": (226, 232, 240),
    "text_primary": (30, 41, 59),
    "text_secondary": (100, 116, 139),
    "accent": (37, 99, 235),
    "accent_dark": (29, 78, 216),
}

OUTPUT_SUBDIR = "generated_instagram"


def _ensure_deps():
    """Import Pillow or fail. Returns (Image, ImageDraw, ImageFont, ImageFilter)."""
    try:
        from PIL import Image, ImageDraw, ImageFont, ImageFilter
        return Image, ImageDraw, ImageFont, ImageFilter
    except ImportError:
        logger.critical("Pillow not installed; run: pip install Pillow")
        return None, None, None, None


def _shape_persian(text: str, use_reshaper: bool = True) -> str:
    """Process Persian/Arabic text for Pillow (reshape + bidi)."""
    if not text or not use_reshaper:
        return text or ""
    try:
        import arabic_reshaper
        from bidi.algorithm import get_display
    except ImportError:
        return text
    config = {
        "delete_harakat": True,
        "support_ligatures": True,
        "use_unshaped_instead_of_isolated": False,
    }
    reshaper = arabic_reshaper.ArabicReshaper(configuration=config)
    reshaped = reshaper.reshape(text)
    return get_display(reshaped)


def _normalize_western_digits(text: str) -> str:
    """Convert Persian/Arabic numerals to 0-9."""
    if not text:
        return text
    persian = "۰۱۲۳۴۵۶۷۸۹"
    arabic = "٠١٢٣٤٥٦٧٨٩"
    western = "0123456789"
    table = str.maketrans(persian + arabic, western * 2)
    return text.translate(table)


def _get_font_root() -> Path:
    base = Path(settings.BASE_DIR)
    font_root = getattr(settings, "PRICE_RENDERER_FONT_ROOT", base / "static" / "fonts")
    return Path(font_root) if font_root else base / "static" / "fonts"


def _load_persian_font(ImageFont, size: int):
    """Load Persian font (Kalameh or farsi_vazir)."""
    font_root = _get_font_root()
    for name in ("Kalameh.ttf", "farsi_vazir.ttf", "dirooz.ttf"):
        path = font_root / name
        if path.exists():
            try:
                return ImageFont.truetype(str(path), size)
            except OSError as e:
                logger.debug("Failed to load %s: %s", path, e)
    raise FileNotFoundError(
        f"No Persian font found under {font_root}. "
        "Place Kalameh.ttf or farsi_vazir.ttf in static/fonts."
    )


def _load_latin_font(ImageFont, size: int):
    """Load Latin font for numbers."""
    font_root = _get_font_root()
    for name in ("montsrrat.otf", "Roboto-Regular.ttf", "Roboto-Bold.ttf"):
        path = font_root / name
        if path.exists():
            try:
                return ImageFont.truetype(str(path), size)
            except OSError:
                continue
    return ImageFont.load_default()


def _build_story_canvas(img, Image, ImageFilter):
    """
    Build 1080x1920 story from source image.
    If not 9:16: blurred+darkened background, center image on top.
    """
    target_w, target_h = STORY_WIDTH, STORY_HEIGHT
    src_w, src_h = img.size
    src_ratio = src_w / max(1, src_h)
    target_ratio = target_w / target_h

    if abs(src_ratio - target_ratio) < 0.06:
        return img.resize((target_w, target_h), Image.Resampling.LANCZOS)

    bg_scale = max(target_w / src_w, target_h / src_h)
    bg_w = int(src_w * bg_scale)
    bg_h = int(src_h * bg_scale)
    bg = img.resize((bg_w, bg_h), Image.Resampling.LANCZOS)
    left = (bg_w - target_w) // 2
    top = (bg_h - target_h) // 2
    bg = bg.crop((left, top, left + target_w, top + target_h))
    bg = bg.filter(ImageFilter.GaussianBlur(radius=30))
    from PIL import ImageEnhance
    bg = ImageEnhance.Brightness(bg).enhance(0.35)

    fit_scale = min(target_w / src_w, target_h / src_h)
    max_fit_h = target_h - STORY_SAFE_TOP - STORY_SAFE_BOTTOM + 100
    if src_h * fit_scale > max_fit_h:
        fit_scale = max_fit_h / src_h
    new_w = int(src_w * fit_scale)
    new_h = int(src_h * fit_scale)
    resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    paste_x = (target_w - new_w) // 2
    paste_y = (target_h - new_h) // 2
    bg.paste(resized, (paste_x, paste_y))
    return bg


def _get_theme(theme: str) -> dict[str, tuple[int, int, int]]:
    if (theme or "").strip().lower() in ("light", "لایت", "blue"):
        return LIGHT_BLUE_THEME
    return DARK_GOLD_THEME


def _render_post_canvas(
    price_entries: list[dict[str, Any]],
    theme_name: str,
    category_title: str | None,
    Image,
    ImageDraw,
    ImageFont,
    ImageFilter,
) -> Any:
    """Render 1080x1080 (1:1) post image with price table. Uses DARK_GOLD when theme is 'dark'."""
    theme = _get_theme(theme_name)
    w, h = POST_WIDTH, POST_HEIGHT
    img = Image.new("RGB", (w, h), theme["background"])
    draw = ImageDraw.Draw(img)

    padding = 60
    header_size = 56
    row_height = 72
    row_gap = 16
    footer_gap = 24

    try:
        font_header = _load_persian_font(ImageFont, header_size)
        font_row_title = _load_persian_font(ImageFont, 36)
    except FileNotFoundError:
        font_header = _load_latin_font(ImageFont, header_size)
        font_row_title = _load_latin_font(ImageFont, 36)
    font_price = _load_latin_font(ImageFont, 42)
    font_footer = _load_latin_font(ImageFont, 24)

    y = padding
    header_text = category_title or "قیمت‌ها"
    header_display = _shape_persian(header_text)
    draw.text((padding, y), header_display, fill=theme["accent"], font=font_header)
    try:
        bbox = draw.textbbox((0, 0), header_display, font=font_header)
    except TypeError:
        bbox = draw.textbbox((0, 0), header_display)
    y += (bbox[3] - bbox[1]) + 24

    max_title_w = w - 2 * padding - 180
    for entry in price_entries:
        title = (entry.get("title") or entry.get("price_type_name") or "").strip()
        price_str = entry.get("price")
        if price_str is None:
            price_str = ""
        else:
            price_str = _normalize_western_digits(str(price_str))
        title_display = _shape_persian(title) if title else ""
        if not title_display and not price_str:
            continue

        card_left = padding
        card_top = y
        card_right = w - padding
        card_bottom = y + row_height
        draw.rounded_rectangle(
            (card_left, card_top, card_right, card_bottom),
            radius=16,
            fill=theme["card"],
            outline=theme["card_highlight"],
            width=1,
        )
        inner_x = card_left + 20
        inner_y = card_top + (row_height - 36) // 2
        draw.text((inner_x, inner_y - 4), title_display[:40], fill=theme["text_primary"], font=font_row_title)
        price_bbox = draw.textbbox((0, 0), price_str, font=font_price) if hasattr(draw, 'textbbox') else (0, 0, len(price_str) * 20, 30)
        pw = price_bbox[2] - price_bbox[0]
        draw.text((card_right - 20 - pw, inner_y - 4), price_str, fill=theme["accent"], font=font_price)
        y = card_bottom + row_gap

    from django.utils import timezone
    now = timezone.now()
    footer_text = now.strftime("%Y-%m-%d %H:%M")
    y_footer = h - padding - 28
    draw.text((padding, y_footer), footer_text, fill=theme["text_secondary"], font=font_footer)

    return img


def _get_media_root() -> Path:
    media_root = getattr(settings, "MEDIA_ROOT", None)
    if not media_root:
        media_root = Path(settings.BASE_DIR) / "public" / "media"
    return Path(media_root)


def generate_price_images(
    price_entries: list[dict[str, Any]],
    theme: str = "dark",
    category_title: str | None = None,
) -> dict[str, str] | None:
    """
    Generate post (1080x1080, 1:1) and story (1080x1920, 9:16) images; save to MEDIA_ROOT/generated_instagram/.
    Default theme is dark (DARK_GOLD) for a luxurious look.

    price_entries: list of dicts with keys title (or price_type_name), price; optional subtitle, meta.
    theme: "dark" | "light".
    category_title: optional header text (e.g. category name).

    Returns {"post_path": str, "story_path": str} or None on failure.
    """
    Image, ImageDraw, ImageFont, ImageFilter = _ensure_deps()
    if not Image:
        return None

    if not price_entries:
        logger.warning("generate_price_images: no price_entries")
        return None

    try:
        post_img = _render_post_canvas(
            price_entries,
            theme,
            category_title,
            Image,
            ImageDraw,
            ImageFont,
            ImageFilter,
        )
    except Exception as e:
        logger.exception("generate_price_images: render post failed: %s", e)
        return None

    media_root = _get_media_root()
    out_dir = media_root / OUTPUT_SUBDIR
    out_dir.mkdir(parents=True, exist_ok=True)
    suffix = uuid.uuid4().hex[:8]

    post_path = out_dir / f"post_{suffix}.png"
    try:
        post_img.save(post_path, format="PNG", optimize=True)
    except Exception as e:
        logger.warning("generate_price_images: save post failed: %s", e)
        return None

    story_img = _build_story_canvas(post_img.copy(), Image, ImageFilter)
    story_path = out_dir / f"story_{suffix}.png"
    try:
        story_img.save(story_path, format="PNG", optimize=True)
    except Exception as e:
        logger.warning("generate_price_images: save story failed: %s", e)
        return {"post_path": str(post_path.resolve()), "story_path": ""}

    return {
        "post_path": str(post_path.resolve()),
        "story_path": str(story_path.resolve()),
    }


def delete_old_generated_images(older_than_hours: int = 24) -> dict[str, int | float]:
    """
    Delete generated Instagram images older than given hours.
    Returns {"deleted_count": int, "freed_mb": float}.
    """
    import time
    media_root = _get_media_root()
    out_dir = media_root / OUTPUT_SUBDIR
    if not out_dir.exists() or not out_dir.is_dir():
        return {"deleted_count": 0, "freed_mb": 0.0}
    cutoff = time.time() - (older_than_hours * 3600)
    deleted = 0
    freed = 0
    for path in out_dir.iterdir():
        if not path.is_file() or path.suffix.lower() not in (".png", ".jpg", ".jpeg"):
            continue
        try:
            if path.stat().st_mtime < cutoff:
                freed += path.stat().st_size
                path.unlink(missing_ok=True)
                deleted += 1
        except OSError as e:
            logger.warning("delete_old_generated_images: %s: %s", path, e)
    return {"deleted_count": deleted, "freed_mb": round(freed / (1024 * 1024), 2)}
