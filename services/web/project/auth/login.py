"""
User authorization module
"""
from flask import request, jsonify
from flask_login import LoginManager, login_user, logout_user
from .. import app
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
    return UserList.get(user_id)


@app.route('/login', methods=['POST'])
def login():
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
    return jsonify({'result': 200, 'data': {'message': 'login success'}})


@app.route('/authorize', methods=['POST'])
def authorize():
    """
    Function for creating a user in the system
    :return: error message or json with information about the user
    """
    user_json = request.get_json()
    user = User.query.filter_by(user_login=user_json['user_login']).first()

    if user:
        return jsonify({"status": 401, "reason": "User already exists"})
    return UserList.post()


@app.route('/logout', methods=['POST'])
def logout():
    """
    Function for user login
    :return: successful message
    """
    logout_user()
    return jsonify({'result': 200, 'data': {'message': 'logout success'}})
