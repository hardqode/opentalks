# from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from core.models import Country, User


class Event(models.Model):
    user = models.ForeignKey(User, verbose_name='Создатель', related_name='events', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название события')
    short_description = models.CharField(max_length=1000, verbose_name='Краткое описание', blank=True)
    full_description = models.TextField(verbose_name='Полное описание')
    start_at = models.DateTimeField(verbose_name='Дата начала')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    url = models.URLField(verbose_name='Ссылка на мероприятие')
    url_id = models.CharField(max_length=255, verbose_name='ID мероприятия', blank=True)
    url_password = models.CharField(max_length=255, verbose_name='Пароль мероприятия', blank=True)
    max_people = models.PositiveSmallIntegerField(default=10, verbose_name='Максимальное кол-во участников')
    country = models.ForeignKey(Country, related_name='country_events', verbose_name='Страна', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name='Активно?')
    views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    def get_absolute_url(self):
        return reverse('event:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-views', 'start_at')


class EventParticipant(models.Model):
    event = models.ForeignKey(Event, verbose_name='Событие', related_name='participants', on_delete=models.NOT_PROVIDED)
    user = models.ForeignKey(User, verbose_name='Участник', related_name='in_events', on_delete=models.NOT_PROVIDED)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('event:detail', kwargs={'pk': self.event.pk})