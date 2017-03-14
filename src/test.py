# '''
# Created on 2017年3月9日
#
# @author: Administrator
# '''

import time, datetime, re, tools

with open("in/20172018华中师大教技群.txt", encoding='utf-8') as f:
    data = f.read()
    pa = r'[\d-]{10}\s[\d:]{7,8}\s+[^\n]+'
    all_people_list = re.findall(pa, data)
    timesec = []
    for apl in all_people_list:
        pa_apl = r'[\d-]{10}\s[\d:]{7,8}\s+'
        timestr = re.findall(pa_apl, apl)
        t = re.split("-|:| ", timestr[0])
        timesec.append(time.mktime(
            datetime.datetime(int(t[0]), int(t[1]), int(t[2]), int(t[3]), int(t[4]), int(t[5])).timetuple()))

    print(timesec)
    a = 0
    b = 0
    for it in range(0, len(timesec)):
        if it >= 1:
            sec = timesec[it] - timesec[it - 1]
            if sec < 1800:
                a += 1
                # tools.add_sheet_type()
            else:
                b += 1
    print(a)
    print(b)
