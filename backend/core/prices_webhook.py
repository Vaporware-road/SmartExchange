import logging
import threading

import requests

from core.prices_snapshot import build_prices_public_snapshot
from setting.models import SiteSettings

logger = logging.getLogger(__name__)

WEBHOOK_TIMEOUT_SEC = 8


def notify_prices_webhook(source: str) -> None:
    """
    Refresh bot gateway rates cache and, if configured, POST outbound webhook.
    Never raises to callers; logs failures.
    """
    try:
        from bot_gateway.services.rates_cache import refresh_live_rates_cache

        prices = refresh_live_rates_cache(source)
    except Exception:
        logger.exception("prices_webhook: cache refresh failed (source=%s)", source)
        try:
            prices = build_prices_public_snapshot()
        except Exception:
            logger.exception("prices_webhook: snapshot failed (source=%s)", source)
            return

    try:
        site = SiteSettings.load()
    except Exception:
        logger.exception("prices_webhook: could not load SiteSettings")
        return

    url = (getattr(site, "prices_webhook_url", None) or "").strip()
    if not url:
        return

    payload = {
        "event": "prices_updated",
        "source": source,
        "prices": prices,
    }

    def _post():
        try:
            requests.post(
                url,
                json=payload,
                timeout=WEBHOOK_TIMEOUT_SEC,
                headers={"Content-Type": "application/json"},
            )
        except requests.RequestException as exc:
            logger.warning("prices_webhook POST failed (source=%s): %s", source, exc)

    threading.Thread(target=_post, daemon=True).start()
