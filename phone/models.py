from django.db import models

# Create your models here.
class Phone(models.Model):
    number = models.IntegerField(verbose_name='Номер', unique=True)
    fio = models.CharField(max_length=200, verbose_name='ФИО')
    address = models.TextField(verbose_name='Адрес', blank=True)
    cotegory = models.CharField(max_length=100, verbose_name='Категория', blank=True)
    mobail_pthone = models.IntegerField(verbose_name='Сотовый',  unique=True)
    email = models.EmailField(max_length=70, verbose_name='Email', blank=True)
    comment = models.TextField(verbose_name='Комментрий', blank=True)
    photo = models.ImageField(verbose_name='Фото', null=True, blank=True, upload_to='static/img/upload_to/')


    def __str__(self):
        return self.fio
