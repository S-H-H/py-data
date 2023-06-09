#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/9 22:37
# @Author  : astone
# @File    : request.py.py
# @Description : 发送request请求


import json_util
import requests
import json


def post(request_body, request_url):
    '''
    发送post请求
    :return:
    '''
    header = {"content-type": "application/json"}
    print("请求头：{}, 请求体：{}，请求url：{}".format(header, request_body, request_url))
    response = requests.post(url=request_url, headers=header, data=request_body)
    print("响应状态码：{}，响应信息：{}".format(response.status_code, response.text))
    json_str = json.loads(response.text)
    json_dicts = json.dumps(json_str, indent=4, ensure_ascii=False)
    print(json_dicts)

if __name__ == '__main__':
    request_body = json_util.get_json_field("request_json")
    request_url = "http://127.0.0.1:2020/data/post"
    post(request_body, request_url)
