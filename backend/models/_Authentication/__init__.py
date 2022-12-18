# encoding: utf-8
"""
Models: Authentication
-------------
Model which holds various security features
"""
from cryptography.fernet import Fernet
from base64 import b64encode
from uuid import uuid4

from backend.extensions import db, bcrypt
# from backend.models import UserModel
from backend.utilities.models import Model


class AuthenticationModel(db.Model, Model):
    """Authentication model"""
    __tablename__ = 'authentication'

    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'), nullable=False)
    user = db.relationship('UserModel', back_populates='authentication')
    enc_id = db.Column(db.Text, nullable=False, default=f'{uuid4()}')

    password = db.Column(db.Text, nullable=False)
    scope = db.Column(db.Text, nullable=False, default='retro:guest')

    def __repr__(self):
        return f'<Authentication Model {self.id}: {self.user.username}>'

    @property
    def __key(self):
        return int(self.user.created.strftime("%S%M%S%d%H%S")) >> 2

    @property
    def __fer(self):
        return Fernet(
            b64encode(
                f'{self.__key}{self.user.ip_register}{self.user.email}{self.user.authentication.enc_id}'[:32].encode('utf8')
            ).decode()
        )

    def set_password(self, pwd):
        self.password = self.__fer.encrypt(bcrypt.generate_password_hash(pwd.encode('utf8')))
        db.session.commit()

    def check_password(self, guess):
        return bcrypt.check_password_hash(self.__fer.decrypt(self.password.encode('utf8')).decode(), guess)

    @property
    def scopes(self):
        """Return all available scopes"""
        return self.scope.split(';')
