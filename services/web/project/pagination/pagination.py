"""
Pagination module
"""
from flask_restx import Resource

from ..resources.genres import GenreList
from ..resources.directors import DirectorList
from ..resources.films import FilmList
from ..resources.users import UserList

from . import return_json_pagination


class PaginationGenre(Resource):
    """Class for pagination of genres"""
    @classmethod
    def get(cls) -> dict:
        """
        Function for pagination of genres, start displaying posts
        from the first, total on a page of 10 posts
        :return: JSON
        """
        return return_json_pagination(GenreList.get()[0], '/genre')


class PaginationFilm(Resource):
    """Class for pagination of films"""
    @classmethod
    def get(cls) -> dict:
        """
        Function for pagination of films, start displaying posts
        from the first, total on a page of 10 posts
        :return: JSON
        """
        return return_json_pagination(FilmList.get()[0], '/film')


class PaginationUser(Resource):
    """Class for pagination of users"""
    @classmethod
    def get(cls) -> dict:
        """
        Function for pagination of users, start displaying posts
        from the first, total on a page of 10 posts
        :return: JSON
        """
        return return_json_pagination(UserList.get()[0], '/user')


class PaginationDirector(Resource):
    """Class for pagination of directors"""
    @classmethod
    def get(cls) -> dict:
        """
        Function for pagination of directors, start displaying posts
        from the first, total on a page of 10 posts
        :return: JSON
        """
        return return_json_pagination(DirectorList.get()[0], '/director')
