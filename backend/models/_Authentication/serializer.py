# encoding: utf-8
"""
Serializer: Authentication
--------------
"""
from flask_marshmallow import base_fields, Schema


class BearerTokenSerializer(Schema):
    access_token = base_fields.String(required=True, description="Authorization token which allows request to the backend")
    refresh_token = base_fields.String(required=False, description="Authorization Refresh token")
