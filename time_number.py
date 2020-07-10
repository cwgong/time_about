# -*- coding: utf-8 -*-

import datetime
import time

current_date = "2016-9-22"
tmp_date_list = current_date.split('-')
# 日期到时间戳的转换
dateC = datetime.datetime(int(tmp_date_list[0]), int(tmp_date_list[1]), int(tmp_date_list[2]))
timestamp = time.mktime(dateC.timetuple())
print(timestamp)  # float类型

print
"==========================================="
# 将时间戳转换到日期
ltime = time.localtime(timestamp)
timeStr = time.strftime("%Y-%m-%d", ltime)
print(timeStr)