"""
Director entity data schema
"""
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models.directors import Director


class DirectorSchema(SQLAlchemyAutoSchema):
    """Define marshmallow schema"""
    class Meta:
        """Define marshmallow schema"""
        model = Director
        load_instance = True
        include_fk = True

        fields = ("dir_first_name", "dir_last_name",)
