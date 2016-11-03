#!/usr/bin/env python3.4
from flask_wtf import Form
from wtforms import BooleanField, DateTimeField, StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Optional, Length, Email, EqualTo
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


class PostForm(Form):
    """
    The Post form is used for creating and editing posts.
    """
    title = StringField('Title', validators=[DataRequired(), Length(1, 120)])
    summary = TextAreaField('Summary', validators=[DataRequired()])
    body = PageDownField('Body', validators=[DataRequired()])
    pub_date = DateTimeField('Publish', format='%d.%m.%Y %H:%M', validators=[Optional()])

    def from_model(self, other):
        """
        Prepopulates the from from the model.

        It seems to be safer than just writing 'obj='.

        :param other: the Post instance that will be updated. Post is defined in
        your views.
        """
        self.title.data = other.title
        self.summary.data = other.summary
        self.body.data = other.body
        self.pub_date.data = other.pub_date

    def to_model(self, other):
        """
        Updates the model instance.

        :param other: the Post instance that will be updated. Post is defined in
        your views.
        """
        other.title = self.title.data
        other.summary = self.summary.data
        other.body = self.body.data
        other.pub_date = self.pub_date.data


class UserForm(Form):
    """
    A form to add a new user.

    TODO: permissions
    """
    username = StringField('Username', validators=[DataRequired(), Length(1, 30)])
    email = StringField('Email', validators=[Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat password')

    def from_model(self, other):
        """
        Prepopulates the from from the model.

        It seems to be safer than just writing 'obj='.

        :param other: the User instance that will be updated defined in your view.
        """
        self.username.data = other.username
        self.email.data = other.email
        self.password.data = other.password_hash

    def to_model(self, other):
        """
        Updates the model instance.

        :param other: the User instance that will be updated defined in your view.
        """
        other.username = self.username.data
        other.email = self.email.data
        other.password = self.password.data


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
