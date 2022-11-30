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
    @blp.response(HTTPStatus.UNAUTHORIZED, HTTPSchemas.Unauthorized())
    @blp.response(
        HTTPStatus.SUCCESS, schemas.UsersSchema(
            many=True,
            exclude=(
                "account_created",
                "account_day_of_birth",
                "auth_ticket",
                "extra_rank",
                "ip_current",
                "ip_register",
                "last_online",
                "machine_id",
                "mail",
                "password",
                "pincode",
                "rank",
                "real_name",
                "secret_key",
                "template",
            )
        )
    )
    def all_users(*args, **kwargs):
        """
        Obtain all users
        """
        return models.UserModel.query.all(), HTTPStatus.SUCCESS
