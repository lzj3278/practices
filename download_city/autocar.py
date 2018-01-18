# -*- coding:utf-8 -*-

import requests
import time
import uuid

timestamp = int(time.time())
uuids = uuid.uuid1()

url = "https://platform.app.autohome.com.cn/platform_v8.2.0/api/violateQuery/addOrUpdateQueryCar"

headers = {
    'User-Agent': 'Android	7.0	autohome	8.6.6	Android',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '378',
    'Host': 'platform.app.autohome.com.cn',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
}

post_data = {
    'registernum': '',
    'memo': '',
    'brandid': 45,
    '_timestamp': timestamp,
    'pm': 2,
    'userpwd': '',
    'net': 'WIFI',
    'deviceid': '866149030893950',
    'carid': 0,
    '_sign': '5DB6907EEA4D3F8C569E48940A2F0D71',
    'userid': 0,
    'querycityids': 650100,
    'a': 2,
    'v': '1.6.0',
    'seriesid': 2056,
    'enginenum': 'G258088',
    'brandtype': 0,
    'username': '',
    'iscomplete': 1,
    'framenum': 'LVGBH51K0DG115674',
    'carnumber': '新A898G0',
    'udid': uuids,
    'specid': 28769,
    'auth': '',
}

r = requests.post(url, headers=headers, data=post_data)
print(r.text)
