# encoding: utf-8
"""
Webserver Tasks
---------------
Available tasks the backend server is able to run in the background.
"""


class TasksConfig(object):
    def __init__(self):
        """Configures enabled endpoints.

        Based on (variable, task name)
        """
        self.ENABLED_TASKS = (
            ('DOWNLOADER', 'downloader',),
        )
