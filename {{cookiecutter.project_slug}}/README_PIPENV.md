# Cookiecutter Flask OpenAPI

> Pipenv GUIDE

### Requirements

- Python {{cookiecutter.python_version}} Installed
- DB and DB Test Up and Running (See README_DOCKER)
- Pipenv Installed

### Set your Pipenv to create virtualenv inside the project

```
export PIPENV_VENV_IN_PROJECT=1
```

### Create the virtual environment

```
pipenv check
```

### Install Python Packages

```
pipenv sync --dev

```

### Run the API

```
pipenv run flask db upgrade
pipenv run flask run

```

Then, 
- access 🚀 http://localhost:5000/api to access the API documentation
- access 🚀 http://localhost:5000/api/status to check the API statuses
- access 🚀 http://localhost:5000/api/{{cookiecutter.main_model_lower}} to list {{cookiecutter.main_model}}

### Tests

```
pipenv run pytest
```

### Linter && Code Style

```
pylint {{cookiecutter.project_slug}}/**/*.py
black -l 88 --check {{cookiecutter.project_slug}}/

```



### Extra

Check the **Makefile** and run `make help` where it has all commands above shortcuts and more...