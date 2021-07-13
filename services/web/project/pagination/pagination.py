"""
Pagination module
"""
from flask import request, jsonify
from .. import app

from ..resources.genres import GenreList
from ..resources.directors import DirectorList
from ..resources.films import FilmList
from ..resources.users import UserList

from ..models.films import Film

from . import get_paginated_list


@app.route('/genre', methods=['GET'])
def get_pagination_genres():
    """
    Function for pagination of genres, start displaying posts
    from the first, total on a page of 10 posts
    :return: JSON
    """
    return jsonify(get_paginated_list(
        data=GenreList.get()[0],
        route='/genre',
        start=request.args.get('start', 1),
        limit=request.args.get('limit', 10)))


@app.route('/film', methods=['GET'])
def get_pagination_films():
    """
    Function for pagination of films, start displaying posts
    from the first, total on a page of 10 posts
    :return: JSON
    """
    return jsonify(get_paginated_list(
        data=FilmList.get()[0],
        route='/film',
        start=request.args.get('start', 1),
        limit=request.args.get('limit', 10)))


@app.route('/user', methods=['GET'])
def get_pagination_users():
    """
    Function for pagination of users, start displaying posts
    from the first, total on a page of 10 posts
    :return: JSON
    """
    return jsonify(get_paginated_list(
        data=UserList.get()[0],
        route='/user',
        start=request.args.get('start', 1),
        limit=request.args.get('limit', 10)))


@app.route('/director', methods=['GET'])
def get_pagination_directors():
    """
    Function for pagination of directors, start displaying posts
    from the first, total on a page of 10 posts
    :return: JSON
    """
    return jsonify(get_paginated_list(
        data=DirectorList.get()[0],
        route='/director',
        start=request.args.get('start', 1),
        limit=request.args.get('limit', 10)))


@app.route('/film/find', methods=['GET'])
def get_pagination_films_find():
    films_find = request.args.get('name')

    search = '%' + films_find + '%'
    films = Film.query.filter(Film.film_name.like(search)).all()

    if not films:
        return {"status": 401, "reason": "Film does not exist"}

    film_list = [{
        'film_name': film.film_name,
        'release_date': film.release_date,
        'description': film.description,
        'rating': film.rating,
        'poster': film.poster
    } for film in films]

    return jsonify(get_paginated_list(
        data=film_list,
        route='/film/find',
        start=request.args.get('start', 1),
        limit=request.args.get('limit', 10),
        name=films_find))
