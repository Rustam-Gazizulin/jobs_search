import factory.django

from users.models import User
from vacancies.models import Vacancy


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = '123qwe'


class VacancyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vacancy

    slug = 'test'
    text = 'test text'
    user = factory.SubFactory(UserFactory)
