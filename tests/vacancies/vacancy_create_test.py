from datetime import date

import pytest


@pytest.mark.django_db
def test_create_vacancy(client, hr_token):
    expected_response = {
        "id": 1,
        "text": "test1",
        "slug": "test1",
        "status": "draft",
        "created": date.today().strftime("%Y-%m-%d"),
        "skills": [],
        "likes": 0,
        "min_experience": None,
        "date_published": None,
        "user": None
    }

    data = {
        "slug": "test1",
        "text": "test1",
        "status": "draft"
    }

    response = client.post(
        "/vacancy/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Token " + hr_token
    )

    assert response.status_code == 201
    assert response.data == expected_response
