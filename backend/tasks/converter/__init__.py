# encoding: utf-8
"""
Task: RetroConverter
---------
This task converts available assets downloaded with the Retro Downloader.
The tool utilized in the background is https://github.com/billsonnn/nitro-converter.
"""
from pathlib import PurePosixPath, Path

import queue
import time
import shutil
import subprocess
import json
import os

from backend.tasks.base import BackgroundThread
from backend.tasks.queues import QUEUE_CONVERTER


class ConvertThread(BackgroundThread):
    PATH_OUT = PurePosixPath(Path(__file__).resolve().parent.parent.parent, 'static').as_posix()
    PATH_ZIP = PurePosixPath(Path(__file__).resolve().parent, 'nitro-converter.zip').as_posix()
    PATH_TMP = PurePosixPath(Path(__file__).resolve().parent, 'tmp').as_posix()

    def startup(self) -> None:
        """
        Setup environment for downloader to work
        """
        Path(self.PATH_TMP).mkdir(exist_ok=True)
        shutil.unpack_archive(self.PATH_ZIP, self.PATH_TMP)
        self._update_config()
        print('* ConvertThread started')

    def shutdown(self) -> None:
        """
        Teardown folders with graceful shutdown
        """
        try:
            shutil.rmtree(self.PATH_TMP)
        except (FileNotFoundError,): pass
        print('* ConvertThread stopped')

    def handle(self) -> None:
        """
        Handle downloader if task has been queued, otherwise listen for queue
        """
        try:
            task_id = QUEUE_CONVERTER.get(block=False)
            print(f'* Assets are getting converted!.')
            self._update_config()
            # command = ["cd", self.PATH_TMP, "&&", "yarn", "start"]
            result_start = subprocess.run(["yarn", "--cwd", self.PATH_TMP, "start"], capture_output=True, shell=True)
            print(result_start.stdout)
            print(result_start.stderr)
            result_bundle = subprocess.run(["yarn", "--cwd", self.PATH_TMP, "start:bundle"], capture_output=True, shell=True)
            print(result_bundle.stdout)
            print(result_bundle.stderr)
            result_extract = subprocess.run(["yarn", "--cwd", self.PATH_TMP, "start:extract"], capture_output=True, shell=True)
            print(result_extract.stdout)
            print(result_extract.stderr)
            result_convert = subprocess.run(["yarn", "--cwd", self.PATH_TMP, "start:convert-swf"], capture_output=True, shell=True)
            print(result_convert.stdout)
            print(result_convert.stderr)
           
            with self.app.app_context():
                from backend.models import SystemTaskModel
                task = SystemTaskModel.query.filter(SystemTaskModel.id == task_id).first()
                # task.update({'running': False, 'has_ran': True, 'exit_code': 0})
                task.update({'running': False})

            print("* Assets have been downloaded")
        except queue.Empty:
            time.sleep(1)

    def _update_config(self):
        """
        Obtains known gordon version which has been downloaded from the retro-downloader tool.
        If gordon version is known, we update the configuration of the converter.
        """
        with open(PurePosixPath(self.PATH_TMP, 'configuration.json').as_posix(), 'r') as _config:
            config = json.load(_config)
            
        if GORDON_VERSIONS := os.listdir(PurePosixPath(self.PATH_OUT, 'gordon')):
            GORDON_VERSION = GORDON_VERSIONS[0]
        else:
            GORDON_VERSION = 'NO-ASSETS'
        config['flash.client.url'] = config['flash.client.url'].replace('GORDON-PRODUCTION', GORDON_VERSION)
        with open(PurePosixPath(self.PATH_TMP, 'configuration.json').as_posix(), 'w') as _config:
            json.dump(config, _config, indent=2)
