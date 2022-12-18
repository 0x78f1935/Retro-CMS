# encoding: utf-8
"""
Resources: Info
----------------
Provides informational endpoints
"""
from flask import request, current_app
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import get_jwt_identity, create_access_token, create_refresh_token
from flask_jwt_extended.view_decorators import jwt_required
from flask_login import login_user, logout_user, current_user, login_required
from flask_jwt_extended import create_access_token, create_refresh_token
from sqlalchemy import or_
from urllib.parse import quote_plus

from . import serializer

from backend.extensions import db
from backend.utilities.http import HTTPSchemas, HTTPStatus
from backend.models import UserModel, UserSerializer, AuthenticationModel, BearerTokenSerializer, SSOTokenSerializer


blp = Blueprint('Information', 'Information', description='Info Endpoint', url_prefix='/api/v1/info')


class InfoView(MethodView):
    @blp.route('/app', methods=['GET'])
    @blp.response(
        HTTPStatus.SUCCESS,
        serializer.ApplicationResponseSerializer(many=False,)
    )
    def app_info(*args, **kwargs):
        """
        Obtain application information
        
        This endpoint
        """
        return {
            'name_short': current_app.config['PROJECT_NAME_SHORT'],
            'name_long': current_app.config['PROJECT_NAME'],
            'logo': f'https://habbofont.net/font/habbo_old_big/{quote_plus(current_app.config["PROJECT_NAME_SHORT"])}.gif'
        }, HTTPStatus.SUCCESS
