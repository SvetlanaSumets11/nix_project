"""
FilmGenre Database model.
"""
from sqlalchemy import exc
from .. import db


class FilmGenre(db.Model):
    """
    FilmGenre class
    """
    __tablename__ = 'film_genre'
    film_genre_id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey("film.film_id", ondelete='SET NULL'))
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.genre_id", ondelete='SET NULL'))

    def __init__(self, film_id, genre_id):
        """
        Constructor
        :param film_id: film`s id
        :param genre_id: genre`s id
        """
        self.film_id = film_id
        self.genre_id = genre_id

    def to_dict(self) -> dict:
        """
        Convert film-genre object to dict
        :return: film-genre
        """
        return {
            'film_genre_id': self.film_genre_id,
            'film_id': self.film_id,
            'genre_id': self.genre_id
        }

    def __repr__(self) -> str:
        """
        Convert film-genre to string
        :return: film-genre
        """
        return '<Film_Genre (film_genre_id = {film_genre_id}, '\
               'film_id = {film_id}, genre_id = {genre_id}>'\
            .format(film_genre_id=self.film_genre_id,
                    film_id=self.film_id,
                    genre_id=self.genre_id)

    @classmethod
    def find_all(cls) -> object:
        """
        Function to find all records of an entity FilmGenre
        :return: film-genre class object
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
