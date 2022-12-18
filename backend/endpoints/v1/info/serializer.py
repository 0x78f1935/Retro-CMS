"""
Serializer: System Tasks
---------------
Introduce system schemas
"""
from flask_marshmallow import Schema, base_fields


class ApplicationResponseSerializer(Schema):
    name_short = base_fields.String(required=True, description='The name of the application, short as possible')
    name_long = base_fields.String(description='Indicates if the task is running, full name')
    logo = base_fields.String(description='Link to generated logo')
