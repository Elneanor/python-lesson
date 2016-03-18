# -*- coding: utf-8 -*-

# 1.    让用户输入一行字符串，输出这行字符串的ASCII码列表。
# a)    运行python chr2Asc.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# Please input a Str:
# 123456 789
# The AscII code list: 49 50 51 52 53 54 32 55 56 57.

drt =raw_input(" Please input a Str:")
#print dr
# dr1 = map(str,map(ord,dr))
print 'The AscII code list:',' '.join(map(str,map(ord,drt)))
