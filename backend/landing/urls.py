from django.urls import path, re_path

from . import views

app_name = "landing"

urlpatterns = [
    path("", views.landing_page, name="home"),
    # Matched with and without the trailing slash: these are SPA routes the
    # router writes without one, and an APPEND_SLASH redirect would cost every
    # visitor a round trip.
    re_path(r"^tutorials/?$", views.tutorial_index, name="tutorials"),
    re_path(r"^tutorials/(?P<slug>[\w-]+)/?$", views.tutorial_detail, name="tutorial"),
]


