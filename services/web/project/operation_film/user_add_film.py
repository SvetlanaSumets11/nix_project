"""
Module for implementing the ability to add a movie by the user
"""
from flask_login import login_required, current_user
from flask_restx import Resource
from flask import request

from ..models.films_directors import FilmDirector
from ..models.films_genres import FilmGenre
from ..models.directors import Director
from ..models.genres import Genre
from ..models.films import Film


def check_genre(genre_list: list):
    """
    The function checks for the presence in the database of each genre that
    the user wrote for his movie, if the genre does not exist, it will return
    an error, otherwise - a list of objects of the Genre class
    :param genre_list: list of movie genres that the user has entered
    :return: error massage or list of objects of the Genre class corresponding
    to the genre that the user wrote
    """
    genre_obj_list = []

    for genre in genre_list:
        is_genre = Genre.query.filter(Genre.genre_name == genre).first()
        if not is_genre:
            return {"status": 401, "reason": "Genre do not exist"}
        genre_obj_list.append(is_genre)

    return genre_obj_list


def check_add_director(director_list: list) -> list:
    """
    The function checks for the presence in the database of each directors that
    the user wrote for his movie (if the director does not exist, it will be added
    to the database), then function return a list of objects of the Director class
    :param director_list: list of movie directors that the user has entered
    :return: list of objects of the Director class corresponding to
    the directors that the user wrote
    """
    director_obj_list = []

    for director in director_list:
        is_director = Director.query.filter(Director.dir_first_name == director[0],
                                            Director.dir_last_name == director[1]).first()
        if not is_director:
            is_director = Director(director[0], director[1])
            is_director.save_to_db()
        director_obj_list.append(is_director)

    return director_obj_list


def final_save(film_info: list, genre_obj_list: list, director_obj_list: list) -> dict:
    """
    A function to save the entered data about the film (and optionally the director)
    in the database. Movie-genre, movie-director records are added to the many-to-many
    intermediate link tables
    :param film_info: movie data
    :param genre_obj_list: list of objects of class Genre
    :param director_obj_list: list of objects of class Director
    :return: successful sms
    """
    film = Film(*film_info)
    film.save_to_db()

    for genre in genre_obj_list:
        film_genre = FilmGenre(film.film_id, genre.genre_id)
        film_genre.save_to_db()

    for director in director_obj_list:
        film_director = FilmDirector(film.film_id, director.director_id)
        film_director.save_to_db()

    return {"status": 201, "message": "Movie added successfully"}


class AddFilm(Resource):
    """Class for implementing the ability to add a movie by the user"""
    @classmethod
    @login_required
    def post(cls) -> dict:
        """
        Post method
        :return: failed sms or successful sms
        """
        data_json = request.get_json()

        film_info = [current_user.get_id(), data_json['film_name'], data_json['release_date'],
                     data_json['description'], data_json['rating'], data_json['poster']]

        genre_list = data_json['genre_name']
        director_list = list(zip(data_json['dir_first_name'], data_json['dir_last_name']))

        genre = check_genre(genre_list)
        director = check_add_director(director_list)

        if current_user.is_authenticated:
            if not isinstance(genre, dict):
                return final_save(film_info, genre, director)
            return genre
        return {"status": 401, "reason": "User is not authenticated"}
