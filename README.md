**AWS Parameter Store Client**
==============================

Just a Python client for AWS Parameter Store. \
It is a wrapper around (and an interface to) boto3.


Usage
=====

---

Local dir install
-----------------
To install this client in a project, from a local dir, add this to `pyproject.toml`:
```toml
[project]
...
dependencies = [
    "aws-parameter-store-client @ file:///Users/nimiq/workspace/aws-parameter-store-client"
]

[tool.poetry.dependencies]
# This section is required only when there are editable (develop = true) dependencies.
aws-parameter-store-client = {develop = true}
```

Github install
--------------
To install this client in a project, from Github, add this to `pyproject.toml`:
```toml
[project]
...
dependencies = [
    "aws-parameter-store-client @ git+https://github.com/puntonim/aws-parameter-store-client",
]
```

Example code
------------
```py
from aws_parameter_store_client.aws_parameter_store_client import (
    AwsParameterStoreClient,
    ParameterNotFound,
)

client = AwsParameterStoreClient()
value = None
try:
    value = client.get_parameter(path="/my/parameter")
except ParameterNotFound as exc:
    ...
assert value == "thisismyvalue"
```


Development setup
=================

---

1 - System requirements
----------------------

**Python 3.13.1**\
The target Python 3.13.1 as it is the latest at the time of writing.\
Install it with pyenv:
```sh
$ pyenv install -l  # List all available versions.
$ pyenv install 3.13.1
```

**Poetry**\
Pipenv is used to manage requirements (and virtual environments).\
Read more about Poetry [here](https://python-poetry.org/). \
Follow the [install instructions](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions).

**Pre-commit**\
Pre-commit is used to format the code with black before each git commit:
```sh
$ pip install --user pre-commit
# On macOS you can also:
$ brew install pre-commit
```

2 - Virtual environment and requirements
----------------------------------------

Create a virtual environment and install all deps with one Make command:
```sh
$ make poetry-create-env
# Or to recreate:
$ make poetry-destroy-and-recreate-env
# Then you can activate the virtual env with:
$ eval $(poetry env activate)
# And later deactivate the virtual env with:
$ deactivate
```

Without using Makefile the full process is:
```sh
# Activate the Python version for the current project:
$ pyenv local 3.13.1  # It creates `.python-version`, to be git-ignored.
$ pyenv which python
~/.pyenv/versions/3.13.1/bin/python

# Now create a venv with poetry:
$ poetry env use ~/.pyenv/versions/3.13.1/bin/python
# Now you can open a shell and/or install:
$ eval $(poetry env activate)
# And finally, install all requirements:
$ poetry install
# And later deactivate the virtual env with:
$ deactivate
```

To add a new requirement:
```sh
$ poetry add requests
$ poetry add pytest --dev  # Dev only.
$ poetry add requests[security,socks]  # With extras.
$ poetry add git+https://github.com/puntonim/strava-client  # From git.
$ poetry add "git+https://github.com/puntonim/strava-client[aws-parameter-store]"  # From git with extras.
```


3 - Pre-commit
--------------

```sh
$ pre-commit install
```


Deployment
==========

---

This client is not deployed to PyPI. \
See the `Usage` section to know how to install and use it.


Copyright
=========

---

Copyright puntonim (https://github.com/puntonim). No License.
