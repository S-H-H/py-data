#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/30 9:35
# @Author  : astone
# @File    : time.py
# @Description : 时间模块datetime及time

import datetime
now = datetime.datetime.now() #获取当前时间
print('今天是{}月{}日{}点{}分{}秒'.format(now.month,now.day,now.hour,now.minute,now.second))
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


import time
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
