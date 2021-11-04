# Book Blog Rest Api Project 
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangoproject120x25.gif" border="0" alt="A Django project." title="A Django project." /></a>
<img src="https://raw.githubusercontent.com/swagger-api/swagger.io/wordpress/images/assets/SW-logo-clr.png" height="50" align="right">
<a href="https://github.com/python/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

## Installation
The first thing to do is to clone the repository:


```sh
$ git clone https://github.com/konerjonlar/muni/
$ cd sample-django-app
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv venvName
$ source venvName/bin/activate
```

Then install the dependencies:

```sh
(env)$pip install poetry
(env)$ poetry install
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venvName`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd muni
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
