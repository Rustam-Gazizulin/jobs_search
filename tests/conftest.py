from pytest_factoryboy import register

from tests.factories import VacancyFactory, UserFactory

pytest_plugins = "tests.fixtures"


register(VacancyFactory)
register(UserFactory)