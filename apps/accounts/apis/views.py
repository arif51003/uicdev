from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView
)
from apps.accounts.models import Education,Author
from apps.accounts.apis.serializers import EducationSerializer,AuthorSerializer

class EducationCreateAPIView(CreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    
class EducationRetriveAPIView(RetrieveAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    
class EducationListAPIView(ListAPIView):
    queryset = Education.objects.all().order_by("name")
    serializer_class = EducationSerializer
    
class EducationUpdateAPIView(UpdateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    
class EducationDeleteAPIView(DestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    
    def perform_destroy(self, instance):
        instance.is_active=False
        instance.save()
        
        
class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all().order_by("first_name")
    serializer_class = AuthorSerializer
    
class AuthorRetriveAPIView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class AuthorUpdateAPIView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class AuthorDeleteAPIView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    
class AuthorCreateAPIView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer