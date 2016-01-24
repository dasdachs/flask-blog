#!/usr/bin/env python3.4
from flask import Blueprint, render_template


blog = Blueprint('blog', __name__)


@blog.route('/')
def main():
    """
    Returns the main page of the blog with a list o recent posts.
    """
    return render_template("base.html")