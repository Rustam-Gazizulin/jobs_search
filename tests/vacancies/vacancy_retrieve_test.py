from datetime import date

import pytest


@pytest.mark.django_db
def test_retrieve_vacancy(client, vacancy, hr_token):
    expected_response = {
        "id": vacancy.pk,
        "text": "test text",
        "slug": "test",
        "status": "draft",
        "created": date.today().strftime("%Y-%m-%d"),
        "skills": [],
        "likes": 0,
        "min_experience": None,
        "date_published": None,
        "username": "test",
    }

    response = client.get(
        f'/vacancy/{vacancy.pk}/',
        HTTP_AUTHORIZATION="Token " + hr_token
    )

    assert response.status_code == 200
    assert response.data == expected_response
