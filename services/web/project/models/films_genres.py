"""
FilmGenre Database model.
"""
from ..application import db


class FilmGenre(db.Model):
    """
    FilmGenre class
    """
    __tablename__ = 'film_genre'
    film_genre_id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey("film.film_id"), nullable=False, )
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.genre_id"), nullable=False)

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
