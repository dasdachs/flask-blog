"""
The basic flask configurations for. We create a base class in subclass it
to different configuration settings.
"""
#!/usr/bin/env python3.5
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    The base class Config defines the secret key and the timezone.
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    DEBUG_TB_ENABLED = True
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'PIY8G!T@F4lH$aY0eZhRkQK1'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') + 'flask_blog' or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = 'very-secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
