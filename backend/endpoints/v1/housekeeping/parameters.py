# encoding: utf-8
"""
Parameters: Users
------------------
"""
from flask_marshmallow import base_fields
from backend.utilities.base import ParameterBaseModel

from backend.endpoints.v1.users.schemas import UsersSchema


class DeleteUserParameters(ParameterBaseModel):
    """
    Schema which represents input details when deleting a user
    """
    class Meta:
        ordered = True
        fields = ('id',)
    id = base_fields.Int(required = True, description = "User ID")


class PatchUserParameters(ParameterBaseModel):
    """
    Schema which represents input details when patching a user
    """
    class Meta:
        ordered = True
        fields = ('id',)
    id = base_fields.Int(required = True, description = "User ID")


class UpdateUsersParameters(ParameterBaseModel, UsersSchema):
    """
    Schema which represents input details when patching a user
    """
    class Meta:
        ordered = True
        fields = ('real_name', 'motto', 'rank', 'credits', 'pixels', 'points',)
