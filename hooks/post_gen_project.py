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

    file_names = ["Dockerfile", ".dockerignore"]
    for file_name in file_names:
        os.remove(file_name)

def main():

    if "{{ cookiecutter.use_dockerfile }}".lower() != "yes":
        print(INFO + "  - Removing 🐳 Dockerfile and the container for the backend" + TERMINATOR)
        remove_docker_files()

    print(SUCCESS + "Huruuuu, projecto criado!" + TERMINATOR)


if __name__ == "__main__":
    main()
