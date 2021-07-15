"""
FilmDirector Database model.
"""
from sqlalchemy import exc
from .. import db


class FilmDirector(db.Model):
    """
    FilmDirector class
    """
    __tablename__ = 'film_director'
    film_director_id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey("film.film_id", ondelete='SET NULL'))
    director_id = db.Column(db.Integer, db.ForeignKey("director.director_id", ondelete='SET NULL'))

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

    @classmethod
    def find_all(cls) -> object:
        """
        Function to find all records of an entity FilmDirector
        :return: film-director class object
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
