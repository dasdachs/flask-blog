"""
Helper functions for our app, like
"""
import datetime
import os
import os.path

from jinja2 import Environment, FileSystemLoader
from flask import current_app, make_response, render_template, url_for

from .models import Post
from .views.blog import blog


def generate_sitemap():
    """
    Generates the sitemap.

    If you add a new model, you have to add it manual to this function.
    Currently it discovers the static sites and the posts.

    Make sure to run this function once a week using cron job or celery
    and to ping Google webmaster if you are concerned with CEO.

    This is the snippet from BlazingQuasar.
    You can look it up on the official Flask site:
    http://flask.pocoo.org/snippets/108/
    """
    pages = []
    ten_days_ago = datetime.datetime.now() - datetime.timedelta(days=10)

    # Static pages
    for rule in current_app.url_map.iter_rules():
        if "GET" in rule.methods and len(rule.arguments) == 0:
            pages.append([rule.rule, ten_days_ago])

    # Posts model pages
    posts = Post.query.order_by(Post.pub_date.desc())
    for post in posts:
        if post.is_visible():
            url = url_for('blog.post_view', post_title=post.title)
            if post.modified:
                modified_time = post.modified.isoformat()
            else:
                modified_time = post.created.isoformat()
            pages.append([url, modified_time])

    sitemap_xml = render_template('sitemap_template.xml', pages=pages)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"

    return response


def add_page(page_name):
    """
    Creates a template for a 'static' page. Make sure that you create the template.

    The function assumes that the pages are part of blog view. If they are not, you
    have to change 'save_to' accordingly.

    page_name: a str, single word, that is the name of the page
    return: <page_name>.html, with page_name caitalizted and saved to the database
    TODO: fix path of new file, to corespond with blog model
    """
    doc_name = page_name + '.html'
    template_root = os.path.join(os.getcwd(), 'templates')

    if blog.template_folder:
        save_to = blog.template_folder
    else:
        save_to = os.path.join(template_root, 'blog', 'pages')

    env = Environment(loader=FileSystemLoader(template_root))
    template = env.get_template('page_temp.html')
    output = template.render(name=page_name, body='{{' + page_name + '.text}}')

    # Save to the results
    with open(os.path.join(save_to, doc_name), "wb") as f:
        f.write(output)

    return None