# Cookiecutter Flask OpenAPI boilerplate

[![GitHub issues](https://img.shields.io/github/issues/huogerac/cookiecutter-flask-openapi?style=for-the-badge)](https://github.com/huogerac/cookiecutter-flask-openapi/issues) [![GitHub stars](https://img.shields.io/github/stars/huogerac/cookiecutter-flask-openapi?style=for-the-badge)](https://github.com/huogerac/cookiecutter-flask-openapi/stargazers) [![GitHub license](https://img.shields.io/github/license/huogerac/cookiecutter-flask-openapi?style=for-the-badge)](https://github.com/huogerac/cookiecutter-flask-openapi/blob/master/LICENSE) [![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://github.com/psf/black)

> 💻 A full-featured Flask + API + OAS3 + JWT + SwaggerUI + ORM + Migrations + Great and Scalable structure project template

> 👉 It's using latest Flask 1.2

> Flask 2 is coming soon 😎

> It uses PostgreSQL everywhere, so Docker is necessary (SQLite with no Docker dependency is on the roadmap) 😎


## Why using this boilerplate ❓

- Focus on the business and creating value
- Faster project setup
- Standard project structure organization (easy to scale)
- Better QA


## What's Included (Features) 🎉


- API Design first using OpenAPI & Connexion
- API documentation using swagger UI
- Login using JWT
- Every layer is separated in context/domain
- Service layer for better tests and reuse
- Using Flask Factory to integrate with extensions
- Migrartions using Alembic
- ORM using SQLAlchemy
- Optimized development and production settings
- Comes with user model ready to go, signup & signin
- Procfile for deploying to Heroku
- Customizable PostgreSQL version
- Tests using pytest
- Unit tests for the API layer
- Unit tests for the service layer

**Development**
- Code linter
- Code formatter (Black+iSort)
- Using .env file
- Docker support using docker-compose for development
- Postgres in development (using docker-compose)
- Docker using multistage (Different build for development)
- CI using Github Actions

## Structure

```
Hackernews-Clone
.
├── hackernews
│   ├── app.py                    👉 Entrypoint (create_app)
│   ├── exceptions.py
│   ├── 🧅 ext                    👉 Settings
│   │   ├── ⚙️ configuration.py
│   │   ├── ⚙️ api.py
│   │   └── ⚙️ database.py
│   │   ...
│   ├── 🧅 api                    👉 API Routes
│   │   ├── 📦 auth.py
│   │   ├── 📦 news.py
│   │   └── 📦 openapi.yaml       👉 API Contract
│   │   ...
│   ├── 🧅 services               👉 Business rules
│   │   ├── 📦 auth.py 🎂
│   │   ├── 📦 news.py 🎂
│   │   └── 📦 token.py 🎂
│   │   ...
│   └── 🧅 models                 👉 ORM
│       ├── 📦 news.py
│       └── 📦 users.py
│       ...
├── ⚙️ migrations                 👉 Database versions
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
├── tests
│   ├── conftest.py
│   ├── api                      👉 Endpoint tests, input, output and validation 
│   ├── database                 👉 Database connection tests
│   └── services                 👉 Business rules tests
├── requirements.txt
├── pytest.ini
├── uwsgi.ini                    👉 Application server settings  
└── wsgi.py                      👉 WSGI Deploy file (Gunicorn/uWSGI)
```

## Requirements

- Python 3.8 or 3.9 (Help us test in other versions)

- Docker to run Postgres locally


## Contribute 🚀

Any help is more than welcome...

- 👉 It could be an [Issue](https://github.com/huogerac/cookiecutter-flask-openapi/issues)
- 💻 It could be using it and give a feedback
- 🌟 It could be a github star
- 🤔 It could be a [Question](https://github.com/huogerac/cookiecutter-flask-openapi/discussions/)
- 🤔 If you dislike this project, feel free to tell us what is wrong with it


## Get Started (Usage) 

Let's pretend you want to create a Flask project called "hackernewsclone". Rather than start from scratch by a ``app.py`` and add each library, Flask extesion and various other configurations that always get forgotten until the worst possible moment, get this cookiecutter template do all the work.

First, get Cookiecutter. Trust me, it's awesome::

```
    $ pip install "cookiecutter>=1.7.0"
```

Now run it against this repo::

```
    $ cookiecutter https://github.com/huogerac/cookiecutter-flask-openapi/
```

You'll be prompted for some values. Provide them...

```
project_name [Hackernews Clone]: 
project_slug [hackernews_clone]: hackernewsclone
main_model [News]: 
main_model_lower [news]: 
description [The Ultimate Flask Template]: 
author_name [Roger Camargo]: 
email [roger-camargo@example.com]: 
version [0.1.0]: 
Select python_version:
1 - 3.8.10
2 - 3.9.5
Choose from 1, 2 [1]: 
Select postgresql_version:
1 - 13.3-alpine
2 - 13.5
3 - 14.1
Choose from 1, 2, 3 [1]: 
use_dockerfile [yes]: 
use_github_actions_CI [yes]: 
deploy_to_heroku [yes]: no
keep_vscode_settings [yes]: 
 [INFO]:   - Removing Procfile (Heroku deploy)

 [SUCCESS]: 🐍 Huruuuu, All done! ✨ 🍰 ✨

What's next?
  1) 🐳 Running using docker
     cd hackernewsclone
     docker-compose up --build

  2) 🐍 Running using virtualenv
     cd hackernewsclone
     make virtualenv
     source .venv/bin/activate
     make all

  Then
     access 🚀 http://localhost:5000/api

 [INFO]: ⚠️ You must have Docker installed, at least to run the postgres database
```


## Articles

- 🇧🇷 [Estrutura e organização de pastas em projetos Flask](https://huogerac.hashnode.dev/estrutura-e-organizacao-de-pastas-em-projetos-flask)







## Thanks and Inspirations

- This template is based on [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django). Thanks PyDanny and the Cookiecutter maintainers

- This Flask structure is based on ["Arquitetura Definitiva para o Projeto Web Com Python e Flask"](https://www.youtube.com/watch?v=-qWySnuoaTM). Thanks Bruno Rocha and all yours Flask contents
