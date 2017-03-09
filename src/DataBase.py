'''
Created on 2017年3月8日

@author: Administrator
'''
import re
import jieba.posseg as pseg

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

# 获取不同时间发言次数的set
def getTimeSet(sourceFile):
    time_list = getTime_list()
    with open(sourceFile, encoding='utf-8') as f:
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
            time_set[i+'点'] = num
        return time_set

# 获取不同人发言次数Set
def getPeopleSaySet(sourceFile):
    all_people_list = getAll_people_list(sourceFile)
    people_list = getPeople_list(all_people_list)
    for people in people_list:
        count = 0
        for people_say in all_people_list:
            if (people_say == people):
                count += 1
        people_list[people] = count
    return people_list

def getHotNounCounts(sourceFile):
    with open(sourceFile, encoding='utf-8') as f:
        data=f.read()
        re_pat = r'[\d-]{10}\s[\d:]{7,8}\s+[^\n]+\d{5,11}\)'  # 记录头数组['2016-06-24 15:42:52  张某(40**21)',…]
        # li=re.findall(re_pat,data)
        li_content = re.split(re_pat, data)
        s=""
        for l in li_content:
            s=s+l
        seg_list = pseg.cut(s.strip())
        lists = []
        for w in seg_list:
            if(w.flag=="ns"):
                lists.append(w.word)
        #print("******群热词统计******")
        #print("带重复名词总量",len(lists))
        seg_list_noRepeat=set(lists)
        #print("不重复名词总量",len(seg_list_noRepeat))
        word_set={}
        for seg in seg_list_noRepeat:
            count=0
            for ss in lists:
                if(ss == seg):
                    count+=1
            word_set[seg]=count
        word_tuple_sort = sorted(word_set.items(), key=lambda e:e[1], reverse=True)
        return word_tuple_sort