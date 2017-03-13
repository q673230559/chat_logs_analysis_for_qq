# '''
# Created on 2017年3月9日
#
# @author: Administrator
# '''
import os
import os.path
rootdir = "d:\32"                                  # 指明被遍历的文件夹
print(os.walk(rootdir))
for p in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    print(p.__dict__)
