"""
Rendering of template-based price banners with themes and usage types.
Uses config.themes and config.usage_theme_map when present; falls back to config.fields.
"""

import logging
from pathlib import Path
from typing import Any, Dict, List

from PIL import Image, ImageDraw

from .utils import (
    draw_text_field,
    render_template as legacy_render_template,
)
from .variables import get_default_sample_value

logger = logging.getLogger(__name__)

# Default base resolution for scaling (config can override with base_width, base_height)
DEFAULT_BASE_WIDTH = 1080
DEFAULT_BASE_HEIGHT = 1080


def _scale_value(value: Any, scale: float) -> int:
    """Scale a numeric value by scale factor; return int."""
    if value is None:
        return None
    try:
        return int(round(float(value) * scale))
    except (TypeError, ValueError):
        return value


def _get_theme_name(config: Dict[str, Any], usage_type: str) -> str:
    """Resolve theme name from usage_theme_map or first theme in config."""
    usage_map = config.get("usage_theme_map") or {}
    if usage_type and usage_type in usage_map:
        return usage_map[usage_type]
    themes = config.get("themes") or {}
    if themes:
        return next(iter(themes))
    return None


def _get_layers_sorted(config: Dict[str, Any], theme_name: str) -> List[Dict[str, Any]]:
    """Get layers for theme, sorted by z_index then by order."""
    themes = config.get("themes") or {}
    theme = themes.get(theme_name) or {}
    layers = theme.get("layers") or []
    return sorted(
        layers,
        key=lambda L: (L.get("z_index", 0), layers.index(L) if L in layers else 0),
    )


def render_price_template(
    template_obj,
    usage_type: str,
    dynamic_data: Dict[str, Any],
    theme_name_override: str = None,
    config_override: Dict[str, Any] = None,
):
    """
    Render a template with usage-based theme selection and optional scaling.

    Config schema (when using themes):
      - base_width, base_height: optional; default 1080. Actual image size is scaled to this.
      - usage_theme_map: { usage_type: theme_name }
      - themes: { theme_name: { layers: [ { variable_key, x, y, font, size, color, align, max_width, z_index } ] } }

    If config has no "themes", falls back to legacy render_template (config.fields).

    theme_name_override: if provided, use this theme instead of resolving from usage_theme_map (e.g. for preview).
    config_override: if provided, use this config instead of template_obj.config (e.g. for live preview).

    Returns:
        PIL Image (RGBA).
    """
    if not template_obj.image:
        raise ValueError("Template has no image.")

    bg_path = template_obj.image.path
    if not Path(bg_path).exists():
        raise FileNotFoundError(f"Template image not found at '{bg_path}'.")

    config = config_override if config_override is not None else (template_obj.config or {})
    themes = config.get("themes")

    if not themes:
        return legacy_render_template(template_obj, dynamic_data, config_override=config)

    theme_name = theme_name_override or _get_theme_name(config, usage_type)
    if not theme_name:
        return legacy_render_template(template_obj, dynamic_data, config_override=config)

    layers = _get_layers_sorted(config, theme_name)
    if not layers:
        # Empty theme: just return background
        base_image = Image.open(bg_path).convert("RGBA")
        return base_image

    base_image = Image.open(bg_path).convert("RGBA")
    draw = ImageDraw.Draw(base_image)
    actual_width, actual_height = base_image.size
    base_width = config.get("base_width", DEFAULT_BASE_WIDTH)
    base_height = config.get("base_height", DEFAULT_BASE_HEIGHT)
    scale_x = actual_width / float(base_width) if base_width else 1.0
    scale_y = actual_height / float(base_height) if base_height else 1.0

    for layer in layers:
        variable_key = layer.get("variable_key") or layer.get("key")
        if not variable_key:
            continue
        text_value = dynamic_data.get(variable_key)
        if text_value is None:
            text_value = get_default_sample_value(variable_key)
        text_value = str(text_value).strip()
        if not text_value:
            continue

        x = _scale_value(layer.get("x", 0), scale_x)
        y = _scale_value(layer.get("y", 0), scale_y)
        size = _scale_value(layer.get("size", 32), min(scale_x, scale_y))
        if size is None or size < 1:
            size = 32
        max_width = _scale_value(layer.get("max_width"), scale_x)
        color = layer.get("color", "#000000")
        align = layer.get("align", "left")
        font_filename = layer.get("font")

        draw_text_field(
            draw,
            x,
            y,
            text_value,
            size=size,
            color=color,
            align=align,
            max_width=max_width,
            font_filename=font_filename,
        )

    return base_image
