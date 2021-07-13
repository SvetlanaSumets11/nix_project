"""
Film entity data schema
"""
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models.films import Film


class FilmSchema(SQLAlchemyAutoSchema):
    """Define marshmallow schema"""
    class Meta:
        """Define marshmallow schema"""
        model = Film
        load_instance = True
        include_fk = True

        fields = ("user_id", "film_name", "release_date", "description", "rating", "poster", )
