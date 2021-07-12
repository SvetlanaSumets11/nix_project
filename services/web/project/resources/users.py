"""
Director entity resources
"""
from flask import request
from flask_restx import Resource

from ..modelschemas.users import UserSchema
from ..models.users import User
from .. import db


class UserList(Resource):
    """User Data Resource Class"""
    USER_NOT_FOUND = "User not found."
    user_schema = UserSchema()
    user_list_schema = UserSchema(many=True)

    def get(self, user_id=None):
        """
        Get method
        :param user_id: user`s id
        :return: error message or json with information about the user
        """
        if not user_id:
            return self.user_list_schema.dump(User.find_all()), 200
        user_data = User.query.get_or_404(user_id)
        if user_data:
            return self.user_schema.dump(user_data), 200
        return {'message': self.USER_NOT_FOUND}, 404

    def delete(self, user_id):
        """
        Delete method
        :param user_id: user`s id
        :return: error message or successful message
        """
        user_data = User.query.get_or_404(user_id)
        if user_data:
            user_data.delete_from_db()
            return {'message': "User Deleted successfully"}, 200
        return {'message': self.USER_NOT_FOUND}, 404

    def put(self, user_id):
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
            user_data.is_admin = user_json['is_admin']
            user_data.first_name = user_json['first_name']
            user_data.last_name = user_json['last_name']
            user_data.email = user_json['email']
        else:
            user_data = self.user_schema.load(user_json, session=db.session)

        user_data.save_to_db()
        return self.user_schema.dump(user_data), 200

    def post(self):
        """
        Post method
        :return: json with information about the user
        """
        user_json = request.get_json()
        user_data = self.user_schema.load(user_json, session=db.session)
        user_data.save_to_db()

        return self.user_schema.dump(user_data), 201
