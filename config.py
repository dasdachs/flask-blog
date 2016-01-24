#!/usr/bin/env python3.4
import os


basedir = os.path.abspath(os.path.dirname(__file__))
# SETTINGS:
# ========
# 1. TZ
# This app uses the pytz library for timezones.
# For more info visit: http://pythonhosted.org/pytz/
TZ = 'Europe/Ljubljana'


class Config(object):
    """
    The base class Config defines the secret key and the timezone.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    DEBUG_TB_ENABLED = True
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'PIY8G!T@F4lH$aY0eZhRkQK1'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = 'very-secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'PIY8G!T@F4lH$aY0eZhRkQK1'
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}