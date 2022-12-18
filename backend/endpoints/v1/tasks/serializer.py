"""
Serializer: System Tasks
---------------
Introduce system schemas
"""
from flask_marshmallow import Schema, base_fields


class SystemTaskSerializer(Schema):
    thread_ident = base_fields.Integer(required=True, description='Thread ident')
    thread_name = base_fields.String(required=True, description='Thread name')
