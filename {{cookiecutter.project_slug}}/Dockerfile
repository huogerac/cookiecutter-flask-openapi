### BASE - Using ubuntu LTS version
FROM ubuntu{% if cookiecutter.python_version == '3.8.10' -%}:20.04{%- else %}:21.04{%- endif %} AS base
# avoid stuck build due to user prompt
ARG DEBIAN_FRONTEND=noninteractive

# make sure all messages always reach console
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

{% if cookiecutter.package_manager == 'requirements.txt' -%}
RUN apt-get update && apt-get install --no-install-recommends -y vim \
   {% if cookiecutter.python_version == '3.8.10' -%}python3.8 python3.8-dev python3.8-venv{%- else %}python3.9 python3.9-dev python3.9-venv{%- endif %} \
   python3-pip python3-wheel libpq-dev build-essential libssl-dev libffi-dev && \
   apt-get clean && rm -rf /var/lib/apt/lists/*
{% else %}
RUN apt-get update && apt-get install --no-install-recommends -y vim \
   {% if cookiecutter.python_version == '3.8.10' -%}python3.8 python3.8-dev {%- else %}python3.9 python3.9-dev {%- endif %} \
   python3-wheel virtualenv pip libpq-dev build-essential libssl-dev libffi-dev && \
   apt-get clean && rm -rf /var/lib/apt/lists/*
{% endif %}

# Get the dependency file
{% if cookiecutter.package_manager == 'requirements.txt' -%}
COPY requirements.txt .
{% else %}
COPY Pipfile .
COPY Pipfile.lock .
{% endif %}

{% if cookiecutter.package_manager == 'requirements.txt' -%}
RUN pip3 install --no-cache-dir wheel
{% else %}
RUN pip3 install --no-cache-dir wheel && pip3 install -U pipenv
{% endif %}

{% if cookiecutter.package_manager == 'requirements.txt' -%}
RUN pip3 install --no-cache-dir -r requirements.txt
{% else %}
RUN pipenv sync
{% endif %}


WORKDIR /app
EXPOSE 5000

ARG GIT_HASH
ENV GIT_HASH=${GIT_HASH:-dev}



### DEV
FROM base AS development

{% if cookiecutter.package_manager == 'requirements.txt' -%}
COPY requirements.txt .
COPY requirements-dev.txt .
RUN pip3 install --no-cache-dir -r requirements-dev.txt
{% else %}
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv sync --dev
{% endif %}

COPY . /app

CMD [{% if cookiecutter.package_manager != 'requirements.txt' -%}"pipenv", "run",{% endif %}"flask", "run", "--reload", "--debugger", "--host", "0.0.0.0"]



### PROD
FROM base AS production

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

COPY . /app

CMD ["uwsgi", "--ini", "uwsgi.ini"]
