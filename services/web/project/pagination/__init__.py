"""
Module for main function pagination
"""
from flask import abort
from flask import request, jsonify


def return_json_pagination(data: list, route: str) -> dict:
    """
    Function to return the query result in JSON format, the result is paginated
    :param data:result data
    :param route: access link
    :return: JSON dict
    """
    return jsonify(get_paginated_list(
        data=data,
        route=route,
        start=request.args.get('start', 1),
        limit=request.args.get('limit', 5)), 200)


def get_paginated_list(data: list, route: str, start: int, limit: int, arg: str = None) -> dict:
    """
    Main function pagination
    :param arg: query parameter
    :param data: entity data
    :param route: access link
    :param start: id of the recording from which the output starts
    :param limit: the number of records to be displayed on the page
    :return: dict - pagination information
    """
    start = int(start)
    limit = int(limit)
    count = len(data)
    if count < start or limit < 0:
        abort(404)

    info = {'start': start, 'limit': limit, 'count': count}

    if start == 1:
        info['previous'] = ''
    else:
        if not arg:
            info['previous'] = route + '?start=%d&limit=%d' \
                           % (max(1, start - limit), start - 1)
        else:
            info['previous'] = route + '%s?start=%d&limit=%d' \
                               % (arg, max(1, start - limit), start - 1)

    if start + limit > count:
        info['next'] = ''
    else:
        if not arg:
            info['next'] = route + '?start=%d&limit=%d' % (start + limit, limit)
        else:
            info['next'] = route + '%s?start=%d&limit=%d' % (arg, start + limit, limit)

    info['data'] = data[(start - 1):(start - 1 + limit)]
    return info
