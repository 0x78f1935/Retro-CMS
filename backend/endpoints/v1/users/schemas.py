# encoding: utf-8
"""
Schemas: Users
--------------
"""
from marshmallow_sqlalchemy import SQLAlchemySchema, SQLAlchemyAutoSchema
from .models import UserModel


class UsersSchema(SQLAlchemyAutoSchema):
    """
    Schema which represents skills presented on the website
    """
    class Meta:
        model = UserModel
        load_instance = False  # Optional: deserialize to model instances
        ordered = True
