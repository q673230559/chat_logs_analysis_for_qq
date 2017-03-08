'''
Created on 2017年3月8日

@author: Administrator
'''
import re;
import xlsxwriter;
 
# 获取24个时间段----->time_list
# 用于之后时间的分段
time_list = []
for i in range(0, 24):
    # 这里的判断用于将类似的‘8’ 转化为 ‘08’ 便于和导出数据匹配
    if i < 10:
        i = '0' + str(i)
    else:
        i = str(i)
    time_list.append(i)
#  创建EXCEL表格并设置参数
workbook = xlsxwriter.Workbook('20172018华中师大教技群.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 5)
worksheet.set_column('B:B', 10)
 
# 定义一个函数，对每一个时间段进行计数
# times是正则匹配到的 “小时” 数据，在一个列表里面
def everytime(i):
    num = 0
    for time in times:
        if time == i:
            num += 1
    print(i, '--->', num)
    # 计数完毕，写入数据，write参数为：行，列，数据
    worksheet.write(int(i), 0, str(i) + "点")
    worksheet.write(int(i), 1, num)
 
# 打开文件，开始匹配“小时”数据，并计数保存
# 这里记得要转换编码为utf-8
with open("20172018华中师大教技群.txt", encoding='utf-8') as f:
    data = f.read()
    # 例如20:50:52，要匹配其中的20
    pa = re.compile(r"(\d\d):\d\d:\d\d")
    times = re.findall(pa, data)
    for i in time_list:
        everytime(i)
    # 记得关闭工作薄
    workbook.close()
    print("处理完毕，快去看看文件夹下面新建的.xlsx文件吧")
