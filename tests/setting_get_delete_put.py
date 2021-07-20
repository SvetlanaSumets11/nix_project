"""
A module for implementing all the necessary functions for testing get, delete, put methods
"""
import requests
from . import PORT, ENTITIES, NUM


def form_parametrize_query(method: str, code: int) -> list:
    """
    Function for forming parameters
    :param method: get/getId/delete/put
    :param code: error code
    :return: list of parameters for testing
    """
    result = []
    for iid in range(NUM):
        for entity in ENTITIES:
            result.append((form_link(method, entity, iid), code))
    return result


def form_link(method: str, entity: str, iid: int) -> int:
    """
    Function to return the request error code
    :param method: get/getId/delete/put
    :param entity: database entity
    :param iid: unique object number
    :return: request error code
    """
    list_method = {
        "get": requests.get(f"http://localhost:{PORT}/{entity}").status_code,
        "getId": requests.get(f"http://localhost:{PORT}/{entity}/{iid}").status_code,
        "delete": requests.delete(f"http://localhost:{PORT}/{entity}/{iid}").status_code,
        "put": requests.put(f"http://localhost:{PORT}/{entity}/{iid}").status_code
    }
    return list_method.get(method)
