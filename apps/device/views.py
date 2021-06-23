from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from apps.device.models import Device
from apps.user.models import Users
from apps.user.serializers import UserInfoSerializer
from apps.record.models import Approve, Record
from apps.device.serializers import DeviceSerializer, DeviceAboutSerializer
from util.custom_page import PageSet


# Create your views here.


class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    pagination_class = PageSet

    @action(detail=False, methods=['post'])
    def apply_borrow(self, request):
        '''
        申请人申请借用
        '''
        device_id = request.data.get("id")
        device = Device.objects.get(pk=device_id)
        if device.state != 0:
            return Response("此设备目前不可借用", status=201)
        device.state = 1
        approve = Approve(username=request.user.username, operation=0, device=device)
        device.save()
        approve.save()
        return Response("申请成功")

    @action(detail=False, methods=['post'])
    def apply_return(self, request):
        '''
        申请人申请归还
        '''
        device_id = request.data.get("id")
        device = Device.objects.get(pk=device_id)
        approve = Approve(username=request.user.username, operation=1, device=device)
        approve.save()
        return Response("申请成功")

    @action(detail=False, methods=['post'])
    def who_use(self, request):
        '''
        获取设备的借用人
        '''
        device_id = request.data.get("id")
        device = Device.objects.get(pk=device_id)
        approve = Approve.objects.filter(device=device.name, operation=0).first()
        user = Users.objects.filter(username=approve.username).first()
        tmp = UserInfoSerializer(user)
        return Response(tmp.data)

    @action(detail=False, methods=['post'])
    def get_all(self, request):
        '''
        根据设备id，返回设备属性及其相关的借出接入记录
        '''
        device_id = request.data.get("id")
        device = Device.objects.get(pk=device_id)
        records = Record.objects.filter(device=device.name).all
        tmp = DeviceAboutSerializer({"device": device, "records": records})
        return Response(tmp.data)
