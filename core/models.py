from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    instagram = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    about = models.CharField(max_length=1000, blank=True)


# Create your models here.
class Country(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название страны(на английском)')
    slug = models.SlugField()
    is_active = models.BooleanField(default=True, verbose_name='Открыта для выбора?')
    is_worldwide = models.BooleanField(default=False, verbose_name='Для всего мира?')

    def __str__(self):
        return self.title

