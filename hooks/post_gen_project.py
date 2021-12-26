"""
NOTE:
    the below code is to be maintained Python 2.x-compatible
    as the whole Cookiecutter Django project initialization
    can potentially be run in Python 2.x environment
    (at least so we presume in `pre_gen_project.py`).

TODO: restrict Cookiecutter Django project initialization to
      Python 3.x environments only
"""
from __future__ import print_function

import json
import os
import random
import shutil
import string

try:
    # Inspired by
    # https://github.com/django/django/blob/master/django/utils/crypto.py
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    using_sysrandom = False

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

DEBUG_VALUE = "debug"


def remove_docker_files():

    file_names = ["Dockerfile", ".dockerignore", ]
    for file_name in file_names:
        os.remove(file_name)


def remove_github_actions_files():
    github_actions_dir = ".github"
    if os.path.exists(github_actions_dir):
        shutil.rmtree(github_actions_dir)


def remove_heroku_files():

    file_names = ["Procfile", ]
    for file_name in file_names:
        os.remove(file_name)


def remove_vscode_files():
    vscode_dir = ".vscode"
    if os.path.exists(vscode_dir):
        shutil.rmtree(vscode_dir)

def remove_package_manager_files():
    file_names = ["Pipfile", "Pipfile.lock"]
    if "{{ cookiecutter.package_manager }}".lower() != "requirements.txt":
        file_names = ["requirements.txt", "requirements-dev.txt"]
    for file_name in file_names:
        os.remove(file_name)


def main():

    if "{{ cookiecutter.use_dockerfile }}".lower() != "yes":
        print(INFO + "  - Removing 🐳 Dockerfile and the container for the backend" + TERMINATOR)
        print(INFO + "  - Removing 🐳 CI Docker Build" + TERMINATOR)
        remove_docker_files()

    if "{{ cookiecutter.use_github_actions_CI }}".lower() != "yes":
        print(INFO + "  - Removing Github Actions workflow file" + TERMINATOR)
        remove_github_actions_files()

    if "{{ cookiecutter.deploy_to_heroku }}".lower() != "yes":
        print(INFO + "  - Removing Procfile (Heroku deploy)" + TERMINATOR)
        remove_heroku_files()

    if "{{ cookiecutter.keep_vscode_settings }}".lower() != "yes":
        print(INFO + "  - Removing VSCode files" + TERMINATOR)
        remove_vscode_files()

    if "{{ cookiecutter.package_manager }}".lower() != "requirements.txt":
        print(INFO + "  - Using Pipenv files" + TERMINATOR)
    else:
        print(INFO + "  - Using requirements.txt and virtualenv" + TERMINATOR)
    remove_package_manager_files()

    print(SUCCESS + "🐍 Your project is created! ✨ 🍰 ✨\n\n" + HINT)

    print("What's next?")
    print("     cd {{ cookiecutter.project_slug }}")
    print("     Check the README_DOCKER 🐳")
    if "{{ cookiecutter.package_manager }}".lower() == "requirements.txt":
        print("     Check the README_VIRTUALENV 🐍")
    else:
        print("     Check the README_PIPENV 🐍")
    
    print(INFO + "⚠️ For more details, check the Makefile or run: make help\n" + TERMINATOR)

if __name__ == "__main__":
    main()
