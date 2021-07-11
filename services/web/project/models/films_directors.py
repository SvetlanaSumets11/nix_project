"""
FilmDirector Database model.
"""
from .. import db


class FilmDirector(db.Model):
    """
    FilmDirector class
    """
    __tablename__ = 'film_director'
    film_director_id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey("film.film_id"), nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey("director.director_id"), nullable=False)

    def __init__(self, film_id, director_id):
        """
        Constructor
        :param film_id: film`s id
        :param director_id: director`s id
        """
        self.film_id = film_id
        self.director_id = director_id

    def to_dict(self) -> dict:
        """
        Convert film-director object to dict
        :return: film-director
        """
        return {
            'film_director_id': self.film_director_id,
            'film_id': self.film_id,
            'director_id': self.director_id
        }

    def __repr__(self) -> str:
        """
        Convert film-director to string
        :return: film-director
        """
        return '<Film_Director (film_director_id = {film_director_id}, '\
               'film_id = {film_id}, director_id = {director_id}>'\
            .format(film_director_id=self.film_director_id,
                    film_id=self.film_id,
                    director_id=self.director_id)
