# encoding: utf-8
"""
Loginmanager
------------
JWT Extension
"""
from flask_smorest import abort
from flask import request, current_app

import jwt

from typing import Union
from functools import wraps

from backend.utilities.http import HTTPSchemas, HTTPStatus
from backend.endpoints.v1.users.models import UserModel


class AuthJWT:
    class Required:
        def __init__(self, scope:Union[str, list]="retro:guest", operator:str='AND'):
            """Check if current_user has valid scope attached to its request

            Args:
                scope (Union[str, list], optional): Scope of the request. Defaults to "retro:guest".
                operator (str, optional): "AND" or "OR". Defaults to 'AND'.
            """
            self.scopes = scope
            if type(self.scopes) == str:
                self.scopes = scope.split(';')

            self.operator = operator.upper()
            if self.operator != 'AND' and self.operator != 'OR':
                raise Exception("Unkown operator, should either be AND or OR")

        def __call__(self, func):
            @wraps(func)
            def my_logic(*args, **kwargs):
                token = None
                if 'authorization' in request.headers:
                    token = request.headers['authorization'].replace('Bearer ', '')

                if not token:
                    return abort(HTTPStatus.UNAUTHORIZED, **HTTPSchemas.Unauthorized().dump({
                        'message': 'Bearer: Authentication required',
                        'errors': {
                            'token': ['missing']
                        }
                    }))

                access_token = request.headers.get('Authorization', '').split().pop(1)
                try:
                    token_data = jwt.decode(access_token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
                except jwt.InvalidSignatureError:
                    return abort(HTTPStatus.UNAUTHORIZED, **HTTPSchemas.Unauthorized().dump({
                        'message': 'Bearer: Signature verification failed.',
                        'errors': {
                            'token': ['signature']
                        }
                    }))
                except jwt.ExpiredSignatureError:
                    return abort(HTTPStatus.UNAUTHORIZED, **HTTPSchemas.Unauthorized().dump({
                        'message': 'Bearer: Expired token. Re-authentication required.',
                        'errors': {
                            'token': ['expired']
                        }
                    }))
                except (jwt.InvalidTokenError):
                    return abort(HTTPStatus.UNAUTHORIZED, **HTTPSchemas.Unauthorized().dump({
                        'message': 'Bearer: Invalid Token',
                        'errors': {
                            'token': ['invalid']
                        }
                    }))

                user = UserModel.query.filter_by(id=token_data['sub']).first()
                
                missing_scopes = [scope for scope in self.scopes if scope not in user.authentication.scopes]
                if self.operator == 'AND' and missing_scopes:
                    print(f'[!] User {user.username} is missing scope(s) ({(f" {self.operator} ".join(missing_scopes))}) for {func}({args} | {kwargs}')
                    return abort(HTTPStatus.UNAUTHORIZED, **HTTPSchemas.Unauthorized().dump({
                        'message': 'You do not meet the required scope requirements!',
                        'errors': {
                            'scope': ['insufficient'],
                            'missing_scopes': missing_scopes,
                            'missing_details': ['Many']
                        }
                    })), HTTPStatus.FORBIDDEN
                elif self.operator == 'OR' and len(missing_scopes) == len(self.scopes):
                    print(f'[!] User {user.username} is missing scope(s) ({(f" {self.operator} ".join(missing_scopes))}) for {func}({args} | {kwargs}')
                    return abort(HTTPStatus.UNAUTHORIZED, **HTTPSchemas.Unauthorized().dump({
                        'message': 'You do not meet the required scope requirements!',
                        'errors': {
                            'scope': ['insufficient'],
                            'missing_scopes': missing_scopes,
                            'missing_details': ['OneOf']
                        }
                    })), HTTPStatus.FORBIDDEN

                # Call request
                result = func(user, *args, **kwargs)

                # Post-Logic
                print(f'[-] User {user.username} requested [{request.method}] {func}({args} | {kwargs})')
                return result

            return my_logic
