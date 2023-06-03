#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/3 10:45
# @Author  : astone
# @File    : mysqlutils.py
# @Description :

import pymysql

def query(sql):
    """

    :param biz_code_list:
    :return:
    """
    __db_host = "数据库服务器地址"
    __db_port = 6066
    __db_user = "账号"
    __db_password = "密码"
    __db_database = "数据库名"
    global conn
    global cursor
    try:
        # 连接数据库
        conn = pymysql.connect(host=__db_host,
                               port=__db_port,
                               user=__db_user,
                               password=__db_password,
                               database=__db_database,
                               charset='utf8')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        result = cursor.fetchall()
        return result
    except Exception as e:
        print("！！！查询数据库异常，{}".format(e))
        return None
    finally:
        cursor.close()  # 关闭游标
        conn.close()    # 关闭数据库连接