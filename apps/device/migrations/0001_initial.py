# Generated by Django 3.2.4 on 2021-06-22 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=255, verbose_name='设备名称')),
                ('location', models.CharField(max_length=255, verbose_name='设备位置')),
                ('classes', models.CharField(max_length=255, verbose_name='设备类型')),
                ('state', models.SmallIntegerField(choices=[(0, '未借出'), (1, '借用审核中'), (2, '已借出')], verbose_name='设备状态')),
            ],
            options={
                'verbose_name': '设备表',
                'verbose_name_plural': '设备表',
            },
        ),
    ]
