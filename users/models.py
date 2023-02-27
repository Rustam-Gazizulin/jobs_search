from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    MALE = 'm'
    FEMALE = 'f'
    SEX = [
        (MALE, 'Муж'),
        (FEMALE, 'Жен')
    ]
    sex = models.CharField(max_length=1, choices=SEX, default=MALE)
