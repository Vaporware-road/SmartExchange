"""Convert filesystem path to public URL for Instagram (Meta must be able to fetch it)."""

import os
from pathlib import Path

from django.conf import settings

from instagram_hub.services.instagram_config import normalize_instagram_base_url


def path_to_public_url(image_path: str, request=None) -> str | None:
    """
    Convert local path under MEDIA_ROOT to a public URL.
    If request is provided and base is not set, uses request.build_absolute_uri.
    """
    path = Path(image_path)
    if not path.exists():
        return None
    media_root = Path(getattr(settings, "MEDIA_ROOT", "") or "")
    if not media_root:
        media_root = Path(settings.BASE_DIR) / "public" / "media"
    media_root = media_root.resolve()
    try:
        rel = path.resolve().relative_to(media_root)
    except ValueError:
        return None
    rel_str = str(rel).replace("\\", "/")
    base = normalize_instagram_base_url(
        (getattr(settings, "INSTAGRAM_BASE_URL", None) or "").strip()
        or os.environ.get("INSTAGRAM_BASE_URL", "").strip()
    )
    if not base and request:
        base = request.build_absolute_uri("/").rstrip("/")
    if not base:
        base = "http://127.0.0.1:8000"
    media_url = (getattr(settings, "MEDIA_URL", "/media/") or "/media/").rstrip("/")
    if not media_url.startswith("/"):
        media_url = "/" + media_url
    return f"{base}{media_url}/{rel_str}"
