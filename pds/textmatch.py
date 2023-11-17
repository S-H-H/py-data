#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Description: TODO 从一列数据中找出包含指定字符串的数据，并进行去重
# @Time : 2023-11-17 下午 04:58
# @Author: Astone
# @File : datamatch.py


import pandas as pd


def text_macth(file, matchedphase):
    """

    :param file:
    :param matchedphase:
    :return:
    """
    phdf = pd.read_csv(file, names=["word"],dtype=str)
    resltdf = phdf[phdf.word.str.contains(matchedphase)] # 匹配指定字符串数据
    resltdf = resltdf.drop_duplicates()
    # resltdf.to_csv("H:\\des.txt",index=False, header=None)
    resltdf.to_excel("destination.xlsx",index=False, header=None)

if __name__ == '__main__':
    text_macth(file="demo.txt", matchedphase="kkk")
