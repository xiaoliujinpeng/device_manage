from django.urls import path, include
from rest_framework import routers
from apps.device.views import DeviceViewSet

router = routers.DefaultRouter()
router.register('device', DeviceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
