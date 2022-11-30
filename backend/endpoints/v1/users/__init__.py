# encoding: utf-8
"""
Resources: Users
----------------
Endpoints for users
"""
from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint('Users', 'Users', description='Users Endpoint', url_prefix='/api/v1/users')

from . import schemas, parameters, models

from backend.utilities.http import HTTPSchemas, HTTPStatus


class UsersView(MethodView):
    @blp.route('/', methods=['GET'])
    @blp.response(HTTPStatus.SUCCESS, HTTPSchemas.Success())
    def all_users(*args, **kwargs):
        """
        Obtain all users
        """
        return {}, HTTPStatus.SUCCESS