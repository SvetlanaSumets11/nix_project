"""
Director entity resources
"""
from flask import request
from flask_restx import Resource

from ..modelschemas.films import FilmSchema
from ..models.films import Film
from .. import db


class FilmList(Resource):
    """Film Data Resource Class"""
    FILM_NOT_FOUND = "Film not found."
    film_schema = FilmSchema()
    film_list_schema = FilmSchema(many=True)

    def get(self, film_id=None):
        """
        Get method
        :param film_id: film`s id
        :return: error message or json with information about the film
        """
        if not film_id:
            return self.film_list_schema.dump(Film.find_all()), 200
        film_data = Film.query.get_or_404(film_id)
        if film_data:
            return self.film_schema.dump(film_data), 200
        return {'message': self.FILM_NOT_FOUND}, 404

    def delete(self, film_id):
        """
        Delete method
        :param film_id: film`s id
        :return: error message or successful message
        """
        film_data = Film.query.get_or_404(film_id)
        if film_data:
            film_data.delete_from_db()
            return {'message': "Film Deleted successfully"}, 200
        return {'message': self.FILM_NOT_FOUND}, 404

    def put(self, film_id):
        """
        Put method
        :param film_id: film`s id
        :return: json with information about the film
        """
        film_data = Film.query.get_or_404(film_id)
        film_json = request.get_json()

        if film_data:
            film_data.user_id = film_json['user_id']
            film_data.film_name = film_json['film_name']
            film_data.release_date = film_json['release_date']
            film_data.description = film_json['description']
            film_data.rating = film_json['rating']
            film_data.poster = film_json['poster']
        else:
            film_data = self.film_schema.load(film_json, session=db.session)

        film_data.save_to_db()
        return self.film_schema.dump(film_data), 200

    def post(self):
        """
        Post method
        :return: json with information about the film
        """
        film_json = request.get_json()
        film_data = self.film_schema.load(film_json, session=db.session)
        film_data.save_to_db()

        return self.film_schema.dump(film_data), 201
