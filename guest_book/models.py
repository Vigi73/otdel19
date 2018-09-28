from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class Post_guest(models.Model):
    g_author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    g_title = models.CharField(verbose_name='Заголовок', max_length=250)
    g_text = RichTextField(verbose_name='Контент сообщения')
    g_date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
       ordering = ['-g_date_create']

    def __str__(self):
        return self.g_title
