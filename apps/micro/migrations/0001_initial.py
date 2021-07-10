# Generated by Django 3.2.4 on 2021-06-26 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('classes', models.CharField(max_length=50, verbose_name='类型')),
                ('image', models.ImageField(blank=True, default='micro/default.jpg', upload_to='micro/%Y/%m', verbose_name='图片')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
    ]