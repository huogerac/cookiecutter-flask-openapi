from sqlalchemy.exc import DataError

from {{cookiecutter.project_slug}}.ext.database import db
from {{cookiecutter.project_slug}}.models.{{cookiecutter.main_model_lower}} import {{cookiecutter.main_model}}


def list_{{cookiecutter.main_model_lower}}():
    """List {{cookiecutter.main_model}}"""
    {{cookiecutter.main_model_lower}}_list = {{cookiecutter.main_model}}.query.order_by({{cookiecutter.main_model}}.id.desc()).all()
    return [t.to_dict() for t in {{cookiecutter.main_model_lower}}_list]


def create_{{cookiecutter.main_model_lower}}(title, description=None, author_id=None):
    """Create {{cookiecutter.main_model}}"""
    # pylint: disable=W0511,W0707
    if not title:
        raise ValueError("Invalid title")

    # TODO: author deve ser obrigatorio

    try:
        {{cookiecutter.main_model_lower}}_add = {{cookiecutter.main_model}}(title=title, description=description, author_id=author_id)
        db.session.add({{cookiecutter.main_model_lower}}_add)
        db.session.commit()
    except DataError:
        raise ValueError("Title is too long")

    return {{cookiecutter.main_model_lower}}_add.to_dict()
