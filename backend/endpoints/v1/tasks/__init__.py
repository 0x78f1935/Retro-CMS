# encoding: utf-8
"""
Resources: System
----------------
Endpoints for tests
"""
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from backend.tasks import queues
from backend.utilities.http import HTTPSchemas, HTTPStatus

from . import parameters, serializer

from backend.models import SystemTaskModel, SystemTaskSerializer
blp = Blueprint('System', 'System', description='System Endpoints', url_prefix='/api/v1/system')


class SystemTasksView(MethodView):
    @blp.route('/tasks', methods=['GET'])
    @blp.response(HTTPStatus.UNAUTHORIZED, HTTPSchemas.Unauthorized())
    @blp.response(HTTPStatus.SUCCESS, SystemTaskSerializer(many=True))
    def available_tasks(*args, **kwargs):
        """
        System Tasks
        
        Obtains available tasks and the concurrent status of that task
        """
        return SystemTaskModel.query.all(), HTTPStatus.SUCCESS

    @blp.route('/tasks', methods=['POST'])
    @blp.arguments(parameters.SystemTaskExecutorParameters(), location='json')
    @blp.response(HTTPStatus.UNAUTHORIZED, HTTPSchemas.Unauthorized())
    @blp.response(HTTPStatus.FORBIDDEN, HTTPSchemas.Forbidden())
    @blp.response(HTTPStatus.NOT_FOUND, HTTPSchemas.NotFound())
    @blp.response(HTTPStatus.SUCCESS, serializer.SystemTaskResponseSerializer(many=False))
    def execute_task(payload, *args, **kwargs):
        """
        Execute Task
        
        Run provided task, task can only start if its not running.
        
        404 -> Task not found
        403 -> Task already running
        200 -> Continue
        """
        task = SystemTaskModel.query.filter(SystemTaskModel.id == payload['id']).first()
        if task is None:
            return abort(HTTPStatus.NOT_FOUND, **HTTPSchemas.NotFound().dump({
                'message': 'No such task found!',
                'errors': {
                    'task': ['not found']
                }
            })), HTTPStatus.NOT_FOUND
        elif task.is_running:
            return abort(HTTPStatus.FORBIDDEN, **HTTPSchemas.Forbidden().dump({
                'message': 'Task is already running!',
                'errors': {
                    'task': ['forbidden']
                }
            })), HTTPStatus.FORBIDDEN
        task.update({'running': True}, commit=True)
        # TODO 
        queues.QUEUE_DOWNLOADER.put(task.id)
        return { 'task': task.id, 'is_running': task.is_running }, HTTPStatus.SUCCESS
