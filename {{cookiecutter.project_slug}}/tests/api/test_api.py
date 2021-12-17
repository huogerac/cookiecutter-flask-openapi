def test_should_return_not_found(client):

    response = client.get("/api/invalid/url")

    assert response.status_code == 404


def test_should_get_the_list_{{cookiecutter.main_model_lower}}(client):

    response = client.get(
        "/api/{{cookiecutter.main_model_lower}}",
        headers={"content-type": "application/json"},
    )

    assert response.status_code == 200
