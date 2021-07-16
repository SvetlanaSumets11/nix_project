"""
Director entity resources
"""
from flask import request
from flask_restx import Resource
from flask_login import login_required, current_user

from ..modelschemas.films import FilmSchema
from ..models.films import Film
from .. import db


FILM_NOT_FOUND = "Film not found."
film_schema = FilmSchema()
film_list_schema = FilmSchema(many=True)


class FilmList(Resource):
    """Film Data Resource Class"""

    @classmethod
    def get(cls) -> (dict, int):
        """
        Get method
        :return: error message or json with information about the film
        """
        return film_list_schema.dump(Film.find_all()), 200

    @classmethod
    @login_required
    def post(cls) -> (dict, int):
        """
        Post method
        :return: json with information about the film
        """
        if current_user.is_authenticated and current_user.is_admin:
            film_json = request.get_json()
            try:
                film_data = film_schema.load(film_json, session=db.session)
            except AssertionError:
                return {"status": 401, "message": "Invalid data"}

            film_data.save_to_db()

            return film_schema.dump(film_data), 201
        return {"status": 401, "reason": "User is not admin"}


class FilmListId(Resource):
    """Film Data Resource Class"""

    @classmethod
    def get(cls, film_id) -> (dict, int):
        """
        Get method
        :param film_id: film`s id
        :return: error message or json with information about the film
        """
        film_data = Film.query.get_or_404(film_id)
        if film_data:
            return film_schema.dump(film_data), 200
        return {"status": 404, 'message': FILM_NOT_FOUND}

    @classmethod
    @login_required
    def delete(cls, film_id) -> dict:
        """
        Delete method
        :param film_id: film`s id
        :return: error message or successful message
        """
        film_data = Film.query.get_or_404(film_id)
        if film_data:
            if current_user.is_authenticated:
                if current_user.is_admin or current_user.user_id == film_data.user_id:
                    film_data.delete_from_db()
                    return {"status": 200, 'message': "Film Deleted successfully"}
                return {"status": 401, "reason": "User is not admin or film owner"}
            return {"status": 401, "reason": "User is not authenticated"}
        return {"status": 404, 'message': FILM_NOT_FOUND}

    @classmethod
    @login_required
    def put(cls, film_id) -> (dict, int):
        """
        Put method
        :param film_id: film`s id
        :return: json with information about the film
        """
        film_data = Film.query.get_or_404(film_id)
        film_json = request.get_json()

        if film_data:
            if current_user.is_authenticated:
                if current_user.is_admin or current_user.user_id == film_data.user_id:
                    film_data.film_name = film_json['film_name']
                    film_data.release_date = film_json['release_date']
                    film_data.description = film_json['description']
                    film_data.rating = film_json['rating']
                    film_data.poster = film_json['poster']
                else:
                    return {"status": 401, "reason": "User is not admin or film owner"}
            else:
                return {"status": 401, "reason": "User is not authenticated"}
        else:
            film_data = film_schema.load(film_json, session=db.session)

        film_data.save_to_db()
        return film_schema.dump(film_data), 200
