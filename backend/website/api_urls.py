from django.urls import path

from . import api_views

urlpatterns = [
    path("site/", api_views.WebsiteSiteAPIView.as_view(), name="api-website-site"),
    path("layout/", api_views.WebsiteLayoutAPIView.as_view(), name="api-website-layout"),
    path("sections/", api_views.WebsiteSectionListAPIView.as_view(), name="api-website-sections"),
    path(
        "sections/reorder/",
        api_views.WebsiteSectionReorderAPIView.as_view(),
        name="api-website-sections-reorder",
    ),
    path(
        "sections/<int:pk>/",
        api_views.WebsiteSectionDetailAPIView.as_view(),
        name="api-website-section",
    ),
    path("assets/", api_views.WebsiteAssetAPIView.as_view(), name="api-website-assets"),
    path("assets/<int:pk>/", api_views.WebsiteAssetDetailAPIView.as_view(), name="api-website-asset"),
    path("preview/", api_views.WebsitePreviewAPIView.as_view(), name="api-website-preview"),
    path("publish/", api_views.WebsitePublishAPIView.as_view(), name="api-website-publish"),
    path("unpublish/", api_views.WebsiteUnpublishAPIView.as_view(), name="api-website-unpublish"),
    path(
        "publications/",
        api_views.WebsitePublicationListAPIView.as_view(),
        name="api-website-publications",
    ),
    path(
        "publications/<int:version>/restore/",
        api_views.WebsitePublicationRestoreAPIView.as_view(),
        name="api-website-publication-restore",
    ),
]
