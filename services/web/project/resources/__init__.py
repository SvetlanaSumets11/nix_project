"""
Module for the function of checking the existence of a row in the database"
"""
from flask_login import current_user
from ..models.films import Film
from ..models.users import User


def already_exist(entity, list_json: list) -> bool:
    """
    Checking for the existence row of such a entity
    :param entity: entity
    :param list_json: Entity data entered by the user
    :return: Status found or not
    """
    for obj in entity.query.all():
        row = entity.query.filter(obj.to_dict() == list_json).first()
        if row:
            return True
    return False


def check_recurring_movie(data_json) -> (bool, list):
    """
    Function for checking if there is such a movie in the data base
    :param data_json: information about the movie, that the user entered
    :return: flag whether there is such a movie in the data base
    """
    film_info = [current_user.get_id(), data_json['film_name'], data_json['release_date'],
                 data_json['description'], data_json['rating'], data_json['poster']]

    films = Film.query.filter(Film.user_id == current_user.get_id()).all()

    for film in films:
        film_in = [getattr(film, 'film_name'), str(getattr(film, 'release_date')),
                   getattr(film, 'description'), getattr(film, 'rating'), getattr(film, 'poster')]

        if film_in == film_info[1:]:
            return True, film_info

    return False, film_info


def user_already_exist(list_json: dict) -> bool:
    """
    Function of checking for the existence of a user in the system
    :param list_json: Entity data entered by the user
    :return: Status found or not
    """
    users = User.query.all()
    for user in users:
        login = user.user_login == list_json["user_login"]
        email = user.email == list_json["email"]
        row = User.query.filter(login and email or login or email).first()
        if row:
            return True
    return False
