"""
Director Database model.
"""
from .. import db


class Director(db.Model):
    """
    Director class
    """
    __tablename__ = 'director'
    director_id = db.Column(db.Integer, primary_key=True)
    dir_first_name = db.Column(db.String(50), nullable=False)
    dir_last_name = db.Column(db.String(50), nullable=False)

    film_director = db.relationship('Director', backref='film_director', lazy='joined')

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
            'director_id': self.director_id,
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
