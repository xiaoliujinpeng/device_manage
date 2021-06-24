from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from apps.record.models import Record, Approve
from apps.record.serializers import RecordSerializer, ApproveSerializer
from util.custom_page import PageSet
from util.custom_permission import ApprovePermission


# Create your views here.


class RecordViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [ApprovePermission, ]
    filter_fields = ['username', 'operation', 'device']


class ApproveViewSet(ModelViewSet):
    queryset = Approve.objects.all()
    serializer_class = ApproveSerializer
    permission_classes = [ApprovePermission, ]
    filter_fields = ['state', 'operation', 'username']

    @action(detail=False, methods=['post'])
    def agree(self, request):
        '''
        管理员同意审批
        :param request:
        :return:
        '''
        admin = request.user
        if not admin.is_superuser:
            return Response("不可操作")
        approve_id = request.data.get("id")
        approve = Approve.objects.get(pk=approve_id)
        approve.state = True
        device = approve.device
        if approve.operation == 0:
            device.state = 2
        else:
            device.state = 0
        record = Record(username=approve.username, operation=approve.operation, device=device.name,
                        approver=request.user.username)
        approve.save()
        device.save()
        record.save()
        return Response("操作成功")

    @action(detail=False, methods=['post'])
    def reject(self, request):
        '''
        管理员拒绝审批
        :param request:
        :return:
        '''
        admin = request.user
        if not admin.is_superuser:
            return Response("不可操作")
        approve_id = request.data.get("id")
        approve = Approve.objects.get(pk=approve_id)
        approve.state = True
        device = approve.device
        if approve.operation == 0 and device.state == 1:
            device.state = 0
            device.save()
        approve.save()
        return Response("操作成功")
