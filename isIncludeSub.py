# -*- coding: utf-8 -*-

# 2.    让用户输入一行字符串，判断其中是不是包含“abc”?
# a)    运行python isIncludeSub.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# Please input a Str:
# abdddabc
# 'abc' was in 'abdddabc'
# b)    运行python isIncludeSub.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# Please input a Str:
# ababab
# 'abc' was not in 'ababab'

str2 = raw_input('Please input a Str:')
if 'abc' in str2:
    print '"abc" was in %s'%(str2)
else:
    print '"abc" was NOT in %s'%(str2)