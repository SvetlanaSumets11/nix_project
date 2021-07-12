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
        GenreList.get()[0],
        '/genre',
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
        FilmList.get()[0],
        '/film',
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
        UserList.get()[0],
        '/user',
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
        DirectorList.get()[0],
        '/director',
        start=request.args.get('start', 1),
        limit=request.args.get('limit', 10)))
