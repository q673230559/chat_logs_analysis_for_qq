#!/usr/bin/python
# -*- coding:utf-8 -*-

# '''
# Created on 2017.3.8
# @author: hxd
# '''

import time
import re
import datetime
import xlsxwriter

workbook = xlsxwriter.Workbook('out/hello.xlsx')

worksheet = workbook.add_worksheet(u"中文")

worksheet.write('A1', u'你好')

workbook.close()
