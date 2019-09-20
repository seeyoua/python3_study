#!/usr/bin/python

import os

environ=os.environ
PROJECT_PATH = os.path.dirname(__file__)
TEMPLATE_FLODER = os.path.join(PROJECT_PATH,'templates')
STATIC_FLODER = os.path.join(PROJECT_PATH,'static')
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:mysql@localhost:3306/flask_ttc'
SQLALCHEMY_TRACK_MODIFICATIONS = False

