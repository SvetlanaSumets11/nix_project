"""
Module for testing get/delete/put methods for all database entities
"""
import pytest
from .setting_get_delete_put import form_parametrize_query


@pytest.mark.parametrize("test_arg, expected", form_parametrize_query("getId", 200))
def test_query_get_id(test_arg: int, expected: int) -> None:
    """
    Testing get method with ID for all database entities
    :param test_arg: The error code that was received
    :param expected: Error code what was expected
    :return: None
    """
    assert test_arg == expected


@pytest.mark.parametrize("test_arg, expected", form_parametrize_query("get", 200))
def test_query_get(test_arg: int, expected: int) -> None:
    """
    Testing get method for all database entities
    :param test_arg: The error code that was received
    :param expected: Error code what was expected
    :return: None
    """
    assert test_arg == expected


@pytest.mark.parametrize("test_arg, expected", form_parametrize_query("delete", 401))
def test_query_delete_not_auth_admin(test_arg: int, expected: int) -> None:
    """
    Testing delete method for all database entities
    provided that the user has not previously logged in to the system
    :param test_arg: The error code that was received
    :param expected: Error code what was expected
    :return: None
    """
    assert test_arg == expected


@pytest.mark.parametrize("test_arg, expected", form_parametrize_query("put", 401))
def test_query_put_not_auth_admin(test_arg: int, expected: int) -> None:
    """
    Testing put method for all database entities
    provided that the user has not previously logged in to the system
    :param test_arg: The error code that was received
    :param expected: Error code what was expected
    :return: None
    """
    assert test_arg == expected
