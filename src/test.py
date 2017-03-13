# '''
# Created on 2017年3月9日
#
# @author: Administrator
# '''
import re

with open("Life.txt", encoding='utf-8') as f:
        data = f.read()
        # 例如20:50:52，要匹配其中的20
        pa = r'[\d-]{10}\s[\d:]{7,8}\s+[^\n]+'
        all_people_list = re.findall(pa, data)
        print( all_people_list)
        people_list = []
        for apl in all_people_list:
            pa_apl = r'[\d-]{10}\s[\d:]{7,8}\s+'
            people_list.append(re.split(pa_apl, apl)[1])
        print(people_list)