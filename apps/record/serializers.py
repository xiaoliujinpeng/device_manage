from rest_framework import serializers
from apps.record.models import Record, Approve
from apps.user.models import Users


class RecordSerializer(serializers.ModelSerializer):
    # name = serializers.CharField()

    def to_representation(self, instance):
        result = super().to_representation(instance)
        obj = Users.objects.filter(username=instance.username).first()
        result['name'] = obj.name
        return result

    class Meta:
        model = Record
        fields = ['created_time', 'username', 'operation', 'approver']


class ApproveSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        result = super().to_representation(instance)
        obj = Users.objects.filter(username=instance.username).first()
        result['name'] = obj.name
        result['deviceName'] = instance.device.name
        result['deviceId'] = instance.device.serial_number
        if result['location'] is None:
            pass
        else:
            result['location'] = instance.location.name
        return result

    class Meta:
        model = Approve
        fields = ['username', 'state', 'created_time', 'operation', 'show', 'modified_time',
                  'id', 'location']
