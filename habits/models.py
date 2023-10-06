from django.db import models
from django.conf import settings

NULLABLE = {
    'null': True,
    'blank': True
}


class Habit(models.Model):
    location = models.CharField(max_length=200, verbose_name='место выполнения', **NULLABLE)
    time = models.TimeField(verbose_name='время выполнения', **NULLABLE)
    action = models.CharField(max_length=500, verbose_name='действие')
    good_habit = models.BooleanField(default=False, verbose_name='признак приятной привыки')
    habit_link = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='связвнная привычка', **NULLABLE)
    periodicity = models.SmallIntegerField(verbose_name='периодичность')
    award = models.CharField(max_length=100, verbose_name='награда', **NULLABLE)
    limit_time = models.SmallIntegerField(verbose_name='продолжительность')
    public = models.BooleanField(default=False, verbose_name='признак публичность')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='пользователь', **NULLABLE)

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
