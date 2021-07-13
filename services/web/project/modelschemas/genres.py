"""
Genre entity data schema
"""
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models.genres import Genre


class GenreSchema(SQLAlchemyAutoSchema):
    """Define marshmallow schema"""
    class Meta:
        """Define marshmallow schema"""
        model = Genre
        load_instance = True
        include_fk = True

        fields = ("genre_name",)
