# {{cookiecutter.project_slug}}-api

API (backend python) para o frontend do {{cookiecutter.project_slug}}-clone

## Setup

- criar virtualenv
- `pip install -r requirements-dev.txt`

## Rodar testes

```
make run_tests
```

OU

```

make db_test_up
pytest
make db_test_down

```

## Rodar API

```
docker-compose up -d
flask db upgrade     # 1a vez apenas
flask run
```

👉 http://localhost:5000/api/
👉 http://localhost:5000/api/{{cookiecutter.main_model_lower}}

## Próximos passos

- https://github.com/confraria-devpro/{{cookiecutter.project_slug}}-api/issues

## Adicionando uma notícia

```
flask shell

Python 3.8.10 (default, Sep 28 2021, 16:10:42)

from {{cookiecutter.project_slug}}.ext.database import db
from {{cookiecutter.project_slug}}.models.{{cookiecutter.main_model_lower}} import {{cookiecutter.main_model}}
from {{cookiecutter.project_slug}}.models.users import User

{{cookiecutter.main_model}}.query.all()
[]


u = User(name="roger", username="rac", email="r@a.c")
db.session.add(u)
db.session.commit()

n = {{cookiecutter.main_model}}(title="Teste", description="1o. teste", author_id=u.id)
db.session.add(n)
db.session.commit()

{{cookiecutter.main_model}}.query.all()
[Teste]
```
