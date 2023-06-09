# -*- coding:utf-8 -*-
# @Time : 2023-06-09 上午 09:07
# @Author: Astone
# @File : json_util.py.py


import json
import os

def read_json(json_file = os.path.join(os.getcwd(), "config.json")):
    '''
    load() 从json文件中读取json格式数据
    loads() 将字符串类型数据转化为json格式数据
    dump() 将json格式数据保存到文件
    dumps() 将json格式数据保存为字符串类型
    :param json_file:
    :return:
    '''
    with open(json_file,encoding='utf-8') as f:
        json_data = json.load(f)
    return json_data


if __name__ == '__main__':
    json_data = read_json()
    qry_result_json = json.dumps(json_data['qry_result_json'])
    print(qry_result_json)