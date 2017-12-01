#!/usr/bin/python
# -*- coding:utf-8 -*-

# '''
# Created on 2017.3.8
# @author: hxd
# '''
import re
import jieba.posseg as pseg


# 匹配出所有名字,带重复
# 返回如：['雲生不知处', '雲生不知处', '韩旭东', '1201－璩诗斌',...]
def get_all_people_list(file_name):
    f = open(file_name, "r")
    data = f.read()
    # 例如20:50:52，要匹配其中的20
    pa = r'[\d-]{10}\s[\d:]{7,8}\s+[^\n]+'
    all_people_list = re.findall(pa, data)
    people_list = []
    for apl in all_people_list:
        pa_apl = r'[\d-]{10}\s[\d:]{7,8}\s+'
        people_list.append(unicode(re.split(pa_apl, apl)[1], "utf-8"))
    return people_list


# 获取所有时间
# 返回如：['00', '01', '02',...]
def get_time_list():
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
# 返回如：{'诗斌': '0', '陈雨': '0', '1204-杨磊': '0', '雲生不知处': '0', ...}
def get_people_set(all_people_list):
    people_list_temp = set(all_people_list)
    people_set = {}
    for plt in people_list_temp:
        people_set[plt] = "0"
    return people_set


# 获取不同时间发言次数的set
# 返回如：{'16点': 449, '06点': 0, '03点': 0, '12点': 118, '00点': 0, '04点': 0,...}
def get_time_set(source_file):
    time_list = get_time_list()
    f = open(source_file, "r")
    data = f.read()
    # 例如20:50:52，要匹配其中的20
    pa = re.compile(r"(\d\d):\d\d:\d\d")
    times = re.findall(pa, data)
    time_set = {}
    for i in time_list:
        num = 0
        for time in times:
            if time == i:
                num += 1
        time_set[i + 'h'] = num
    return time_set


# 获取不同人发言次数Set
# 返回如：{'诗斌': 171, '陈雨': 216, '1204-杨磊': 48, '雲生不知处': 2,...}
def get_people_say_set(source_file):
    all_people_list = get_all_people_list(source_file)
    people_set = get_people_set(all_people_list)
    for people in people_set:
        count = 0
        for people_say in all_people_list:
            if (people_say == people):
                count += 1
        people_set[people] = count
    return people_set


# 获取热门名词
# 返回如：[('东西', 16), ('上海', 16), ('武汉', 14), ('杭州', 9), ('滨江', 6),...]
def get_hot_noun_counts(source_file):
    f = open(source_file, "r")
    data = f.read()
    re_pat = r'[\d-]{10}\s[\d:]{7,8}\s+[^\n]+\d{5,11}\)'  # 记录头数组['2016-06-24 15:42:52  张某(40**21)',…]
    # li=re.findall(re_pat,data)
    li_content = re.split(re_pat, data)
    s = ""
    for l in li_content:
        s = s + l
    seg_list = pseg.cut(s.strip())
    lists = []
    for w in seg_list:
        if (w.flag == "ns"):
            lists.append(w.word)
    # print("******群热词统计**0【kp-****")
    # print("带重复名词总量",len(lists))
    seg_list_norepeat = set(lists)
    # print("不重复名词总量",len(seg_list_noRepeat))
    word_set = {}
    for seg in seg_list_norepeat:
        count = 0
        for ss in lists:
            if (ss == seg):
                count += 1
        word_set[seg] = count
    word_tuple_sort = sorted(word_set.items(), key=lambda e: e[1], reverse=True)
    return word_tuple_sort
