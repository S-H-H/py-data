#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/1 11:31
# @Author  : astone
# @File    : test.py
# @Description :

import json

string = """{"code": "1000000", "data": [{"address": "", "productClass": "GM630", "hasWiFi": "1", "presetVersion": "3.0.2", "provinceCode": 50, "swversion": "V1.2.00.208", "userId": "28137379981957", "phone": "13538358081", "vendor": "CIOT", "name": "", "nickname": "智能家庭网关", "osType": 0, "online": "", "macFlag": 0, "gwsn": "CIOT26C21E78", "provinceName": "广东", "activationTime": "2021-10-20 15:18:32", "broadbandAccount": "13538358081@139.gd", "did": "8427B6C21E78", "productType": 1, "status": 1}]}"""



rdict = json.loads(string)
print(rdict['data'][0]['phone'])
print(type(rdict['data'][0]))
print(type(rdict['data'][0]))