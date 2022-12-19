# encoding: utf-8
"""
Model: System Task
-------------
"""
from backend.extensions import db
from backend.utilities.models import Model


class SystemTaskModel(db.Model, Model):
    """System Tasks table

    Columns:
        sysname (str): Name of the task which the system uses to identify the task
        name (str): The name of a task the server might run, used in frontend
        description (str): The description of a task the server might run, used in frontend
        running (bool): Indicator if the task is running
        exit_code (Int): Last known exit code status
        has_ran (bool): Once True this task has been ran before successfully

    properties:
        is_running (bool): Indication if the task is running
    """
    __tablename__ = "system_tasks"
    sysname = db.Column(db.String(25), nullable=False, unique=True)  # Name of the task which the system uses to identify the task
    name = db.Column(db.String(25), nullable=False)  # Name of the task
    description = db.Column(db.String(250), nullable=False)  # Task description
    running = db.Column(db.Boolean, default=False, nullable=False)  # Indicator if the task is running
    exit_code = db.Column(db.BigInteger, default=404, nullable=False)  # Last known exit status code
    has_ran = db.Column(db.Boolean, default=False, nullable=False)  # Once True this task has been ran before successfully

    @property
    def is_running(self):
        return self.running
