"""
User authorization module
"""
from flask import request, jsonify
from flask_login import LoginManager, login_user, logout_user
from flask_restx import Resource

from .. import app, db

from ..models.users import User
from ..resources.users import UserList


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    """
    User loader
    :param user_id: users`s id, where user is the person who added the system
    :return: error message or json with information about the user
    """
    return User.query.get(int(user_id))


class Login(Resource):
    """Class for user login"""
    @classmethod
    def post(cls) -> dict:
        """
        Function for user login
        :return: error message or successful message
        """
        user_json = request.get_json()
        user = User.query.filter_by(user_login=user_json['user_login']).first()

        if not user:
            if not user.check_password(user_json['user_password']):
                return jsonify({"status": 401, "reason": "Username or Password Error"})

        login_user(user)
        db.session.commit()
        return jsonify({'result': 200, 'data': {'message': 'login success'}})


class SignUp(Resource):
    """Class for creating a user in the system"""
    @classmethod
    def post(cls) -> dict:
        """
        Function for creating a user in the system
        :return: error message or json with information about the user
        """
        user_json = request.get_json()
        user = User.query.filter_by(user_login=user_json['user_login']).first()

        if user:
            return jsonify({"status": 401, "reason": "User already exists"})
        return UserList.post()


class Logout(Resource):
    """Class for user logout"""
    @classmethod
    def post(cls) -> dict:
        """
        Function for user logout
        :return: successful message
        """
        logout_user()
        return jsonify({'result': 200, 'data': {'message': 'logout success'}})
