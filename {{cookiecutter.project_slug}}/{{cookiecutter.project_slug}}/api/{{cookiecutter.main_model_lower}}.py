from flask import jsonify

from {{cookiecutter.project_slug}}.services import {{cookiecutter.main_model_lower}} as {{cookiecutter.main_model_lower}}_services


def list_{{cookiecutter.main_model_lower}}():
    """API to list {{cookiecutter.main_model}}"""
    return jsonify({"result": {{cookiecutter.main_model_lower}}_services.list_{{cookiecutter.main_model_lower}}()})


def create_{{cookiecutter.main_model_lower}}(body):
    """API to create {{cookiecutter.main_model}}"""
    new_data = {{cookiecutter.main_model_lower}}_services.create_{{cookiecutter.main_model_lower}}(body["title"], body.get("description"))
    return jsonify(new_data), 201
