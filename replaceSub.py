# -*- coding: utf-8 -*-

# 3.    让用户输入一行字符串，将其中的第一个“abc”替换为“hexie”，并输出。
# a)    运行python replaceSub.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# Please input a Str:
# ==abc==abc==
# After replace: '==hexie==abc=='

str3 = raw_input("Please input a Str:")
print " After replace:%s"%(str3.replace('abc', 'hexie',1))