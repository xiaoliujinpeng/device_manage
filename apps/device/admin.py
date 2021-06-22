from django.contrib import admin
from apps.device.models import *
from apps.user.models import *
from apps.record.models import *

# Register your models here.

admin.site.register(Device)
admin.site.register(Record)
admin.site.register(Approve)
admin.site.register(Users)
