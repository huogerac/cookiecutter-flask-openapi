from unittest.mock import ANY
from {{cookiecutter.project_slug}}.models.{{cookiecutter.main_model_lower}} import {{cookiecutter.main_model}}
from {{cookiecutter.project_slug}}.services import {{cookiecutter.main_model_lower}} as {{cookiecutter.main_model_lower}}_services


def test_should_list_tab{{cookiecutter.main_model_lower}}(db_session, user_mock):

    # Given a Tab{{cookiecutter.main_model_lower}}
    the_{{cookiecutter.main_model_lower}} = {{cookiecutter.main_model}}(
        title="The very first {{cookiecutter.main_model_lower}}",
        description="This is the first {{cookiecutter.main_model_lower}}...",
        author_id=user_mock.id,
    )
    db_session.add(the_{{cookiecutter.main_model_lower}})
    db_session.commit()

    # When we list tab{{cookiecutter.main_model_lower}}
    my_{{cookiecutter.main_model_lower}} = {{cookiecutter.main_model_lower}}_services.list_{{cookiecutter.main_model_lower}}()

    # Then
    assert my_{{cookiecutter.main_model_lower}} == [
        {
            "author": {
                "avatar": user_mock.avatar,
                "created_at": ANY,
                "email": user_mock.email,
                "id": user_mock.id,
                "name": user_mock.name,
                "username": "jd",
            },
            "created_at": ANY,
            "description": "This is the first {{cookiecutter.main_model_lower}}...",
            "id": ANY,
            "title": "The very first {{cookiecutter.main_model_lower}}",
        },
    ]
