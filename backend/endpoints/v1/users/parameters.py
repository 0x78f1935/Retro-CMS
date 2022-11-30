# encoding: utf-8
"""
Parameters: Users
------------------
"""
from .schemas import UsersSchema
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
