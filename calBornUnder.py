# -*- coding: utf-8 -*-

# 4.    让用户输入出生年份，输出其属相。
# a)    运行python calBornUnder.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# Please input year number:
# 2011
# The born under is: Rabbit.

year = int(raw_input('Please input year number:'))
shuxiang = ['monkey','cock','dog','pig','rat','cow','tiger','rabbit','dragon','snake','horse','sheep']
yearSX = year%12
print 'The born under is:',(shuxiang[yearSX])