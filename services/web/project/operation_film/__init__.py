"""
Module for output functions
"""
import logging

from flask import request, jsonify

from ..pagination import get_paginated_list


def results(films: list, arg: str, route: str) -> dict:
    """
    Function to return the query result in JSON format, the result is paginated
    :param films: result data
    :param arg: argument in link
    :param route: access link
    :return: JSON dict
    """
    film_list = []
    for film in films:
        film_list.append(film.to_dict())

    return jsonify(get_paginated_list(
        data=film_list,
        route='/film/' + route,
        start=request.args.get('start', 1),
        limit=request.args.get('limit', 10),
        arg=arg), 200)


def valid_return(films: list, arg: str, route: str) -> dict:
    """
    Function to final return
    :param films: result data
    :param arg: argument in link
    :param route: access link
    :return: JSON dict with query result or error sms
    """
    if films:
        return results(films, arg, route)

    logging.info("Film was not found")
    return {"status": 404, "reason": "Films do not exist"}
