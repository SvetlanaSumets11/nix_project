"""
Module for sorting films by rating and release date
"""
from sqlalchemy import desc

from flask_restx import Resource

from ..models.films import Film
from . import valid_return


def film_sort(arg: str) -> list:
    """
    Function for sorting films by rating and release date
    :param arg: sort argument - rating or date
    :return: all relevant objects of the class Film
    """
    sorting = {'rating': Film.query.order_by(desc(Film.rating)).all(),
               "date": Film.query.order_by(desc(Film.release_date)).all()}

    return sorting.get(arg)


class Sort(Resource):
    """Class for sorting films by rating and release date"""
    @classmethod
    def get(cls, arg_sort: str) -> dict:
        """
        Get method
        :param arg_sort: sort argument - rating or date
        :return: all relevant objects of the class Film in JSON format
        """
        films = film_sort(arg_sort)
        return valid_return(films, arg_sort, 'sort/')
