#!/usr/bin/env python3.4
from flask.ext.wtf import Form
from wtforms import BooleanField, DateTimeField, StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_pagedown.fields import PageDownField


class LoginForm(Form):
    """
    The login form. It is a copy of Miguel Grinbergs Login form. The only difference
    is that this form uses DataRequired instead of Required as it will be deprecated.

    https://github.com/miguelgrinberg/flask-pycon2014/blob/master/app/auth/forms.py
    """
    username = StringField('Username', validators=[DataRequired(), Length(1, 30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(1, 120)])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class AddPostForm(Form):
    """
    The Post form is used for creating and editing posts.
    """
    title = StringField('Title', validators=[DataRequired(), Length(1, 120)])
    slug = StringField('Slug', validators=[DataRequired(), Length(1, 120)])
    summary = TextAreaField('Summary', validators=[DataRequired()])
    body = PageDownField('Body', validators=[DataRequired()])
    pub_date = DateTimeField('Publish', format='%d.%m.%Y %H:%M')


class AddUserForm(Form):
    """
    A form to add a new user.

    TODO: permissions
    """
    username = StringField('Username', validators=[DataRequired(), Length(1, 30)])
    email = StringField('Email', validators=[Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat password')


class AddPage(Form):
    """
    The
    """
    pass


class EditPage(Form):
    """
    The Edit page form is used for creating and editing posts.
    """
    title = StringField('Title', validators=[DataRequired(), Length(1, 120)])
    summary = TextAreaField('Summary', validators=[DataRequired()])
    body = PageDownField('Body', validators=[DataRequired()])
    pub_date = DateTimeField('Publish', format='%d.%m.%Y %H:%M')