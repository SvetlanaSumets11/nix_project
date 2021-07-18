"""
Director entity resources
"""
import logging

from flask import request
from flask_restx import Resource
from flask_login import login_required, current_user

from ..modelschemas.users import UserSchema
from ..models.users import User
from . import user_already_exist
from .. import db


USER_NOT_FOUND = "User not found."
user_schema = UserSchema()
user_list_schema = UserSchema(many=True)


class UserList(Resource):
    """User Data Resource Class"""

    @classmethod
    def get(cls) -> (dict, int):
        """
        Get method
        :return: error message or json with information about the user
        """
        logging.info("All users are displayed")
        return user_list_schema.dump(User.find_all()), 200

    @classmethod
    def post(cls) -> (dict, int):
        """
        Post method
        :return: json with information about the user
        """
        user_json = request.get_json()

        if user_already_exist(user_json):
            logging.info("User already exists. User %s", user_json["user_login"])
            return {"status": 401, "reason": "User already exist"}

        try:
            user_data = user_schema.load(user_json, session=db.session)
        except AssertionError:
            logging.info("Invalid data. User %s", user_json["user_login"])
            return {"status": 401, "message": "Invalid data"}

        user_data.save_to_db()

        logging.info("User added. User %s", user_json["user_login"])
        return user_schema.dump(user_data), 201


class UserListId(Resource):
    """User Data Resource Class"""

    @classmethod
    def get(cls, user_id) -> (dict, int):
        """
        Get method
        :param user_id: user`s id
        :return: error message or json with information about the user
        """
        user_data = User.query.get(user_id)

        if user_data:
            logging.info("User returned from ID %d. User %s", user_id, user_data.user_login)
            return user_schema.dump(user_data), 200

        logging.info("User with ID %d was not found", user_id)
        return {"status": 404, 'message': USER_NOT_FOUND}

    @classmethod
    @login_required
    def delete(cls, user_id) -> dict:
        """
        Delete method
        :param user_id: user`s id
        :return: error message or successful message
        """
        if current_user.is_authenticated and current_user.is_admin:
            user_data = User.query.get(user_id)

            if user_data:
                user_data.delete_from_db()
                logging.info("User Deleted successfully. User %s", user_data.user_login)
                return {"status": 200, 'message': "User Deleted successfully"}

            logging.info("%s User with ID %d", USER_NOT_FOUND, user_id)
            return {"status": 404, 'message': USER_NOT_FOUND}

        logging.info("User is not admin. User %s", current_user.user_login)
        return {"status": 401, "reason": "User is not admin"}

    @classmethod
    @login_required
    def put(cls, user_id) -> (dict, int):
        """
        Put method
        :param user_id: user`s id
        :return: json with information about the user
        """
        if current_user.is_authenticated and current_user.is_admin:
            user_data = User.query.get(user_id)
            user_json = request.get_json()

            if not user_data:
                logging.info("%s User with ID %d", USER_NOT_FOUND, user_id)
                return {"status": 404, 'message': USER_NOT_FOUND}

            if user_already_exist(user_json):
                logging.info("User already exist. User %s", user_json["user_login"])
                return {"status": 401, "reason": "User already exist"}

            try:
                user_data.user_login = User.validate_login_name(user_json['user_login'])
                user_data.user_password = user_json['user_password']
                user_data.first_name = User.validate_login_name(user_json['first_name'])
                user_data.last_name = User.validate_login_name(user_json['last_name'])
                user_data.email = User.validate_email(user_json['email'])
            except AssertionError:
                logging.info("Invalid data. User %s", user_json["user_login"])
                return {"status": 401, "message": "Invalid data"}

            user_data.save_to_db()
            logging.info("User data changed successfully. User %s", user_data.user_login)
            return user_schema.dump(user_data), 200

        logging.info("User is not admin. User %s", current_user.user_login)
        return {"status": 401, "reason": "User is not admin"}
