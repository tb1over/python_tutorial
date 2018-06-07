# -*- coding:utf8 -*-

from flask import Flask

from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
'''
>>> from microblog import app
>>> app.config['SECRET_KEY']
'you-will-never-guess'
'''

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models


