from rest_framework.serializers import ModelSerializer

from apps.interactions.models import LessonAnswer


class LessonAnswerSerializer(ModelSerializer):
    class Meta:
        model = LessonAnswer
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]