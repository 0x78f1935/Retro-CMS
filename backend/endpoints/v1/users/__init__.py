# encoding: utf-8
"""
Resources: Users
----------------
Endpoints for users
"""
from flask import request, current_app
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_login import login_user
from uuid import uuid4
from sqlalchemy import or_

blp = Blueprint('Users', 'Users', description='Users Endpoint', url_prefix='/api/v1/users')

from . import schemas, parameters, models

from backend.extensions import db
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

    @blp.route('/', methods=['POST'])
    @blp.arguments(parameters.UserRegistrationParameters(), location='json')
    @blp.response(HTTPStatus.UNAUTHORIZED, HTTPSchemas.Unauthorized())
    @blp.response(
        HTTPStatus.SUCCESS, schemas.UsersSchema(
            many=False,
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
    def register_user(formdata, *args, **kwargs):
        """
        Register new user
        """
        user = models.UserModel.query.filter(
            or_(
                models.UserModel.username == formdata["username"],
                models.UserModel.mail == formdata["mail"])
            ).first()

        if user:
            return abort(HTTPStatus.UNPROCESSABLE_ENTITY, **HTTPSchemas.UnprocessableEntry().dump({
                'message': 'User already exists!',
                'errors': {
                    'user': ['Cannot commit duplicate entity']
                }
            })), HTTPStatus.UNPROCESSABLE_ENTITY
        
        _pwd = formdata['password']
        del formdata['password']

        user = models.UserModel(
            **formdata,
            **{
                "account_created": 1,
                "ip_register": request.remote_addr,
                "ip_current": request.remote_addr,
                "password": "UNKNOWN",
                "real_name": "Retro Guest",
                "machine_id": f'{uuid4()}'
            }
        )
        db.session.add(user)
        db.session.commit()
        auth = models.AuthenticationModel(**{
            'user_id': user.id,
            'password': current_app.config['SECRET_KEY']
        })
        db.session.add(auth)
        db.session.commit()
        user.password = "SET"
        auth.set_password(_pwd)
        return user, HTTPStatus.SUCCESS

    @blp.route('/login', methods=['POST'])
    @blp.arguments(parameters.UserAuthorizationParameters(), location='json')
    @blp.response(HTTPStatus.UNAUTHORIZED, HTTPSchemas.Unauthorized())
    @blp.response(HTTPStatus.SUCCESS, schemas.BearerTokenSchema(many=False))
    def authenticate_user(formdata, *args, **kwargs):
        """
        Authenticate User
        """
        user = models.UserModel.query.filter(models.UserModel.mail == formdata["mail"]).first()
        if user is None:
            return abort(HTTPStatus.NOT_FOUND, **HTTPSchemas.NotFound().dump({
                'message': 'User not found!',
                'errors': {
                    'user': ['Not existing in the database']
                }
            })), HTTPStatus.NOT_FOUND
        if user.authentication.check_password(formdata['password']):
            login_user(user)
            return user, HTTPStatus.SUCCESS

        return abort(HTTPStatus.UNAUTHORIZED, **HTTPSchemas.Unauthorized().dump({
                'message': 'Invalid Credentials!',
                'errors': {
                    'user': ['Invalid Credentials']
                }
            })), HTTPStatus.UNAUTHORIZED
