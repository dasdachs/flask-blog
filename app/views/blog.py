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


@blog.route('/post/<post_title>')
def post_view(post_title):
    """
    Displays a single post.
    """
    post = Post.query.filter_by(title=post_title).first_or_404()
    return render_template('blog/post.html', post=post)


# The info pages, like about and
# TODO: make them static and add content editable
# and use a editor like medium for this kind of pages
@blog.route('/about')
def about():
    """
    The about me page.
    """
    return render_template('blog/about.html', page='about')


@blog.route('/links')
def links():
    """
    The links site.
    """
    return render_template('blog/links.html', page='links')