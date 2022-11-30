# encoding: utf-8
"""
Resources: Housekeeping
-----------------------
Endpoints for housekeeping
"""
from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint('Housekeeping', 'Housekeeping', description='Housekeeping endpoints', url_prefix='/api/v1/housekeeping')

from backend.extensions import db, loginmanager
from backend.utilities.http import HTTPSchemas, HTTPStatus


class HousekeepingView(MethodView):
    @blp.route('/', methods=['GET'])
    @blp.response(HTTPStatus.UNAUTHORIZED, HTTPSchemas.Unauthorized())
    @blp.response(HTTPStatus.SUCCESS, HTTPSchemas.Success())
    @loginmanager.auth_jwt.Required(scope=['retro:guest', 'retro:admin'], operator='OR')
    def modify_users(user, *args, **kwargs):
        """
        Ignore this endpoint please
        """
        # TODO
        return {}, HTTPStatus.SUCCESS
