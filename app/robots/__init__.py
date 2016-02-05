"""
We added a separated Blueprint for created robots.txt, humans.txt and sitemap.xml into
It is recommended that Flask does not serve static filed in production.
You would normally leave that to Ngnix or Apache, but for certain deployments,
e.g. Heroku, you do not have that access. Therefore we registered a separate
Blueprint to server these static files.

The files are placed in robots/static, the folder is registered in the Blueprint.
If you wish to serve these files from your webserver, unregister this Blueprint in
the app_factory() and move the files to the corresponding folder.

For more on this topic reade this Stackoverflow thread:
http://stackoverflow.com/questions/4239825/static-files-in-flask-robot-txt-sitemap-xml-mod-wsgi
"""
from flask import Blueprint, request, send_from_directory

from .utils import generate_sitemap


robots = Blueprint('robots', __name__, static_folder='static')


@robots.route('/robots.txt')
@robots.route('/humans.txt')
def static_from_root():
    """
    Returns the robots.txt or humans.txt as if it is based in the root
    directory of our app. Those files are actually placed in the static
    folder of the robots Blueprints. That way follow the design principles
    not to place static files in the root directory of the app.
    """
    return send_from_directory(robots.static_folder, request.path[1:])


@robots.route('/sitemap.xml')
def sitemap_from_root():
    """
    Returns the response from the generate_sitemap function from utils.py.
    """
    return generate_sitemap()