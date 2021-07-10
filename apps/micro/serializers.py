from rest_framework import serializers
from apps.micro.models import Carousel
from django.conf import settings


class CarouselSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        classes_items = ['image','video']
        result = super().to_representation(instance)
        result['url'] = settings.HOST_URL + instance.image.url
        result['classes'] = classes_items[result['classes']]
        return result

    class Meta:
        model = Carousel
        fields = ['id', 'classes']
