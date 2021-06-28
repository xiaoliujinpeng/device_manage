from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAdminUser
from apps.micro.serializers import CarouselSerializer
from apps.micro.models import Carousel


# Create your views here.

class CarouselViewSet(ReadOnlyModelViewSet):
    serializer_class = CarouselSerializer
    queryset = Carousel.objects.all()


class ManageCarouselViewSet(ModelViewSet):
    serializer_class = CarouselSerializer
    queryset = Carousel.objects.all()
    permission_classes = [IsAdminUser, ]


