__author__ = 'dasDachs'
__version__ = '0.1'
"""
The main part of the app. The center is the app factory that returns the Flask
app with all the setting needed to run in your environment.
"""
from flask import Flask

from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import config


api = Api()
db = SQLAlchemy()

# App factory
# ===========
# Read about it in Miguel Grinberg Flask Web Development
# or check out his talk at PyCon 2014 talk Flask by Example
# (https://github.com/miguelgrinberg/flask-pycon2014))
def app_factory(config_name):
    """
    The app factory takes the configuration name (development, testing,
    production) and returns a Flask instance.

    First it creates an app instance. Then it loads the configurations.
    Next it initialises the extensions and registers the blueprints.
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate = Migrate(app, db)

    from .api import api
    api.init_app(app)

    # If you serve robots.txt,
    # humans.txt and sitemap.xml
    # from your webserver,
    # unregister (delete) this
    # Blueprint
    # and follow the
    # webserver's
    # documentation.
    from .robots import robots as robots_blueprint
    app.register_blueprint(robots_blueprint)

    return app
