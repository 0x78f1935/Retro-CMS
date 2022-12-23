# encoding: utf-8
"""
Resources: Users
----------------
Endpoints for users
"""
from flask import request, current_app
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import get_jwt_identity, create_access_token, create_refresh_token
from flask_jwt_extended.view_decorators import jwt_required
from flask_login import login_user, logout_user, current_user, login_required
from flask_jwt_extended import create_access_token, create_refresh_token
from sqlalchemy import or_

from . import parameters

from backend.extensions import db
from backend.utilities.http import HTTPSchemas, HTTPStatus

from backend.models import UserModel, UserSerializer, AuthenticationModel, BearerTokenSerializer, SSOTokenSerializer


blp = Blueprint('Users', 'Users', description='Users Endpoint', url_prefix='/api/v1/users')


class UsersView(MethodView):
    @blp.route('/', methods=['GET'])
    @blp.response(HTTPStatus.UNAUTHORIZED, HTTPSchemas.Unauthorized())
    @blp.response(
        HTTPStatus.SUCCESS,
        UserSerializer(
            many=True,
            exclude=(
                "email",
                "updated",
                "ip_current",
                "ip_register",
                "mail_verified",
                "password",
                "last_login",
                "last_online",
                "auth_ticket",
            )
        )
    )
    def all_users(*args, **kwargs):
        """
        Obtain all users

        Fetch a overview of all available users.
        """
        return UserModel.query.all(), HTTPStatus.SUCCESS

    @blp.route('/', methods=['POST'])
    @blp.arguments(parameters.UserRegistrationParameters(), location='json')
    @blp.response(HTTPStatus.UNAUTHORIZED, HTTPSchemas.Unauthorized())
    @blp.response(
        HTTPStatus.SUCCESS,
        UserSerializer(
            many=False,
            exclude=(
                "email",
                "ip_current",
                "ip_register",
                "mail_verified",
                "password",
                "last_login",
                "last_online",
                "auth_ticket",
            )
        )
    )
    def register_user(formdata, *args, **kwargs):
        """
        Register new user

        A new user will be created with the provided data.
        After this endpoint has been executed, the user should be able to authenticate with `api/v1/users/login`
        """
        user = UserModel.query.filter(
            or_(
                UserModel.username == formdata["username"],
                UserModel.email == formdata["email"]
            )
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

        user = UserModel(
            **formdata,
            **{
                "ip_register": request.remote_addr,
                "ip_current": request.remote_addr,
                "password": "UNKNOWN",
                "credits": current_app.config["STARTING_CREDITS"],
                "pixels": current_app.config["STARTING_PIXELS"],
                "points": current_app.config["STARTING_POINTS"],
                "diamonds": current_app.config["STARTING_DIAMONDS"],
            }
        )
        db.session.add(user)
        db.session.commit()
        auth = AuthenticationModel(**{
            'user_id': user.id,
            'password': current_app.config['SECRET_KEY']
        })

        # Assuming first created user is the owner of the host.
        if AuthenticationModel.query.count() == 0:
            auth.scope = "retro:guest;retro:admin;retro:owner"

        db.session.add(auth)
        db.session.commit()
        user.password = "SET"
        auth.set_password(_pwd)
        return user, HTTPStatus.SUCCESS

    @blp.route('/login', methods=['POST'])
    @blp.arguments(parameters.UserAuthorizationParameters(), location='json')
    @blp.response(HTTPStatus.UNAUTHORIZED, HTTPSchemas.Unauthorized())
    @blp.response(HTTPStatus.SUCCESS, BearerTokenSerializer(many=False))
    def authenticate_user(formdata, *args, **kwargs):
        """
        Authenticate User

        Authenticate user with provided user credentials, after successful authentication
        a new SSO ticket will be generated. Returns bearer token.

        > No bearer token required
        """
        user = UserModel.query.filter(UserModel.username == formdata["username"]).first()
        if user is None:
            return abort(HTTPStatus.NOT_FOUND, **HTTPSchemas.NotFound().dump({
                'message': 'User not found!',
                'errors': {
                    'user': ['Not existing in the database']
                }
            })), HTTPStatus.NOT_FOUND
        if user.authentication.check_password(formdata['password']):
            user.generate_sso_ticket()
            user._access_token = create_access_token(identity=user.id, fresh=True)
            user._refresh_token = create_refresh_token(user.id)
            login_user(user)
            return user, HTTPStatus.SUCCESS

        return abort(HTTPStatus.UNAUTHORIZED, **HTTPSchemas.Unauthorized().dump({
            'message': 'Invalid Credentials!',
            'errors': {
                'user': ['Invalid Credentials']
            }
        })), HTTPStatus.UNAUTHORIZED
        
    @blp.route('/refresh', methods=['POST'])
    @jwt_required(refresh=True)
    @blp.response(HTTPStatus.UNAUTHORIZED, HTTPSchemas.Unauthorized())
    @blp.response(HTTPStatus.SUCCESS, BearerTokenSerializer(many=False))
    def authenticate_user(*args, **kwargs):
        """
        Refresh JWT Token
        """
        user_id = get_jwt_identity()
        user = UserModel.query.filter(UserModel.id == user_id).first()
        if user is None:
            return abort(HTTPStatus.NOT_FOUND, **HTTPSchemas.NotFound().dump({
                'message': 'User not found!',
                'errors': {
                    'user': ['Not existing in the database']
                }
            })), HTTPStatus.NOT_FOUND
            
        user._access_token = create_access_token(identity=user_id, fresh=True)
        user._refresh_token = create_refresh_token(user_id)
        return user, 200

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

    @blp.route('/sso', methods=['GET'])
    @blp.response(HTTPStatus.UNAUTHORIZED, HTTPSchemas.Unauthorized())
    @blp.response(HTTPStatus.SUCCESS, SSOTokenSerializer())
    @login_required
    def ticket(*args, **kwargs):
        """
        SSO Ticket

        Returns SSO ticket of logged in user.

        > No bearer token required
        """
        return {
            'auth_ticket': current_user.auth_ticket,
            'scope': current_user.authentication.scopes
        }, HTTPStatus.SUCCESS
