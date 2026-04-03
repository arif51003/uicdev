from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from apps.common.models import Media
from apps.common.serializers import MediaSerializer


class MediaCreateAPIView(CreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class MediaRetrieveAPIView(RetrieveAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class MediaListAPIView(ListAPIView):
    queryset = Media.objects.all().order_by("-created_at")
    serializer_class = MediaSerializer


class MediaUpdateAPIView(UpdateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class MediaDeleteAPIView(DestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer