from django.db import models
from django.contrib.auth.models import AbstractUser
from util.base_model import BaseModel


# Create your models here.

class Users(AbstractUser):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="用户姓名")

    def __str__(self):
        return self.username + '-' + self.name

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = "用户表"


class UserRegister(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="用户姓名")
    username = models.CharField(max_length=255, null=False, blank=False, verbose_name="学号")
    password = models.CharField(max_length=255, null=False, blank=False, verbose_name="密码")

    def __str__(self):
        return self.username + '-' + self.name

    class Meta:
        verbose_name = "用户注册表"
        verbose_name_plural = "用户注册表"
