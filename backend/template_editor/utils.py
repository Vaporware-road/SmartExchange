"""
Utility functions for rendering templates with dynamic data.
"""
import logging
from pathlib import Path
from typing import Any, Dict, Optional, Tuple
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from django.utils.text import slugify
import os

logger = logging.getLogger(__name__)

# Default font candidates - prioritize Persian fonts
STATIC_ROOT_DIR = Path(settings.BASE_DIR) / "static"
FONT_ROOT = Path(getattr(settings, "PRICE_RENDERER_FONT_ROOT", STATIC_ROOT_DIR / "fonts"))


def get_available_fonts() -> list[tuple[str, str]]:
    """
    Get list of available font files in the fonts directory.
    Returns list of tuples: (filename, display_name)
    Only returns .ttf and .otf files (PIL/Pillow compatible formats).
    """
    if not FONT_ROOT.exists():
        return []
    
    fonts = []
    for font_file in sorted(FONT_ROOT.glob("*")):
        if font_file.is_file() and font_file.suffix.lower() in ('.ttf', '.otf'):
            # Use filename without extension as display name
            display_name = font_file.stem
            fonts.append((font_file.name, display_name))
    
    return fonts

DEFAULT_FONT_CANDIDATES = (
    getattr(settings, "TEMPLATE_EDITOR_DEFAULT_FONT", None),
    str(FONT_ROOT / "Kalameh.ttf"),    # Kalameh - Persian & English
    str(FONT_ROOT / "montsrrat.otf"),  # Same font as tether banner
    str(FONT_ROOT / "YekanBakh.ttf"),  # Persian font fallback
    str(FONT_ROOT / "Morabba.ttf"),    # Persian font fallback
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
    "arial.ttf",
)


def _get_font(size: int, weight: str = 'normal', font_filename: str = None) -> ImageFont.ImageFont:
    """
    Get font with specified size and weight.
    
    Args:
        size: Font size in pixels
        weight: Font weight (not directly supported by PIL, kept for compatibility)
        font_filename: Optional font filename (e.g., 'montsrrat.otf'). If provided, uses this font.
                      If not provided, uses default font candidates.
    """
    # If specific font is requested, try to load it first
    if font_filename:
        font_path = FONT_ROOT / font_filename
        if font_path.exists():
            try:
                return ImageFont.truetype(str(font_path), size=size)
            except (OSError, IOError) as e:
                logger.warning(f"Failed to load requested font '{font_filename}': {e}. Falling back to default.")
    
    # Fall back to default font candidates
    for path in DEFAULT_FONT_CANDIDATES:
        if not path:
            continue
        try:
            # Check if path exists
            if not Path(path).exists():
                continue
            font = ImageFont.truetype(path, size=size)
            # Note: PIL doesn't directly support font weight, but we can use different font files
            # For now, we'll use the same font regardless of weight
            return font
        except (OSError, IOError) as e:
            logger.debug(f"Failed to load font '{path}': {e}")
            continue
    logger.warning("Falling back to default bitmap font. Persian text may not display correctly.")
    return ImageFont.load_default()


def _parse_color(color_str: str) -> Tuple[int, int, int]:
    """Parse color string to RGB tuple."""
    if not color_str:
        return (0, 0, 0)
    color_str = color_str.strip()
    if color_str.startswith('#'):
        color_str = color_str[1:]
    if len(color_str) == 3:
        color_str = ''.join(c * 2 for c in color_str)
    try:
        return tuple(int(color_str[i:i+2], 16) for i in range(0, 6, 2))
    except ValueError:
        logger.warning(f"Invalid color value '{color_str}', defaulting to black.")
        return (0, 0, 0)


def _measure_text(text: str, font: ImageFont.ImageFont, draw: ImageDraw.ImageDraw) -> float:
    """Measure text width."""
    if hasattr(draw, "textlength"):
        return draw.textlength(text, font=font)
    if hasattr(font, "getlength"):
        return font.getlength(text)
    return font.getsize(text)[0]


def _wrap_text(text: str, font: ImageFont.ImageFont, max_width: int, draw: ImageDraw.ImageDraw) -> list:
    """Wrap text to fit within max_width."""
    if not text:
        return ['']
    
    words = text.split()
    if not words:
        return [text]
    
    lines = []
    current_line = words[0]
    
    for word in words[1:]:
        trial_line = f"{current_line} {word}"
        width = _measure_text(trial_line, font, draw)
        if width <= max_width:
            current_line = trial_line
        else:
            lines.append(current_line)
            current_line = word
    
    lines.append(current_line)
    return lines


def _is_rtl(text: str) -> bool:
    """Check if text is right-to-left (Persian/Arabic)."""
    for char in text:
        if "\u0600" <= char <= "\u06FF" or "\u0750" <= char <= "\u077F":
            return True
    return False


def draw_text_field(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    text_value: str,
    size: int = 32,
    color: str = "#000000",
    align: str = "left",
    max_width: int = None,
    font_filename: str = None,
    weight: str = "normal",
    stroke_width: Optional[int] = None,
    shadow: bool = True,
) -> None:
    """
    Draw a single text field on the image (optional shadow + stroke).
    stroke_width=None keeps legacy auto stroke; 0 disables outline.
    """
    font = _get_font(size=size, weight=weight, font_filename=font_filename)
    color_rgb = _parse_color(color)
    if align == "center" and max_width:
        text_width = _measure_text(str(text_value), font, draw)
        if text_width < max_width:
            x = x + (max_width - int(text_width)) // 2
    elif align == "right" and max_width:
        text_width = _measure_text(str(text_value), font, draw)
        if text_width < max_width:
            x = x + max_width - int(text_width)
    is_rtl = _is_rtl(str(text_value))
    direction = "rtl" if is_rtl else None
    text_to_draw = str(text_value)
    if stroke_width is None:
        stroke_eff = max(size // 14, 1)
    else:
        stroke_eff = max(0, int(stroke_width))

    def _draw_one_line(px: int, py: int, line: str) -> None:
        def _safe_draw_text(position, *, fill, with_stroke=False):
            kwargs = {"font": font, "fill": fill}
            if with_stroke and stroke_eff > 0:
                kwargs["stroke_width"] = stroke_eff
                kwargs["stroke_fill"] = (0, 0, 0)
            if direction:
                kwargs["direction"] = direction
            try:
                draw.text(position, line, **kwargs)
            except KeyError as exc:
                # Pillow without libraqm cannot draw text with RTL direction.
                if "libraqm" not in str(exc).lower() or "direction" not in kwargs:
                    raise
                kwargs.pop("direction", None)
                draw.text(position, line, **kwargs)

        if shadow:
            shadow_offset = max(size // 18, 1)
            shadow_pos = (px + shadow_offset, py + shadow_offset)
            _safe_draw_text(shadow_pos, fill=(0, 0, 0, 192))
        if stroke_eff > 0:
            _safe_draw_text((px, py), fill=color_rgb, with_stroke=True)
        else:
            _safe_draw_text((px, py), fill=color_rgb)

    if max_width:
        lines = _wrap_text(text_to_draw, font, max_width, draw)
        try:
            line_height = font.getbbox("Ay")[3]
        except AttributeError:
            line_height = font.getsize("Ay")[1]
        for i, line in enumerate(lines):
            line_y = y + i * (line_height + 4)
            _draw_one_line(x, line_y, line)
    else:
        _draw_one_line(x, y, text_to_draw)


def render_template(template_obj, dynamic_data_dict: Dict[str, Any], config_override: Dict[str, Any] = None) -> Image.Image:
    """
    Render a template with dynamic data.

    Args:
        template_obj: Template model instance
        dynamic_data_dict: Dictionary with field names as keys and text values as values
                          Example: {'english_date': '2024-01-15', 'buy_price': '1,234.56'}
        config_override: Optional config dict to use instead of template_obj.config (e.g. for preview).

    Returns:
        PIL Image object with rendered template
    """
    if not template_obj.image:
        raise ValueError("Template has no image.")

    # Load template image
    bg_path = template_obj.image.path
    if not Path(bg_path).exists():
        raise FileNotFoundError(f"Template image not found at '{bg_path}'.")

    logger.info(f"Rendering template '{template_obj.name}' using image '{bg_path}'.")

    # Open and convert to RGBA
    base_image = Image.open(bg_path).convert('RGBA')
    draw = ImageDraw.Draw(base_image)
    canvas_size = base_image.size

    # Get configuration
    config = (config_override if config_override is not None else template_obj.config or {}).get('fields', {})
    
    # Draw each text field
    for field_name, field_config in config.items():
        # Get value from dynamic_data_dict, or use field name as fallback
        text_value = dynamic_data_dict.get(field_name, field_name)

        # Skip if text is empty
        if not str(text_value).strip():
            continue

        x = field_config.get('x', 0)
        y = field_config.get('y', 0)
        size = field_config.get('size', 32)
        color = field_config.get('color', '#000000')
        align = field_config.get('align', 'left')
        max_width = field_config.get('max_width')
        weight = field_config.get('font_weight', 'normal')
        font_filename = field_config.get('font')

        draw_text_field(
            draw, x, y, str(text_value),
            size=size, color=color, align=align, max_width=max_width,
            font_filename=font_filename, weight=weight,
        )

    return base_image

