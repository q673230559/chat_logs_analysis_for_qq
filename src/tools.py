#!/usr/bin/python
# -*- coding:utf-8 -*-

# '''
# Created on 2017.3.8
# @author: hxd
# '''


# 添加sheet,两列结构 最后一个参数是元组
def add_sheet_type(workbook, sheetname, thistuple, a_title, b_title):
    # 创建sheet
    worksheet = workbook.add_worksheet(sheetname)
    worksheet.set_column('A:A', 40)
    worksheet.set_column('B:B', 10)
    # 写入数据，write参数为：行，列，数据
    i = 1
    worksheet.write(0, 0, a_title)
    worksheet.write(0, 1, b_title)
    for pls in thistuple:
        worksheet.write(int(i), 0, pls[0])
        worksheet.write(int(i), 1, pls[1])
        i += 1


# 添加sheet,两列结构 最后一个参数是Set
def add_sheet_type2(workbook, sheetname, thistuple, a_title, b_title):
    # print("正在写入数据至 :", sheetname, " 工作簿")
    # 创建sheet
    worksheet = workbook.add_worksheet(sheetname)
    worksheet.set_column('A:A', 40)
    worksheet.set_column('B:B', 10)
    # 写入数据，write参数为：行，列，数据
    i = 1
    worksheet.write(0, 0, a_title)
    worksheet.write(0, 1, b_title)
    for pls in thistuple:
        worksheet.write(int(i), 0, pls)
        worksheet.write(int(i), 1, thistuple[pls])
        i += 1
    # print("写入完成")
