from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response


from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    GenericAPIView
)
from apps.accounts.models import Education
from apps.accounts.serializers import EducationSerializer

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
        