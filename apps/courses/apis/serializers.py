from rest_framework.serializers import ModelSerializer
from apps.courses.models import Category,Tag

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields="__all__"
        read_only_fields = ["id","created_at","updated_at"]
        
class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields="__all__"
        read_only_fields = ["id","created_at","updated_at"]