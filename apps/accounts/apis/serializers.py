from rest_framework.serializers import ModelSerializer

from apps.accounts.models import Education,Author

class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"
        read_only_fields = ["id","created_at","updated_at"]
        
class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
        read_only_fields = ["id","created_at","updated_at"]
