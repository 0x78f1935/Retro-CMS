# encoding: utf-8
"""
Resources: Housekeeping
-----------------------
Endpoints for housekeeping
"""
from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint('Housekeeping', 'Housekeeping', description='Housekeeping endpoints', url_prefix='/api/v1/housekeeping')

from . import parameters

from backend.extensions import db, loginmanager
from backend.utilities.http import HTTPSchemas, HTTPStatus

from backend.endpoints.v1.users.schemas import UsersSchema
from backend.endpoints.v1.users.models import UserModel, AuthenticationModel


class HousekeepingView(MethodView):
    @blp.route('/user', methods=['PATCH'])
    @blp.arguments(parameters.PatchUserParameters(), location='query')
    @blp.arguments(parameters.UpdateUsersParameters(), location='json')
    @blp.response(HTTPStatus.UNAUTHORIZED, HTTPSchemas.Unauthorized())
    @blp.response(HTTPStatus.FORBIDDEN, HTTPSchemas.Forbidden())
    @blp.response(HTTPStatus.UNPROCESSABLE_ENTITY, HTTPSchemas.UnprocessableEntry())
    @blp.response(HTTPStatus.NOT_FOUND, HTTPSchemas.NotFound())
    @blp.response(
        HTTPStatus.SUCCESS, UsersSchema(
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
    @loginmanager.auth_jwt.Required(scope=['retro:admin',], operator='AND')
    def modify_users(user, query_data, form_data, *args, **kwargs):
        """
        Modify user by ID
        
        query_param:
            id (int): The user ID which you would like modify
        """
        user = UserModel.query.filter(UserModel.id == query_data['id']).first()
        if user is None:
            return abort(HTTPStatus.NOT_FOUND, **HTTPSchemas.NotFound().dump({
                'message': 'User not found!',
                'errors': {
                    'user': ['not found']
                }
            })), HTTPStatus.NOT_FOUND
        user.update(form_data)
        return user, HTTPStatus.SUCCESS

    @blp.route('/user', methods=['DELETE'])
    @blp.arguments(parameters.DeleteUserParameters(), location='query')
    @blp.response(HTTPStatus.UNAUTHORIZED, HTTPSchemas.Unauthorized())
    @blp.response(HTTPStatus.FORBIDDEN, HTTPSchemas.Forbidden())
    @blp.response(HTTPStatus.UNPROCESSABLE_ENTITY, HTTPSchemas.UnprocessableEntry())
    @blp.response(HTTPStatus.NOT_FOUND, HTTPSchemas.NotFound())
    @blp.response(HTTPStatus.SUCCESS, HTTPSchemas.Success())
    @loginmanager.auth_jwt.Required(scope=['retro:admin',], operator='AND')
    def delete_user(user, query_data, *args, **kwargs):
        """
        Delete user by ID
        
        query_param:
            id (int): The user ID which you would like to remove
            
        A user can only be removed if the user has no 'retro:owner' scope.
        """
        user = UserModel.query.filter(UserModel.id == query_data['id']).first()
        if user is None:
            return abort(HTTPStatus.NOT_FOUND, **HTTPSchemas.NotFound().dump({
                'message': 'User not found!',
                'errors': {
                    'user': ['not found']
                }
            })), HTTPStatus.NOT_FOUND

        # Fallback if the user has no authentication scope, we fallback to empty list and allow removal
        if 'retro:owner' in user.authentication.scopes if user.authentication else []:
            return abort(HTTPStatus.NOT_FOUND, **HTTPSchemas.NotFound().dump({
                'message': 'Unable to remove owner!',
                'errors': {
                    'user': ['forbidden']
                }
            })), HTTPStatus.NOT_FOUND

        UserModel.query.filter(UserModel.id == query_data['id']).delete()
        db.session.commit()
        return {}, HTTPStatus.SUCCESS
