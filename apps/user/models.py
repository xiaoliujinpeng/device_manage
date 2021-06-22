from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Users(AbstractUser):
    id = models.CharField(max_length=15, null=False, blank=False, primary_key=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = "用户表"
