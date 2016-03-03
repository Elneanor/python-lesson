# # -*- coding: utf-8 -*-
# 
# 4.    让用户输入一行字符串，截取其前十个字符，并反向输出，如果用户的输入不满十个，则直接反向输出。
# a)    运行python revertStr.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# Please input a Str:
# 1234
# After revert: '4321'
# b)    运行python revertStr.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# Please input a Str:
# 12345678901
# After revert: '0987654321'

str4 = raw_input("Please input a Str:")

if len(str4)>=10:
    str5 = str4[:10:]
    print "After reverted: '%s'"%(str5[::-1]) 
else:
    print "After reverted: '%s'"%(str4[::-1])
    