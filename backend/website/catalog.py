"""Loader for the shared website catalog.

The JSON under ``website/catalog/`` is the one place that says what a customer
site can be made of. Python reads it to validate what the builder sends; the
SPA imports the same files through the ``@catalog`` Vite alias to render with.
One copy, so a layout can never claim a variant the frontend cannot draw.

Files are read once and cached in module state: they ship with the code and
cannot change between requests, so re-reading them per request would be four
stat calls for nothing.
"""
import json
from functools import lru_cache
from pathlib import Path

CATALOG_DIR = Path(__file__).resolve().parent / "catalog"

DEFAULT_LAYOUT = "aurora"
DEFAULT_LOCALE = "en"

# Style groups an owner may override on top of a theme. ``brand_color`` is a
# free colour rather than a preset, so it is validated separately.
STYLE_GROUPS = ("button", "card", "background", "corner", "density", "font_pair")


@lru_cache(maxsize=None)
def _load(name):
    with (CATALOG_DIR / f"{name}.json").open(encoding="utf-8") as fh:
        return json.load(fh)


def layouts():
    return _load("layouts")


def themes():
    return _load("themes")


def sections():
    return _load("sections")


def styles():
    return _load("styles")


def layout(slug):
    """The manifest for ``slug``, falling back to the default layout."""
    return layouts().get(slug) or layouts()[DEFAULT_LAYOUT]


def theme(slug):
    spec = themes().get(slug)
    if spec is None:
        spec = themes()[layout(DEFAULT_LAYOUT)["default_theme"]]
    return spec


def is_layout(slug):
    return slug in layouts()


def is_theme(slug):
    return slug in themes()


def is_section_type(section_type):
    return section_type in sections()


def variants_for(section_type):
    spec = sections().get(section_type)
    return tuple(spec["variants"]) if spec else ()


def default_variant(layout_slug, section_type):
    """The variant a layout draws a section type with when none is pinned."""
    chosen = layout(layout_slug)["defaults"].get(section_type)
    if chosen in variants_for(section_type):
        return chosen
    available = variants_for(section_type)
    return available[0] if available else ""


def field_defaults(section_type):
    """Starter content for a section: every field that declares a default."""
    spec = sections().get(section_type)
    if not spec:
        return {}
    content = {}
    for field in spec["fields"]:
        if "default" in field:
            content[field["key"]] = field["default"]
        elif field["type"] == "list":
            content[field["key"]] = []
    return content


def resolve_tokens(theme_slug, overrides=None):
    """Flatten a theme plus the owner's style choices into CSS custom properties.

    Order matters and is the whole theming contract: theme colours first, then
    the style presets the theme asks for, then the owner's overrides on top.
    A site therefore inherits a coherent look and still bends where the owner
    touched it, which is what lets one theme dress ten different layouts.
    """
    theme_spec = theme(theme_slug)
    overrides = overrides or {}
    style_catalog = styles()

    tokens = dict(theme_spec["tokens"])
    chosen = {}
    families = []

    for group in STYLE_GROUPS:
        options = style_catalog.get(group, {})
        value = overrides.get(group) or theme_spec["defaults"].get(group)
        if value not in options:
            value = theme_spec["defaults"].get(group)
        chosen[group] = value
        option = options.get(value) or {}
        tokens.update(option.get("tokens", {}))
        families.extend(option.get("families", []))

    brand = (overrides.get("brand_color") or "").strip()
    if brand:
        tokens["--ws-primary"] = brand
        tokens["--ws-primary-hover"] = brand
        tokens["--ws-on-primary"] = _readable_on(brand)

    return {
        "mode": theme_spec["mode"],
        "tokens": tokens,
        "styles": chosen,
        "font_families": families,
    }


def _readable_on(hex_color):
    """Black or white text for a background, by perceived luminance.

    An owner picking their brand colour has no way to also pick a legible
    foreground, so the contrast decision has to be made for them.
    """
    value = hex_color.lstrip("#")
    if len(value) == 3:
        value = "".join(ch * 2 for ch in value)
    if len(value) != 6:
        return "#ffffff"
    try:
        r, g, b = (int(value[i : i + 2], 16) for i in (0, 2, 4))
    except ValueError:
        return "#ffffff"
    luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
    return "#0b0b0a" if luminance > 0.6 else "#ffffff"
