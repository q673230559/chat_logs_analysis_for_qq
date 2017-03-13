# '''
# Created on 2017年3月9日
#
# @author: Administrator
# '''
import os
import os.path
import re

rootdir = "./in/"                                  # 指明被遍历的文件夹
print(os.listdir(rootdir))
for rd in os.listdir(rootdir):
    s = "in/"+rd
    print(s.split(".txt")[0]+".xls")
    # with open(s, encoding='utf-8') as f:
    #     data = f.read()
    #     print(data)
