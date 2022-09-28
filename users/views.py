from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class CustomUserViews(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data["password"])
            user.save()
            return Response({"message": "User Created"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = request.data["email"]
            password = request.data["password"]
            user = authenticate(email=email, password=password)
            if user:
                token = RefreshToken.for_user(user)
                data = ReadUserSerializer(user).data
                return Response(
                    {
                        "refresh_token": str(token),
                        "access_token": str(token.access_token),
                        "user": data,
                    },
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"message": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
