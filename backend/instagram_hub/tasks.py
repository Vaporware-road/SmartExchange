"""
Instagram Hub — background job: generate images and publish to Instagram after finalize.
"""

import logging
from typing import List

from celery import shared_task

from instagram_hub.services.instagram_api import CAPTION_MAX

logger = logging.getLogger(__name__)


def _feed_caption_with_config_extras(base: str) -> str:
    """Append active InstagramConfig feed_caption_suffix and feed_hashtags; cap at CAPTION_MAX."""
    text = (base or "").strip()
    try:
        from instagram_hub.models import InstagramConfig

        cfg = InstagramConfig.objects.filter(is_active=True).order_by("pk").first()
        if not cfg:
            return text[:CAPTION_MAX]
        suffix = (cfg.feed_caption_suffix or "").strip()
        hashtags = (cfg.feed_hashtags or "").strip()
        parts = [text] if text else []
        if suffix:
            parts.append(suffix)
        if hashtags:
            parts.append(hashtags)
        combined = "\n\n".join(parts) if parts else ""
        return combined[:CAPTION_MAX]
    except Exception:
        return text[:CAPTION_MAX]


def _log_instagram_publication(
    *,
    kind: str,
    category_ids: List[int],
    special_price_history_ids: List[int],
    result: dict,
) -> None:
    try:
        from instagram_hub.models import InstagramPublicationLog

        InstagramPublicationLog.objects.create(
            kind=kind,
            success=bool(result.get("success")),
            error_message=(
                (result.get("message") or "")[:4000] if not result.get("success") else ""
            ),
            media_id=str(result.get("id") or "")[:128],
            container_id=str(result.get("creation_id") or "")[:128],
            category_ids=list(category_ids),
            special_price_history_ids=list(special_price_history_ids),
        )
    except Exception:
        logger.exception("Failed to write InstagramPublicationLog")


def schedule_instagram_post_finalize(
    category_ids: List[int],
    special_price_history_ids: List[int],
    theme: str = "dark",
) -> None:
    """Queue Celery task to render and publish finalize snapshot to Instagram."""
    post_finalize_to_instagram_task.delay(
        category_ids=list(category_ids),
        special_price_history_ids=list(special_price_history_ids),
        theme=theme,
    )


def _build_price_entries_for_finalize(
    category_ids: List[int],
    special_price_history_ids: List[int],
) -> tuple:
    """
    Build combined price_entries and a category_title for the image.
    Returns (entries, category_title). category_title is used as header (e.g. "Price Update").
    """
    from instagram_hub.api_views import _build_price_entries_from_category_ids
    from special_price.models import SpecialPriceHistory

    entries = []
    if category_ids:
        entries.extend(_build_price_entries_from_category_ids(category_ids))
    if special_price_history_ids:
        for sp_id in special_price_history_ids:
            try:
                sph = SpecialPriceHistory.objects.select_related(
                    "special_price_type"
                ).get(id=sp_id)
                entries.append({
                    "title": sph.special_price_type.name,
                    "price_type_name": sph.special_price_type.name,
                    "price": str(sph.price),
                })
            except SpecialPriceHistory.DoesNotExist:
                pass

    category_title = None
    if category_ids and len(category_ids) == 1:
        from category.models import Category
        cat = Category.objects.filter(id=category_ids[0]).values_list("name", flat=True).first()
        if cat:
            category_title = cat
    if (
        not category_title
        or category_title == "Price Update"
    ) and special_price_history_ids and len(special_price_history_ids) == 1 and not category_ids:
        from special_price.models import SpecialPriceHistory
        name = (
            SpecialPriceHistory.objects.filter(id=special_price_history_ids[0])
            .values_list("special_price_type__name", flat=True)
            .first()
        )
        if name:
            category_title = name
    if not category_title:
        category_title = "Price Update"  # fallback

    return entries, category_title or "Price Update"


def run_post_finalize_to_instagram(
    category_ids: List[int],
    special_price_history_ids: List[int],
    theme: str = "dark",
) -> None:
    """
    Generate post + story images from finalized prices and publish to Instagram.
    Logs errors; does not raise. Safe to run in a background thread.
    Failures here must NOT affect the finalize API response (no 500 to frontend).
    """
    from instagram_hub.services.instagram_config import (
        get_instagram_readiness,
        is_instagram_configured,
        is_ready_for_publish,
    )

    if not is_instagram_configured():
        logger.info("Instagram not configured; skipping post_finalize_to_instagram")
        return
    if not is_ready_for_publish():
        logger.warning(
            "Instagram credentials present but not ready for publish "
            "(check INSTAGRAM_BASE_URL and token expiry)"
        )
        try:
            from setting.utils import log_event
            log_event(
                level="WARNING",
                source="other",
                message="Instagram post skipped: not ready for publish (INSTAGRAM_BASE_URL or token)",
                details=str(get_instagram_readiness().get("warnings")),
                user=None,
            )
        except Exception:
            pass
        return

    try:
        entries, category_title = _build_price_entries_for_finalize(
            category_ids, special_price_history_ids
        )
    except Exception as e:
        logger.exception(
            "post_finalize_to_instagram: failed to build price entries: %s",
            e,
            exc_info=True,
        )
        try:
            from setting.utils import log_event
            log_event(
                level="ERROR",
                source="other",
                message="Instagram post after finalize: failed to build price entries",
                details=str(e)[:500],
                user=None,
            )
        except Exception:
            pass
        return

    if not entries:
        logger.warning("post_finalize_to_instagram: no price entries to render")
        return

    # Image generation (Pillow) — catch all to avoid 500
    try:
        from instagram_hub.services.image_generator import generate_price_images
        result = generate_price_images(
            price_entries=entries,
            theme=theme,
            category_title=category_title,
        )
    except Exception as e:
        logger.exception(
            "post_finalize_to_instagram: image generation failed (Pillow/IO): %s",
            e,
            exc_info=True,
        )
        try:
            from setting.utils import log_event
            log_event(
                level="ERROR",
                source="other",
                message="Instagram post after finalize: image generation failed",
                details=str(e)[:500],
                user=None,
            )
        except Exception:
            pass
        return

    if not result:
        logger.warning("post_finalize_to_instagram: generate_price_images returned None")
        try:
            from setting.utils import log_event
            log_event(
                level="ERROR",
                source="other",
                message="Instagram post after finalize: image generation failed",
                details=None,
                user=None,
            )
        except Exception:
            pass
        return

    post_path = result.get("post_path")
    story_path = result.get("story_path")
    caption = _feed_caption_with_config_extras(category_title or "")

    # Publish to Meta API (requests) — catch all to avoid 500
    from instagram_hub.models import InstagramPublicationLog
    from instagram_hub.services.instagram_api import publish_to_instagram

    if post_path:
        try:
            pub = publish_to_instagram(
                post_path,
                caption=caption,
                is_story=False,
                request=None,
            )
            _log_instagram_publication(
                kind=InstagramPublicationLog.KIND_FEED,
                category_ids=category_ids,
                special_price_history_ids=special_price_history_ids,
                result=pub,
            )
            if not pub.get("success"):
                logger.warning(
                    "Instagram post (feed) failed: %s",
                    pub.get("message", "Unknown"),
                )
        except Exception as e:
            logger.exception(
                "post_finalize_to_instagram: Meta API (post) failed: %s",
                e,
                exc_info=True,
            )
            _log_instagram_publication(
                kind=InstagramPublicationLog.KIND_FEED,
                category_ids=category_ids,
                special_price_history_ids=special_price_history_ids,
                result={"success": False, "message": str(e)[:500], "creation_id": None},
            )
            try:
                from setting.utils import log_event
                log_event(
                    level="ERROR",
                    source="other",
                    message="Instagram post after finalize: publish (feed) failed",
                    details=str(e)[:500],
                    user=None,
                )
            except Exception:
                pass

    if story_path:
        try:
            pub = publish_to_instagram(
                story_path,
                caption="",
                is_story=True,
                request=None,
            )
            _log_instagram_publication(
                kind=InstagramPublicationLog.KIND_STORY,
                category_ids=category_ids,
                special_price_history_ids=special_price_history_ids,
                result=pub,
            )
            if not pub.get("success"):
                logger.warning(
                    "Instagram story failed: %s",
                    pub.get("message", "Unknown"),
                )
        except Exception as e:
            logger.exception(
                "post_finalize_to_instagram: Meta API (story) failed: %s",
                e,
                exc_info=True,
            )
            _log_instagram_publication(
                kind=InstagramPublicationLog.KIND_STORY,
                category_ids=category_ids,
                special_price_history_ids=special_price_history_ids,
                result={"success": False, "message": str(e)[:500], "creation_id": None},
            )
            try:
                from setting.utils import log_event
                log_event(
                    level="ERROR",
                    source="other",
                    message="Instagram post after finalize: publish (story) failed",
                    details=str(e)[:500],
                    user=None,
                )
            except Exception:
                pass


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    max_retries=2,
    retry_backoff=True,
    retry_jitter=True,
)
def post_finalize_to_instagram_task(
    self,
    *,
    category_ids: List[int],
    special_price_history_ids: List[int],
    theme: str = "dark",
) -> None:
    run_post_finalize_to_instagram(
        category_ids=category_ids,
        special_price_history_ids=special_price_history_ids,
        theme=theme,
    )


def enqueue_post_finalize_to_instagram(
    category_ids: List[int],
    special_price_history_ids: List[int],
    theme: str = "dark",
) -> None:
    """
    Queue post-finalize Instagram job in Celery (alias for schedule_instagram_post_finalize).
    """
    schedule_instagram_post_finalize(
        category_ids=category_ids,
        special_price_history_ids=special_price_history_ids,
        theme=theme,
    )


@shared_task(name="instagram_hub.refresh_token_if_needed")
def refresh_instagram_token_if_needed() -> dict:
    """
    Refresh long-lived Meta token when within 30 days of expiry.
    Logs warnings when expired or refresh fails.
    """
    from datetime import timedelta

    from instagram_hub.models import InstagramConfig
    from instagram_hub.services.instagram_config import get_token_status
    from instagram_hub.services.instagram_oauth import exchange_for_long_lived_token

    config = InstagramConfig.objects.filter(is_active=True).order_by("pk").first()
    if not config:
        return {"action": "skip", "reason": "no_config"}

    token = config.get_decrypted_token()
    if not token:
        return {"action": "skip", "reason": "no_token"}

    status = get_token_status(config)
    if status["expired"]:
        try:
            from setting.utils import log_event
            log_event(
                level="WARNING",
                source="other",
                message="Instagram token expired — reconnect from Settings",
                details=f"ig_user_id={config.ig_user_id}",
                user=None,
            )
        except Exception:
            pass
        return {"action": "warn", "reason": "token_expired"}

    days = status["days_remaining"]
    if days is None or days > 30:
        return {"action": "skip", "reason": "not_due", "days_remaining": days}

    app_id = (config.app_id or "").strip()
    app_secret = config.get_app_secret()
    if not app_id or not app_secret:
        return {"action": "skip", "reason": "missing_app_credentials"}

    result = exchange_for_long_lived_token(token, app_id, app_secret)
    if not result.get("success"):
        try:
            from setting.utils import log_event
            log_event(
                level="WARNING",
                source="other",
                message="Instagram token refresh failed",
                details=str(result.get("error", ""))[:500],
                user=None,
            )
        except Exception:
            pass
        return {"action": "failed", "error": result.get("error")}

    from django.utils import timezone

    expires_in = result.get("expires_in", 5184000)
    config.set_access_token(result["access_token"])
    config.token_expires_at = timezone.now() + timedelta(seconds=expires_in)
    config.save(update_fields=["access_token_encrypted", "token_expires_at", "updated_at"])
    logger.info("Instagram token refreshed; expires in %s days", expires_in // 86400)
    return {"action": "refreshed", "days_remaining": expires_in // 86400}
