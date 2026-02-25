from django.urls import path

from . import api_views

urlpatterns = [
    path("dashboard/", api_views.FinalizeDashboardAPIView.as_view(), name="api-finalize-dashboard"),
    path(
        "category/<int:category_id>/",
        api_views.FinalizeCategoryAPIView.as_view(),
        name="api-finalize-category",
    ),
    path(
        "special-price/<int:special_price_history_id>/",
        api_views.FinalizeSpecialPriceAPIView.as_view(),
        name="api-finalize-special-price",
    ),
]
