"""
Director entity resources
"""
from flask import request
from flask_restx import Resource

from ..modelschemas.genres import GenreSchema
from ..models.genres import Genre
from .. import db

GENRE_NOT_FOUND = "Genre not found."
genre_schema = GenreSchema()
genre_list_schema = GenreSchema(many=True)


class GenreList(Resource):
    """Genre Data Resource Class"""
    @classmethod
    def get(cls, genre_id=None):
        """
        Get method
        :param genre_id: genre`s id
        :return: error message or json with information about the genre
        """
        if not genre_id:
            return genre_list_schema.dump(Genre.find_all()), 200
        genre_data = Genre.query.get_or_404(genre_id)
        if genre_data:
            return genre_schema.dump(genre_data), 200
        return {'message': GENRE_NOT_FOUND}, 404

    @classmethod
    def delete(cls, genre_id):
        """
        Delete method
        :param genre_id: genre`s id
        :return: error message or successful message
        """
        genre_data = Genre.query.get_or_404(genre_id)
        if genre_data:
            genre_data.delete_from_db()
            return {'message': "Genre Deleted successfully"}, 200
        return {'message': GENRE_NOT_FOUND}, 404

    @classmethod
    def put(cls, genre_id):
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
            genre_data = genre_schema.load(genre_json, session=db.session)

        genre_data.save_to_db()
        return genre_schema.dump(genre_data), 200

    @classmethod
    def post(cls):
        """
        Post method
        :return: json with information about the genre
        """
        genre_json = request.get_json()
        genre_data = genre_schema.load(genre_json, session=db.session)
        genre_data.save_to_db()

        return genre_schema.dump(genre_data), 201
