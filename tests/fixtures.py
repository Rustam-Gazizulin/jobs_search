import pytest


@pytest.fixture
@pytest.mark.django_db
def hr_token(client, django_user_model):
    username = "hr"
    password = "123qwe"

    django_user_model.objects.create_user(
        username=username, password=password, role="hr"
    )

    response = client.post(
        "/user/login/",
        {"username": username, "password": password},
        format='json'
    )

    return response.data["token"]

