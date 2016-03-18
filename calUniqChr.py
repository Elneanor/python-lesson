# -*- coding: utf-8 -*-

# 1.    让用户输入一行字符串，统计并输出字符串中不相同的字符个数。
# a)    运行python calUniqChr.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# Please input a Str:
# abcddcabcd
# The uniq char number is: 4.

t = list(raw_input(' Please input a Str:'))
print ' The uniq char number is:',len(set(t))

