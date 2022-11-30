# encoding: utf-8
"""
Schemas: Users
--------------
"""
from marshmallow_sqlalchemy import SQLAlchemySchema, SQLAlchemyAutoSchema
from flask_marshmallow import base_fields, Schema
from .models import UserModel


class UsersSchema(SQLAlchemyAutoSchema):
    """
    Schema which represents skills presented on the website
    """
    class Meta:
        model = UserModel
        load_instance = False  # Optional: deserialize to model instances
        ordered = True


class BearerTokenSchema(Schema):
    access_token = base_fields.String(required=True, description="Authorization token which allows request to the backend")
