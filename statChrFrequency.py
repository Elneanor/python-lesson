# -*- coding: utf-8 -*-

# 2.    让用户输入一行字符串，统计并输出其中每个字符出现的次数。
# a)    运行python statChrFrequency.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# Please input a Str:
# abcdcdabcd
# The stat char list:
# a => 2 
# c => 3
# b => 2
# d => 3

ll = raw_input('Please input Str:')
set1 = set(ll)
lll = ''.join(set1)
#print lll

for x in lll:
    t = ll.count(x)
    print "%s => %d"%(x,t)

    




#print 'The stat char list:'