from {{cookiecutter.project_slug}}.ext import api, configuration, database
from {{cookiecutter.project_slug}}.models.{{cookiecutter.main_model_lower}} import {{cookiecutter.main_model}}  # pylint: disable=W0611
from {{cookiecutter.project_slug}}.models.users import User  # pylint: disable=W0611


def create_app(**config):
    """Cria flask app"""
    app = api.create_api_app()
    configuration.init_app(app, **config)
    database.init_app(app)
    return app
