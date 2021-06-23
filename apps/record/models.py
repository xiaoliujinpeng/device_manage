from django.db import models
from util.base_model import BaseModel
from apps.device.models import Device

# Create your models here.
OPERATION_ITEMS = (
    (0, "借出"),
    (1, "归还"),
)


class Record(BaseModel):
    username = models.CharField(max_length=255, null=False, blank=False, verbose_name="借用人")
    operation = models.SmallIntegerField(choices=OPERATION_ITEMS, null=False, blank=False, verbose_name="操作")
    device = models.CharField(max_length=255, null=False, blank=False, verbose_name="设备")
    approver = models.CharField(max_length=255, null=False, blank=False, verbose_name="审批人")

    def __str__(self):
        return "记录" + str(self.id)

    class Meta:
        verbose_name = "记录表"
        verbose_name_plural = "记录表"
        ordering = ['created_time']


class Approve(BaseModel):
    STATE_ITEMS = (
        (0, "申请借用"),
        (1, "申请归还"),
    )
    username = models.CharField(max_length=255, null=False, blank=False, verbose_name="借用人")
    operation = models.SmallIntegerField(choices=STATE_ITEMS, null=False, blank=False, verbose_name="操作")
    device = models.ForeignKey(Device, null=True, on_delete=models.SET_NULL)
    deviceId = models.CharField(max_length=255, null=False, blank=False, verbose_name="设备序列号")
    deviceName = models.CharField(max_length=255, null=False, blank=False, verbose_name="设备名称")
    state = models.BooleanField(default=False, verbose_name="审批状态")

    def __str__(self):
        tmp = {0: "申请借用", 1: "申请归还"}
        return self.username + "-" + tmp.get(self.operation)

    class Meta:
        verbose_name = "审批表"
        verbose_name_plural = "审批表"
        ordering = ['created_time']
