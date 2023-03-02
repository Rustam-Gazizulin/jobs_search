def test_root_not_founf(client):
    response = client.get('/')

    assert response.status_code == 404
