#!/usr/bin/env python3.4
import os
import sys
from subprocess import call

from flask_script import Manager
from flask_migrate import MigrateCommand

from config import config
from backend import app_factory, db
from backend.models import User, Post, Page


app = app_factory(os.getenv('FLASK_CONFIG'))
manager = Manager(app)

# The migrate comand
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    call(['nosetests', '-v',
          '--with-coverage', '--cover-package=app', '--cover-branches',
          '--cover-erase', '--cover-html', '--cover-html-dir=cover'])


@manager.command
def createsuperuser():
    """
    Creates a superuser.
    """
    from getpass import getpass
    db.create_all()
    username = input("Please enter a username: ")
    email = input("Please enter your mail: ")
    if "@" not in email:
        sys.exit('Error: enter a valid e-mail.')
    password = getpass()
    password2 = getpass(prompt='Confirm: ')
    if password != password2:
        sys.exit('Error: passwords do not match.')
    user = User(email=email, username=username, password=password, is_admin=True)
    db.session.add(user)
    db.session.commit()
    print("User {0} was registered successfully.".format(user))

if __name__ == '__main__':
    manager.run()
