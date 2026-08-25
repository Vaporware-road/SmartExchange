from django.urls import path

from . import api_views

urlpatterns = [
    path("checkin/", api_views.FleetCheckinAPIView.as_view(), name="api-fleet-checkin"),
    path("trials/", api_views.TrialCustomerListAPIView.as_view(), name="api-fleet-trials"),
    path("trials/<int:pk>/extend/", api_views.TrialExtendAPIView.as_view(), name="api-fleet-trial-extend"),
    path("trials/<int:pk>/convert/", api_views.TrialConvertAPIView.as_view(), name="api-fleet-trial-convert"),
    path("trials/<int:pk>/provision/", api_views.TrialProvisionAPIView.as_view(), name="api-fleet-trial-provision"),
    path("deployments/", api_views.LicensedDeploymentListAPIView.as_view(), name="api-fleet-deployments"),
    path(
        "deployments/<int:pk>/reissue-license/",
        api_views.LicenseReissueAPIView.as_view(),
        name="api-fleet-license-reissue",
    ),
]
