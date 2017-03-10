'''
Created on 2017年3月9日

@author: Administrator
'''
import re
with open("003.txt", encoding='utf-8') as f:
        data = f.read()
        # 例如20:50:52，要匹配其中的20
        pa = r'ヅ緈运的泪|邬思娜'
        all_people_list = re.findall(pa, data)
        print (all_people_list)
        count =0
        her=0
        for apl in all_people_list:
            if(apl=="ヅ緈运的泪"):
                count+=1
            else:
                her+=1
        print (count,"--->",her)



