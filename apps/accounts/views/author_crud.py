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
from apps.accounts.models import Author
from apps.accounts.serializers import AuthorSerializer

class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all().order_by("first_name")
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    
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