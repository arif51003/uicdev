from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,CreateAPIView

from apps.courses.apis.serializers import CategorySerializer,TagSerializer
from apps.courses.models import Category,Tag

class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryRetriveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    
class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagCreateAPIView(CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
class TagRetriveAPIView(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
class TagListAPIView(ListAPIView):
    queryset = Tag.objects.all().order_by("name")
    serializer_class = TagSerializer
    
class TagUpdateAPIView(UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
class TagDeleteAPIView(DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
