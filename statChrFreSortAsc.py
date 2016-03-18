# -*- coding: utf-8 -*-

# 3.    让用户输入一行字符串，统计并输出其中每个字符出现的次数，按字符顺序排列。
# a)    运行python statChrFreSortAsc.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# Please input a Str:
# abcdcdabcd
# The stat char list:
# a => 2
# b => 2 
# c => 3
# d => 3

ll = raw_input('Please input Str:')
# print ll
set1 = set(ll)
t =sorted(set1)
lll = ''.join(t)
print lll

for x in lll:
    t = ll.count(x)
    print "%s => %d"%(x,t)
    
