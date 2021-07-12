"""
Director entity resources
"""
from flask import request
from flask_restx import Resource

from ..modelschemas.directors import DirectorSchema
from ..models.directors import Director
from .. import db


class DirectorList(Resource):
    """Director Data Resource Class"""
    DIRECTOR_NOT_FOUND = "Director not found."
    director_schema = DirectorSchema()
    director_list_schema = DirectorSchema(many=True)

    def get(self, director_id=None):
        """
        Get method
        :param director_id: director`s id
        :return: error message or json with information about the directors
        """
        if not director_id:
            return self.director_list_schema.dump(Director.find_all()), 200
        director_data = Director.query.get_or_404(director_id)
        if director_data:
            return self.director_schema.dump(director_data), 200
        return {'message': self.DIRECTOR_NOT_FOUND}, 404

    def delete(self, director_id):
        """
        Delete method
        :param director_id: director`s id
        :return: error message or successful message
        """
        director_data = Director.query.get_or_404(director_id)
        if director_data:
            director_data.delete_from_db()
            return {'message': "Director Deleted successfully"}, 200
        return {'message': self.DIRECTOR_NOT_FOUND}, 404

    def put(self, director_id):
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
            director_data = self.director_schema.load(director_json, session=db.session)

        director_data.save_to_db()
        return self.director_schema.dump(director_data), 200

    def post(self):
        """
        Post method
        :return: json with information about the directors
        """
        director_json = request.get_json()
        director_data = self.director_schema.load(director_json, session=db.session)
        director_data.save_to_db()

        return self.director_schema.dump(director_data), 201
