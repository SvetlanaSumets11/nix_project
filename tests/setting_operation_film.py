"""
Module for generating parameters for testing operations on films
"""
import requests
from . import PORT, NUM, FILM_PART, YEAR
from . import GENRE_PART_EXIST, GENRE_PART_NOT_EXIST
from . import DIRECTOR_PART_EXIST, DIRECTOR_PART_NOT_EXIST


def form_parametrize_query_operation(method: str, expected: int = None) -> list:
    """
    Function for forming parameters
    :param method: info/find/filter/sort
    :param expected: error code what is expected
    :return: list of parameters for testing
    """
    result = []
    if method == "info":
        for iid in range(NUM):
            result.append((form_link(method, iid), expected))
    if method == "find":
        for part in FILM_PART:
            result.append((form_link(method, part), expected))
    if method == "filter/genre":
        for part in GENRE_PART_EXIST:
            result.append((form_link(method, part), 200))
        for part in GENRE_PART_NOT_EXIST:
            result.append((form_link(method, part), 404))
    if method == "filter/director":
        for part in DIRECTOR_PART_EXIST:
            result.append((form_link(method, part), 200))
        for part in DIRECTOR_PART_NOT_EXIST:
            result.append((form_link(method, part), 404))
    if method == "filter/year":
        for part in YEAR:
            result.append((form_link(method, part), expected))
    if method == "sort":
        for sort in ["rating", "date"]:
            result.append((form_link(method, sort), expected))
    return result


def form_link(method: str, iid_or_part) -> int:
    """
    Function to return the request error code
    :param method: info/find/filter/sort
    :param iid_or_part: unique object number or part of name
    :return: request error code
    """
    return requests.get(f"http://localhost:{PORT}/film/{method}/{iid_or_part}").status_code
