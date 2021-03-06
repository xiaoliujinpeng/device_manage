from django.db import models
from util.base_model import BaseModel


# Create your models here.

class Device(BaseModel):
    """
        Stores a single blog entry, related to :model:`blog.Blog` and
        :model:`auth.User`.
        """
    STATE_ITEMS = (
        (0, "未借出"),
        (1, "借用审核中"),
        (2, "已借出")
    )
    serial_number = models.CharField(max_length=255, null=False, unique=True, blank=False, verbose_name="设备编号")
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="设备名称")
    location = models.ForeignKey("Location", on_delete=models.SET_NULL, null=True, verbose_name="设备位置")
    classes = models.CharField(max_length=255, null=False, blank=False, verbose_name="设备类型")
    comments = models.CharField(max_length=500, null=True, blank=True, verbose_name="备注")
    state = models.SmallIntegerField(choices=STATE_ITEMS, null=False, default=0, blank=False, verbose_name="设备状态")

    def __str__(self):
        return self.name + "-" + str(self.id)

    class Meta:
        verbose_name = "设备表"
        verbose_name_plural = "设备表"
        ordering = ['serial_number']


class Location(BaseModel):
    serial_number = models.CharField(max_length=255, null=False, unique=True, blank=False, verbose_name="位置编号")
    name = models.CharField(max_length=55, null=False, blank=False, verbose_name="位置")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "位置表"
        verbose_name_plural = "位置表"
