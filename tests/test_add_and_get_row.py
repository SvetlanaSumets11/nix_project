"""
A module for testing the correct addition of value to the database,
the correct return of ID values, valid data addition
"""
import requests
import pytest
from services.web.project.models.films import Film
from services.web.project.models.users import User
from . import PORT, ENTITIES, DATA_1, RATING


def test_new_entities(new_entity: list) -> None:
    """
    Tests correct addition to the database
    :param new_entity: Fixture - a list of objects of all existing entities
    :return: None
    """
    assert new_entity[0].dir_first_name == "Filanova"
    assert new_entity[0].dir_last_name == "Svetlana"

    assert new_entity[1].genre_name == "Military"

    assert new_entity[2].user_login == "KovalenkoDen"
    assert new_entity[2].first_name == "Kovalenko"
    assert new_entity[2].last_name == "Denis"
    assert new_entity[2].email == "kovalenko@gmail.com"

    assert new_entity[3].user_id == 1
    assert new_entity[3].film_name == "Some film"
    assert new_entity[3].release_date == "2004-11-16"
    assert new_entity[3].description == "Some description"
    assert new_entity[3].rating == 3.2
    assert new_entity[3].poster == "http://some_link"

    assert new_entity[4].film_id == 1
    assert new_entity[4].genre_id == 1

    assert new_entity[5].film_id == 2
    assert new_entity[5].director_id == 2


def test_get_row() -> None:
    """
    Tests the correct return of data by ID
    :return: None
    """
    for entity, data in zip(ENTITIES, DATA_1):
        response = requests.get(f"http://localhost:{PORT}/{entity}/1")
        json_list = response.json()
        if entity == "users":
            del json_list["user_password"]
        assert json_list == data


def test_valid_user_login() -> None:
    """
    Tests the validation function for the user login when adding user data to the database
    :return: None
    """
    with pytest.raises(AssertionError):
        User("Sv", "1234", "Svetlana", "Sumets", "svetlanasum@gmail.com")


def test_valid_user_first_name() -> None:
    """
    Tests the validation function for the user`s first_name when adding user data to the database
    :return: None
    """
    with pytest.raises(AssertionError):
        User("SvetlanaSum11", "1234", "Sv", "Sumets", "svetlanasum@gmail.com")


def test_valid_user_last_name() -> None:
    """
    Tests the validation function for the user`s last_name when adding user data to the database
    :return: None
    """
    with pytest.raises(AssertionError):
        User("SvetlanaSum11", "1234", "Svetlana", "Sum", "svetlanasum@gmail.com")


def test_valid_user_email() -> None:
    """
    Tests the validation function for the user`s email when adding user data to the database
    :return: None
    """
    with pytest.raises(AssertionError):
        User("SvetlanaSum11", "1234", "Svetlana", "Sumets", "svetlanasumgmail.com")


@pytest.mark.parametrize("rating", RATING)
def test_valid_film_rating(rating: int) -> None:
    """
    Tests the validation function for the film`s rating when adding film data to the database
    :param rating: average movie rating
    :return: None
    """
    with pytest.raises(AssertionError):
        Film(1, "Some film", "2001-12-19", "Some description", rating, "http://some_link")
