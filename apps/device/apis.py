from django.urls import path, include
from rest_framework import routers
from apps.device.views import DeviceViewSet, LocationViewSet

router = routers.DefaultRouter()
router.register('device', DeviceViewSet)
router.register("location", LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
