from django.urls import path, re_path

from . import views

app_name = "website"

urlpatterns = [
    # Matched with and without the trailing slash: the SPA router writes these
    # without one, and an APPEND_SLASH redirect would cost every visitor a hop.
    re_path(r"^site/?$", views.public_site, name="public-site"),
    re_path(r"^site/(?P<slug>[\w-]+)/?$", views.public_site, name="public-site-slug"),
]
