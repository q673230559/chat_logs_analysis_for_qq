'''
Created on 2017年3月8日

@author: Administrator
'''
import xlsxwriter
import DataBase
import Tools

# 建立活跃图
def buildGraph(sourceFile, buildFile):
    # 创建EXCEL工作簿
    workbook = xlsxwriter.Workbook(buildFile)
    
    ###  时间段活跃统计图
    time_set=DataBase.getTimeSet(sourceFile)
    time_tuple=sorted(time_set.items(), key=lambda e:e[0], reverse=False)
    ### 排序写入工作簿
    Tools.addSheetTpye1(workbook, "时间段活跃", time_tuple,"时间","活跃量")
            
    ### 成员活跃图              
    people_say_set=DataBase.getPeopleSaySet(sourceFile)
    people_say_tuple=sorted(people_say_set.items(), key=lambda e:e[1], reverse=True)
    # 写入工作簿
    Tools.addSheetTpye1(workbook, "成员活跃", people_say_tuple,"成员","活跃量")
   
    ### 热词统计
    word_tuple=DataBase.getHotNounCounts(sourceFile)
    # 写入工作簿
    Tools.addSheetTpye1(workbook, "热词统计", word_tuple,"词汇","出现次数")
    
    # 关闭文档
    workbook.close()




    


# Going
print("~程序正在运行~")
buildGraph("bo.txt", 'bo.xlsx')
print("~程序执行完成~")
    




