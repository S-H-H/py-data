#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/3 10:35
# @Author  : astone
# @File    : fileutils.py
# @Description : 工具类


import os

def mkdir(path):
    """
    创建指定的文件夹
    :param path:
    :return:
    """
    path = path.strip()  # 去除首位空格
    path = path.rstrip("\\") # 去除尾部 \ 符号
    isExists = os.path.exists(path) # 判断路径是否存在，存在返回True，不存在返回 False

    if isExists:
        print(path + ' 目录已存在，无需创建')
        return False
    else:
        os.makedirs(path)
        print(path + ' 创建成功')
        return True


def del_files(path, file_type) -> True:
    """
    删除指定目录下的指定文件类型
    :param path: 指定目录
    :param file_type: 指定文件类型如，.jpg、.csv等文件
    :return: 
    """""

    for root , dirs, files in os.walk(path):
        for name in files:
            if name.endswith(file_type):
                os.remove(os.path.join(root,name))
    #print ("Delete File: " + os.path.join(root, name))
    return True





if __name__ == "__main__":
    path = r'E:\VedioClassfication\five-video-classification-methods-master\five-video-classification-methods-master\data\train'
    del_files(path)

