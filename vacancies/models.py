from django.db import models


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

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['text']

    def __str__(self):
        return self.text
