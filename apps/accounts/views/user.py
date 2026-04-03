from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response


from rest_framework.generics import (
    GenericAPIView,
    RetrieveAPIView
)
from apps.accounts.models import User
from apps.accounts.serializers import UserProfileSerializer,UserRegisterSerializer


class UserRegisterAPIView(GenericAPIView):
    queryset = User.objects.filter(is_active=True, is_deleted=False)
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if User.objects.filter(phone=serializer.validated_data["phone"]).exists():
            raise ValidationError("User already exists")

        user = serializer.save()
        return Response(UserRegisterSerializer(user).data)


class UserProfileAPIView(RetrieveAPIView):
    queryset = User.objects.filter(is_active=True, is_deleted=False).select_related("avatar")
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get_object(self):
        return self.request.user