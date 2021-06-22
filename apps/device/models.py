from django.db import models
from util.base_model import BaseModel


# Create your models here.

class Device(BaseModel):
    STATE_ITEMS = (
        (0, "未借出"),
        (1, "借用审核中"),
        (2, "已借出")
    )
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="设备名称")
    location = models.CharField(max_length=255, null=False, blank=False, verbose_name="设备位置")
    classes = models.CharField(max_length=255, null=False, blank=False, verbose_name="设备类型")
    state = models.SmallIntegerField(choices=STATE_ITEMS, null=False, blank=False, verbose_name="设备状态")
    image = models.CharField(max_length=500, blank=False, verbose_name="设备照片")

    def __str__(self):
        return self.name + "-" + str(self.id)

    class Meta:
        verbose_name = "设备表"
        verbose_name_plural = "设备表"
