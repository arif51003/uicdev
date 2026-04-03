from rest_framework.serializers import ModelSerializer

from apps.common.models import Region


class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]