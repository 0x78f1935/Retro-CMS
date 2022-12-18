# encoding: utf-8
"""
Models: Users
-------------
"""
from flask import current_app
from flask_smorest import abort
from flask_login import UserMixin
from flask_jwt_extended import create_access_token, create_refresh_token

from datetime import datetime, timedelta
from secrets import token_urlsafe
import jwt

from backend.extensions import db
from backend.utilities.models import Model
from backend.utilities.http import HTTPSchemas, HTTPStatus


class UserModel(db.Model, UserMixin, Model):
    __tablename__ = "users"

    authentication = db.relationship(
        'AuthenticationModel',
        back_populates='user',
        cascade='delete,delete-orphan',
        passive_deletes=True,
        uselist=False
    )

    username = db.Column(db.String(25), nullable=False, unique=True)  # Username
    password = db.Column(db.String(64), nullable=False)  # Placeholder password column
    email = db.Column(db.String(500), nullable=False, unique=True)  # Provided email
    mail_verified = db.Column(db.Boolean, default=False)  # User mail verification indicator
    last_login = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # Last time the user logged in
    last_online = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # Last time the user logged out
    motivation = db.Column(db.String(127), default='New arrival!', nullable=False)  # The motivation of a user
    look = db.Column(db.String(127), default='hr-115-42.hd-195-19.ch-3030-82.lg-275-1408.fa-1201.ca-1804-64', nullable=False)
    gender = db.Column(db.Enum('M', 'F',), default='M', nullable=False)  # Gender,
    rank = db.Column(db.Integer, default=1, nullable=False)  # The default permissions the user gets
    credits = db.Column(db.Integer, default=2500, nullable=False)  # Amount of credits user has
    pixels = db.Column(db.Integer, default=500, nullable=False)  # Amount of pixels a user has
    points = db.Column(db.Integer, default=10, nullable=False)  # Amount of points a user has
    diamonds = db.Column(db.Integer, default=5, nullable=False)  # Amount of diamonds a user has
    online = db.Column(db.Boolean, default=False, nullable=False)  # Indicator if the user is online
    auth_ticket = db.Column(db.String(1024), default='', nullable=False)  # auth_ticket to play the game
    ip_register = db.Column(db.String(45), nullable=False)  # Registered IP when account got created
    ip_current = db.Column(db.String(45), nullable=False)  # Current IP user
    home_room = db.Column(db.Integer, default=0, nullable=False)  # Starting room user
    template = db.Column(db.String(25), default="dark", nullable=False)  # CMS Theme, dark mode default
    
    _access_token = None
    _refresh_token = None

    def generate_sso_ticket(self) -> str:
        """
        Generates SSO ticket

        Returns:
            str: SSO ticket
        """
        self.auth_ticket = token_urlsafe(256)
        db.session.commit()
        return self.auth_ticket

    @classmethod
    def decode_jwt(cls, request):
        """Decodes content of bearer header present in request header.

        Only works if the request in question requires to be authenticated

        Args:
            request (flask request): from flask import request

        Returns:
            dict: decoded format of the JWT token
        """
        access_token = request.headers.get('Authorization', '').split().pop(1)
        try:
            return jwt.decode(access_token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.InvalidSignatureError:
            return abort(HTTPStatus.UNAUTHORIZED, **HTTPSchemas.Unauthorized().dump({
                'message': 'Bearer: Signature verification failed.',
                'errors': {
                    'token': ['signature']
                }
            }))
        except jwt.ExpiredSignatureError:
            return abort(HTTPStatus.UNAUTHORIZED, **HTTPSchemas.Unauthorized().dump({
                'message': 'Bearer: Expired token. Re-authentication required.',
                'errors': {
                    'token': ['expired']
                }
            }))
        except (jwt.InvalidTokenError):
            return abort(HTTPStatus.UNAUTHORIZED, **HTTPSchemas.Unauthorized().dump({
                'message': 'Bearer: Invalid Token',
                'errors': {
                    'token': ['invalid']
                }
            }))
    
    @property
    def access_token(self):
        return self._access_token

    @property
    def refresh_token(self):
        return self._refresh_token

    def to_dict(self, exclude: tuple = tuple()):
        """Converts model into json blob"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name not in exclude}

    def update(self, formdata, commit: bool = True):
        for k, v in formdata.items():
            if hasattr(self, k):
                setattr(self, k, v)
        if commit:
            db.session.add(self)
            db.session.commit()
