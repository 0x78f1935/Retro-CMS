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
    assets_ran = base_fields.Boolean(description='Indicator if the application contains required assets')
    assets_status = base_fields.Integer(description='Last known status of the downloader')
    converter_ran = base_fields.Boolean(description='Indicator if the application ran the converter before')
    converter_status = base_fields.Integer(description='Last known status of the converter')
