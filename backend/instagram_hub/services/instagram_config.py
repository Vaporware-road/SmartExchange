"""Instagram configuration helpers. Reads from InstagramConfig model."""


def is_instagram_configured() -> bool:
    """Return True if an active InstagramConfig has token and ig_user_id set."""
    try:
        from instagram_hub.models import InstagramConfig
        config = InstagramConfig.objects.filter(is_active=True).first()
        if not config:
            return False
        token = config.get_decrypted_token()
        ig_id = (config.ig_user_id or "").strip()
        return bool(token and ig_id)
    except Exception:
        return False
