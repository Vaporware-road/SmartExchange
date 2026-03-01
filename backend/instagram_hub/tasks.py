"""
Instagram Hub — background job: generate images and publish to Instagram after finalize.

Runs in a thread (or Celery task when available). Failures are logged; they do not
affect the finalize API response.
"""

import logging
import threading
from typing import List

logger = logging.getLogger(__name__)


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
    from instagram_hub.services.instagram_config import is_instagram_configured

    if not is_instagram_configured():
        logger.info("Instagram not configured; skipping post_finalize_to_instagram")
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
    caption = (category_title or "")[:2200]

    # Publish to Meta API (requests) — catch all to avoid 500
    from instagram_hub.services.instagram_api import publish_to_instagram

    if post_path:
        try:
            pub = publish_to_instagram(
                post_path,
                caption=caption,
                is_story=False,
                request=None,
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


def enqueue_post_finalize_to_instagram(
    category_ids: List[int],
    special_price_history_ids: List[int],
    theme: str = "dark",
) -> None:
    """
    Run post-finalize Instagram job in a background thread so the HTTP response
    is not blocked. Use Celery in production when available.
    """
    def _run():
        try:
            run_post_finalize_to_instagram(
                category_ids=category_ids,
                special_price_history_ids=special_price_history_ids,
                theme=theme,
            )
        except Exception as exc:
            logger.exception("post_finalize_to_instagram thread failed: %s", exc)
            try:
                from setting.utils import log_event
                log_event(
                    level="ERROR",
                    source="other",
                    message="Instagram post after finalize failed",
                    details=str(exc)[:500],
                    user=None,
                )
            except Exception:
                pass

    t = threading.Thread(target=_run, daemon=True)
    t.start()
