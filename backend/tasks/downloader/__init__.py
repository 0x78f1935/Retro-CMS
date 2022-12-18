# encoding: utf-8
"""
Task: RetroDownloader
---------
This task downloads available assets based on the provided configuration.
The tool utilized in the background is https://github.com/0x78f1935/Retro-Downloader which has been written by the
same author of this CMS. The files downloaded this way still are required to be converted.
"""
from pathlib import PurePosixPath, Path
from importlib import import_module

import logging
import queue
import time
import shutil

from backend.tasks.base import BackgroundThread
from backend.tasks.queues import QUEUE_DOWNLOADER


class DownloadThread(BackgroundThread):
    PATH_OUT = PurePosixPath(Path(__file__).resolve().parent.parent.parent, 'static').as_posix()
    PATH_ZIP = PurePosixPath(Path(__file__).resolve().parent, 'RetroDownloader.zip').as_posix()
    PATH_TMP = PurePosixPath(Path(__file__).resolve().parent, 'tmp').as_posix()

    def startup(self) -> None:
        """
        Setup environment for downloader to work
        """
        Path(self.PATH_TMP).mkdir(exist_ok=True)
        shutil.unpack_archive(self.PATH_ZIP, self.PATH_TMP)
        print('* DownloadThread started')

    def shutdown(self) -> None:
        """
        Teardown folders with graceful shutdown
        """
        try:
            shutil.rmtree(self.PATH_TMP)
        except (FileNotFoundError,): pass
        print('* DownloadThread stopped')

    def handle(self) -> None:
        """
        Handle downloader if task has been queued, otherwise listen for queue
        """
        try:
            task_id = QUEUE_DOWNLOADER.get(block=False)
            print(f'* Assets are getting downloaded!.')
            downloader = import_module('backend.tasks.downloader.tmp.wrapper').DownloadWrapper
            downloader = downloader(
                False,
                self.PATH_OUT,
                'latest',
                'Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/534.2.1 (KHTML, like Gecko) Chrome/35.0.822.0 Safari/534.2.1',
                100,
                True,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                "backend;tasks;downloader;tmp"
            )
            while (downloader.is_running or downloader.isRunning):
                time.sleep(1)

            with self.app.app_context():
                from backend.models import SystemTaskModel
                task = SystemTaskModel.query.filter(SystemTaskModel.id == task_id).first()
                task.update({'running': False})
            print("* Assets have been downloaded")
        except queue.Empty:
            time.sleep(1)
