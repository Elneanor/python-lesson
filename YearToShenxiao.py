# -*- coding: utf-8 -*-

#6 输入年份，输出属相
year = int(raw_input('请输入年份:'))
shenxiao = ['monkey','cock','dog','pig','rat','cow','tiger','rabbit','dragon','snake','horse','sheep']

year_s = year%12
print "对应的生肖是：",shenxiao[year_s]