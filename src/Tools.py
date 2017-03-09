'''
Created on 2017年3月9日

@author: Administrator
'''


# 添加sheet,两列结构 最后一个参数是元组
def addSheetTpye1(workBook,sheetName,thisTuple,A_title,B_title):
    print("正在写入数据至 :",sheetName," 工作簿")
    # 创建sheet
    workSheet = workBook.add_worksheet(sheetName)
    workSheet.set_column('A:A', 40)
    workSheet.set_column('B:B', 10)
    # 写入数据，write参数为：行，列，数据
    i = 1
    workSheet.write(0, 0, A_title)
    workSheet.write(0, 1, B_title)
    for pls in thisTuple:
        workSheet.write(int(i), 0, pls[0])
        workSheet.write(int(i), 1, pls[1])
        i += 1
    print("写入完成")

# 添加sheet,两列结构 最后一个参数是Set
def addSheetTpye2(workBook,sheetName,thisSet):
    # 创建sheet
    workSheet = workBook.add_worksheet(sheetName)
    workSheet.set_column('A:A', 40)
    workSheet.set_column('B:B', 10)
    # 写入数据，write参数为：行，列，数据
    i = 0
    for pls in thisSet:
        workSheet.write(int(i), 0, pls)
        workSheet.write(int(i), 1, thisSet[pls])
        i += 1