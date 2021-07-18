"""
Director entity resources
"""
import logging

from flask import request
from flask_restx import Resource
from flask_login import login_required, current_user

from ..modelschemas.genres import GenreSchema
from ..models.genres import Genre
from . import already_exist
from .. import db

GENRE_NOT_FOUND = "Genre not found."
genre_schema = GenreSchema()
genre_list_schema = GenreSchema(many=True)


class GenreList(Resource):
    """Genre Data Resource Class"""

    @classmethod
    def get(cls) -> (dict, int):
        """
        Get method
        :return: error message or json with information about the genre
        """
        logging.info("All genres are displayed")
        return genre_list_schema.dump(Genre.find_all()), 200

    @classmethod
    @login_required
    def post(cls) -> (dict, int):
        """
        Post method
        :return: json with information about the genre
        """
        if current_user.is_authenticated and current_user.is_admin:
            genre_json = request.get_json()

            if already_exist(Genre, genre_json):
                logging.info("Genre already exists. Genre %s", genre_json["genre_name"])
                return {"status": 401, "reason": "Genre already exist"}

            genre_data = genre_schema.load(genre_json, session=db.session)
            genre_data.save_to_db()
            logging.info("Genre added. Genre %s", genre_json["genre_name"])
            return genre_schema.dump(genre_data), 201

        logging.info("User is not admin. User %s", current_user.user_login)
        return {"status": 401, "reason": "User is not admin"}


class GenreListId(Resource):
    """Genre Data Resource Class"""

    @classmethod
    def get(cls, genre_id) -> (dict, int):
        """
        Get method
        :param genre_id: genre`s id
        :return: error message or json with information about the genre
        """
        genre_data = Genre.query.get(genre_id)

        if genre_data:
            logging.info("Genre returned from ID %d. Genre %s", genre_id, genre_data.genre_name)
            return genre_schema.dump(genre_data), 200

        logging.info("Genre with ID %d was not found", genre_id)
        return {"status": 404, 'message': GENRE_NOT_FOUND}

    @classmethod
    @login_required
    def delete(cls, genre_id) -> dict:
        """
        Delete method
        :param genre_id: genre`s id
        :return: error message or successful message
        """
        if current_user.is_authenticated and current_user.is_admin:
            genre_data = Genre.query.get(genre_id)

            if genre_data:
                genre_data.delete_from_db()
                logging.info("Genre Deleted successfully. Genre %s", genre_data.genre_name)
                return {"status": 200, 'message': "Genre Deleted successfully"}

            logging.info("%s Genre with ID %d", GENRE_NOT_FOUND, genre_id)
            return {"status": 404, 'message': GENRE_NOT_FOUND}

        logging.info("User is not admin. User %s", current_user.user_login)
        return {"status": 401, "reason": "User is not admin"}

    @classmethod
    @login_required
    def put(cls, genre_id) -> (dict, int):
        """
        Put method
        :param genre_id: genre`s id
        :return: json with information about the genre
        """
        if current_user.is_authenticated and current_user.is_admin:
            genre_data = Genre.query.get(genre_id)
            genre_json = request.get_json()

            if not genre_data:
                logging.info("%s Genre with ID %d", GENRE_NOT_FOUND, genre_id)
                return {"status": 404, 'message': GENRE_NOT_FOUND}

            if already_exist(Genre, genre_json):
                logging.info("Genre already exist. Genre %s", genre_json["genre_name"])
                return {"status": 401, "reason": "Genre already exist"}

            genre_data.genre_name = genre_json['genre_name']
            genre_data.save_to_db()
            logging.info("Genre data changed successfully. Genre %s", genre_data.genre_name)
            return genre_schema.dump(genre_data), 200

        logging.info("User is not admin. User %s", current_user.user_login)
        return {"status": 401, "reason": "User is not admin"}
