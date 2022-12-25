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
    name = 'Nitro-Converter'
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
            subprocess.run(["yarn", "--cwd", self.PATH_TMP, "start"], shell=True)
            
            shutil.copytree(PurePosixPath(self.PATH_TMP, 'assets', 'bundled').as_posix(), PurePosixPath(self.PATH_OUT, 'bundled').as_posix(), dirs_exist_ok=True)
            shutil.copytree(PurePosixPath(self.PATH_TMP, 'assets', 'gamedata').as_posix(), PurePosixPath(self.PATH_OUT, 'gamedata').as_posix(), dirs_exist_ok=True)

            # shutil.rmtree(self.PATH_TMP)
            with self.app.app_context():
                from backend.models import SystemTaskModel
                task = SystemTaskModel.query.filter(SystemTaskModel.id == task_id).first()
                task.update({'running': False, 'has_ran': True, 'exit_code': 0})
                imager = SystemTaskModel.query.filter(SystemTaskModel.id == 3).first()
                imager.update({'has_ran': True, 'exit_code': 0})

            print("* Assets have been converted")
        except queue.Empty:
            time.sleep(1)

    def _update_config(self):
        """
        Obtains known gordon version which has been downloaded from the retro-downloader tool.
        If gordon version is known, we update the configuration of the converter.
        """           
        GORDON_VERSION = 'NO-ASSETS'
        if Path(self.PATH_OUT, 'gordon').exists():
            if GORDON_VERSIONS := os.listdir(PurePosixPath(self.PATH_OUT, 'gordon')):
                GORDON_VERSION = GORDON_VERSIONS[0]

        CONFIG = {
            "output.folder": self.PATH_OUT,
            "flash.client.url": f"http://127.0.0.1:5000/gordon/{GORDON_VERSION}/",
            "furnidata.load.url": "http://127.0.0.1:5000/gamedata/furnidata.xml",
            "productdata.load.url": "http://127.0.0.1:5000/gamedata/productdata.xml",
            "figuredata.load.url": "http://127.0.0.1:5000/gamedata/figuredata.xml",
            "figuremap.load.url": "http://127.0.0.1:5000/gamedata/figuremapV2.xml",
            "effectmap.load.url": "http://127.0.0.1:5000/gamedata/effectmap.xml",
            "dynamic.download.pet.url": "${flash.client.url}pets/%className%.swf",
            "dynamic.download.figure.url": "${flash.client.url}figure/%className%.swf",
            "dynamic.download.effect.url": "${flash.client.url}effects/%className%.swf",
            "flash.dynamic.download.url": "http://127.0.0.1:5000/dcr/hof_furni/",
            "dynamic.download.furniture.url": "${flash.dynamic.download.url}%className%.swf",
            "external.variables.url": "http://127.0.0.1:5000/gamedata/external_variables.txt",
            "external.texts.url": "http://127.0.0.1:5000/gamedata/external_flash_texts.txt",
            "convert.productdata": "1",
            "convert.exteraltexts": "1",
            "convert.figure": "1",
            "convert.figuredata": "1",
            "convert.effect": "1",
            "convert.furniture": "1",
            "convert.furniture.floor.only": "0",
            "convert.furniture.wall.only": "0",
            "convert.pet": "1",
        }

        with open(PurePosixPath(self.PATH_TMP, 'configuration.json').as_posix(), 'w') as _config:
            json.dump(CONFIG, _config, indent=2)
