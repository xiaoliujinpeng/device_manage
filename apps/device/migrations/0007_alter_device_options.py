# Generated by Django 3.2.4 on 2021-12-19 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0006_alter_device_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'ordering': ['serial_number'], 'verbose_name': '设备表', 'verbose_name_plural': '设备表'},
        ),
    ]
