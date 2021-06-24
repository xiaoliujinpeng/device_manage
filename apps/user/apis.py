from django.urls import path, include
from rest_framework import routers
from apps.user.views import UserViewSet, UserRegisterViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('register', UserRegisterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
