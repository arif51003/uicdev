from rest_framework.serializers import ModelSerializer
from apps.accounts.models import User

class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "phone", "password", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def save(self, **kwargs):
        user = User(
            phone=self.validated_data["phone"],
            password=self.validated_data["password"],
            is_active=False,
            is_deleted=False,
        )
        user.save()
        return user


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]