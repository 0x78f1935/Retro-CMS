# encoding: utf-8
"""
Parameters: Users
------------------
"""
from .schemas import UsersSchema
from flask_marshmallow import base_fields
from backend.utilities.base import ParameterBaseModel


class UserRegistrationParameters(ParameterBaseModel, UsersSchema):
    """
    Schema which represents input details when registering a new user
    """
    class Meta:
        ordered = True
        fields = ('username', 'password', 'mail',)

class UserAuthorizationParameters(ParameterBaseModel, UsersSchema):
    """
    Schema which represents input details when authorizing a new user
    """
    class Meta:
        ordered = True
        fields = ('mail', 'password',)

class UpdateMeParameters(ParameterBaseModel, UsersSchema):
    """
    Schema which represents input details when a logged in user wants to update information about themself.
    """
    class Meta:
        ordered = True
        fields = ('real_name', 'password', 'motto',)
    password = base_fields.String(required=False, description="Provide when changing password")
