# encoding: utf-8
"""
Loginmanager
------------
"""
from flask_login import LoginManager as _LM

from .auth_jwt import AuthJWT


class LoginManager(object):
    """
        LoginManager
        Based on: https://flask-login.readthedocs.io/en/latest/#installation
    """

    def __init__(self, app=None):
        """
        app (FlaskApp): Can be None and initialized later with self.init_app
        """
        self.app = None
        self.login_manager = _LM()
        self._configure_decorators()
        if app:
            self.init_app(app)

    def init_app(self, app):
        """
        Common Flask interface to initialize the logging according to the
        application configuration.
        """
        self.app = app
        self.login_manager.init_app(app)

        @self.login_manager.user_loader
        def load_user(user_id):
            from backend.endpoints.v1.users.models import UserModel
            return UserModel.query.filter_by(id=user_id).first()
    
    def _configure_decorators(self):
        """Initialized all available decorators"""
        self.auth_jwt = AuthJWT()
