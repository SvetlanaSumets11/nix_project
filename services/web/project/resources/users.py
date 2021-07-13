"""
Director entity resources
"""
from flask import request
from flask_restx import Resource

from ..modelschemas.users import UserSchema
from ..models.users import User
from .. import db


USER_NOT_FOUND = "User not found."
user_schema = UserSchema()
user_list_schema = UserSchema(many=True)


class UserList(Resource):
    """User Data Resource Class"""

    @classmethod
    def get(cls):
        """
        Get method
        :return: error message or json with information about the user
        """
        return user_list_schema.dump(User.find_all()), 200

    @classmethod
    def post(cls):
        """
        Post method
        :return: json with information about the user
        """
        user_json = request.get_json()
        user_data = user_schema.load(user_json, session=db.session)
        user_data.save_to_db()

        return user_schema.dump(user_data), 201


class UserListId(Resource):
    """User Data Resource Class"""
    @classmethod
    def get(cls, user_id):
        """
        Get method
        :param user_id: user`s id
        :return: error message or json with information about the user
        """
        user_data = User.query.get_or_404(user_id)
        if user_data:
            return user_schema.dump(user_data), 200
        return {'message': USER_NOT_FOUND}, 404

    @classmethod
    def delete(cls, user_id):
        """
        Delete method
        :param user_id: user`s id
        :return: error message or successful message
        """
        user_data = User.query.get_or_404(user_id)
        if user_data:
            user_data.delete_from_db()
            return {'message': "User Deleted successfully"}, 200
        return {'message': USER_NOT_FOUND}, 404

    @classmethod
    def put(cls, user_id):
        """
        Put method
        :param user_id: user`s id
        :return: json with information about the user
        """
        user_data = User.query.get_or_404(user_id)
        user_json = request.get_json()

        if user_data:
            user_data.user_login = user_json['user_login']
            user_data.user_password = user_json['user_password']
            user_data.first_name = user_json['first_name']
            user_data.last_name = user_json['last_name']
            user_data.email = user_json['email']
        else:
            user_data = user_schema.load(user_json, session=db.session)

        user_data.save_to_db()
        return user_schema.dump(user_data), 200
