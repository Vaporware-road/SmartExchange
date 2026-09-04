"""Instagram Hub — OAuth connect/callback views (Django views for browser redirects)."""

import logging
from urllib.parse import quote

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.http import require_GET

from instagram_hub.models import InstagramConfig
from instagram_hub.services import instagram_oauth

logger = logging.getLogger(__name__)

OAUTH_RETURN_SESSION_KEY = "instagram_oauth_return_to"
ALLOWED_RETURN_PATHS = frozenset({"settings", "instagram"})


def _get_config_for_oauth():
    """First active config with app_id and app_secret set."""
    for config in InstagramConfig.objects.filter(is_active=True).order_by("pk"):
        if (config.app_id or "").strip() and config.get_app_secret():
            return config
    return None


def _store_oauth_return_path(request) -> None:
    return_to = (request.GET.get("return_to") or "").strip().lower()
    if return_to in ALLOWED_RETURN_PATHS:
        request.session[OAUTH_RETURN_SESSION_KEY] = return_to


def _pop_oauth_return_path(request) -> str:
    return request.session.pop(OAUTH_RETURN_SESSION_KEY, "instagram")


def _frontend_redirect(query: str, return_path: str) -> str:
    if return_path == "settings":
        return f"/settings?{query}"
    return f"/instagram?{query}"


@login_required
@require_GET
def instagram_connect(request):
    """Start OAuth: save state, redirect to Meta."""
    config = _get_config_for_oauth()
    if not config:
        return redirect(_frontend_redirect("instagram_callback=error&msg=App+ID+or+App+Secret+not+configured", "instagram"))

    _store_oauth_return_path(request)

    app_id = (config.app_id or "").strip()
    redirect_uri = request.build_absolute_uri(reverse("instagram_hub:callback"))
    state = instagram_oauth.generate_oauth_state()
    config.oauth_state = state
    config.save(update_fields=["oauth_state", "updated_at"])

    auth_url = instagram_oauth.build_authorization_url(app_id, redirect_uri, state)
    return redirect(auth_url)


@login_required
@require_GET
def instagram_callback(request):
    """OAuth callback: validate state, exchange code, save token, redirect to frontend."""
    return_path = _pop_oauth_return_path(request)

    error = request.GET.get("error")
    if error:
        desc = request.GET.get("error_description") or request.GET.get("error_reason") or error
        return redirect(_frontend_redirect("instagram_callback=error&msg=" + quote(desc), return_path))

    code = (request.GET.get("code") or "").strip()
    state = (request.GET.get("state") or "").strip()
    if not code:
        return redirect(_frontend_redirect("instagram_callback=error&msg=No+authorization+code", return_path))

    config = _get_config_for_oauth()
    if not config or (config.oauth_state or "").strip() != state:
        if config:
            config.oauth_state = ""
            config.save(update_fields=["oauth_state", "updated_at"])
        return redirect(_frontend_redirect("instagram_callback=error&msg=State+mismatch", return_path))

    redirect_uri = request.build_absolute_uri(reverse("instagram_hub:callback"))
    result = instagram_oauth.perform_full_oauth_exchange(code, redirect_uri, config)

    if result.get("success"):
        suffix = "#instagram" if return_path == "settings" else ""
        return redirect(_frontend_redirect("instagram_callback=success", return_path) + suffix)
    return redirect(
        _frontend_redirect(
            "instagram_callback=error&msg=" + quote(result.get("error", "Unknown")),
            return_path,
        )
    )
