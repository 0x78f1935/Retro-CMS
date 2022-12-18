# encoding: utf-8
"""
Task: Handler
---------
Handles various background tasks required to setup the retro game.
Factory which basically hooks the background tasks into the webserver.
"""
from backend.tasks.downloader import DownloadThread


class BackgroundThreadFactory:
    @staticmethod
    def create(app, thread_type: str):
        if thread_type == 'downloader':
            return DownloadThread(app)

        # if thread_type == 'some_other_type':
        #     return SomeOtherThread()

        raise NotImplementedError('Specified thread type is not implemented.')
