# encoding: utf-8
"""
Task: RetroImager
---------
This task allows avatars to be rendered locally.
The tool utilized in the background is https://github.com/billsonnn/nitro-imager.
"""
from pathlib import PurePosixPath, Path

import shutil
import subprocess
import json
import time
import queue

from backend.tasks.base import BackgroundThread


class ImagerThread(BackgroundThread):
    name = 'Nitro-Imager'
    PATH_ZIP = PurePosixPath(Path(__file__).resolve().parent, 'nitro-imager.zip').as_posix()
    PATH_TMP = PurePosixPath(Path(__file__).resolve().parent, 'tmp').as_posix()

    def startup(self) -> None:
        """
        Setup environment for downloader to work
        """
        Path(self.PATH_TMP).mkdir(exist_ok=True)
        try:
            shutil.unpack_archive(self.PATH_ZIP, self.PATH_TMP)
        except (PermissionError): pass
        self._update_config()
        print('* Imager started')

    def shutdown(self) -> None:
        """
        Teardown folders with graceful shutdown
        """
        try:
            shutil.rmtree(self.PATH_TMP)
        except (FileNotFoundError,): pass
        print('* Imager stopped')
        
    def handle(self) -> None:
        waiting = True
        while waiting:
            with self.app.app_context():
                from backend.models import SystemTaskModel
                task = SystemTaskModel.query.filter(SystemTaskModel.id == 3).first()
                waiting = not task.has_ran
            time.sleep(1)
            
        subprocess.run(["yarn", "--cwd", self.PATH_TMP, "start"], shell=True)

    def _update_config(self):
        """
        Set configuration for the nitro-imager
        """           
        CONFIG = {
            "api.host": "127.0.0.1",
            "api.port": 8889,
            "asset.url": "http://127.0.0.1:5000",
            "gamedata.url": "${asset.url}/gamedata",
            "avatar.save.path": "./saved-figures",
            "avatar.actions.url": "${gamedata.url}/HabboAvatarActions.json",
            "avatar.figuredata.url": "${gamedata.url}/FigureData.json",
            "avatar.figuremap.url": "${gamedata.url}/FigureMap.json",
            "avatar.effectmap.url": "${gamedata.url}/EffectMap.json",
            "avatar.asset.url": "${asset.url}/bundled/figure/%libname%.nitro",
            "avatar.asset.effect.url": "${asset.url}/bundled/effect/%libname%.nitro",
            "avatar.mandatory.libraries": ["bd:1", "li:0"],
            "avatar.mandatory.effect.libraries": [
                "dance.1",
                "dance.2",
                "dance.3",
                "dance.4"
            ],
            "avatar.default.figuredata": {
                "palettes": [
                    {
                        "id": 1,
                        "colors": [
                            {
                                "id": 99999,
                                "index": 1001,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "DDDDDD"
                            },
                            {
                                "id": 99998,
                                "index": 1001,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "FAFAFA"
                            }
                        ]
                    },
                    {
                        "id": 3,
                        "colors": [
                            {
                                "id": 10001,
                                "index": 1001,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "EEEEEE"
                            },
                            {
                                "id": 10002,
                                "index": 1002,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "FA3831"
                            },
                            {
                                "id": 10003,
                                "index": 1003,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "FD92A0"
                            },
                            {
                                "id": 10004,
                                "index": 1004,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "2AC7D2"
                            },
                            {
                                "id": 10005,
                                "index": 1005,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "35332C"
                            },
                            {
                                "id": 10006,
                                "index": 1006,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "EFFF92"
                            },
                            {
                                "id": 10007,
                                "index": 1007,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "C6FF98"
                            },
                            {
                                "id": 10008,
                                "index": 1008,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "FF925A"
                            },
                            {
                                "id": 10009,
                                "index": 1009,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "9D597E"
                            },
                            {
                                "id": 10010,
                                "index": 1010,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "B6F3FF"
                            },
                            {
                                "id": 10011,
                                "index": 1011,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "6DFF33"
                            },
                            {
                                "id": 10012,
                                "index": 1012,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "3378C9"
                            },
                            {
                                "id": 10013,
                                "index": 1013,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "FFB631"
                            },
                            {
                                "id": 10014,
                                "index": 1014,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "DFA1E9"
                            },
                            {
                                "id": 10015,
                                "index": 1015,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "F9FB32"
                            },
                            {
                                "id": 10016,
                                "index": 1016,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "CAAF8F"
                            },
                            {
                                "id": 10017,
                                "index": 1017,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "C5C6C5"
                            },
                            {
                                "id": 10018,
                                "index": 1018,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "47623D"
                            },
                            {
                                "id": 10019,
                                "index": 1019,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "8A8361"
                            },
                            {
                                "id": 10020,
                                "index": 1020,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "FF8C33"
                            },
                            {
                                "id": 10021,
                                "index": 1021,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "54C627"
                            },
                            {
                                "id": 10022,
                                "index": 1022,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "1E6C99"
                            },
                            {
                                "id": 10023,
                                "index": 1023,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "984F88"
                            },
                            {
                                "id": 10024,
                                "index": 1024,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "77C8FF"
                            },
                            {
                                "id": 10025,
                                "index": 1025,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "FFC08E"
                            },
                            {
                                "id": 10026,
                                "index": 1026,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "3C4B87"
                            },
                            {
                                "id": 10027,
                                "index": 1027,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "7C2C47"
                            },
                            {
                                "id": 10028,
                                "index": 1028,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "D7FFE3"
                            },
                            {
                                "id": 10029,
                                "index": 1029,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "8F3F1C"
                            },
                            {
                                "id": 10030,
                                "index": 1030,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "FF6393"
                            },
                            {
                                "id": 10031,
                                "index": 1031,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "1F9B79"
                            },
                            {
                                "id": 10032,
                                "index": 1032,
                                "club": 0,
                                "selectable": False,
                                "hexCode": "FDFF33"
                            }
                        ]
                    }
                ],
                "setTypes": [
                    {
                        "type": "hd",
                        "paletteId": 1,
                        "mandatory_f_0": True,
                        "mandatory_f_1": True,
                        "mandatory_m_0": True,
                        "mandatory_m_1": True,
                        "sets": [
                            {
                                "id": 99999,
                                "gender": "U",
                                "club": 0,
                                "colorable": True,
                                "selectable": False,
                                "preselectable": False,
                                "sellable": False,
                                "parts": [
                                    {
                                        "id": 1,
                                        "type": "bd",
                                        "colorable": True,
                                        "index": 0,
                                        "colorindex": 1
                                    },
                                    {
                                        "id": 1,
                                        "type": "hd",
                                        "colorable": True,
                                        "index": 0,
                                        "colorindex": 1
                                    },
                                    {
                                        "id": 1,
                                        "type": "lh",
                                        "colorable": True,
                                        "index": 0,
                                        "colorindex": 1
                                    },
                                    {
                                        "id": 1,
                                        "type": "rh",
                                        "colorable": True,
                                        "index": 0,
                                        "colorindex": 1
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "bds",
                        "paletteId": 1,
                        "mandatory_f_0": False,
                        "mandatory_f_1": False,
                        "mandatory_m_0": False,
                        "mandatory_m_1": False,
                        "sets": [
                            {
                                "id": 10001,
                                "gender": "U",
                                "club": 0,
                                "colorable": True,
                                "selectable": False,
                                "preselectable": False,
                                "sellable": False,
                                "parts": [
                                    {
                                        "id": 10001,
                                        "type": "bds",
                                        "colorable": True,
                                        "index": 0,
                                        "colorindex": 1
                                    },
                                    {
                                        "id": 10001,
                                        "type": "lhs",
                                        "colorable": True,
                                        "index": 0,
                                        "colorindex": 1
                                    },
                                    {
                                        "id": 10001,
                                        "type": "rhs",
                                        "colorable": True,
                                        "index": 0,
                                        "colorindex": 1
                                    }
                                ],
                                "hiddenLayers": [
                                    { "partType": "bd" },
                                    { "partType": "rh" },
                                    { "partType": "lh" }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "ss",
                        "paletteId": 3,
                        "mandatory_f_0": False,
                        "mandatory_f_1": False,
                        "mandatory_m_0": False,
                        "mandatory_m_1": False,
                        "sets": [
                            {
                                "id": 10010,
                                "gender": "F",
                                "club": 0,
                                "colorable": True,
                                "selectable": False,
                                "preselectable": False,
                                "sellable": False,
                                "parts": [
                                    {
                                        "id": 10001,
                                        "type": "ss",
                                        "colorable": True,
                                        "index": 0,
                                        "colorindex": 1
                                    }
                                ],
                                "hiddenLayers": [
                                    { "partType": "ch" },
                                    { "partType": "lg" },
                                    { "partType": "ca" },
                                    { "partType": "wa" },
                                    { "partType": "sh" },
                                    { "partType": "ls" },
                                    { "partType": "rs" },
                                    { "partType": "lc" },
                                    { "partType": "rc" },
                                    { "partType": "cc" },
                                    { "partType": "cp" }
                                ]
                            },
                            {
                                "id": 10011,
                                "gender": "M",
                                "club": 0,
                                "colorable": True,
                                "selectable": False,
                                "preselectable": False,
                                "sellable": False,
                                "parts": [
                                    {
                                        "id": 10002,
                                        "type": "ss",
                                        "colorable": True,
                                        "index": 0,
                                        "colorindex": 1
                                    }
                                ],
                                "hiddenLayers": [
                                    { "partType": "ch" },
                                    { "partType": "lg" },
                                    { "partType": "ca" },
                                    { "partType": "wa" },
                                    { "partType": "sh" },
                                    { "partType": "ls" },
                                    { "partType": "rs" },
                                    { "partType": "lc" },
                                    { "partType": "rc" },
                                    { "partType": "cc" },
                                    { "partType": "cp" }
                                ]
                            }
                        ]
                    }
                ]
            },
            "avatar.default.actions": {
                "actions": [
                    {
                        "id": "Default",
                        "state": "std",
                        "precedence": 1000,
                        "main": True,
                        "isDefault": True,
                        "geometryType": "vertical",
                        "activePartSet": "figure",
                        "assetPartDefinition": "std"
                    }
                ]
            }
        }

        with open(PurePosixPath(self.PATH_TMP, 'config.json').as_posix(), 'w') as _config:
            json.dump(CONFIG, _config, indent=2)
