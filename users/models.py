from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    MALE = 'm'
    FEMALE = 'f'
    SEX = [
        (MALE, 'Муж'),
        (FEMALE, 'Жен')
    ]

    HR = 'hr'
    STAFF = 'staff'
    UNKNOWN = 'unknown'
    ROLE = [
        (HR, 'Кадровик'),
        (STAFF, 'Сотрудник'),
        (UNKNOWN, 'Посетитель')
    ]

    sex = models.CharField(max_length=1, choices=SEX, default=MALE)
    role = models.CharField(max_length=8, choices=ROLE, default=UNKNOWN)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
