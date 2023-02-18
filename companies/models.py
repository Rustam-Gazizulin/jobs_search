from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название', null=True)
    logo = models.ImageField(upload_to='logo/', null=True, verbose_name='Логотип')

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name
