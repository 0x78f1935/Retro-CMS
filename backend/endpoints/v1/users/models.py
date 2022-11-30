# encoding: utf-8
"""
Models: Users
-------------
"""
from flask import current_app
from flask_smorest import abort
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

from cryptography.fernet import Fernet
from datetime import datetime, timedelta
from base64 import b64encode
from uuid import uuid4
import jwt

from backend.config import connection_url
from backend.extensions import db, bcrypt
from backend.utilities.base import BaseModel
from backend.utilities.http import HTTPSchemas, HTTPStatus

load_dotenv()
engine = create_engine(connection_url, convert_unicode=True, echo=False)
Base = declarative_base()
Base.metadata.reflect(engine)


class UserModel(db.Model):
    __table__ = Base.metadata.tables['users']
    
    authentication = db.relationship(
        'AuthenticationModel',
        back_populates='user',
        cascade='delete,delete-orphan',
        passive_deletes=True,
        uselist=False
    )

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
        return jwt.encode(
            {
                'sub': self.id,  # Issuer
                'iat': datetime.utcnow(),  # JWT issue date
                'exp': datetime.utcnow() + timedelta(minutes=int(current_app.config['JWT_EXPIRE_IN_MINUTES'])),
            },
            current_app.config['SECRET_KEY']
        )


class AuthenticationModel(db.Model, BaseModel):
    """Authentication model"""
    __tablename__ = 'cms_authentication'

    user_id = db.Column(db.Integer, db.ForeignKey(UserModel.id, ondelete='CASCADE'), nullable=False)
    user = db.relationship('UserModel', back_populates='authentication')
    
    password = db.Column(db.Text, nullable=False)
    scope = db.Column(db.Text, nullable=False, default='retro:guest')

    def __repr__(self):
        return f'<Authentication Model {self.id}: {self.user.username}>'

    @property
    def __fer(self):
        return Fernet(b64encode(f'{self.user.id}{self.user.ip_register}{self.user.mail}{uuid4()}'[:32].encode('utf8')).decode())

    def set_password(self, pwd):
        self.password = self.__fer.encrypt(bcrypt.generate_password_hash(pwd.encode('utf8')))
        db.session.commit()
    
    def check_password(self, guess):
        return bcrypt.check_password_hash(self.__fer.decrypt(self.password.encode('utf8')).decode(), guess)

    @property
    def scopes(self):
        """Return all available scopes"""
        return self.scope.split(';')
