"""
Initialize module
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
from flask_restx import Api

from . import config

# create Flask application
app = Flask(__name__)
# Environment Configuration
app.config.from_object(config.Config)

# initialize the database connection
db = SQLAlchemy(app)
# initialize the database migration
migrate = Migrate(app, db)

# initialize api
api = Api(app, title='Film library')

from .models import directors, users, genres, films_directors, films_genres, films
from . import add_resources
from .auth import login
