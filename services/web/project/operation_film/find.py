"""
Module for searching for a movie by partial match of the title
"""
from flask_restx import Resource

from ..models.films import Film
from . import valid_return


def film_find(film_name: str) -> list:
    """
    Function for searching for a movie by partial match of the title
    :param film_name: any part of the movie name to search
    :return: all relevant objects of the class Film
    """
    search = '%' + film_name + '%'
    return Film.query.filter(Film.film_name.like(search)).all()


class Find(Resource):
    """Class for searching for a movie by partial match of the title"""
    @classmethod
    def get(cls, name: str) -> dict:
        """
        Get method
        :param name: any part of the movie name to search
        :return: all relevant objects of the class Film in JSON format
        """
        films = film_find(name)
        return valid_return(films, name, 'find/')
