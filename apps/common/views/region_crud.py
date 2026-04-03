from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from apps.common.models import Region
from apps.common.serializers import RegionSerializer


class RegionCreateAPIView(CreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionRetrieveAPIView(RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all().order_by("name")
    serializer_class = RegionSerializer


class RegionUpdateAPIView(UpdateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionDeleteAPIView(DestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer