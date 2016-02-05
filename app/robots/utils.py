import datetime

from flask import current_app, make_response, render_template, url_for

from ..models import Post


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
        if "GET" in rule.methods and len(rule.arguments) == 0 and "admin" not in rule.rule:
            pages.append([rule.rule, ten_days_ago])

    # Posts model pages
    posts = Post.query.order_by(Post.pub_date.desc())
    for post in posts:
        if post.is_visible():
            url = url_for('blog.post_view', post_slug=post.slug)
            if post.modified:
                modified_time = post.modified.isoformat()
            else:
                modified_time = post.created.isoformat()
            pages.append([url, modified_time])

    sitemap_xml = render_template('sitemap_template.xml', pages=pages)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"

    return response