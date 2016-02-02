#!/usr/bin/env python3.4
import datetime

from flask import Blueprint, flash, render_template, redirect, url_for
from flask.ext.login import current_user, login_required

from .. import db
from ..models import User, Post, Page
from ..forms import AddUserForm, AddPostForm


admin = Blueprint('admin', __name__, url_prefix='/admin')


# The get methods are listed first
# The CRUD operations for Post, Page and User are in the second part
@admin.route('/')
@login_required
def dashboard():
    """
    The admin dashboard. Here you get some analytics, you can add users, add posts
    and manage scrapers.
    """
    posts_count = Post.query.count()
    users_count = User.query.count()
    return render_template('admin/dashboard.html', page='index', posts=posts_count, users=users_count)


@admin.route('/posts/')
@login_required
def posts():
    """
    Shows all posts: the author, when they were created, when they were modified, if they are published.

    From here you can do the CRUD actions.
    """
    all_posts = Post.query.all()
    return render_template('admin/posts.html', page='posts', posts=all_posts)


@admin.route('/pages')
@login_required
def pages():
    """
    Returns the 'static' pages, the date they were created and a link to edit them.
    """
    all_pages = Page.query.all()
    return render_template('admin/pages.html', page='pages', pages=all_pages)


@admin.route('/users/')
@login_required
def users():
    """
    Show all the users and offers a add, edit and delete option.
    """
    all_users = User.query.all()
    return render_template('admin/users.html', page='users', users=all_users)


# The CRUD views
# ==============
# The Post CRUD views
@admin.route('/posts/add', methods=['GET', 'POST'])
@login_required
def add_post():
    """
    The create post view. The user has to be logged in.

    The form takes a title, the summary and the body, while the pub date is optional.

    The author is retrieved from the 'current_user', the flask-login extension proxy object.
    """
    form = AddPostForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data, summary=form.summary.data,body=form.body.data,
                        created=datetime.datetime.now(), pub_date=form.pub_date.data, user=current_user)
        db.session.add(new_post)
        db.session.commit()
        flash('New post has ben added', 'success')
        return redirect(url_for('admin.posts'))
    return render_template('admin/add_post.html', form=form)


@admin.route('/posts/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    """
    Edit a post.

    TODO: add permissions
    """
    post = Post.query.get(post_id)
    form = AddPostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.summary = form.summary.data,
        post.body = form.body.data
        post.pub_date = form.publish.data
        db.session.add(post)
        db.session.commit()
        flash('Your post has ben updated', 'success')
        return redirect(url_for('admin.posts'))
    return render_template('admin/add_post.html', form=form)


@admin.route('/posts/delete/<int:post_id>')
@login_required
def delete_post(post_id):
    """
    Deletes the post.

    TODO: add permissions
    """
    post = Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post {0} was deleted.'.format(post.title), 'success')
    return redirect(url_for('admin.posts'))

# The User CRUD views
@admin.route('/users/add', methods=['GET', 'POST'])
@login_required
def add_user():
    """
    The create view for user
    """
    form = AddUserForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data,
                    password=form.password.data, is_admin=False)
        db.session.add(user)
        db.session.commit()
        flash('New user has ben added', 'success')
        return redirect(url_for('admin.users'))
    return render_template('admin/add_user.html', form=form)


@admin.route('/users/edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    """
    Edits the user.
    """
    user = User.query.get(user_id)
    form = AddUserForm(obj=user)
    return render_template('admin/add_user.html', form=form)


@admin.route('/users/delete/<int:user_id>')
@login_required
def delete_user(user_id):
    """
    Deletes the user.

    The functions checks if the current_user is the user being deleted
    and redirects him back to the users view and flashes a massage.
    """
    if user_id == current_user.id:
        flash('You tried to delete yourself. That\'s some bad voodoo.', 'danger')
    else:
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        flash('User {0} was deleted.'.format(user.username), 'success')
    return redirect(url_for('admin.users'))