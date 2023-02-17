from django.db import models


class Vacancy(models.Model):
    text = models.CharField(max_length=100, verbose_name='Описание')
