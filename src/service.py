#!/usr/bin/python
# -*- coding:utf-8 -*-

# '''
# Created on 2017.3.8
# @author: hxd
# '''
import xlsxwriter
import database
import tools
import os


# 循环建立excel文档
def build_graph():
    # 指明被遍历的文件夹
    rootdir = "./in/"
    for rd in os.listdir(rootdir):
        build_one_graph("in/"+rd, "out/"+rd.split(".txt")[0]+".xlsx")


# 建立图表
def build_one_graph(source_file, build_file):
    # 创建EXCEL工作簿
    workbook = xlsxwriter.Workbook(build_file)

    # 时间段活跃统计图
    time_set = database.get_time_set(source_file)
    # 排序
    time_tuple = sorted(time_set.items(), key=lambda e: e[0], reverse=False)
    # 写入工作簿
    tools.add_sheet_type(workbook, u"时间段活跃", time_tuple, u"时间", u"活跃量")

    # 成员活跃图
    people_say_set = database.get_people_say_set(source_file)
    # 排序
    people_say_tuple = sorted(people_say_set.items(), key=lambda e: e[1], reverse=True)

    # 写入工作簿
    tools.add_sheet_type(workbook, u"成员活跃", people_say_tuple, u"成员", u"活跃量")

    # 热词统计
    word_tuple = database.get_hot_noun_counts(source_file)
    # 写入工作簿
    tools.add_sheet_type(workbook, u"热词统计", word_tuple, u"词汇", u"出现次数")

    # 关闭文档
    workbook.close()
