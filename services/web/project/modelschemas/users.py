"""
User entity data schema
"""
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models.users import User


class UserSchema(SQLAlchemyAutoSchema):
    """Define marshmallow schema"""
    class Meta:
        """Define marshmallow schema"""
        model = User
        load_instance = True
        include_fk = True

        fields = ("user_login", "user_password", "is_admin", "first_name", "last_name", "email",)
