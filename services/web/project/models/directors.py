"""
Director Database model.
"""
from sqlalchemy import exc
from .. import db


class Director(db.Model):
    """
    Director class
    """
    __tablename__ = 'director'
    director_id = db.Column(db.Integer, primary_key=True)
    dir_first_name = db.Column(db.String(50), nullable=False)
    dir_last_name = db.Column(db.String(50), nullable=False)

    def __init__(self, dir_first_name, dir_last_name):
        """
        Constructor
        :param dir_first_name: director`s first name
        :param dir_last_name: director`s first name
        """
        self.dir_first_name = dir_first_name
        self.dir_last_name = dir_last_name

    def to_dict(self) -> dict:
        """
        Convert director object to dict
        :return: director
        """
        return {
            'dir_first_name': self.dir_first_name,
            'dir_last_name': self.dir_last_name
        }

    def __repr__(self) -> str:
        """
        Convert director to string
        :return: director
        """
        return '<Director (director_id = {director_id}, '\
               'dir_first_name = {dir_first_name}, '\
               'dir_last_name = {dir_last_name}>'.format(director_id=self.director_id,
                                                         dir_first_name=self.dir_first_name,
                                                         dir_last_name=self.dir_last_name)

    @classmethod
    def find_all(cls) -> object:
        """
        Function to find all records of an entity Director
        :return: director class object
        """
        return cls.query.all()

    def save_to_db(self) -> None:
        """
        Function to save a record in the database
        :return: None
        """
        try:
            db.session.add(self)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()

    def delete_from_db(self) -> None:
        """
        Function to delete a record in the database
        :return: None
        """
        try:
            db.session.delete(self)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
