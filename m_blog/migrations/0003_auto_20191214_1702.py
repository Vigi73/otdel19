# Generated by Django 2.1.1 on 2019-12-14 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m_blog', '0002_auto_20181002_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_create',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания'),
        ),
    ]
