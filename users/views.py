from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer, UserCreateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for the Users"""
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # def get_permissions(self):
    #     """setting up rights for User """
    #     if self.action == 'create':
    #         self.permission_classes = [AllowAny]
    #     else:
    #         self.permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)
