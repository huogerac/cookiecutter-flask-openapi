from sqlalchemy.exc import DataError

from {{cookiecutter.project_slug}}.ext.database import db
from {{cookiecutter.project_slug}}.models.news import News


def list_news():
    """Retorna lista de notícias"""
    news_list = News.query.order_by(News.id.desc()).all()
    return [t.to_dict() for t in news_list]


def create_news(title, description=None, author_id=None):
    """Cria uma notícia"""
    # pylint: disable=W0511,W0707
    if not title:
        raise ValueError("Invalid title")

    # TODO: author deve ser obrigatorio

    try:
        news_add = News(title=title, description=description, author_id=author_id)
        db.session.add(news_add)
        db.session.commit()
    except DataError:
        raise ValueError("Title is too long")

    return news_add.to_dict()
