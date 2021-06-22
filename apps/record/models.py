from django.db import models
from util.base_model import BaseModel


# Create your models here.

class Record(BaseModel):
    OPERATION_ITEMS = (
        (0, "借出"),
        (1, "归还"),
    )
    username = models.CharField(max_length=255, null=False, blank=False, verbose_name="借用人")
    operation = models.SmallIntegerField(choices=OPERATION_ITEMS, null=False, blank=False, verbose_name="操作")
    device = models.CharField(max_length=255, null=False, blank=False, verbose_name="设备")
    approver = models.CharField(max_length=255, null=False, blank=False, verbose_name="审批人")

    def __str__(self):
        return "记录" + str(self.id)

    class Meta:
        verbose_name = "记录表"
        verbose_name_plural = "记录表"


class Approve(BaseModel):
    STATE_ITEMS = (
        (0, "申请借用"),
        (1, "申请归还"),
    )
    username = models.CharField(max_length=255, null=False, blank=False, verbose_name="借用人")
    operation = models.SmallIntegerField(choices=STATE_ITEMS, null=False, blank=False, verbose_name="操作")
    state = models.BooleanField(verbose_name="审批状态")

    def __str__(self):
        tmp = {0: "申请借用", 1: "申请归还"}
        return self.username + "-" + tmp.get(self.operation)

    class Meta:
        verbose_name = "审批表"
        verbose_name_plural = "审批表"
