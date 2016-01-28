#!/usr/bin/env python3.4
from flask import Flask

from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown
from flask_pagedown import PageDown
from flask_migrate import Migrate

from config import config


login_manager = LoginManager()
db = SQLAlchemy()
toolbar = DebugToolbarExtension()

login_manager.login_view = "auth.login"

# App factory
# ===========
# Read about it in Miguel Grinberg Flask Web Development
# or check out his talk at PyCon 2014 talk Flask by Example
# (https://github.com/miguelgrinberg/flask-pycon2014))


def app_factory(config_name):
    """
    The app factory takes the configuration name (development, testing, production)
    and returns a Flask instance.

    First it creates an app instance. Then it loads the configurations.
    Next it initialises the extensions and registers the blueprints.
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    login_manager.init_app(app)
    db.init_app(app)
    toolbar.init_app(app)

    migrate = Migrate(app, db)

    Markdown(app, extensions=['footnotes'])
    pagedown = PageDown(app)

    from .views.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .views.blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)

    from .views.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    # If you serve robots.txt, humans.txt and sitemap.xml
    # from your webserver, unregister (delete) this Blueprint
    # and follow the webserver's documentation.
    from .robots import robots as robots_blueprint
    app.register_blueprint(robots_blueprint)

    return app