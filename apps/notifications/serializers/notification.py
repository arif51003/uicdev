from rest_framework.serializers import ModelSerializer

from apps.notifications.models import Notification


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]