'''
Created on 2017年3月8日

@author: Administrator
'''
import re;
import xlsxwriter;



# 所有出现的成员带有重复
def getAll_people_list():
    with open("20172018华中师大教技群.txt", encoding='utf-8') as f:
        data = f.read()
        # 例如20:50:52，要匹配其中的20
        pa = re.compile(r"\S+\([0-9]+\)")
        all_people_list = re.findall(pa, data)
        return all_people_list

# 所有出现的成员不重复
def getPeople_list(all_people_list):    
        people_list_temp = set(all_people_list)
        people_list = {}
        for plt in people_list_temp:
            people_list[plt]="0"
        return people_list

# 统计成员发言次数
def countSayTimes(all_people_list,people_list):
    for people in people_list:
        count = 0;
        for people_say in all_people_list:
            if (people_say == people):
                count += 1
        people_list[people] = count


#按照发言次数排序
def sortByCount(people_list):
    people_list_sort = sorted(people_list.items(), key=lambda e:e[1], reverse=True);
    return people_list_sort


def outToExcel(worksheet,people_list_sort):
    i=0;
    for pls in people_list_sort:
        i+=1;
        print (pls);
        # 计数完毕，写入数据，write参数为：行，列，数据
        worksheet.write(int(i), 0, pls[0])
        worksheet.write(int(i), 1, pls[1])
    # 记得关闭工作薄
    workbook.close()

    


# Going
print("~START~")
# 创建EXCEL表格并设置参数
workbook = xlsxwriter.Workbook('20172018华中师大教技群.xlsx')
worksheet = workbook.add_worksheet("成员活跃")
worksheet.set_column('A:A', 40)
worksheet.set_column('B:B', 5)
all_people_list = getAll_people_list()
people_list = getPeople_list(all_people_list)
countSayTimes(all_people_list,people_list)
people_list_sort=sortByCount(people_list)
outToExcel(worksheet,people_list_sort)
worksheet1 = workbook.add_worksheet("时间段活跃")
worksheet1.set_column('A:A', 10)
worksheet1.set_column('B:B', 5)







    


print("~END~")
    




