# encoding: utf-8
"""
Resources: Test
----------------
Endpoints for tests
"""
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_login import current_user

blp = Blueprint('Tests', 'Tests', description='Test Endpoint', url_prefix='/api/v1/tests')

from backend.extensions import db, loginmanager
from backend.utilities.http import HTTPSchemas, HTTPStatus


class TestView(MethodView):
    @blp.route('/', methods=['GET'])
    @blp.response(HTTPStatus.UNAUTHORIZED, HTTPSchemas.Unauthorized())
    @blp.response(HTTPStatus.SUCCESS, HTTPSchemas.Success())
    @loginmanager.auth_jwt.Required(scope=['retro:guest', 'retro:admin'], operator='OR')
    def all_users(user, *args, **kwargs):
        """
        Obtain all users
        """
        return {}, HTTPStatus.SUCCESS
