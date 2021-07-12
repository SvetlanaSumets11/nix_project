"""
Genre Database model.
"""
from .. import db
from sqlalchemy import exc


class Genre(db.Model):
    """
    Genre class
    """
    __tablename__ = 'genre'
    genre_id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(50), nullable=False)

    film_genres = db.relationship('FilmGenre', backref='genre_film', lazy=True)

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
            'genre_id': self.genre_id,
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
