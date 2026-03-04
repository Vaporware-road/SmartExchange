"""
Custom views for the SmartExchangePanel project.
"""
from pathlib import Path

from django.conf import settings
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.views.generic import View


def handler404(request, exception):
    """
    Custom 404 error handler.
    This view is automatically called by Django when a 404 error occurs.
    """
    return render(request, '404.html', status=404)


def favicon_view(request):
    """
    Handle favicon.ico requests to prevent 404 errors.
    Returns a 204 No Content response.
    """
    return HttpResponse(status=204)


class SPAView(View):
    """
    Serve the Vue SPA index.html for client-side routing.
    All non-API, non-admin routes are handled by the Vue app.
    """

    def get(self, request, *args, **kwargs):
        index_path = Path(settings.BASE_DIR) / "static" / "vue" / "index.html"
        if not index_path.exists():
            return HttpResponse(
                "<h1>Vue app not built</h1><p>Run: cd frontend && npm run build</p>",
                status=503,
                content_type="text/html",
            )
        return HttpResponse(index_path.read_text(), content_type="text/html")

