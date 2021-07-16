"""
Module with routes
"""
from . import api

from .resources.directors import DirectorList, DirectorListId
from .resources.genres import GenreList, GenreListId
from .resources.films import FilmList, FilmListId
from .resources.users import UserList, UserListId

from .resources.user_add_film import AddFilm

from .pagination.pagination import PaginationFilm, PaginationGenre
from .pagination.pagination import PaginationUser, PaginationDirector

from .operation_film.find import Find
from .operation_film.sorting import Sort
from .operation_film.filter import YearFilter, GenreFilter, DirectorFilter

from .auth.login import Login, Logout, SignUp

from .operation_film.pretty_print import Print


# standard resources (all record) without pagination
api.add_resource(FilmList, "/films")
api.add_resource(UserList, "/users")
api.add_resource(GenreList, "/genres")
api.add_resource(DirectorList, "/directors")

# standard resources (one record)
api.add_resource(FilmListId, "/films/<int:film_id>")
api.add_resource(UserListId, "/users/<int:user_id>")
api.add_resource(GenreListId, "/genres/<int:genre_id>")
api.add_resource(DirectorListId, "/directors/<int:director_id>")

# get method (all record) with pagination - get
api.add_resource(PaginationFilm, "/film")
api.add_resource(PaginationUser, "/user")
api.add_resource(PaginationGenre, "/genre")
api.add_resource(PaginationDirector, "/director")

# user login - post
api.add_resource(Login, "/user/login")
api.add_resource(SignUp, "/user/signup")
api.add_resource(Logout, "/user/logout")

# operation with films(partial search) with pagination - get
api.add_resource(Find, "/film/find/<name>")

# operation with films(sort) with pagination -get
api.add_resource(Sort, "/film/sort/<arg_sort>")

# operation with films(filter) with partial search(except years) and pagination - get
api.add_resource(YearFilter, "/film/filter/year/<starting>/<finishing>")
api.add_resource(GenreFilter, "/film/filter/genre/<genre_name>")
api.add_resource(DirectorFilter, "/film/filter/director/<name_or_surname>")

# operation with films(add) - post
api.add_resource(AddFilm, "/film/add")

# pretty print information about film (info about film, user, genre, director)
api.add_resource(Print, "/film/info/<int:film_id>")
