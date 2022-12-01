# encoding: utf-8
"""
Resources: Users
----------------
Endpoints for users
"""
from flask import request, current_app
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_login import login_user, logout_user, current_user, login_required
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
                "real_name",
                "secret_key",
                "template",
            )
        )
    )
    def all_users(*args, **kwargs):
        """
        Obtain all users
        
        Fetch a overview of all available users.
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
        
        A new user will be created with the provided data.
        After this endpoint has been executed, the user should be able to authenticate with `api/v1/users/login`
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
                "machine_id": f'{uuid4()}',
                "credits": current_app.config["STARTING_CREDITS"],
                "pixels": current_app.config["STARTING_PIXELS"],
                "points": current_app.config["STARTING_POINTS"],
            }
        )
        db.session.add(user)
        db.session.commit()
        auth = models.AuthenticationModel(**{
            'user_id': user.id,
            'password': current_app.config['SECRET_KEY']
        })
        if models.AuthenticationModel.query.count() == 0:
            auth.scope = "retro:guest;retro:admin;retro:owner"
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
        
        Authenticate user with provided user credentials, after successful authentication
        a new SSO ticket will be generated. Returns bearer token.
        
        > No bearer token required
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
            user.generate_sso_ticket()
            login_user(user)
            return user, HTTPStatus.SUCCESS

        return abort(HTTPStatus.UNAUTHORIZED, **HTTPSchemas.Unauthorized().dump({
                'message': 'Invalid Credentials!',
                'errors': {
                    'user': ['Invalid Credentials']
                }
            })), HTTPStatus.UNAUTHORIZED

    @blp.route('/logout', methods=['GET'])
    @blp.response(HTTPStatus.FORBIDDEN, HTTPSchemas.Forbidden())
    @blp.response(HTTPStatus.SUCCESS, HTTPSchemas.Success())
    def logout_user(*args, **kwargs):
        """
        Logout user
        
        Logs the current logged in user out.
        Also resets SSO Ticket
        
        > No bearer token required
        """
        if not current_user.is_authenticated:
            return abort(HTTPStatus.FORBIDDEN, **HTTPSchemas.Forbidden().dump({
                'message': 'No one to logout!',
                'errors': {
                    'user': ['Already anonymous']
                }
            })), HTTPStatus.FORBIDDEN
        current_user.generate_sso_ticket()
        logout_user()
        return {'status': 'success'}, HTTPStatus.SUCCESS

    @blp.route('/me', methods=['PATCH'])
    @blp.arguments(parameters.UpdateMeParameters(), location='json')
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
                "real_name",
                "secret_key",
                "template",
            )
        )
    )
    @login_required
    def patch_me(formdata, *args, **kwargs):
        """
        Update Me
        
        This endpoint allows the logged in user to update his/her account.
        Before a user can use this endpoint, that user is required to have
        logged in before with `api/v1/users/login` after which this endpoint works.
        
        > No bearer token required
        """
        if 'password' in formdata.keys():
            _pwd = formdata['password']
            del formdata['password']
            current_user.authentication.set_password(_pwd)
        
        current_user.update(formdata)
        return current_user, HTTPStatus.SUCCESS


    @blp.route('/sso', methods=['GET'])
    @blp.response(HTTPStatus.UNAUTHORIZED, HTTPSchemas.Unauthorized())
    @blp.response(HTTPStatus.SUCCESS, schemas.SSOTokenSchema())
    @login_required
    def ticket(*args, **kwargs):
        """
        SSO Ticket
        
        Returns SSO ticket of logged in user.
        
        > No bearer token required
        """       
        return {
            'auth_ticket': f'{current_app.config["EMULATOR_HOST"]}?sso={current_user.auth_ticket}'
        }, HTTPStatus.SUCCESS
