# -*- coding: utf-8 -*- 

# 3.    让用户输入一个数字（以秒为单位），计算并输出，这个数字代表的“年日时分秒”格式（一年按365天算）。
# a)    运行python calSeconds.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# Please input seconds:
# 123456789
# 123456789 seconds equal to '3 years, 333 days, 21 hours, 33 minutes, 9 seconds'


ttt = int(raw_input('Please input seconds:'))
tupYear = divmod(ttt, 365*24*60*60)
years = tupYear[0]
#print years
tupDay=divmod(tupYear[1],24*60*60)
days = tupDay[0]
#print days
tupHours = divmod(tupDay[1],60*60)
hours = tupHours[0]
#print hours
tupSeconds = divmod(tupHours[1],60)
minutes = tupSeconds[0]
#print minutes
seconds1 = tupSeconds[1]

print "%d seconds equal to '%s years, %s days, %s hours, %s minutes, %s seconds'"%(ttt,years,days,hours,minutes,seconds1)



#import time
#tt = time.localtime(input('Please input seconds:'))
#print time.strftime('%Y-%m-%d %H:%M:%S',tt)
#1973-11-30 05:33:09