# -*- coding:utf-8 -*-
# @Time : 2023-05-31 下午 05:17
# @Author: Astone
# @File : repeate_data_statistic.py



import pandas as pd
from collections import Counter
import os

def repeate_statistc(excel_path):
    '''
    统计文件中重复元素的个数
    :param excel_path:
    :return:
    '''
    df = pd.read_csv(excel_path, names=['logid'], encoding='utf8', dtype=str, delimiter=',')
    value_list = list(df["logid"])
    b = dict(Counter(value_list))
    print({key: value for key, value in b.items() if value > 1})  # 展现重复元素和重复次数


def file_name_walk(file_dir):
    '''
    取出指定目录下所有文件名
    :param file_dir:
    :return:
    '''
    for root, dirs, files in os.walk(file_dir):
        print("root", root)  # 当前目录路径
        print("dirs", dirs)  # 当前路径下所有子目录
        print("files", files)  # 当前路径下所有非目录子文件
    filename_list = [os.path.join(file_dir, file) for file in files]
    return filename_list


if __name__ == '__main__':
    for filepath in file_name_walk( "F:\\py-data\\orderboss"):
        repeate_statistc(filepath)


