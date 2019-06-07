from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор', auto_created=True, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    text = RichTextField(verbose_name='Контент сообщения')
    files = models.FileField(verbose_name='Аттач файл', null=True, blank=True, upload_to='static/files/upload_to/')
    date_create = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    class Meta:
        db_table = 'Объявления'
        ordering = ['-date_create']
        verbose_name = "запись объявления"
        verbose_name_plural = "записи объявления"

    def __str__(self):
        return self.title
