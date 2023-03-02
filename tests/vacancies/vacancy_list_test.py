from datetime import date

import pytest

from vacancies.models import Vacancy


@pytest.mark.django_db
def test_vacancy_list(client):
    vacancy = Vacancy.objects.create(
        slug="test1",
        text="test1"
    )
    expected_response = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [{
            "id": vacancy.pk,
            "text": "test1",
            "slug": "test1",
            "status": "draft",
            "created": date.today().strftime("%Y-%m-%d"),
            "username": None,
            "skills": []
        }]
    }

    response = client.get("/vacancy/")

    assert response.status_code == 200
    assert response.data == expected_response
