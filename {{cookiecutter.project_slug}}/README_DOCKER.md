# Cookiecutter Flask OpenAPI

> Docker GUIDE


### Requirements

- Install [Docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/)

{% if cookiecutter.use_dockerfile == 'yes' -%}

### Build and initialize the DB and the API containers

```
docker-compose up --build -d
```


### Create the initial database

```
docker exec {{cookiecutter.project_slug}}-api {% if cookiecutter.package_manager == 'Pipenv' -%}pipenv run {% endif %} flask db upgrade
```


### Logs

```
docker logs -f {{cookiecutter.project_slug}}-api
```

{% else %}

### Run the Database

```
docker-compose up
```

### Logs

```
docker-compose logs -f postgres_local
```

{% endif %}

### Stop

```
docker-compose down
```

## Run the TEST Database

```
docker-compose -f docker-compose.test.yml up -d
```