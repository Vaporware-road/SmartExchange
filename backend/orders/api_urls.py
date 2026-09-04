from django.urls import path

from orders.api_views import (
    OrderIntakeDetailView,
    OrderIntakeLinkView,
    OrderIntakeListView,
    OrderIntakeReviewView,
    OrderPendingCountView,
)

urlpatterns = [
    path("pending-count/", OrderPendingCountView.as_view(), name="orders-pending-count"),
    path("intake-link/", OrderIntakeLinkView.as_view(), name="orders-intake-link"),
    path("", OrderIntakeListView.as_view(), name="orders-list"),
    path("<uuid:uuid>/", OrderIntakeDetailView.as_view(), name="orders-detail"),
    path("<uuid:uuid>/review/", OrderIntakeReviewView.as_view(), name="orders-review"),
]
