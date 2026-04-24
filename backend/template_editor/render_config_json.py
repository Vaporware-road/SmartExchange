"""
Render Template.config_json.widgets onto the base image (PIL).
Coordinates are percentage strings relative to logical canvas (canvas_width x canvas_height).
"""

from __future__ import annotations

import io
import logging
from numbers import Real
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.request import urlopen

from django.conf import settings
from PIL import Image, ImageDraw

from core.utils import format_price_display
from .utils import draw_text_field, _parse_color
from .variables import get_default_sample_value

logger = logging.getLogger(__name__)


def _format_widget_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return str(value)
    if isinstance(value, Real):
        return format_price_display(value)
    if isinstance(value, str) and value.strip():
        return format_price_display(value)
    return str(value)


def _text_fx_from_style(style: Dict[str, Any]) -> tuple[str, Optional[int], bool]:
    """Resolve PIL text weight, stroke width (None=legacy auto), and shadow flag from widget style."""
    fw = style.get("fontWeight") or style.get("weight") or "normal"
    s = str(fw).strip().lower()
    weight = "bold" if s in ("bold", "700", "800", "900") else "normal"
    if style.get("plainText") is True or style.get("plain_text") is True:
        return weight, 0, False
    ts = style.get("textShadow")
    if ts is False or ts == 0 or str(ts).lower() == "false":
        use_shadow = False
    else:
        use_shadow = True
    sw = style.get("textStrokeWidth")
    if sw is not None:
        try:
            return weight, max(0, int(sw)), use_shadow
        except (TypeError, ValueError):
            pass
    if style.get("textOutline") is False or style.get("text_outline") is False:
        return weight, 0, use_shadow
    return weight, None, use_shadow


def _pct_to_fraction(raw: Any) -> float:
    if raw is None:
        return 0.0
    if isinstance(raw, (int, float)):
        return float(raw) / 100.0 if raw <= 100 else float(raw) / 100.0  # allow bare numbers as percent
    s = str(raw).strip().replace("%", "")
    try:
        return float(s) / 100.0
    except (TypeError, ValueError):
        return 0.0


def _logical_to_actual(
    raw: Any,
    design_size: int,
    actual_size: int,
) -> int:
    frac = _pct_to_fraction(raw)
    px_design = frac * float(design_size)
    if design_size <= 0:
        return 0
    scale = actual_size / float(design_size)
    return int(round(px_design * scale))


def _widget_text_value(w: Dict[str, Any], dynamic_data: Dict[str, Any]) -> str:
    style = w.get("style") if isinstance(w.get("style"), dict) else {}
    binding = (
        w.get("bindingKey")
        or w.get("binding_key")
        or style.get("bindingKey")
        or style.get("binding_key")
    )
    wtype = (w.get("type") or "text").strip()
    if binding:
        val = dynamic_data.get(str(binding).strip())
        if val is not None and str(val).strip():
            return _format_widget_value(val).strip()
        fallback_content = w.get("content")
        if fallback_content is not None and str(fallback_content).strip():
            return str(fallback_content).strip()
        sample = get_default_sample_value(str(binding).strip())
        return _format_widget_value(sample).strip()
    if wtype in ("date", "weekday"):
        key = style.get("dateKey") or style.get("date_key") or "date_fa"
        return _format_widget_value(dynamic_data.get(key) or get_default_sample_value(key)).strip()
    if wtype == "clock":
        return _format_widget_value(dynamic_data.get("time") or get_default_sample_value("time")).strip()
    content = w.get("content", "")
    return str(content) if content is not None else ""


def _resolve_local_image_path(content: str) -> Optional[Path]:
    c = (content or "").strip()
    if not c:
        return None
    media_prefix = settings.MEDIA_URL.rstrip("/") if settings.MEDIA_URL else "/media"
    if c.startswith("/media/") or (media_prefix and c.startswith(media_prefix + "/")):
        prefix = "/media/" if c.startswith("/media/") else f"{media_prefix}/"
        rel = c[len(prefix) :].lstrip("/")
        p = Path(settings.MEDIA_ROOT) / rel
        return p if p.is_file() else None
    p = Path(c)
    if p.is_file():
        return p
    static_path = Path(settings.BASE_DIR) / "static" / c.lstrip("/")
    if static_path.is_file():
        return static_path
    return None


def _paste_scaled_image(
    base: Image.Image,
    box_xy,
    box_wh,
    src: Image.Image,
    opacity: float = 1.0,
) -> None:
    x0, y0 = box_xy
    bw, bh = box_wh
    if bw < 1 or bh < 1:
        return
    resized = src.resize((bw, bh), Image.Resampling.LANCZOS)
    if resized.mode != "RGBA":
        resized = resized.convert("RGBA")
    try:
        op = float(opacity)
    except (TypeError, ValueError):
        op = 1.0
    op = max(0.0, min(1.0, op))
    if op < 1.0 - 1e-6:
        r, g, b, a = resized.split()
        a = a.point(lambda p: int(round(p * op)))
        resized = Image.merge("RGBA", (r, g, b, a))
    base.paste(resized, (x0, y0), resized)


def _draw_price_board(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    w: int,
    h: int,
    style: Dict[str, Any],
    dynamic_data: Dict[str, Any],
) -> None:
    title = (style.get("title") or "Prices").strip()
    rows_raw = style.get("rows") if isinstance(style.get("rows"), list) else None
    if not rows_raw:
        rows_raw = style.get("mockRows") if isinstance(style.get("mockRows"), list) else []
    try:
        cols = max(1, min(4, int(style.get("columns") or 1)))
    except (TypeError, ValueError):
        cols = 1
    pad = max(4, min(16, w // 40))
    header_h = max(22, min(48, h // 8))
    body_h = h - header_h - pad * 2
    if body_h < 20:
        body_h = 20
    # header background
    draw.rectangle([x, y, x + w, y + header_h], fill=_parse_color(style.get("headerBg") or style.get("panelBg") or "#1e293b"))
    font_size = max(12, min(22, header_h - 8))
    hw, hstroke, hshadow = _text_fx_from_style(style)
    draw_text_field(
        draw,
        x + pad,
        y + max(2, (header_h - font_size) // 2),
        title,
        size=font_size,
        color=style.get("headerColor") or "#e2e8f0",
        align="left",
        max_width=w - 2 * pad,
        weight=hw,
        stroke_width=hstroke,
        shadow=hshadow,
    )
    row_y = y + header_h + pad
    row_h = max(18, int((body_h - pad) / max(1, len(rows_raw) or 1)))
    for i, row in enumerate(rows_raw[:20]):
        if not isinstance(row, dict):
            continue
        label = str(row.get("label") or "")
        bk = row.get("bindingKey") or row.get("binding_key")
        price = str(row.get("price") or "").strip()
        if bk:
            val = dynamic_data.get(str(bk).strip())
            if val is not None and str(val).strip():
                price = format_price_display(val)
        ry0 = row_y + i * (row_h + 2)
        draw.rectangle(
            [x + pad, ry0, x + w - pad, ry0 + row_h],
            fill=_parse_color(style.get("rowBg") or "#334155"),
        )
        fs = max(11, min(18, row_h - 6))
        rw, rstroke, rshadow = _text_fx_from_style(style)
        label_color = style.get("labelColor") or style.get("label_color") or "#f1f5f9"
        if label:
            draw_text_field(
                draw,
                x + pad * 2,
                ry0 + 2,
                label,
                size=fs,
                color=label_color,
                align="left",
                max_width=w // 2,
                weight=rw,
                stroke_width=rstroke,
                shadow=rshadow,
            )
        if price:
            draw_text_field(
                draw,
                x + w // 2,
                ry0 + 2,
                price,
                size=fs,
                color=style.get("priceColor") or "#d4af37",
                align="right",
                max_width=w // 2 - pad * 2,
                weight=rw,
                stroke_width=rstroke,
                shadow=rshadow,
            )


def render_template_from_config_json(
    template_obj,
    dynamic_data: Dict[str, Any],
    config_json_override: Optional[Dict[str, Any]] = None,
) -> Image.Image:
    """
    Draw widgets from config_json onto template_obj.image (required).
    Logical size: template canvas_width / canvas_height (defaults 1920x1080).
    Output size matches the background image dimensions.
    """
    raw = config_json_override if config_json_override is not None else (template_obj.config_json or {})
    if not isinstance(raw, dict):
        raw = {}
    widgets = raw.get("widgets")
    if not isinstance(widgets, list):
        widgets = []

    design_w = int(getattr(template_obj, "canvas_width", None) or 1920)
    design_h = int(getattr(template_obj, "canvas_height", None) or 1080)
    if design_w < 1:
        design_w = 1920
    if design_h < 1:
        design_h = 1080

    if getattr(template_obj, "image", None):
        bg_path = template_obj.image.path
        if Path(bg_path).is_file():
            base_image = Image.open(bg_path).convert("RGBA")
        else:
            bg_hex = (
                raw.get("backgroundColor")
                or raw.get("background_color")
                or "#0b1220"
            )
            try:
                fill = _parse_color(bg_hex)
            except Exception:
                fill = (11, 18, 32, 255)
            base_image = Image.new("RGBA", (design_w, design_h), fill)
    else:
        bg_hex = (
            raw.get("backgroundColor")
            or raw.get("background_color")
            or "#0b1220"
        )
        try:
            fill = _parse_color(bg_hex)
        except Exception:
            fill = (11, 18, 32, 255)
        base_image = Image.new("RGBA", (design_w, design_h), fill)

    actual_w, actual_h = base_image.size

    sorted_widgets: List[Dict[str, Any]] = sorted(
        [w for w in widgets if isinstance(w, dict)],
        key=lambda w: int(w.get("zIndex") or w.get("z_index") or 0),
    )
    draw = ImageDraw.Draw(base_image)

    for w in sorted_widgets:
        if w.get("visible") is False:
            continue
        wtype = (w.get("type") or "text").strip()
        x = _logical_to_actual(w.get("x"), design_w, actual_w)
        y = _logical_to_actual(w.get("y"), design_h, actual_h)
        ww = _logical_to_actual(w.get("width"), design_w, actual_w)
        hh = _logical_to_actual(w.get("height"), design_h, actual_h)
        if ww < 2 or hh < 2:
            continue
        style = w.get("style") if isinstance(w.get("style"), dict) else {}

        if wtype == "image":
            content = str(w.get("content") or "").strip()
            pth = _resolve_local_image_path(content)
            im_src = None
            if pth:
                try:
                    im_src = Image.open(pth).convert("RGBA")
                except OSError as e:
                    logger.warning("widget image load failed path=%s err=%s", pth, e)
            elif content.startswith(("http://", "https://")):
                try:
                    with urlopen(content, timeout=10) as resp:  # noqa: S310 — admin-controlled URL
                        im_src = Image.open(io.BytesIO(resp.read())).convert("RGBA")
                except Exception as e:
                    logger.warning("widget image url failed url=%s err=%s", content[:120], e)
            if im_src:
                try:
                    iop = float(style.get("opacity", 1))
                except (TypeError, ValueError):
                    iop = 1.0
                _paste_scaled_image(base_image, (x, y), (ww, hh), im_src, opacity=iop)
            continue

        if wtype == "price_board":
            _draw_price_board(draw, x, y, ww, hh, style, dynamic_data)
            continue

        text_val = _widget_text_value(w, dynamic_data)
        if not text_val.strip():
            continue
        try:
            font_size = int(style.get("fontSize") or style.get("font_size") or max(14, min(hh - 4, int(hh * 0.45))))
        except (TypeError, ValueError):
            font_size = max(14, min(hh - 4, int(hh * 0.45)))
        font_size = max(8, min(200, font_size))
        color = style.get("color") or "#ffffff"
        font_fn = style.get("font") or style.get("fontFilename") or style.get("font_filename")
        tw, tstroke, tshadow = _text_fx_from_style(style)
        draw_text_field(
            draw,
            x + 4,
            y + 4,
            text_val,
            size=font_size,
            color=str(color),
            align=str(style.get("align") or "center"),
            max_width=max(8, ww - 8),
            font_filename=font_fn,
            weight=tw,
            stroke_width=tstroke,
            shadow=tshadow,
        )

    return base_image
