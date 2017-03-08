'''
Created on 2017年3月8日

@author: Administrator
'''
import xlsxwriter;

list_sa = [1,2]

def addSheet():
    workBook = xlsxwriter.Workbook("demo.xlsx");
    workSheet = workBook.add_worksheet();
    workSheet.set_column('A:A', 20);
    
addSheet();



def test():
    list_sa.append([10,11])
    
test()
print(list_sa) 