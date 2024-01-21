#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/21 19:54
# @Author  : astone
# @File    : read2excel.py
# @Description :


import pandas as pd


def read2statistic(filepath):
    """
    读取文件并统计，将分组后的dataframe写入文件
    :param filepath:
    :return:
    """
    df = pd.read_excel(filepath, names=["servid", "servname", "prodid", "prodname", "amount"])
    print(df.amount.sum())
    groupnums = df.groupby("servid").ngroups
    groupkeys = df.groupby("servid").groups.keys()
    # print(df)
    # print(groupnums)
    # print(groupkeys)
    # 分业务写入同一个shell
    with pd.ExcelWriter(r'C:\\Users\\songhuahua\\Desktop\\result.xlsx') as writer:
        for item in groupkeys:
            # print(item)
            # dfitem = df.groupby("servid").get_group(item)['count'].count
            df_item = df.groupby("servid").get_group(item).reset_index()
            serv_name = df_item.servname.iloc[0]
            amount_sum = df_item.amount.sum()
            print(str(item) + "    " + serv_name + "    " + str(amount_sum))
            result = pd.DataFrame(df_item).drop(columns=['index'])
            result.servid = result.servid.apply(lambda x: "'" + str(x))
            result.prodid = result.prodid.apply(lambda x: "'" + str(x))
            result.to_excel(writer, sheet_name=serv_name)


def dataframe_group_generator(file_path):
    """
        读取文件并统计
        :param file_path:
        :return:
    """
    df = pd.read_excel(file_path, names=["servid", "servname", "prodid", "prodname", "amount"])
    # print(df.amount.sum())
    groupnums = df.groupby("servid").ngroups
    groupkeys = df.groupby("servid").groups.keys()
    # print(df)
    # print(groupnums)
    # print(groupkeys)
    for item in groupkeys:
        df_item = df.groupby("servid").get_group(item).reset_index()
        serv_name = df_item.servname.iloc[0]
        amount_sum = df_item.amount.sum()
        print(str(item) + "    " + serv_name + "    " + str(amount_sum))
        result = pd.DataFrame(df_item).drop(columns=['index'])
        result.servid = result.servid.apply(lambda x: "'" + str(x)) # 避免科学计数法保存
        result.prodid = result.prodid.apply(lambda x: "'" + str(x)) # 避免科学计数法保存
        yield result #返回一个生成器对象


def write2excel(file_path):
    """
    将结果写入文件，根据分组类别将数据写入同一个文件的多个sheet中
    :param file_path:
    :return:
    """
    dataframe_iterator = dataframe_group_generator(file_path)
    with pd.ExcelWriter(r'C:\\Users\\songhuahua\\Desktop\\result.xlsx') as writer:
        for item in dataframe_iterator:
            item.to_excel(writer, sheet_name=item.servname.iloc[0])


if __name__ == '__main__':
    path = "C:\\Users\\songhuahua\\Desktop\\provfunc.xlsx"
    # read2statistic(path)
    write2excel(path)
