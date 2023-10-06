from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    telegram = models.CharField(unique=True, verbose_name='telegram')

    chat_id = models.PositiveIntegerField(default=0, verbose_name='чат', **NULLABLE)
    update_id = models.PositiveIntegerField(default=0, verbose_name='номер последнего сообщения', **NULLABLE)

    name = models.CharField(verbose_name='имя', max_length=50, **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
