from django.db import models
from util.base_model import BaseModel


# Create your models here.

class Carousel(BaseModel):
    # url = models.URLField(max_length=500, null=False, blank=False, verbose_name="url")
    CLASSES_ITEMS = (
        (0, "图片"),
    )
    classes = models.SmallIntegerField(choices=CLASSES_ITEMS, default=0, null=True, blank=True, verbose_name="类型")
    image = models.ImageField(upload_to="micro/%Y/%m", default="micro/default.jpg", blank=True, verbose_name="图片")

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = "轮播图"
