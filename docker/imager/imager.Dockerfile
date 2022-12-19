FROM annihilator708/py_node:3.9.13 AS deplayer
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get install -y zip
WORKDIR /workspaceFolder
COPY ./docker/imager/nitro-imager.zip .
RUN unzip nitro-imager.zip

RUN sh -c "$(/bin/echo -e 'cat > /workspaceFolder/config.json << EOF\
    \n{\
    \n    "api.host": "0.0.0.0",\
    \n    "api.port": 1338,\
    \n    "asset.url": "http://127.0.0.1:5000",\
    \n    "gamedata.url": "\${asset.url}/gamedata",\
    \n    "avatar.save.path": "/workspaceFolder/saved-figures",\
    \n    "avatar.actions.url": "\${gamedata.url}/HabboAvatarActions.json",\
    \n    "avatar.figuredata.url": "\${gamedata.url}/FigureData.json",\
    \n    "avatar.figuremap.url": "\${gamedata.url}/FigureMap.json",\
    \n    "avatar.effectmap.url": "\${gamedata.url}/EffectMap.json",\
    \n    "avatar.asset.url": "\${asset.url}/bundled/figure/%libname%.nitro",\
    \n    "avatar.asset.effect.url": "\${asset.url}/bundled/effect/%libname%.nitro",\
    \n    "avatar.mandatory.libraries": [\
    \n        "bd:1",\
    \n        "li:0"\
    \n    ],\
    \n    "avatar.mandatory.effect.libraries": [\
    \n        "dance.1",\
    \n        "dance.2",\
    \n        "dance.3",\
    \n        "dance.4"\
    \n    ],\
    \n    "avatar.default.figuredata": {"palettes":[{"id":1,"colors":[{"id":99999,"index":1001,"club":0,"selectable":false,"hexCode":"DDDDDD"},{"id":99998,"index":1001,"club":0,"selectable":false,"hexCode":"FAFAFA"}]},{"id":3,"colors":[{"id":10001,"index":1001,"club":0,"selectable":false,"hexCode":"EEEEEE"},{"id":10002,"index":1002,"club":0,"selectable":false,"hexCode":"FA3831"},{"id":10003,"index":1003,"club":0,"selectable":false,"hexCode":"FD92A0"},{"id":10004,"index":1004,"club":0,"selectable":false,"hexCode":"2AC7D2"},{"id":10005,"index":1005,"club":0,"selectable":false,"hexCode":"35332C"},{"id":10006,"index":1006,"club":0,"selectable":false,"hexCode":"EFFF92"},{"id":10007,"index":1007,"club":0,"selectable":false,"hexCode":"C6FF98"},{"id":10008,"index":1008,"club":0,"selectable":false,"hexCode":"FF925A"},{"id":10009,"index":1009,"club":0,"selectable":false,"hexCode":"9D597E"},{"id":10010,"index":1010,"club":0,"selectable":false,"hexCode":"B6F3FF"},{"id":10011,"index":1011,"club":0,"selectable":false,"hexCode":"6DFF33"},{"id":10012,"index":1012,"club":0,"selectable":false,"hexCode":"3378C9"},{"id":10013,"index":1013,"club":0,"selectable":false,"hexCode":"FFB631"},{"id":10014,"index":1014,"club":0,"selectable":false,"hexCode":"DFA1E9"},{"id":10015,"index":1015,"club":0,"selectable":false,"hexCode":"F9FB32"},{"id":10016,"index":1016,"club":0,"selectable":false,"hexCode":"CAAF8F"},{"id":10017,"index":1017,"club":0,"selectable":false,"hexCode":"C5C6C5"},{"id":10018,"index":1018,"club":0,"selectable":false,"hexCode":"47623D"},{"id":10019,"index":1019,"club":0,"selectable":false,"hexCode":"8A8361"},{"id":10020,"index":1020,"club":0,"selectable":false,"hexCode":"FF8C33"},{"id":10021,"index":1021,"club":0,"selectable":false,"hexCode":"54C627"},{"id":10022,"index":1022,"club":0,"selectable":false,"hexCode":"1E6C99"},{"id":10023,"index":1023,"club":0,"selectable":false,"hexCode":"984F88"},{"id":10024,"index":1024,"club":0,"selectable":false,"hexCode":"77C8FF"},{"id":10025,"index":1025,"club":0,"selectable":false,"hexCode":"FFC08E"},{"id":10026,"index":1026,"club":0,"selectable":false,"hexCode":"3C4B87"},{"id":10027,"index":1027,"club":0,"selectable":false,"hexCode":"7C2C47"},{"id":10028,"index":1028,"club":0,"selectable":false,"hexCode":"D7FFE3"},{"id":10029,"index":1029,"club":0,"selectable":false,"hexCode":"8F3F1C"},{"id":10030,"index":1030,"club":0,"selectable":false,"hexCode":"FF6393"},{"id":10031,"index":1031,"club":0,"selectable":false,"hexCode":"1F9B79"},{"id":10032,"index":1032,"club":0,"selectable":false,"hexCode":"FDFF33"}]}],"setTypes":[{"type":"hd","paletteId":1,"mandatory_f_0":true,"mandatory_f_1":true,"mandatory_m_0":true,"mandatory_m_1":true,"sets":[{"id":99999,"gender":"U","club":0,"colorable":true,"selectable":false,"preselectable":false,"sellable":false,"parts":[{"id":1,"type":"bd","colorable":true,"index":0,"colorindex":1},{"id":1,"type":"hd","colorable":true,"index":0,"colorindex":1},{"id":1,"type":"lh","colorable":true,"index":0,"colorindex":1},{"id":1,"type":"rh","colorable":true,"index":0,"colorindex":1}]}]},{"type":"bds","paletteId":1,"mandatory_f_0":false,"mandatory_f_1":false,"mandatory_m_0":false,"mandatory_m_1":false,"sets":[{"id":10001,"gender":"U","club":0,"colorable":true,"selectable":false,"preselectable":false,"sellable":false,"parts":[{"id":10001,"type":"bds","colorable":true,"index":0,"colorindex":1},{"id":10001,"type":"lhs","colorable":true,"index":0,"colorindex":1},{"id":10001,"type":"rhs","colorable":true,"index":0,"colorindex":1}],"hiddenLayers":[{"partType":"bd"},{"partType":"rh"},{"partType":"lh"}]}]},{"type":"ss","paletteId":3,"mandatory_f_0":false,"mandatory_f_1":false,"mandatory_m_0":false,"mandatory_m_1":false,"sets":[{"id":10010,"gender":"F","club":0,"colorable":true,"selectable":false,"preselectable":false,"sellable":false,"parts":[{"id":10001,"type":"ss","colorable":true,"index":0,"colorindex":1}],"hiddenLayers":[{"partType":"ch"},{"partType":"lg"},{"partType":"ca"},{"partType":"wa"},{"partType":"sh"},{"partType":"ls"},{"partType":"rs"},{"partType":"lc"},{"partType":"rc"},{"partType":"cc"},{"partType":"cp"}]},{"id":10011,"gender":"M","club":0,"colorable":true,"selectable":false,"preselectable":false,"sellable":false,"parts":[{"id":10002,"type":"ss","colorable":true,"index":0,"colorindex":1}],"hiddenLayers":[{"partType":"ch"},{"partType":"lg"},{"partType":"ca"},{"partType":"wa"},{"partType":"sh"},{"partType":"ls"},{"partType":"rs"},{"partType":"lc"},{"partType":"rc"},{"partType":"cc"},{"partType":"cp"}]}]}]},    \
    \n    "avatar.default.actions": {\
    \n        "actions": [\
    \n            {\
    \n                "id": "Default",\
    \n                "state": "std",\
    \n                "precedence": 1000,\
    \n                "main": true,\
    \n                "isDefault": true,\
    \n                "geometryType": "vertical",\
    \n                "activePartSet": "figure",\
    \n                "assetPartDefinition": "std"\
    \n            }\
    \n        ]\
    \n    }\
    \n}\
    \nEOF\n')"

RUN npm install
RUN npm run build

EXPOSE 1338
ENTRYPOINT [ "npm", "start" ]
