from django.urls import path
from . import views

app_name = "instagram_hub"

urlpatterns = [
    path("connect/", views.instagram_connect, name="connect"),
    path("callback/", views.instagram_callback, name="callback"),
]
