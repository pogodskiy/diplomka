from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=20,verbose_name='Имя')
    second_name = models.CharField(max_length=20, verbose_name='Фамилия')
    username = models.CharField(max_length=20, unique=True, verbose_name='Ник')
    email = models.EmailField(unique=True, verbose_name='@mail')
    password = models.CharField(max_length=15, verbose_name='Пароль')
    customer = models.BooleanField(default=False)






