from rest_framework import serializers
from apps.record.models import Record, Approve


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = "__all__"


class ApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approve
        fields = "__all__"

