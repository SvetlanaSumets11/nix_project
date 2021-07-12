"""
Director entity resources
"""
from flask import request
from flask_restx import Resource

from ..modelschemas.genres import GenreSchema
from ..models.genres import Genre
from .. import db


class GenreList(Resource):
    """Genre Data Resource Class"""
    GENRE_NOT_FOUND = "Genre not found."
    genre_schema = GenreSchema()
    genre_list_schema = GenreSchema(many=True)

    def get(self, genre_id=None):
        """
        Get method
        :param genre_id: genre`s id
        :return: error message or json with information about the genre
        """
        if not genre_id:
            return self.genre_list_schema.dump(Genre.find_all()), 200
        genre_data = Genre.query.get_or_404(genre_id)
        if genre_data:
            return self.genre_schema.dump(genre_data), 200
        return {'message': self.GENRE_NOT_FOUND}, 404

    def delete(self, genre_id):
        """
        Delete method
        :param genre_id: genre`s id
        :return: error message or successful message
        """
        genre_data = Genre.query.get_or_404(genre_id)
        if genre_data:
            genre_data.delete_from_db()
            return {'message': "Genre Deleted successfully"}, 200
        return {'message': self.GENRE_NOT_FOUND}, 404

    def put(self, genre_id):
        """
        Put method
        :param genre_id: genre`s id
        :return: json with information about the genre
        """
        genre_data = Genre.query.get_or_404(genre_id)
        genre_json = request.get_json()

        if genre_data:
            genre_data.genre_name = genre_json['genre_name']
        else:
            genre_data = self.genre_schema.load(genre_json, session=db.session)

        genre_data.save_to_db()
        return self.genre_schema.dump(genre_data), 200

    def post(self):
        """
        Post method
        :return: json with information about the genre
        """
        genre_json = request.get_json()
        genre_data = self.genre_schema.load(genre_json, session=db.session)
        genre_data.save_to_db()

        return self.genre_schema.dump(genre_data), 201
