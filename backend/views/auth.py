#!/usr/bin/env python3.4
from flask import Blueprint, flash, redirect, render_template, request, url_for

from flask.ext.login import login_user, logout_user, login_required

from ..models import User
from ..forms import LoginForm


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    The login view. It uses the login form from forms and relies on
    Flask-login to do it's biding.

    If the form is valid on submit, the functions gets the user object
    using his username.
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user or not user.verify_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('auth.login'))
        login_user(user, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('admin.dashboard'))
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out and good to go.')
    return redirect(url_for('blog.main'))