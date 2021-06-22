from django.urls import path, include
from rest_framework import routers
from apps.record.views import RecordViewSet, ApproveViewSet

router = routers.DefaultRouter()
router.register('record', RecordViewSet)
router.register('approve', ApproveViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
