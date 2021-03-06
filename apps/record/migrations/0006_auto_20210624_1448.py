# Generated by Django 3.2.4 on 2021-06-24 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0005_auto_20210623_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approve',
            name='operation',
            field=models.SmallIntegerField(choices=[(0, '借出'), (1, '归还')], verbose_name='操作'),
        ),
        migrations.AlterField(
            model_name='approve',
            name='state',
            field=models.SmallIntegerField(choices=[(0, '未审核'), (1, '审核通过'), (2, '审核拒绝')], default=0, verbose_name='审批状态'),
        ),
    ]
