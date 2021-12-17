import pytest
from unittest.mock import ANY

from {{cookiecutter.project_slug}}.services import {{cookiecutter.main_model_lower}} as {{cookiecutter.main_model_lower}}_services


def test_should_not_create_{{cookiecutter.main_model_lower}}_without_title():

    with pytest.raises(ValueError) as error:
        {{cookiecutter.main_model_lower}}_services.create_{{cookiecutter.main_model_lower}}(title=None)

    assert str(error.value) == "Invalid title"


def test_should_add_{{cookiecutter.main_model_lower}}_using_just_title():
    new_item = {{cookiecutter.main_model_lower}}_services.create_{{cookiecutter.main_model_lower}}(title="Simple Title")

    assert new_item["id"] is not None
    assert new_item["created_at"] is not None
    assert new_item["title"] == "Simple Title"

    # TODO: Logo nao devemos aceitar criar {{cookiecutter.main_model_lower}} sem um Author
    assert new_item["author"] is None


def test_should_create_a_complete_{{cookiecutter.main_model_lower}}(user_mock):
    new_item = {{cookiecutter.main_model_lower}}_services.create_{{cookiecutter.main_model_lower}}(
        title="The very first {{cookiecutter.main_model_lower}}",
        description="This is the first {{cookiecutter.main_model_lower}}...",
        author_id=user_mock.id,
    )

    assert new_item == {
        "author": {
            "avatar": user_mock.avatar,
            "created_at": ANY,
            "email": user_mock.email,
            "id": user_mock.id,
            "name": user_mock.name,
            "username": user_mock.username,
        },
        "created_at": ANY,
        "description": "This is the first {{cookiecutter.main_model_lower}}...",
        "id": ANY,
        "title": "The very first {{cookiecutter.main_model_lower}}",
    }


def test_should_not_accept_long_titles(db_session):
    # Given an long title
    long_title = "L" * 130

    # When the title is invalid
    with pytest.raises(ValueError) as error:
        {{cookiecutter.main_model_lower}}_services.create_{{cookiecutter.main_model_lower}}(title=long_title)

    # Then
    assert str(error.value) == "Title is too long"
