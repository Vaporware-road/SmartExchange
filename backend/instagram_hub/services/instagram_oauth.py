"""
Instagram Hub — Meta OAuth 2.0 flow.

Code → short-lived token → long-lived token (60 days); resolve IG Business ID; save to InstagramConfig.
"""

import logging
import secrets
from datetime import timedelta

import requests
from django.utils import timezone

logger = logging.getLogger(__name__)

GRAPH_API_VERSION = "v18.0"
GRAPH_API_BASE = f"https://graph.facebook.com/{GRAPH_API_VERSION}"
FACEBOOK_OAUTH_URL = f"https://www.facebook.com/{GRAPH_API_VERSION}/dialog/oauth"
REQUEST_TIMEOUT = 15

INSTAGRAM_SCOPES = [
    "instagram_basic",
    "instagram_content_publish",
    "pages_show_list",
    "pages_read_engagement",
]


def generate_oauth_state() -> str:
    return secrets.token_urlsafe(48)


def build_authorization_url(app_id: str, redirect_uri: str, state: str) -> str:
    params = {
        "client_id": app_id,
        "redirect_uri": redirect_uri,
        "scope": ",".join(INSTAGRAM_SCOPES),
        "response_type": "code",
        "state": state,
    }
    qs = "&".join(f"{k}={requests.utils.quote(str(v))}" for k, v in params.items())
    return f"{FACEBOOK_OAUTH_URL}?{qs}"


def exchange_code_for_short_lived_token(
    code: str, app_id: str, app_secret: str, redirect_uri: str
) -> dict:
    try:
        r = requests.get(
            f"{GRAPH_API_BASE}/oauth/access_token",
            params={
                "client_id": app_id,
                "client_secret": app_secret,
                "redirect_uri": redirect_uri,
                "code": code,
            },
            timeout=REQUEST_TIMEOUT,
        )
        data = r.json()
        if r.ok and data.get("access_token"):
            return {
                "success": True,
                "access_token": data["access_token"],
                "expires_in": data.get("expires_in", 3600),
            }
        return {"success": False, "error": data.get("error", {}).get("message", r.text[:300])}
    except requests.RequestException as e:
        logger.exception("Instagram OAuth code exchange: %s", e)
        return {"success": False, "error": str(e)[:300]}


def exchange_for_long_lived_token(
    short_lived_token: str, app_id: str, app_secret: str
) -> dict:
    try:
        r = requests.get(
            f"{GRAPH_API_BASE}/oauth/access_token",
            params={
                "grant_type": "fb_exchange_token",
                "client_id": app_id,
                "client_secret": app_secret,
                "fb_exchange_token": short_lived_token,
            },
            timeout=REQUEST_TIMEOUT,
        )
        data = r.json()
        if r.ok and data.get("access_token"):
            return {
                "success": True,
                "access_token": data["access_token"],
                "expires_in": data.get("expires_in", 5184000),
            }
        return {"success": False, "error": data.get("error", {}).get("message", r.text[:300])}
    except requests.RequestException as e:
        logger.exception("Instagram OAuth long-lived exchange: %s", e)
        return {"success": False, "error": str(e)[:300]}


def resolve_instagram_business_id(access_token: str) -> dict:
    try:
        r = requests.get(
            f"{GRAPH_API_BASE}/me/accounts",
            params={
                "access_token": access_token,
                "fields": "id,name,instagram_business_account",
            },
            timeout=REQUEST_TIMEOUT,
        )
        data = r.json()
        if not r.ok:
            return {"success": False, "error": data.get("error", {}).get("message", r.text[:300])}
        for page in data.get("data", []):
            ig = page.get("instagram_business_account")
            if ig and ig.get("id"):
                return {
                    "success": True,
                    "ig_user_id": ig["id"],
                    "page_id": page.get("id", ""),
                    "page_name": page.get("name", ""),
                }
        return {
            "success": False,
            "error": "No Facebook Page with linked Instagram Business account found.",
        }
    except requests.RequestException as e:
        logger.exception("Instagram resolve business ID: %s", e)
        return {"success": False, "error": str(e)[:300]}


def perform_full_oauth_exchange(code: str, redirect_uri: str, config) -> dict:
    """
    code → short-lived → long-lived; resolve ig_user_id; save to config.
    config: InstagramConfig instance with app_id and app_secret set.
    """
    app_id = (config.app_id or "").strip()
    app_secret = config.get_app_secret()

    if not app_id or not app_secret:
        return {"success": False, "error": "App ID or App Secret not configured."}

    step1 = exchange_code_for_short_lived_token(code, app_id, app_secret, redirect_uri)
    if not step1.get("success"):
        return {"success": False, "error": step1.get("error", "Code exchange failed")}

    step2 = exchange_for_long_lived_token(step1["access_token"], app_id, app_secret)
    if not step2.get("success"):
        return {"success": False, "error": step2.get("error", "Long-lived exchange failed")}

    long_token = step2["access_token"]
    expires_in = step2.get("expires_in", 5184000)
    expires_at = timezone.now() + timedelta(seconds=expires_in)

    step3 = resolve_instagram_business_id(long_token)
    if not step3.get("success"):
        return {
            "success": False,
            "error": step3.get("error", "Could not resolve Instagram Business account."),
        }

    ig_user_id = step3.get("ig_user_id", "")
    if not ig_user_id:
        return {
            "success": False,
            "error": "No Instagram Business account ID returned from Meta.",
        }

    config.set_access_token(long_token)
    config.token_expires_at = expires_at
    config.oauth_state = ""
    config.ig_user_id = ig_user_id or config.ig_user_id
    config.save(update_fields=["access_token_encrypted", "token_expires_at", "oauth_state", "ig_user_id", "updated_at"])

    return {
        "success": True,
        "message": f"Connected. IG ID: {ig_user_id}. Token expires: {expires_at.strftime('%Y-%m-%d %H:%M')}.",
        "ig_user_id": ig_user_id,
        "expires_at": expires_at,
    }
