from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Users(AbstractUser):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="用户姓名")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = "用户表"
