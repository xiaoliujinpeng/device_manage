from django.urls import path, include
from rest_framework import routers
from apps.micro.views import CarouselViewSet, ManageCarouselViewSet

router = routers.DefaultRouter()
router.register('micro/read', CarouselViewSet)
router.register('micro/manage', ManageCarouselViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
