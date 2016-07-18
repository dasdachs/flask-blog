#!/usr/bin/env python3.4
import datetime

from flask import Blueprint, render_template

from flask.ext.login import current_user

from ..models import Post, Page


blog = Blueprint('blog', __name__)


@blog.route('/')
def main():
    """
    Returns the main page of the blog with a list o recent posts.

    TODO: paginate
    """
    posts = Post.query.filter(Post.pub_date <= datetime.datetime.now()).order_by(Post.pub_date.desc())
    return render_template("blog/home.html", posts=posts, page='main')


@blog.route('/post/<post_slug>')
def post_view(post_slug):
    """
    Displays a single post.
    """
    post = Post.query.filter_by(slug=post_slug).first_or_404()
    return render_template('blog/post.html', post=post)


# The info pages, like about and
# TODO: make them static and add content editable
# and use a editor like medium for this kind of pages
@blog.route('/about')
def about():
    """
    The about me page.
    """
    about_page = Page.query.filter(name='about')
    return render_template('blog/about.html', about=about_page,  page='about')


@blog.route('/links')
def links():
    """
    The links site.
    """
    links_page = Page.query.filter(name='about')
    return render_template('blog/about.html', links=links_page,  page='about')