'''
Created on 2017年3月8日

@author: Administrator
'''
import re

# 匹配出所有名字,带重复
def getAll_people_list(fileName):
    with open(fileName, encoding='utf-8') as f:
        data = f.read()
        # 例如20:50:52，要匹配其中的20
        pa = re.compile(r"\S+\([0-9]+\)")
        all_people_list = re.findall(pa, data)
        return all_people_list

# 获取所有时间 
def getTime_list():
    time_list = []
    for i in range(0, 24):
        # 这里的判断用于将类似的‘8’ 转化为 ‘08’ 便于和导出数据匹配
        if i < 10:
            i = '0' + str(i)
        else:
            i = str(i)
        time_list.append(i)
    return time_list

# 成员列表,不重复
def getPeople_list(all_people_list):    
        people_list_temp = set(all_people_list)
        people_list = {}
        for plt in people_list_temp:
            people_list[plt] = "0"
        return people_list