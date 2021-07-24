"""
Genre Database model.
"""
from sqlalchemy import exc
from .. import db


class Genre(db.Model):
    """
    Genre class
    """
    __tablename__ = 'genre'
    genre_id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, genre_name):
        """
        Constructor
        :param genre_name: genre`s name
        """
        self.genre_name = genre_name

    def to_dict(self) -> dict:
        """
        Convert genre object to dict
        :return: genre
        """
        return {
            'genre_name': self.genre_name
        }

    def __repr__(self) -> str:
        """
        Convert genre to string
        :return: genre
        """
        return '<Genre (genre_id = {genre_id}, '\
               'genre_name = {genre_name}>'.format(genre_id=self.genre_id,
                                                   genre_name=self.genre_name)

    @classmethod
    def find_all(cls) -> object:
        """
        Function to find all records of an entity Genre
        :return: genre class object
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
