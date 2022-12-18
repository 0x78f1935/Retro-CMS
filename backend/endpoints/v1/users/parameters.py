# encoding: utf-8
"""
Parameters: Users
------------------
"""
from flask_marshmallow import base_fields
from backend.utilities.parameters import Parameters

from backend.models import UserSerializer


class UserRegistrationParameters(Parameters, UserSerializer):
    """
    Schema which represents input details when registering a new user
    """
    class Meta:
        ordered = True
        fields = ('username', 'password', 'email',)


class UserAuthorizationParameters(Parameters, UserSerializer):
    """
    Schema which represents input details when authorizing a new user
    """
    class Meta:
        ordered = True
        fields = ('email', 'password',)


class UpdateMeParameters(Parameters, UserSerializer):
    """
    Schema which represents input details when a logged in user wants to update information about themself.
    """
    class Meta:
        ordered = True
        fields = ('password', 'motivation', 'home_room')
    password = base_fields.String(required=False, description="Provide when changing password")
