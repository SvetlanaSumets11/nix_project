"""
Film Database model.
"""
from sqlalchemy import exc
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
    rating = db.Column(db.Float, nullable=False)
    poster = db.Column(db.Text)

    film_directors = db.relationship('Director', secondary='film_director')
    film_genres = db.relationship("Genre", secondary='film_genre')

    def __init__(self, user_id, film_name, release_date, description, rating, poster):
        """
        Constructor
        :param user_id: users`s id, where user is the person who added the movie
        :param film_name: movie title
        :param release_date: movie release date
        :param description: movie information
        :param rating: average movie rating
        :param poster: movie cover link
        """
        self.user_id = user_id
        self.film_name = film_name
        self.release_date = release_date
        self.description = description
        self.rating = Film.validate_rating(rating)
        self.poster = poster

    @classmethod
    def validate_rating(cls, rating: float) -> float:
        """
        Check validation of rating
        :param rating: average movie rating
        :return: rating
        """
        if not rating:
            raise AssertionError("Rating is None")
        if rating > 10 or rating < 0:
            raise AssertionError("Rating should be between 0 and 10")
        return rating

    def to_dict(self) -> dict:
        """
        Convert film object to dict
        :return: film
        """
        return {
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

    @classmethod
    def find_all(cls) -> object:
        """
        Function to find all records of an entity Film
        :return: film class object
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
