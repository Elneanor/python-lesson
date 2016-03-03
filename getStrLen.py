# -*- coding: utf-8 -*- 

# 1.    让用户输入一行字符串，去掉两头空白符（\n,\t, ,\b等），计算并输出其长度。
# a)    运行python getStrLen.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# Please input a Str:
#   3456
# length = 4.

str1 = raw_input('Please input a Str:')
print str1.strip()
print "length = %d"%(len(str1.strip()))
