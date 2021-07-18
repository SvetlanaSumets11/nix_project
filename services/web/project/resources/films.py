"""
Director entity resources
"""
import logging

from flask import request
from flask_restx import Resource
from flask_login import login_required, current_user

from ..modelschemas.films import FilmSchema
from ..models.films import Film
from .. import db

from . import check_recurring_movie

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
        logging.info("All films are displayed")
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
                logging.info("Invalid data. Film %s", film_json["film_name"])
                return {"status": 401, "message": "Invalid data"}

            film_data.save_to_db()
            logging.info("Film added. Film %s", film_json["film_name"])
            return film_schema.dump(film_data), 201

        logging.info("User is not admin. User %s", current_user.user_login)
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
        film_data = Film.query.get(film_id)

        if film_data:
            logging.info("Film returned from ID %d. Film %s", film_id, film_data.film_name)
            return film_schema.dump(film_data), 200

        logging.info("Film with ID %d was not found", film_id)
        return {"status": 404, 'message': FILM_NOT_FOUND}

    @classmethod
    @login_required
    def delete(cls, film_id) -> dict:
        """
        Delete method
        :param film_id: film`s id
        :return: error message or successful message
        """
        film_data = Film.query.get(film_id)
        if film_data:
            if current_user.is_authenticated:

                if current_user.is_admin or current_user.user_id == film_data.user_id:
                    film_data.delete_from_db()
                    logging.info("Film Deleted successfully. Film %s", film_data.film_name)
                    return {"status": 200, 'message': "Film Deleted successfully"}

                logging.info("User is not admin or film owner. User %s", current_user.user_login)
                return {"status": 401, "reason": "User is not admin or film owner"}

            logging.info("User is not authenticated. User %s", current_user.user_login)
            return {"status": 401, "reason": "User is not authenticated"}

        logging.info("%s Film with ID %d", FILM_NOT_FOUND, film_id)
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

        owner = current_user.user_id == film_data.user_id

        if current_user.is_authenticated:
            if current_user.is_admin or owner:
                if owner:
                    if check_recurring_movie(film_json)[0]:
                        logging.info("%s already add this film. Film %s",
                                     current_user.user_login, film_json["film_name"])
                        return {"status": 404, 'message': "You already add this film"}
                try:
                    film_data.film_name = film_json['film_name']
                    film_data.release_date = film_json['release_date']
                    film_data.description = film_json['description']
                    film_data.rating = Film.validate_rating(film_json['rating'])
                    film_data.poster = film_json['poster']
                except AssertionError:
                    logging.info("Invalid data. Film %s", film_json["film_name"])
                    return {"status": 401, "message": "Invalid data"}
            else:
                logging.info("User is not admin or film owner. User %s", current_user.user_login)
                return {"status": 401, "reason": "User is not admin or film owner"}
        else:
            logging.info("User is not authenticated. User %s", current_user.user_login)
            return {"status": 401, "reason": "User is not authenticated"}

        film_data.save_to_db()
        logging.info("Film data changed successfully. Film %s", film_data.film_name)
        return film_schema.dump(film_data), 200
