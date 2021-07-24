"""
Module for testing operations on films
"""
import pytest
from .setting_operation_film import form_parametrize_query_operation


@pytest.mark.parametrize("test_arg, expected", form_parametrize_query_operation("info", 200))
def test_query_get_film_info(test_arg: int, expected: int) -> None:
    """
    Testing pretty_print method for films
    :param test_arg: The error code that was received
    :param expected: Error code what was expected
    :return: None
    """
    assert test_arg == expected


@pytest.mark.parametrize("test_arg, expected", form_parametrize_query_operation("find", 200))
def test_query_get_film_find_part(test_arg: int, expected: int) -> None:
    """
    Testing get method of partial search by movie title
    :param test_arg: The error code that was received
    :param expected: Error code what was expected
    :return: None
    """
    assert test_arg == expected


@pytest.mark.parametrize("test_arg, expected", form_parametrize_query_operation("filter/genre"))
def test_query_film_filter_genre_part(test_arg: int, expected: int) -> None:
    """
    Testing get method of filtering method by genre
    (where the genre name can be specified as part of the name)
    :param test_arg: The error code that was received
    :param expected: Error code what was expected
    :return: None
    """
    assert test_arg == expected


@pytest.mark.parametrize("test_arg, expected", form_parametrize_query_operation("filter/director"))
def test_query_film_filter_director_part(test_arg: int, expected: int) -> None:
    """
    Testing get method of filtering method by director
    (where the director`s first name or last name can be specified as part of the name)
    :param test_arg: The error code that was received
    :param expected: Error code what was expected
    :return: None
    """
    assert test_arg == expected


@pytest.mark.parametrize("test_arg, expected", form_parametrize_query_operation("filter/year", 200))
def test_query_film_filter_year(test_arg: int, expected: int) -> None:
    """
    Testing get method of year range filtering
    :param test_arg: The error code that was received
    :param expected: Error code what was expected
    :return: None
    """
    assert test_arg == expected


@pytest.mark.parametrize("test_arg, expected", form_parametrize_query_operation("sort", 200))
def test_query_film_sort(test_arg: int, expected: int) -> None:
    """
        Testing get method of sorting movies by rating or release date
        :param test_arg: The error code that was received
        :param expected: Error code what was expected
        :return: None
        """
    assert test_arg == expected
