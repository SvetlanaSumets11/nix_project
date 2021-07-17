"""
Module for displaying complete information about the film
"""
from flask_restx import Resource
from flask import jsonify

from ..models.films_directors import FilmDirector
from ..models.films_genres import FilmGenre
from ..models.directors import Director
from ..models.genres import Genre
from ..models.films import Film
from ..models.users import User


def genre_director_json(genre_or_director: list) -> dict:
    """
    Function for converting the data of the entity Director or Genre to JSON format
    :param genre_or_director: list of Director or Genre entity objects
    :return: JSON dict
    """
    genre_director_list = []
    for genre_director in genre_or_director:
        genre_director_list.append(genre_director.to_dict())
    if not genre_director_list:
        genre_director_list = {'director': 'unknown'}

    return genre_director_list


def film_user_json(obj) -> dict:
    """
    Function for converting the data of the entity User or Film to JSON format
    :param obj: User entity or Film entity object
    :return: JSON dict
    """
    return obj.to_dict()


def return_json(film_list, user_list, genre_list, director_list):
    """
    Final JSON with all information
    :param film_list: film data JSON dictionary
    :param user_list: user data JSON dictionary
    :param genre_list: genre data JSON dictionary
    :param director_list: director data JSON dictionary
    :return: JSON dict
    """
    final_list = dict()
    final_list['film'] = film_list
    final_list['user'] = user_list
    final_list['genre'] = genre_list
    final_list['director'] = director_list

    return jsonify(final_list)


class Print(Resource):
    """Class for displaying complete information about the film"""
    @classmethod
    def get(cls, film_id: int) -> dict:
        """
        Get method
        :param film_id: film`s id
        :return: Full information about the movie: data about the movie,
        the user who added it, genres and directors
        """
        film = Film.query.filter(Film.film_id == film_id).first()
        if film:
            user = User.query.filter(User.user_id == film.user_id).first()
            genres = Genre.query.join(FilmGenre).filter(FilmGenre.film_id == film_id).all()
            directors = Director.query.join(FilmDirector).filter(FilmDirector.film_id == film_id)

            return return_json(film_user_json(film), film_user_json(user),
                               genre_director_json(genres), genre_director_json(directors))
        return {"status": 404, 'message': 'Film does not exist'}
