"""
Initialize module
"""
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
from flask_restx import Api

from . import config
from .ui_swagger import swaggerui_blueprint


# create Flask application
app = Flask(__name__)
app.secret_key = 'super secret key'
# Environment Configuration
app.config.from_object(config.Config)

# initialize the database connection
db = SQLAlchemy(app)
# initialize the database migration
migrate = Migrate(app, db)

# initialize api
api = Api(app, title='Film library')

# swagger settings
app.register_blueprint(swaggerui_blueprint)

# logging
logging.basicConfig(level=logging.INFO, filename="logs.txt", filemode="a",
                    format='%(asctime)s:%(levelname)s:%(message)s')

from .models import directors, users, genres, films_directors, films_genres, films
from . import add_resources
