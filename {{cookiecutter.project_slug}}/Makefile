.ONESHELL:

{% if cookiecutter.package_manager == 'requirements.txt' -%}
ENV_PREFIX=$(shell python -c "if __import__('pathlib').Path('.venv/bin/pip').exists(): print('.venv/bin/')")
{% endif %}

.PHONY: help
help:                      ## Show this help
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep


.PHONY: show
show:                      ## Show the current environment
	{% if cookiecutter.package_manager == 'requirements.txt' -%}@echo "Current environment:"
	if [ -z "${ENV_PREFIX}" ]
	then
		if [ -d .venv ]; then
			echo "Virtualenv not activated"
			echo "Run:"
			echo "  source .venv/bin/activate"
		else
			echo "Virtualenv not created"
			echo "Run:"
			echo "  make virtualenv"
		fi
		exit 1
	fi
	@echo "Current environment:"
	@echo ">>> Running using '$(ENV_PREFIX)'"
	@$(ENV_PREFIX)python -V
	@$(ENV_PREFIX)python -m site
	{% else %}@echo "Checking environment:"
	@pipenv check 2> /dev/null || (echo "pipenv not installed. Error $$?"; exit 1)
	@pipenv check
	{% endif %}


.PHONY: virtualenv
virtualenv:                ## Create a virtual environment
	{% if cookiecutter.package_manager == 'requirements.txt' -%}@echo "creating virtualenv ..."
	@rm -rf .venv
	@virtualenv .venv
	@./.venv/bin/pip install -U pip
	@echo
	@echo "!!! Please run 'source .venv/bin/activate' to enable the environment !!!"
	{% else %}@echo "creating virtualenv using Pipenv..."
	@pipenv check
	@echo "Use 'pipenv shell' or 'pipenv run' to run commands inside your virtualenv"
	{% endif %}


.PHONY: system-packages
system-packages:           ## Install SO dependencies
	@sudo apt install -y libpq-dev build-essential libssl-dev libffi-dev


.PHONY: python-packages
python-packages:           ## Install project dependencies (dev mode)
	{% if cookiecutter.package_manager == 'requirements.txt' -%}@echo "Installing dependencies..."
	if [ -z "${ENV_PREFIX}" ]
	then
		echo "Virtualenv not activated"
		echo "Run:"
		echo "  make show"
		exit 1
	fi
	@$(ENV_PREFIX)pip install -r requirements-dev.txt
	{% else %}@echo "Installing dependencies..."
	@pipenv sync --dev
	{% endif %}@echo "Project dependencies installed!!!"


.PHONY: install
install: system-packages python-packages    ## Install all dependencies


.PHONY: clean
clean:                     ## Clean unused files
	@find ./ -name '*.pyc' -exec rm -f {} \; 2> /dev/null
	@find ./ -name '__pycache__' -exec rm -rf {} \; 2> /dev/null
	@rm -rf .cache
	@rm -rf .pytest_cache


.PHONY: code-fmt
code-fmt:                  ## Format code using black & isort
	{% if cookiecutter.package_manager == 'requirements.txt' -%}$(ENV_PREFIX)isort {{cookiecutter.project_slug}}/
	$(ENV_PREFIX)black -l 88 {{cookiecutter.project_slug}}/
	{% else %}@pipenv run isort {{cookiecutter.project_slug}}/
	@pipenv run black -l 88 {{cookiecutter.project_slug}}/
	{% endif %}

.PHONY: linter
linter:                    ## Run pep8, black
	{% if cookiecutter.package_manager == 'requirements.txt' -%}$(ENV_PREFIX)pylint {{cookiecutter.project_slug}}/**/*.py
	$(ENV_PREFIX)black -l 88 --check {{cookiecutter.project_slug}}/
	{% else %}@pipenv run pylint {{cookiecutter.project_slug}}/**/*.py
	@pipenv run black -l 88 --check {{cookiecutter.project_slug}}
	{% endif %}


.PHONY: db-test-up
db-test-up:                ## Run Postgres for testing (using docker)
	@docker-compose -f docker-compose.test.yml up -d


.PHONY: db-test-down
db-test-down:              ## Stop Postgres (test instance)
	@docker-compose -f docker-compose.test.yml down


.PHONY: tests
tests: linter db-test-up   ## Run tests using pytest and docker DB
	@sleep 1
	{% if cookiecutter.package_manager == 'requirements.txt' -%}$(ENV_PREFIX)pytest
	{% else %}@pipenv run pytest
	{% endif %}


.PHONY: db-up
db-up:                     ## Run Postgres for testing (using docker)
	@docker-compose up -d postgres_local


.PHONY: run
run: db-up                 ## Run the Flask app
	{% if cookiecutter.package_manager == 'requirements.txt' -%}@flask db upgrade
	@flask run
	{% else %}@pipenv run flask db upgrade
	@pipenv run flask run
	{% endif %}


.PHONY: all
all: show clean install tests run                ## Run all


.PHONY: db-down
dk-down:                   ## Stop Postgres (test instance)
	@docker-compose down


.PHONY: dk-clean
dk-clean:                  ## Docker Clean up (unused containers/volumes)
	@docker stop $(docker ps -a -q)
	@docker rm $(docker ps -a -q)
	@docker system prune --volumes
