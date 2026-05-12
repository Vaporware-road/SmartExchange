"""
Instagram Hub — publish to Instagram via Meta Graph API.

Container creation + media_publish; uses InstagramConfig credentials.
"""

import logging
import time

import requests

from instagram_hub.models import InstagramConfig
from instagram_hub.utils import path_to_public_url

logger = logging.getLogger(__name__)

GRAPH_API_BASE = "https://graph.facebook.com/v18.0"
REQUEST_TIMEOUT = 15
MAX_RETRIES = 2
RETRY_DELAY_SECONDS = 0.5
CAPTION_MAX = 2200


def _get_credentials() -> tuple:
    """Return (ig_user_id, access_token) from first active InstagramConfig."""
    config = InstagramConfig.objects.filter(is_active=True).first()
    if not config:
        return None, None
    token = config.get_decrypted_token()
    ig_id = (config.ig_user_id or "").strip()
    if ig_id and token:
        return ig_id, token
    if token:
        try:
            r = requests.get(
                f"{GRAPH_API_BASE}/me",
                params={"access_token": token, "fields": "id"},
                timeout=REQUEST_TIMEOUT,
            )
            if r.ok:
                ig_id = r.json().get("id", "")
                if ig_id:
                    config.ig_user_id = ig_id
                    config.save(update_fields=["ig_user_id", "updated_at"])
                    return ig_id, token
        except Exception as e:
            logger.warning("Could not resolve ig_user_id: %s", e)
    return None, None


def create_media_container(
    ig_user_id: str,
    token: str,
    image_url: str,
    caption: str,
    is_story: bool,
) -> dict:
    """
    POST /{ig-user-id}/media — create container.

    Returns dict: success (bool), container_id (str|None), message (str).
    """
    payload = {"image_url": image_url, "access_token": token}
    cap = (caption or "")[:CAPTION_MAX] if not is_story else ""
    if not is_story and cap:
        payload["caption"] = cap
    if is_story:
        payload["media_type"] = "STORIES"
    create_url = f"{GRAPH_API_BASE}/{ig_user_id}/media"
    try:
        r = requests.post(create_url, data=payload, timeout=REQUEST_TIMEOUT)
        r.raise_for_status()
        data = r.json()
        container_id = data.get("id")
        if not container_id:
            err = data.get("error", {})
            return {
                "success": False,
                "container_id": None,
                "message": err.get("message", "No container id"),
            }
        return {"success": True, "container_id": str(container_id), "message": "ok"}
    except requests.RequestException as e:
        msg = str(e)
        if getattr(e, "response", None) is not None:
            try:
                msg = e.response.json().get("error", {}).get("message", msg)
            except Exception:
                pass
        return {"success": False, "container_id": None, "message": msg}


def publish_media_container(ig_user_id: str, token: str, creation_id: str) -> dict:
    """
    POST /{ig-user-id}/media_publish — publish a container.

    Returns dict: success (bool), media_id (str|None), message (str).
    """
    try:
        r2 = requests.post(
            f"{GRAPH_API_BASE}/{ig_user_id}/media_publish",
            data={"creation_id": creation_id, "access_token": token},
            timeout=REQUEST_TIMEOUT,
        )
        r2.raise_for_status()
        media_id = r2.json().get("id")
        if not media_id:
            return {"success": False, "media_id": None, "message": "No media id in response"}
        return {"success": True, "media_id": str(media_id), "message": "Published"}
    except requests.RequestException as e:
        msg = str(e)
        if getattr(e, "response", None) is not None:
            try:
                msg = e.response.json().get("error", {}).get("message", msg)
            except Exception:
                pass
        return {"success": False, "media_id": None, "message": msg}


def publish_to_instagram(
    image_url_or_path: str,
    caption: str = "",
    is_story: bool = False,
    request=None,
) -> dict:
    """
    Publish image to Instagram. image_url_or_path: public URL or filesystem path.

    Returns dict: {success, message, id (media_id if success), creation_id (container if known)}.
    """
    ig_user_id, token = _get_credentials()
    if not ig_user_id or not token:
        return {"success": False, "message": "Instagram not configured", "creation_id": None}

    image_url = image_url_or_path
    if not image_url.startswith("http"):
        image_url = path_to_public_url(image_url_or_path, request=request)
    if not image_url or not image_url.startswith("http"):
        return {
            "success": False,
            "message": "Image URL not accessible (set INSTAGRAM_BASE_URL for local paths)",
            "creation_id": None,
        }

    caption = (caption or "")[:CAPTION_MAX] if not is_story else ""

    last_creation_id = None
    last_message = "Unknown error"

    for attempt in range(1, MAX_RETRIES + 1):
        cr = create_media_container(
            ig_user_id, token, image_url, caption, is_story=is_story
        )
        if not cr.get("success"):
            last_message = cr.get("message", "Create failed")
            last_creation_id = None
            logger.warning(
                "Instagram publish attempt %d/%d (create): %s",
                attempt,
                MAX_RETRIES,
                last_message,
            )
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY_SECONDS)
                continue
            break

        creation_id = cr["container_id"]
        last_creation_id = creation_id
        pr = publish_media_container(ig_user_id, token, creation_id)
        if pr.get("success"):
            media_id = pr.get("media_id")
            logger.info("Instagram publish: media_id=%s is_story=%s", media_id, is_story)
            return {
                "success": True,
                "message": "Published",
                "id": media_id,
                "creation_id": creation_id,
            }
        last_message = pr.get("message", "Publish failed")
        logger.warning(
            "Instagram publish attempt %d/%d (publish): %s",
            attempt,
            MAX_RETRIES,
            last_message,
        )
        if attempt < MAX_RETRIES:
            time.sleep(RETRY_DELAY_SECONDS)
            continue
        break

    msg = str(last_message)[:500]
    try:
        from setting.utils import log_event
        log_event(
            level="ERROR",
            source="other",
            message="Instagram post failed: %s" % msg,
            details=None,
            user=None,
        )
    except Exception:
        pass
    return {
        "success": False,
        "message": msg,
        "creation_id": last_creation_id,
    }
