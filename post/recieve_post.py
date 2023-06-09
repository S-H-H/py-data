#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/8 22:30
# @Author  : astone
# @File    : recieve_post.py
# @Description :

import json
import logging

from flask import Flask, request, jsonify

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
app.debug = True


@app.route('/data/post', methods=['post'])
def add_stu():
	if not request.data:  # 检测是否有数据
		return ('fail')
	request_data = request.data.decode('utf-8')
	# 获取到POST过来的数据，数据需要转换一下编码。根据晶具体情况而定
	request_json = json.loads(request_data)
	app.logger.info("接收请求参数：" + json.dumps(request_json))
	result_json = {
		"lastday": "20230421",
		"appkey": "AOPL",
		"response": {
			"wcode": "00000",
			"wdesc": "success"
		},
		"result": "{\"OprTime\":\"20230421152532\",\"ResultDesc\":\"成功\"}",
		"trans": "55463dhfgh",
		"transTime": "20230421152532",
		"testFlag": "fghdfghfg"
	}
	# 把区获取到的数据转为JSON格式，返回JSON数据。
	return jsonify(result_json)

if __name__ == '__main__':
	# 这里指定了地址和端口号。
    app.run(host='127.0.0.1', port=2020)



