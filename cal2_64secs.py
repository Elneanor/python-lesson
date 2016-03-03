# -*- coding: utf-8 -*- 

# 4.    计算2的64次方秒，相当于多少年（结果保留小数）？
# a)    运行python cal2_64secs.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# 2**64 seconds equal to 584942417355.07 years

#from __future__ import division   #导入这个模板也可实现结果保留小数
# 在python中进行两个整数相除的时候，在默认情况下都是只能够得到整数的值

seconds = 2**64
year_tup = float(seconds) / (365*24*60*60)  
print " 2**64 seconds equal to %.2f years"%(year_tup)



