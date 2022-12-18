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

from backend.tasks.base import BackgroundThread
from backend.tasks.queues import QUEUE_DOWNLOADER


class DownloadThread(BackgroundThread):
    PATH_OUT = PurePosixPath(Path(__file__).resolve().parent.parent.parent, 'static').as_posix()

    def startup(self) -> None:
        print('DownloadThread started')

    def shutdown(self) -> None:
        print('DownloadThread stopped')

    def handle(self) -> None:
        try:
            QUEUE_DOWNLOADER.get(block=False)
            print(f'Assets are getting downloaded!.')
        except queue.Empty:
            # print('DownloadThread waiting for signal')
            time.sleep(1)
