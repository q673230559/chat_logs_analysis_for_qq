'''
Created on 2017年3月9日

@author: Administrator
'''
import re
import jieba.posseg as pseg

    
def hotNounCounts():
    with open("20172018华中师大教技群.txt", encoding='utf-8') as f:
        data=f.read()
        re_pat = r'[\d-]{10}\s[\d:]{7,8}\s+[^\n]+\d{5,11}\)'  # 记录头数组['2016-06-24 15:42:52  张某(40**21)',…]
        li=re.findall(re_pat,data)
        li_content = re.split(re_pat, data)
        s=""
        for l in li_content:
            s=s+l
        seg_list = pseg.cut(s.strip())
        lists = []
        for w in seg_list:
            if(w.flag=="ns"):
                lists.append(w.word)
        print("******群热词统计******")
        print("带重复名词总量",len(lists))
        seg_list_noRepeat=set(lists)
        print("不重复名词总量",len(seg_list_noRepeat))
        word_set={}
        for seg in seg_list_noRepeat:
            count=0
            for ss in lists:
                if(ss == seg):
                    count+=1
            word_set[seg]=count
            
        word_set_sort = sorted(word_set.items(), key=lambda e:e[1], reverse=True)
        for wss in word_set_sort:
            print (wss[0],"-->",wss[1])
    
    
    
    
hotNounCounts()
    