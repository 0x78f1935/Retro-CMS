# encoding: utf-8
"""
Models: Users
-------------
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from flask import current_app
from base64 import b64encode

from backend.config import connection_url
from backend.extensions import db
from backend.utilities.base import BaseModel

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


class AuthenticationModel(db.Model, BaseModel):
    """Authentication model"""
    __tablename__ = 'cms_authentication'

    user_id = db.Column(db.Integer, db.ForeignKey(UserModel.id, ondelete='CASCADE'), nullable=False)
    user = db.relationship('UserModel', back_populates='authentication')
    
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Authentication Model {self.id}: {self.user.username}>'

    @property
    def __fer(self):
        return Fernet(b64encode(current_app.config['SECRET_KEY'].encode('utf8')).decode())

    def set_password(self, pwd):
        self.password = self.__fer.encrypt(pwd.encode('utf8'))
    
    def check_password(self, guess):
        return guess == self.__fer.decrypt(self.password.encode('utf8')).decode()
