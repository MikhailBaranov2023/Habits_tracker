from users.apps import UsersConfig
from rest_framework import routers
from users.views import UserViewSet
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
urlpatterns = [
                  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              ] + router.urls
