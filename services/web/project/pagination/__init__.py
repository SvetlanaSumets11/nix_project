"""
Module for main function pagination
"""
from flask import abort


def get_paginated_list(data, route, start, limit) -> dict:
    """
    Main function pagination
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
        info['previous'] = route + '?start=%d&limit=%d' \
                           % (max(1, start - limit), start - 1)

    if start + limit > count:
        info['next'] = ''
    else:
        info['next'] = route + '?start=%d&limit=%d' % (start + limit, limit)

    info['data'] = data[(start - 1):(start - 1 + limit)]
    return info
