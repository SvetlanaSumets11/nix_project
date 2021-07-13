"""
Pagination module
"""
from flask import request, jsonify
from .. import app

from ..resources.genres import GenreList
from ..resources.directors import DirectorList
from ..resources.films import FilmList
from ..resources.users import UserList


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
