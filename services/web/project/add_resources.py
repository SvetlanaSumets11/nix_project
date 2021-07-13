"""
Module with routes
"""
from . import api
from .resources.directors import DirectorList, DirectorListId
from .resources.genres import GenreList, GenreListId
from .resources.films import FilmList, FilmListId
from .resources.users import UserList, UserListId


api.add_resource(FilmList, "/films")
api.add_resource(FilmListId, "/films/<int:film_id>")

api.add_resource(UserList, "/users")
api.add_resource(UserListId, "/users/<int:user_id>")

api.add_resource(GenreList, "/genres")
api.add_resource(GenreListId, "/genres/<int:genre_id>")

api.add_resource(DirectorList, "/directors")
api.add_resource(DirectorListId, "/directors/<int:director_id>")
