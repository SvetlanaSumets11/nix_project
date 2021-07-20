"""
Module for testing user authorization in the system
"""
import pytest
from .setting_login_signup import form_parametrize_query_login
from .setting_login_signup import form_parametrize_query_signup


@pytest.mark.parametrize("test_arg, expected", form_parametrize_query_login("login"))
def test_query_user_login(test_arg: int, expected: int) -> None:
    """
    Testing login method for users
    :param test_arg: The error code that was received
    :param expected: Error code what was expected
    :return: None
    """
    assert test_arg == expected


@pytest.mark.parametrize("test_arg, expected", form_parametrize_query_signup("signup"))
def test_query_user_signup(test_arg, expected):
    """
    Testing signup method for users.
    Warning: the test can be run once, to run it again, it is worth restarting the containers
    (after the first run of the test, records will be added to the database, and the ban on
    adding the same data will be triggered on restarting, then the error code will be 401,
    because such records will already exist, and the test will not pass. When you restart
    the container, the data will be overwritten with the original)
    :param test_arg: The error code that was received
    :param expected: Error code what was expected
    :return: None
    """
    assert test_arg == expected
