"""
Custom views for the MrExchangePanel project.
"""
from pathlib import Path

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import View
from django.views.static import serve as django_static_serve


def handler404(request, exception):
    """
    Custom 404 error handler.
    This view is automatically called by Django when a 404 error occurs.
    """
    try:
        return render(request, '404.html', status=404)
    except Exception:
        # Never turn a not-found into 500 if the template has issues.
        return HttpResponseNotFound("404 page not found")


def favicon_view(request):
    """
    Handle favicon.ico requests to prevent 404 errors.
    Returns a 204 No Content response.
    """
    return HttpResponse(status=204)


_NO_CACHE_STATIC_NAMES = frozenset(
    {
        "sw.js",
        "registerSW.js",
        "manifest.webmanifest",
        "manifest.json",
        "index.html",
    }
)


def serve_static_with_cache(request, path, document_root=None, show_indexes=False):
    """
    Serve static files with cache policy suited to the Vue SPA:

    - Service worker / manifest / shell → no-cache (always revalidate)
    - Content-hashed /static/vue/assets/* → long-lived immutable

    document_root defaults to STATIC_ROOT (the collected build). When the
    requested file exists in the editable source dir (STATICFILES_DIRS), it is
    served from there instead so source edits hot-reload without collectstatic.
    """
    source_root = settings.STATICFILES_DIRS[0]
    if document_root is None or (source_root / path.strip("/")).is_file():
        document_root = source_root

    response = django_static_serve(
        request, path, document_root=document_root, show_indexes=show_indexes
    )
    if response.status_code != 200:
        return response

    normalized = path.replace("\\", "/").lstrip("/")
    basename = Path(normalized).name

    if basename in _NO_CACHE_STATIC_NAMES or normalized.endswith("/index.html"):
        response["Cache-Control"] = "no-cache, must-revalidate"
    elif normalized.startswith("vue/assets/"):
        response["Cache-Control"] = "public, max-age=31536000, immutable"

    return response


def spa_index_path():
    """
    Locate the built SPA shell.

    Prefer the collectstatic copy under STATIC_ROOT so the shell matches assets
    served from /static/vue/; fall back to the build output dir. Returns None
    when the frontend has not been built.
    """
    candidates = [
        Path(settings.STATIC_ROOT) / "vue" / "index.html",
        Path(settings.BASE_DIR) / "static" / "vue" / "index.html",
    ]
    return next((p for p in candidates if p.exists()), None)


def spa_not_built_response():
    return HttpResponse(
        "<h1>Vue app not built</h1><p>Run: cd frontend && npm run build</p>",
        status=503,
        content_type="text/html",
    )


class SPAView(View):
    """
    Serve the Vue SPA index.html for client-side routing.
    All non-API, non-admin routes are handled by the Vue app, `/` included —
    see landing/views.py, which serves the same shell with marketing metadata.
    """

    def get(self, request, *args, **kwargs):
        index_path = spa_index_path()
        if index_path is None:
            return spa_not_built_response()
        response = HttpResponse(index_path.read_text(), content_type="text/html")
        response["Cache-Control"] = "no-store, no-cache, must-revalidate"
        return response
