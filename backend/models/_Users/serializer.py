# encoding: utf-8
"""
Schemas: Users
--------------
"""
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from flask_marshmallow import base_fields
from backend.models import UserModel


class UserSerializer(SQLAlchemyAutoSchema):
    """
    Schema which represents skills presented on the website
    """
    class Meta:
        model = UserModel
        load_instance = False  # Optional: deserialize to model instances
        ordered = True
    id = auto_field(description="The ID of the Task")
    created = auto_field(description="The datetime this task was created")
    updated = auto_field(description="The datetime this task was updated")
    username = auto_field(description="The name of the user, the username")
    password = auto_field(description="Hold the status of the password of the user")
    email = auto_field(description="E-mail address of the user")
    mail_verified = auto_field(description="Indicator if the e-mail address of the user is validated")
    last_login = auto_field(description="Datetime which indicates the last time the user logged in")
    last_online = auto_field(description="Datetime which indicates the last time the user was seen online")
    motivation = auto_field(description="Holds the users motto")
    look = auto_field(description="Holds the look of the user")
    gender = auto_field(description="Holds the gender of the user")
    rank = auto_field(description="Holds the rank of the user")
    credits = auto_field(description="The total amount of credits the user has")
    pixels = auto_field(description="The total amount of pixels the user has")
    points = auto_field(description="The total amount of points the user has")
    diamonds = auto_field(description="The total amount of diamonds the user has")
    online = auto_field(description="Indicator if the user is currently online")
    auth_ticket = auto_field(description="SSO Ticket required for the client to start")
    ip_register = auto_field(description="IP address of the user when the account got registered")
    ip_current = auto_field(description="Current IP of the user")
    home_room = auto_field(description="The room set which the user will spawn in")
    template = auto_field(description="Theme of the website")


class SSOTokenSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('auth_ticket', 'scope',)
    scope = base_fields.List(base_fields.Str, required=True, description="Same scope as JWT token.")
