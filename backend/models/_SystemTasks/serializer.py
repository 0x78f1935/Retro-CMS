# encoding: utf-8
"""
Serializer: System Tasks
--------------
"""
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from backend.models import SystemTaskModel


class SystemTaskSerializer(SQLAlchemyAutoSchema):
    """
    Schema which represents tasks running on the server
    """
    class Meta:
        model = SystemTaskModel
        load_instance = False  # Optional: deserialize to model instances
        ordered = True
    id = auto_field(description="The ID of the Task")
    created = auto_field(description="The datetime this task was created")
    updated = auto_field(description="The datetime this task was updated")
    sysname = auto_field(description="The name of a task the server might run")
    name = auto_field(description="The name of a task the server might run")
    description = auto_field(description="The description of a task the server might run")
    running = auto_field(description="Indicator if the task is running")
    exit_code = auto_field(description="Last known exit code of last ran task")
