# encoding: utf-8
"""
Models: Users
-------------
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

from backend.config import connection_url
from backend.extensions import db
from backend.utilities.base import BaseModel

load_dotenv()
engine = create_engine(connection_url, convert_unicode=True, echo=False)
Base = declarative_base()
Base.metadata.reflect(engine)


class UserModel(db.Model):
    __table__ = Base.metadata.tables['users']
