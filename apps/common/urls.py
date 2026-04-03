from django.urls import path

from apps.common.views import (
    CountryListCreateAPIView,
    CountryRetrieveUpdateDestroyAPIView,
    MediaCreateAPIView,
    MediaDeleteAPIView,
    MediaListAPIView,
    MediaRetrieveAPIView,
    MediaUpdateAPIView,
    RegionCreateAPIView,
    RegionDeleteAPIView,
    RegionListAPIView,
    RegionRetrieveAPIView,
    RegionUpdateAPIView,
)

urlpatterns = [
    path("countries/", CountryListCreateAPIView.as_view(), name="country-list"),
    path(
        "countries/<int:pk>/",
        CountryRetrieveUpdateDestroyAPIView.as_view(),
        name="country-detail",
    ),
    path("regions/list/", RegionListAPIView.as_view(), name="region-list"),
    path("region/create/", RegionCreateAPIView.as_view(), name="region-create"),
    path("region/delete/<int:pk>", RegionDeleteAPIView.as_view(), name="region-delete"),
    path("region/update/<int:pk>", RegionUpdateAPIView.as_view(), name="region-update"),
    path("region/<int:pk>", RegionRetrieveAPIView.as_view(), name="region-single"),
    path("media/", MediaListAPIView.as_view(), name="media-list"),
    path("media/create/", MediaCreateAPIView.as_view(), name="media-create"),
    path("media/<int:pk>/", MediaRetrieveAPIView.as_view(), name="media-detail"),
    path("media/update/<int:pk>/", MediaUpdateAPIView.as_view(), name="media-update"),
    path("media/delete/<int:pk>/", MediaDeleteAPIView.as_view(), name="media-delete"),
]
