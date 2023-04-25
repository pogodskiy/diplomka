from django.db import models
from user.models import UserModel


class Post(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    post_body = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(UserModel, on_delete=models.PROTECT, verbose_name='Автор')
    comments = models.CharField(max_length=200, )
    date = models.TimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title
