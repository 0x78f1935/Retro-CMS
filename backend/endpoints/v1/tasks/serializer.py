"""
Serializer: System Tasks
---------------
Introduce system schemas
"""
from flask_marshmallow import Schema, base_fields


class SystemTaskSerializer(Schema):
    task = base_fields.Integer(required=True, description='Task ID')
    is_running = base_fields.Boolean(description='Indicates if the task is running')
