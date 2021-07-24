"""
Module for filtering films by year range, genre and director
"""
import logging
from sqlalchemy import extract
from flask_restx import Resource

from ..models.films import Film
from ..models.genres import Genre
from ..models.directors import Director

from . import valid_return


def film_filter_year(starting: str, finishing: str) -> list:
    """
    Function for filtering films by year range
    :param starting: year at the beginning of the range for filtering
    :param finishing: year at the end of the range for filtering
    :return: all relevant objects of the class Film
    """
    return Film.query.filter(extract('year', Film.release_date).between(starting, finishing)).all()


def film_filter_genre(genre_name: str) -> list:
    """
    Function for filtering films by genre
    :param genre_name: any part of the genre`s name
    :return: all relevant objects of the class Film
    """
    search = '%' + genre_name + '%'
    return Film.query.join(Film.film_genres).filter(Genre.genre_name.ilike(search))


def film_filter_director(name_or_surname: str) -> list:
    """
    Function for filtering films by director
    :param name_or_surname: any part of the director`s first name or director`s last name
    :return: all relevant objects of the class Film
    """
    search = '%' + name_or_surname + '%'
    films = Film.query.join(Film.film_directors).filter(Director.dir_last_name.ilike(search))
    if not films.first():
        films = Film.query.join(Film.film_directors).filter(Director.dir_first_name.ilike(search))
    return films


class YearFilter(Resource):
    """Class for filtering films by year range"""
    @classmethod
    def get(cls, starting: str, finishing: str) -> dict:
        """
        Get method
        :param starting: year at the beginning of the range for filtering
        :param finishing: year at the end of the range for filtering
        :return: all relevant objects of the class Film in JSON format
        """
        films = film_filter_year(starting, finishing)
        logging.info("Filtered list of movies by year between %s and %s ", starting, finishing)
        return valid_return(films, starting + '/' + finishing, 'filter/year/')


class GenreFilter(Resource):
    """Class for filtering films by genre"""
    @classmethod
    def get(cls, genre_name: str) -> dict:
        """
        Get method
        :param genre_name: any part of the genre`s name
        :return: all relevant objects of the class Film in JSON format
        """
        films = film_filter_genre(genre_name)
        logging.info("Filtered list of movies by genre name with part %s", genre_name)
        return valid_return(films, genre_name, 'filter/genre/')


class DirectorFilter(Resource):
    """Class for filtering films by director"""
    @classmethod
    def get(cls, name_or_surname: str) -> dict:
        """
        Get method
        :param name_or_surname: any part of the director`s first name or director`s last name
        :return: all relevant objects of the class Film in JSON format
        """
        films = film_filter_director(name_or_surname)
        logging.info("Filtered list of movies by director first name or last name with part %s",
                     name_or_surname)
        return valid_return(films, name_or_surname, 'filter/director/')
