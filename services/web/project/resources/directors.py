"""
Director entity resources
"""
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
                return {"status": 401, "reason": "Director already exist"}

            director_data = director_schema.load(director_json, session=db.session)
            director_data.save_to_db()

            return director_schema.dump(director_data), 201
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
        director_data = Director.query.get_or_404(director_id)
        if director_data:
            return director_schema.dump(director_data), 200
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
            director_data = Director.query.get_or_404(director_id)
            if director_data:
                director_data.delete_from_db()
                return {"status": 200, 'message': "Director Deleted successfully"}
            return {"status": 404, 'message': DIRECTOR_NOT_FOUND}
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
            director_data = Director.query.get_or_404(director_id)
            director_json = request.get_json()

            if already_exist(Director, director_json):
                return {"status": 401, "reason": "Such a director already exist"}

            director_data.dir_first_name = director_json['dir_first_name']
            director_data.dir_last_name = director_json['dir_last_name']
            director_data.save_to_db()

            return director_schema.dump(director_data), 200
        return {"status": 401, "reason": "User is not admin"}
