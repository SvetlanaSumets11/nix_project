"""
Director entity resources
"""
import logging

from flask import request
from flask_restx import Resource
from flask_login import login_required, current_user

from ..modelschemas.directors import DirectorSchema
from ..models.directors import Director
from . import already_exist
from .. import db

DIRECTOR_NOT_FOUND = "Director not found."
director_schema = DirectorSchema()
director_list_schema = DirectorSchema(many=True)


class DirectorList(Resource):
    """Director Data Resource Class"""

    @classmethod
    def get(cls) -> (dict, int):
        """
        Get method
        :return: error message or json with information about the directors
        """
        logging.info("All directors are displayed")
        return director_list_schema.dump(Director.find_all()), 200

    @classmethod
    @login_required
    def post(cls) -> (dict, int):
        """
        Post method
        :return: json with information about the directors
        """
        if current_user.is_authenticated and current_user.is_admin:
            director_json = request.get_json()

            if already_exist(Director, director_json):
                logging.info("Director already exists. Director %s %s",
                             director_json["dir_first_name"], director_json["dir_last_name"])
                return {"status": 401, "reason": "Director already exist"}

            director_data = director_schema.load(director_json, session=db.session)
            director_data.save_to_db()

            logging.info("Director added. Director %s %s",
                         director_json["dir_first_name"], director_json["dir_last_name"])
            return director_schema.dump(director_data), 201

        logging.info("User is not admin. User %s", current_user.user_login)
        return {"status": 401, "reason": "User is not admin"}


class DirectorListId(Resource):
    """Director Data Resource Class"""

    @classmethod
    def get(cls, director_id) -> (dict, int):
        """
        Get method
        :param director_id: director`s id
        :return: error message or json with information about the directors
        """
        director_data = Director.query.get(director_id)
        if director_data:

            logging.info("Director returned from ID %d. Director %s %s", director_id,
                         director_data.dir_first_name, director_data.dir_last_name)
            return director_schema.dump(director_data), 200

        logging.info("Director with ID %d was not found", director_id)
        return {"status": 404, 'message': DIRECTOR_NOT_FOUND}

    @classmethod
    @login_required
    def delete(cls, director_id) -> dict:
        """
        Delete method
        :param director_id: director`s id
        :return: error message or successful message
        """
        if current_user.is_authenticated and current_user.is_admin:
            director_data = Director.query.get(director_id)

            if director_data:
                director_data.delete_from_db()
                logging.info("Director Deleted successfully. Director %s %s",
                             director_data.dir_first_name, director_data.dir_last_name)
                return {"status": 200, 'message': "Director Deleted successfully"}

            logging.info("%s Director with ID %d", DIRECTOR_NOT_FOUND, director_id)
            return {"status": 404, 'message': DIRECTOR_NOT_FOUND}

        logging.info("User is not admin. User %s", current_user.user_login)
        return {"status": 401, "reason": "User is not admin"}

    @classmethod
    @login_required
    def put(cls, director_id) -> (dict, int):
        """
        Put method
        :param director_id: director`s id
        :return: json with information about the directors
        """
        if current_user.is_authenticated and current_user.is_admin:
            director_data = Director.query.get(director_id)
            director_json = request.get_json()

            if not director_data:
                logging.info("%s User with ID %d", DIRECTOR_NOT_FOUND, director_id)
                return {"status": 404, 'message': DIRECTOR_NOT_FOUND}

            if already_exist(Director, director_json):
                logging.info("Director already exist. Director %s %s",
                             director_json["dir_first_name"], director_json["dir_last_name"])
                return {"status": 401, "reason": "Such a director already exist"}

            director_data.dir_first_name = director_json['dir_first_name']
            director_data.dir_last_name = director_json['dir_last_name']
            director_data.save_to_db()
            logging.info("Director data changed successfully. Director %s %s",
                         director_data.dir_first_name, director_data.dir_last_name)
            return director_schema.dump(director_data), 200

        logging.info("User is not admin. User %s", current_user.user_login)
        return {"status": 401, "reason": "User is not admin"}
