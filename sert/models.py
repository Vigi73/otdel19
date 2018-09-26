from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class Sert_post(models.Model):
    s_author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    s_title = models.CharField(verbose_name='Заголовок', max_length=200)
    s_text = RichTextField(verbose_name='Контент сообщения')
    s_date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


    class Meta:
        db_table = 'Сертификация'
        ordering = ['-s_date_create']
        verbose_name = "запись объявления"
        verbose_name_plural = "записи объявления"

    def __str__(self):
        return self.s_title
