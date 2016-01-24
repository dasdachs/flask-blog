# The app is under construction. Thank you for you patience.

# flask-blog
A blog written with Flask with some scrapers running in the background

## Description

The app has two parts: a **blog** and some **scrapers**.

I use it as my personal [blog](http://dasdachs.pythonanywhere.com) while scrapers are meant for personal use. But they could be used to make something similar to the [django-dynamic-scraper](https://github.com/holgerd77/django-dynamic-scraper).

Since the site is dynamic I use [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/) and PostgreSQL in production. 

The app follows design patterns laid out by [Miguel Grinberg](https://github.com/miguelgrinberg) (especially his book [Flask Web Development](flaskbook.com) and his talk PyCon 2014 talk [Flask by Example](https://github.com/miguelgrinberg/flask-pycon2014)) and [cookiecutter-flask](https://github.com/sloria/cookiecutter-flask).

The app is written in **Python 3**.

## Installation

1. Create a virtual environment (use [Virtual Enviroments](http://docs.python-guide.org/en/latest/dev/virtualenvs/) or [venv](https://docs.python.org/3.4/library/venv.html))

_Example:_
`python -m venv flask-blog`

2. Within your virtual environment folder (in this case `flask-blog`) create a folder named `app`

3. Clone or copy this repository into this folder

4. Run `pip install -r requirements.txt`

5. Change the directory to `flask-blog`

6. Execute `python manage.py createsuperuser`

7. Run `python manage.py runserver`

## Deploying

For this project I use [Pythonanywhere](https://www.pythonanywhere.com/). You can deploy your app using git or you could just upload your files from your profile. It's really straight forward and you have the option to edit you code using their online editor. 

Since [Jacob Kaplan-Moss](https://github.com/jacobian) mentioned that Python frameworks are in decline at Heroku (somewhere [here](https://youtu.be/UKAkKXFMQP8?t=978)) I added a procfile and use Gunicorn to make deploying to Heroku as easy as possible. Consult Heroku's instructions for installations. 

For other deployment please see the respective instructions.

## Misc

I am not using Flask-Boostrap, but I am using Boostrap and I build my style on top of it. If you don't want to be bothered with design, just use Flask-Bootstrap and remove the custom `style.css`.

The WYSIWYG editor of choice is the excellent [Medium](https://github.com/yabwe/medium-editor) editor.

If you have any suggestions, wishes or just some ideas contact me.
