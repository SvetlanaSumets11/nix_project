"""
Director Database model.
"""
from .. import db
from sqlalchemy import exc


class Director(db.Model):
    """
    Director class
    """
    __tablename__ = 'director'
    director_id = db.Column(db.Integer, primary_key=True)
    dir_first_name = db.Column(db.String(50), nullable=False)
    dir_last_name = db.Column(db.String(50), nullable=False)

    film_directors = db.relationship('FilmDirector', backref='director_film', lazy=True)

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
