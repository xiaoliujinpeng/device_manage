from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from apps.record.models import Record, Approve
from apps.record.serializers import RecordSerializer, ApproveSerializer
from util.custom_page import PageSet


# Create your views here.


class RecordViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    pagination_class = PageSet


class ApproveViewSet(ModelViewSet):
    queryset = Approve.objects.all()
    serializer_class = ApproveSerializer

    @action(detail=False,methods=['post'])
    def