#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/10 22:15
# @Author  : astone
# @File    : thread_test.py
# @Description :

import time
import concurrent.futures as futures
from concurrent.futures import ThreadPoolExecutor


def thread_text(x, y):
    print("执行线程1")
    time.sleep(x + y)
    return x + y


def thread_text2():
    print("执行线程2")
    return "thread_text2"

def thread_text3():
    print("执行线程3")
    return "thread_text3"

if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=5)
    executor1 = executor.submit(thread_text, 1, 1)
    executor2 = executor.submit(thread_text2)
    executor3 = executor.submit(thread_text3)
    for i in futures.as_completed([executor1, executor2, executor3]):
        print(i.result())
    executor.shutdown()