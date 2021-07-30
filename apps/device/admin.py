from django.contrib import admin
from apps.device.models import *
from apps.user.models import *
from apps.record.models import *

# Register your models here.
admin.site.site_header = 'CUBOT物资管理'
admin.site.site_title = 'CUBOT物资管理'
admin.site.index_title = 'CUBOT物资管理'

admin.site.register(Device)
admin.site.register(Record)
admin.site.register(Approve)
admin.site.register(Users)
admin.site.register(Location)
