from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from apps.device.models import Device
from apps.record.models import Approve, Record
from apps.device.serializers import DeviceSerializer
from util.custom_page import PageSet


# Create your views here.


class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    pagination_class = PageSet

    @action(detail=False, methods=['get'])
    def apply_borrow(self, request):
        device_id = request.data.get("id")
        device = Device.objects.get(pk=device_id)
        if device.state != 0:
            return Response("此设备目前不可借用", status=201)
        device.state = 1
        device.save()
        approve = Approve(username=request.user.username, state=0)
        approve.save()
        return Response("申请成功")

    @action(detail=False, methods=['post'])
    def apply_return(self, request):
        device_id = request.data.get("id")
        device = Device.objects.get(pk=device_id)
        device.state = 0
        device.save()
        approve = Approve(username=request.user.username, state=1)
        approve.save()
        return Response("申请成功")
