from apps.device.models import Device, Location
from rest_framework import serializers
from apps.record.serializers import RecordSerializer


class DeviceSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        result = super().to_representation(instance)
        location_id = result['location']
        if location_id is None:
            pass
        else:
            location = Location.objects.get(pk=location_id)
            result['location'] = location.name
        return result

    class Meta:
        model = Device
        fields = "__all__"


class DeviceAboutSerializer(serializers.Serializer):
    records = RecordSerializer(many=True)
    device = DeviceSerializer()

    class Meta:
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["name", "serial_number", "id"]
