"""
Director entity resources
"""
from flask import request
from flask_restx import Resource

from ..modelschemas.directors import DirectorSchema
from ..models.directors import Director
from .. import db

DIRECTOR_NOT_FOUND = "Director not found."
director_schema = DirectorSchema()
director_list_schema = DirectorSchema(many=True)


class DirectorList(Resource):
    """Director Data Resource Class"""

    @classmethod
    def get(cls, director_id=None):
        """
        Get method
        :param director_id: director`s id
        :return: error message or json with information about the directors
        """
        if not director_id:
            return director_list_schema.dump(Director.find_all()), 200
        director_data = Director.query.get_or_404(director_id)
        if director_data:
            return director_schema.dump(director_data), 200
        return {'message': DIRECTOR_NOT_FOUND}, 404

    @classmethod
    def delete(cls, director_id):
        """
        Delete method
        :param director_id: director`s id
        :return: error message or successful message
        """
        director_data = Director.query.get_or_404(director_id)
        if director_data:
            director_data.delete_from_db()
            return {'message': "Director Deleted successfully"}, 200
        return {'message': DIRECTOR_NOT_FOUND}, 404

    @classmethod
    def put(cls, director_id):
        """
        Put method
        :param director_id: director`s id
        :return: json with information about the directors
        """
        director_data = Director.query.get_or_404(director_id)
        director_json = request.get_json()

        if director_data:
            director_data.dir_first_name = director_json['dir_first_name']
            director_data.dir_last_name = director_json['dir_last_name']
        else:
            director_data = director_schema.load(director_json, session=db.session)

        director_data.save_to_db()
        return director_schema.dump(director_data), 200

    @classmethod
    def post(cls):
        """
        Post method
        :return: json with information about the directors
        """
        director_json = request.get_json()
        director_data = director_schema.load(director_json, session=db.session)
        director_data.save_to_db()

        return director_schema.dump(director_data), 201
