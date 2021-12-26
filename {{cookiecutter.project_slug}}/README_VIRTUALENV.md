# Cookiecutter Flask OpenAPI

> Virtualenv GUIDE

### Requirements

- Python {{cookiecutter.python_version}} Installed
- DB and DB Test Up and Running (See README_DOCKER)


### Create the virtual environment

```
virtualenv .venv
OR
virtualenv .venv --python [Python interpreter]

# Update pip
./.venv/bin/pip install -U pip

# Active your environment
source .venv/bin/activate
```

### Install Python Packages

```
pip install -r requirements-dev.txt

```

### Run the API

```
flask db upgrade
flask run

OR 

python -m flask db upgrade
python -m flask run
```

Then, 
- access 🚀 http://localhost:5000/api to access the API documentation
- access 🚀 http://localhost:5000/api/status to check the API statuses
- access 🚀 http://localhost:5000/api/{{cookiecutter.main_model_lower}} to list {{cookiecutter.main_model}}


### Tests

```
pytest
```

### Linter && Code Style

```
pylint {{cookiecutter.project_slug}}/**/*.py
black -l 88 --check {{cookiecutter.project_slug}}/

```

### Extra

Check the **Makefile** and run `make help` where it has all commands above shortcuts and more...