"""
Film Database model.
"""
from .. import db


class Film(db.Model):
    """
    Film class
    """
    __tablename__ = 'film'
    film_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    film_name = db.Column(db.String(50), nullable=False)
    release_date = db.Column(db.Date)
    description = db.Column(db.Text)
    rating = db.Column(db.Integer)
    poster = db.Column(db.String(100))

    film_director = db.relationship('FilmDirector', backref='film', lazy='joined')
    film_genre = db.relationship('FilmGenre', backref='film', lazy='joined')

    def __init__(self, *args):
        """
        Constructor
        :param user_id: users`s id, where user is the person who added the movie
        :param film_name: movie title
        :param release_date: movie release date
        :param description: movie information
        :param rating: average movie rating
        :param poster: movie cover link
        """
        self.user_id, self.film_name,\
            self.release_date, self.description,\
            self.rating, self.poster = args

    def to_dict(self) -> dict:
        """
        Convert film object to dict
        :return: film
        """
        return {
            'film_id': self.film_id,
            'user_id': self.user_id,
            'film_name': self.film_name,
            'release_date': self.release_date,
            'description': self.description,
            'rating': self.rating,
            'poster': self.poster
        }

    def __repr__(self) -> str:
        """
        Convert film to string
        :return: film
        """
        return '<Film (film_id = {film_id}, user_id = {user_id}, '\
               'film_name = {film_name}, release_date = {release_date}, '\
               'description = {description}, rating = {rating},'\
               'poster = {poster}>'.format(film_id=self.film_id, user_id=self.user_id,
                                           film_name=self.film_name,
                                           release_date=self.release_date,
                                           description=self.description,
                                           rating=self.rating, poster=self.poster)
