"""
A module for implementing all the necessary functions for testing login and signup
"""
import json
import requests
from . import PORT, HEADERS, USER_LOGIN_DATA, USER_SIGNUP_DATA


def form_parametrize_query_login(method: str) -> list:
    """
    Function for forming parameters
    :param method: login
    :return: list of parameters for testing
    """
    result = []
    expected = {'status': 200, 'massage': 'login success'}

    for user in USER_LOGIN_DATA:
        response = requests.post(form_link_auth(method),
                                 data=json.dumps(user), headers=HEADERS).text
        result.append((json.loads(response), expected))
    return result


def form_parametrize_query_signup(method: str) -> list:
    """
    Function for forming parameters
    :param method: signup
    :return: list of parameters for testing
    """
    result = []

    for user in USER_SIGNUP_DATA:
        expected = [user["user_login"], user["email"]]
        response = requests.post(form_link_auth(method),
                                 data=json.dumps(user), headers=HEADERS).text
        data = [json.loads(response)["user_login"], json.loads(response)["email"]]
        result.append((data, expected))
    return result


def form_link_auth(method: str) -> str:
    """
    Function for forming a link
    :param method: login/signup
    :return: str link
    """
    return f"http://localhost:{PORT}/user/{method}"
