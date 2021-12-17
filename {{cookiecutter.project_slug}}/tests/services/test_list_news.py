from unittest.mock import ANY
from {{cookiecutter.project_slug}}.models.news import News
from {{cookiecutter.project_slug}}.services import news as news_services


def test_should_list_tabnews(db_session, user_mock):

    # Given a Tabnews
    the_news = News(
        title="The very first news",
        description="This is the first news...",
        author_id=user_mock.id,
    )
    db_session.add(the_news)
    db_session.commit()

    # When we list tabnews
    my_news = news_services.list_news()

    # Then
    assert my_news == [
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
            "description": "This is the first news...",
            "id": ANY,
            "title": "The very first news",
        },
    ]
