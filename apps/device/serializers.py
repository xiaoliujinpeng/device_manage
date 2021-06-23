from apps.device.models import Device
from rest_framework import serializers
from apps.record.serializers import RecordSerializer


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"


class DeviceAboutSerializer(serializers.Serializer):
    records = RecordSerializer(many=True)
    device = DeviceSerializer()

    class Meta:
        fields = "__all__"
