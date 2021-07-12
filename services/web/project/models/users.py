"""
User Database model.
"""
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from .. import db
from sqlalchemy import exc


class User(UserMixin, db.Model):
    """
    User class
    """
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    user_login = db.Column(db.String(50), unique=True, nullable=False)
    user_password = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)

    film_users = db.relationship('Film', backref='user_film', lazy=True)

    def __init__(self, user_login, user_password, is_admin, first_name, last_name, email):
        """
        Constructor
        :param user_login: users`s personal login name
        :param user_password: user`s secret conditional character set
        :param is_admin: flag whether the user is an admin
        :param first_name: users`s first name
        :param last_name: users`s last name
        :param email: user`s mail for sending and receiving emails
        """
        self.user_login = user_login
        self.user_password = user_password
        self.is_admin = is_admin
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def check_password(self, password) -> bool:
        """
        Managing passwords using Werkzeug security library
        :param password: user`s secret conditional character set
        :return: boolean of whether the password was correct
        """
        return check_password_hash(self.user_password, password)

    def set_password(self, password) -> None:
        """
        Set user`s password
        :param password: user`s secret conditional character set
        """
        self.user_password = generate_password_hash(password)  # from werkzeug.security

    def to_dict(self) -> dict:
        """
        Convert user object to dict
        :return: user
        """
        return {
            'user_id': self.user_id,
            'user_login': self.user_login,
            'user_password': self.user_password,
            'is_admin': self.is_admin,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }

    def __repr__(self) -> str:
        """
        Convert user to string
        :return: user
        """
        return '<User (user_id = {user_id}, user_login = {user_login}, '\
               'user_password = {user_password}, is_admin = {is_admin}, '\
               'first_name = {first_name}, last_name = {last_name},'\
               'email = {email}>'.format(user_id=self.user_id,
                                         user_login=self.user_login,
                                         user_password=self.user_password,
                                         is_admin=self.is_admin,
                                         first_name=self.first_name,
                                         last_name=self.last_name,
                                         email=self.email)

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()

    def delete_from_db(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
