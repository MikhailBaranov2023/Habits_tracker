from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer, UserCreateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class UserCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteApiView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
