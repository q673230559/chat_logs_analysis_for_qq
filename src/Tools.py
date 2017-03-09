'''
Created on 2017年3月9日

@author: Administrator
'''

import xlsxwriter

# 添加sheet,两列结构
def addSheetType1(workBook,sheetName,thislist):
    workSheet = workBook.add_worksheet(sheetName)
    workSheet.set_column('A:A', 40)
    workSheet.set_column('B:B', 10)
    
    