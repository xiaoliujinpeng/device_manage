from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from apps.device.models import Device, Location
from apps.user.models import Users
from apps.user.serializers import UserInfoSerializer
from apps.record.models import Approve, Record
from apps.device.serializers import DeviceSerializer, DeviceAboutSerializer, LocationSerializer
from util.custom_permission import DevicePermission, LocationPermission
from util.custom_page import PageSet


# Create your views here.


class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated, DevicePermission, ]

    # pagination_class = PageSet
    def create(self, request, *args, **kwargs):
        if Device.objects.filter(serial_number=request.data.get("serial_number")).count() > 0:
            return Response("设备的序列号已存在", 400)
        name = request.data.get("name")
        serial_number = request.data.get("serial_number")
        location_name = request.data.get("location")
        comments = request.data.get("comments")
        classes = request.data.get("classes")
        location = Location.objects.filter(name=location_name).first()
        if location is None:
            return Response("所选位置不存在", status=400)
        device = Device.objects.create(name=name, serial_number=serial_number, location=location, classes=classes,
                                       comments=comments)
        serializer = self.get_serializer(device)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        location = request.data.get("location")
        if location is None:
            return Response("位置不能为空", status=400)
        L = Location.objects.filter(name=location).first()
        if L is None:
            return Response("位置不存在", status=400)
        request.data['location'] = L.id
        response = super().update(request, *args, **kwargs)
        return response

    def list(self, request, *args, **kwargs):
        '''
        根据类别进行分类
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        queryset = self.filter_queryset(self.get_queryset())
        results = dict()
        for i, each in enumerate(queryset):
            classes = each.classes
            serializer = DeviceSerializer(each)
            if classes in results:
                results[classes].append(serializer.data)
            else:
                results[classes] = list()
                results[classes].append(serializer.data)
        return Response(results, status=200)

    @action(detail=False, methods=['post'])
    def apply_borrow(self, request):
        '''
        申请人申请借用
        '''
        device_id = request.data.get("serial_number")
        device = Device.objects.filter(serial_number=device_id).first()
        if device is None:
            return Response("设备不存在", status=400)
        if device.state != 0:
            return Response("此设备目前不可借用", status=201)
        device.state = 1
        try:
            approve = Approve(username=request.user.username, operation=0, device=device)
            device.save()
            approve.save()
        except Exception as e:
            return Response(str(e))
        return Response("申请成功")

    @action(detail=False, methods=['post'])
    def apply_return(self, request):
        '''
        申请人申请归还
        '''
        device_id = request.data.get("serial_number")
        location_id = request.data.get("location_number")
        device = Device.objects.filter(serial_number=device_id).first()
        location = Location.objects.filter(serial_number=location_id).first()
        if location is None:
            Response("位置不存在", status=400)
        if device is None:
            return Response("输入的设备不存在", status=400)
        approve_id = request.data.get("id")
        try:
            old_approve = Approve.objects.get(pk=approve_id)
        except Exception as e:
            return Response("无此审批表", status=400)
        if location != device.location:
            return Response(
                "位置与原来的位置不一致,应前往[位置名称:{} 编号:{}]归还".format(device.location.name, device.location.serial_number),
                status=400)
        if old_approve.show:
            try:
                approve = Approve(username=request.user.username, operation=1, device=device, location=location)
                approve.save()
            except Exception as e:
                return Response(str(e))
        old_approve.show = False
        old_approve.save()
        return Response("申请成功")

    @action(detail=False, methods=['post'])
    def who_use(self, request):
        '''
        获取设备的借用人
        '''
        device_id = request.data.get("serial_number")
        device = Device.objects.filter(serial_number=device_id).first()
        approve = Approve.objects.filter(device=device, operation=0).first()
        user = Users.objects.filter(username=approve.username).first()
        tmp = UserInfoSerializer(user)
        return Response(tmp.data)

    @action(detail=False, methods=['post'])
    def get_all(self, request):
        '''
        根据设备id，返回设备属性及其相关的借出接入记录
        '''
        device_id = request.data.get("serial_number")
        device = Device.objects.filter(serial_number=device_id).first()
        if device is None:
            return Response("输入的设备不存在", status=400)
        records = Record.objects.filter(device=device).all()
        tmp = DeviceAboutSerializer({"device": device, "records": records})
        return Response(tmp.data)


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated, LocationPermission]
    filter_fields = ['serial_number', 'name']

    def create(self, request, *args, **kwargs):
        if Location.objects.filter(serial_number=request.data.get("serial_number")).count() > 0:
            return Response("位置的序列号已存在", 400)
        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=['POST', 'GET'])
    def retrieves(self, request, *args, **kwargs):
        serial_number = request.data.get("serial_number")
        location = Location.objects.filter(serial_number=serial_number).first()
        if location is None:
            return Response("位置不存在", status=400)
        serializer = self.get_serializer(location)
        return Response(serializer.data)
