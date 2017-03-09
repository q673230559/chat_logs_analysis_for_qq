'''
Created on 2017年3月8日

@author: Administrator
'''
import xlsxwriter
import re
import DataBase

# 建立活跃图
def buildActiveGraph(sourceFile, buildFile):
    # 创建EXCEL表格并设置参数
    workbook = xlsxwriter.Workbook(buildFile)
    ### 时间段活跃图
    worksheet = workbook.add_worksheet("时间段活跃")
    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:B', 10)
    time_list = DataBase.getTime_list()
    with open(sourceFile, encoding='utf-8') as f:
        data = f.read()
        # 例如20:50:52，要匹配其中的20
        pa = re.compile(r"(\d\d):\d\d:\d\d")
        times = re.findall(pa, data)
        for i in time_list:
            num = 0
            for time in times:
                if time == i:
                    num += 1
            print(i, '--->', num)
            # 计数完毕，写入数据，write参数为：行，列，数据
            worksheet.write(int(i), 0, str(i) + "点")
            worksheet.write(int(i), 1, num)
    ### 成员活跃图           
    worksheet1 = workbook.add_worksheet("成员活跃")
    worksheet1.set_column('A:A', 40)
    worksheet1.set_column('B:B', 5)    
    # 统计发言次数
    all_people_list = DataBase.getAll_people_list(sourceFile)
    people_list = DataBase.getPeople_list(all_people_list)
    for people in people_list:
        count = 0
        for people_say in all_people_list:
            if (people_say == people):
                count += 1
        people_list[people] = count
    # 排序
    people_list_sort = sorted(people_list.items(), key=lambda e:e[1], reverse=True)
    # 写入数据，write参数为：行，列，数据
    i = 0
    for pls in people_list_sort:
        print (pls);
        worksheet1.write(int(i), 0, pls[0])
        worksheet1.write(int(i), 1, pls[1])
        i += 1
        
    ### 热词
    
    # 关闭工作薄
    workbook.close()




    


# Going
print("~START~")
buildActiveGraph("20172018华中师大教技群.txt", '20172018华中师大教技群.xlsx')
print("~END~")
    




