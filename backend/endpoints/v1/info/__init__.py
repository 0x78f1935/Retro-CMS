# encoding: utf-8
"""
Resources: Info
----------------
Provides informational endpoints
"""
from flask import current_app
from flask.views import MethodView
from flask_smorest import Blueprint
from urllib.parse import quote_plus
from pathlib import Path, PurePosixPath
from sqlalchemy.sql import func

from . import serializer

from backend.models import SystemTaskModel, UserModel
from backend.utilities.http import HTTPSchemas, HTTPStatus

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
        assets = SystemTaskModel.query.filter(SystemTaskModel.sysname == 'downloader').first()
        converter = SystemTaskModel.query.filter(SystemTaskModel.sysname == 'converter').first()
        random_character = UserModel.query.order_by(func.random()).first()
        return {
            'name_short': current_app.config['PROJECT_NAME_SHORT'],
            'name_long': current_app.config['PROJECT_NAME'],
            'logo': f'https://habbofont.net/font/habbo_old_big/{quote_plus(current_app.config["PROJECT_NAME_SHORT"])}.gif',
            'assets_ran': assets.has_ran,
            'assets_status': assets.exit_code,
            'converter_ran': converter.has_ran,
            'converter_status': converter.exit_code,
            'random_look': 'hr-115-42.hd-195-19.ch-3030-82.lg-275-1408.fa-1201.ca-1804-64' if random_character is None \
                else random_character.look,
        }, HTTPStatus.SUCCESS
