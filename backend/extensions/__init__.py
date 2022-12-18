# encoding: utf-8
"""
Webserver Extensions
--------------------
This file loads global available extensions of third/private/custom code
"""
from flask_smorest import Api  # noqa: E402
api = Api()

from flask_sqlalchemy import SQLAlchemy  # noqa: E402
db = SQLAlchemy()

from flask_migrate import Migrate  # noqa: E402


def init_app(app) -> None:
    """
    Application extensions initialiation method -> Lazy load
    """
    for extensions in (
        api,
        db,
    ):
        extensions.init_app(app)
    Migrate(app, db)
