"""
Settings swagger
"""
from os import getenv
from flask_swagger_ui import get_swaggerui_blueprint


SWAGGER_URL = getenv("SWAGGER_URL")
API_URL = getenv("API_URL")

swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
