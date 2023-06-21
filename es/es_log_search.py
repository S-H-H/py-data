#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/21 22:14
# @Author  : astone
# @File    : es_log_search.py
# @Description : ES日志信息查询

from elasticsearch import Elasticsearch
from flask import Flask, request, jsonify
from collections import OrderedDict
import logging
import json
import json_util
import os
import re
import datetime
from datetime import timedelta
# 忽略告警信息
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)

# 配置日志记录器及日志级别
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 配置日志处理器
handler = logging.FileHandler('app.log', encoding='utf-8')
handler.setLevel(logging.DEBUG)

# 配置日志格式化器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# 添加日志处理器到日志记录器
logger.addHandler(handler)


@app.route('/es/query', methods=['post'])
def es_query_request():
    if not request.data:  # 检测是否有数据
        return 'Receive Request param failure!'
    # 获取到POST过来的数据，因为我这里传过来的数据需要转换一下编码。根据具体情况而定
    request_data = request.data.decode('utf-8')
    # 将数据转化为字典
    request_json = json.loads(request_data)
    start_time = request_json["startTime"]
    end_time = request_json["endTime"]
    module_name = request_json["moduleName"]
    key_word = request_json["keyWord"]
    query_json = request_json["queryJson"]
    logger.debug("接收到业务受理查询接口的请求参数：" + json.dumps(request_json))
    es_query_clause = [query_json, "keyword_query"][json_util.read_value_by_key(query_json) is None]
    response_dict = es_query(module_name, key_word, start_time, end_time, es_query_clause)
    return response_dict


def es_client(es_index_list=['k8s-index1', 'k8s-index2']):
    """
    建立客户端连接
    :param es_index_list: es索引列表
    :return:
    """
    http_auth = ('elastic_account', 'elastic_password')
    es_1 = Elasticsearch(["http://es_yuanqu_ip:9200"], http_auth=http_auth).options(request_timeout=50)
    es_2 = Elasticsearch(["http://es_shiqiao_ip:9200"], http_auth=http_auth).options(request_timeout=50)
    es_client_dict = {es_index_list[0]: es_1, es_index_list[1]: es_2}
    logger.info("建立客户端连接成功。")
    return es_client_dict


def save_qry_log(es_client, es_index, module_name, logid, start_time, end_time, query_json) -> bool:
    """
     从ES查询日志信息，并保存在相应文件中
    :param es_client: ES
    :param es_index:
    :param module_name:
    :param logid:
    :param start_time:
    :param end_time:
    :param query_json:
    :return:
    # body_dict = json.loads(content)
    """
    query_clause = json_util.read_value_by_key(query_json)
    content = query_clause.replace("{keyword}", logid) \
        .replace("{startdate}", time_to_utc_format(start_time)) \
        .replace("{enddate}", time_to_utc_format(end_time)) \
        .replace("{modulename}", module_name).replace("{logid}", logid)
    reslut_dict = es_client.search(index=es_index, body=json.loads(content))
    now = datetime.datetime.now()
    file = os.getcwd() + os.sep + now.strftime("%Y%m%d") + '.log'
    k8s_pod = None
    result_flag = False
    with open(file, 'a+') as f:
        f.write("#########################查询结果输入文件开始#############################\n")
        for x in reslut_dict['hits']['hits']:
            col = x['_source']
            k8s_pod = str(col['k8s_pod'])
            message = str(col['message'])
            if message is not None:
                result_flag = True
                f.write(message + "\n")
            # if keyword in message:
            #     # 正则匹配提取消息中的powerkey的值
            #     matchresult = re.findall("powerkey：(.*)", message)[0]
        f.write("#########################查询结果输入文件结束#############################\n\n")
    print(k8s_pod)
    return result_flag, k8s_pod


def time_to_utc_format(bj_time) -> str:
    """

    :param bj_time:
    :return:
    """
    # t_bj = datetime.datetime.strptime(bj_time, '%Y%m%d%H%M%S')
    t_bj = datetime.datetime.strptime(bj_time, '%Y-%m-%d %H:%M:%S')
    t_utc = t_bj - timedelta(hours=8)
    t_utc_format = str(t_utc).replace(" ", "T") + ".000Z"
    # print("北京时间：", t_bj, "\n世界时间：", t_utc_format)
    return t_utc_format


def es_query(module_name, key_word, start_time, end_time, query_json):
    """
    ES查询初始化
    :param module_name: ES查询中模块索引字段
    :param key_word: 搜索关键词
    :param start_time: 查询时间范围的开始时间
    :param end_time: 查询时间范围的结束时间
    :param query_json: ES查询语句
    :return:
    """
    result_dict = OrderedDict()
    data = OrderedDict()
    for index, client in es_client().items():
        logger.info("ELK集群数据库索引：{}，客户端：{}".format(index, client))
        result, k8s_pod = save_qry_log(client, index, module_name, key_word, start_time, end_time, query_json)
        if result:
            data['index'] = index
            data['k8s_pod'] = k8s_pod
            data['es_client'] = str(client)
            result_dict['code'] = 200
            result_dict['desc'] = "success"
            result_dict['data'] = data
            return result_dict

    result_dict['code'] = 500
    result_dict['desc'] = "Query result is empty!"
    result_dict['data'] = "None"
    return result_dict


if __name__ == '__main__':
    module_name = "order-boss"
    start_time = "2023-06-16 09:00:00"
    end_time = "2023-06-16 10:30:00"
    key_word = "HOPT2023061205181210039"
    # es_query(module_name, key_word, start_time, end_time, es_query_clause="keyword_query")
    # 这里指定了地址和端口号。
    app.run(host='127.0.0.1', port=2020)
