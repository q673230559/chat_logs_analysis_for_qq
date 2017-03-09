'''
Created on 2017年3月9日

@author: Administrator
'''
import jieba
import re

seg_list = jieba.cut("我来到北京清华大学",cut_all=True)
for seg in seg_list:
    print (seg)
    
    

with open("20172018华中师大教技群.txt", encoding='utf-8') as f:
    data=f.read()
    re_pat = r'[\d-]{10}\s[\d:]{7,8}\s+[^\n]+\d{5,11}\)'  # 记录头数组['2016-06-24 15:42:52  张某(40**21)',…]
    li=re.findall(re_pat,data)
    li_content = re.split(re_pat, data)
    s=""
    for l in li_content:
        s=s+l
    seg_list = jieba.cut(s.strip(),cut_all=True)
    seg_list=list(seg_list)
    print(len(seg_list))
    print(len(seg_list))
    seg_list_noRepeat=set(seg_list)
    print(len(seg_list_noRepeat))
    word_set={}
    for seg in seg_list_noRepeat:
        count=0
        for ss in seg_list:
            if(ss == seg):
                count+=1
        word_set[seg]=count
        
    word_set_sort = sorted(word_set.items(), key=lambda e:e[1], reverse=True)
    for wss in word_set_sort:
        print (wss[0],"-->",wss[1])
    
    
    
    
    
    