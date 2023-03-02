from django.core.validators import MinValueValidator
from django.db import models

from users.models import User


class Skill(models.Model):
    name = models.CharField(max_length=20, verbose_name='Навыки')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    STATUS = [
        ('draft', 'Черновик'),
        ('open', 'Окрытая'),
        ('closed', 'Закрытая')
    ]
    slug = models.SlugField(max_length=50, verbose_name='Краткое описание', default='Старая вакансия')
    text = models.CharField(max_length=100, verbose_name='Описание')
    status = models.CharField(max_length=10, choices=STATUS, default='draft', verbose_name='Статус вакансии')
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    skills = models.ManyToManyField(Skill)

    likes = models.IntegerField(default=0)

    min_experience = models.IntegerField(null=True, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.text

    @property
    def username(self):
        return self.user.username if self.user else None
