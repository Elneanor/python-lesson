# -*- coding: utf-8 -*-

# 4.    让用户输入一行字符串，统计并输出其中每个字符出现的次数，按次数从多到少排列。
# a)    运行python statChrFreSortNum.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# Please input a Str:
# abcdbbcddd
# The stat char list:
# a => 1
# c => 2
# b => 3
# d => 4

ll = raw_input('Please input Str:')
set1 = set(ll)    #去重
lll = ''.join(set1)

dict1 = {}
for x in lll:   #统计个数
    t = ll.count(x)
    dict1[x]=t   
#print dict1
print 'The stat char list:'
# print sorted(dict1.iteritems(),key=lambda y:y[0],reverse=True)  #按键排序 ([0])
s = sorted(dict1.iteritems(),key=lambda y:y[1],reverse=False)  #按键值排序 ([1])
for t in s:
    for k in range(len(t)-1): 
        print t[0],'=>',t[1]
        
# for key, value in dict1.items():
#     print key, '=>',  value
#    

