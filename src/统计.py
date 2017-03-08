'''
Created on 2017年3月8日

@author: Administrator
'''
import re;
import xlsxwriter;

people_list = {}
all_people_list = [];

# Going
print("Going...");

#  创建EXCEL表格并设置参数
workbook = xlsxwriter.Workbook('20172018华中师大教技群1.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 5)
worksheet.set_column('B:B', 10)

# 构造出成员里列表
with open("20172018华中师大教技群.txt", encoding='utf-8') as f:
    data = f.read()
    # 例如20:50:52，要匹配其中的20
    pa = re.compile(r"\S+\([0-9]+\)");
    all_people_list = re.findall(pa, data);
    people_list_temp = set(all_people_list);
    for plt in people_list_temp:
        people_list[plt]="0"
    # 记得关闭工作薄
    # workbook.close()
    # print("处理完毕，快去看看文件夹下面新建的.xlsx文件吧")

# 统计成员发言次数
for people in people_list:
    count = 0;
    for people_say in all_people_list:
        if (people_say == people):
            count += 1
    people_list[people] = count;


#排序
b = sorted(people_list.items(), key=lambda e:e[1], reverse=True);
i=0;
for bb in b:
    i+=1;
    print (bb[0],"--->",bb[1]);
    # 计数完毕，写入数据，write参数为：行，列，数据
    worksheet.write(int(i), 0, bb[0])
    worksheet.write(int(i), 1, bb[1])
    
# 记得关闭工作薄
workbook.close()
print("End")
    




