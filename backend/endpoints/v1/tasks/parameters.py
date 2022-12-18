# encoding: utf-8
"""
Parameters: System Tasks
------------------
"""
from backend.utilities.parameters import Parameters

from backend.models import SystemTaskSerializer


class SystemTaskExecutorParameters(Parameters, SystemTaskSerializer):
    """
    Schema which represents input for executing a system task
    """
    class Meta:
        ordered = True
        fields = ('id',)
