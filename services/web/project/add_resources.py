"""
Module with routes
"""
from . import api
from .resources.directors import DirectorList
from .resources.genres import GenreList
from .resources.films import FilmList
from .resources.users import UserList


api.add_resource(FilmList, "/films", "/films/<int:film_id>")
api.add_resource(UserList, "/users", "/users/<int:user_id>")
api.add_resource(GenreList, "/genres", "/genres/<int:genre_id>")
api.add_resource(DirectorList, "/directors", "/directors/<int:director_id>")
