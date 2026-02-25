from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import api

urlpatterns = [
    path("currencies/", api.CurrencyListAPIView.as_view(), name="api-currencies"),
]

router = DefaultRouter()
router.register(r"", api.CategoryViewSet, basename="category")

price_type_router = DefaultRouter()
price_type_router.register(r"", api.PriceTypeViewSet, basename="pricetype")

urlpatterns += [
    path(
        "<int:category_pk>/price-types/",
        include((price_type_router.urls, "price-types")),
    ),
    path("", include(router.urls)),
]
