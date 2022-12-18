# encoding: utf-8
"""
Base Class
----------
Base class for SQLalchemy ORM Models
"""
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime

from backend.extensions import db


class Model(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

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
