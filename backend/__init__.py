# encoding: utf-8
"""
Backend: Webserver
---------
This file represents the core of the server
"""
from flask import Flask, request, send_from_directory, redirect
from pathlib import Path, PurePosixPath
from importlib import import_module

from backend.config import Configuration
from backend.utilities.http import HTTPSchemas, HTTPStatus
from backend.extensions import init_app as _init_extensions
import sys


class Webserver(Flask):
    """The core of the webserver (backend) itself"""
    def __init__(self, *args, **kwargs) -> None:
        Flask.__init__(
            self,
            __name__,
            static_url_path='/',
            static_folder=PurePosixPath(Path(__file__).resolve().parent, 'static').as_posix(),
            template_folder=PurePosixPath(Path(__file__).resolve().parent, 'templates').as_posix(),
            *args,
            **kwargs
        )
        self.config.from_object(Configuration())

        _init_extensions(self)
        self._attach_endpoints()
        self._reset_tasks()

        @self.errorhandler(404)
        def catch_all(path):
            """
            Redirects each non existing endpoint to the main page.
            When `API` is included in the url we ignore this redirect.
            """
            if 'api' not in request.base_url and 'static' not in request.base_url and 'auth' not in request.base_url:
                return redirect(f"{request.host_url[:len(request.host_url)-1]}", code=302)
            elif 'static' not in request.base_url and 'auth' not in request.base_url and hasattr(path, 'data'):
                return HTTPSchemas.NotFound().dump(path.data), HTTPStatus.NOT_FOUND
            elif 'static' not in request.base_url and 'auth' not in request.base_url:
                return HTTPSchemas.NotFound().dump({}), HTTPStatus.NOT_FOUND
            elif 'static' in request.base_url and 'auth' not in request.base_url and 'api' not in request.base_url:
                return send_from_directory(directory='static', path=request.base_url.split('static')[1][1:])

    def _attach_endpoints(self) -> None:
        """Attach endpoints based on modules.ModulesConfig.ENABLED_MODULES"""
        from backend.extensions import api

        available_modules = list(self.config['ENABLED_MODULES'])

        for api_version, endpoint in available_modules:
            try:
                blueprint = import_module(f'backend.endpoints.{api_version}.{endpoint}').blp
                api.register_blueprint(blueprint)
            except ModuleNotFoundError as e:
                raise ModuleNotFoundError(
                    str(
                        f"Could not locate '{endpoint}' in api {api_version}, "
                        "dubble check if modules.ModulesConfig.ENABLED_MODULES file is correctly set"
                    )
                ) from e
        print("* Server ready for connections")

    def _reset_tasks(self) -> None:
        """Set tasks to default value, this method only start once the server boots"""
        from backend.models import SystemTaskModel
        with self.app_context():
            tasks = SystemTaskModel.query.filter(SystemTaskModel.running == True).all()
            for task in tasks:
                task.update({'running': False}, commit=True)
