# -*- coding: utf-8 -*-

# 5.    让用户分两次输入若干个数字，统计并输出两次输入的数字中，相同的数字和不同的数字。
# a)    运行python statNumListSet.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# Please input number list a:
# 1 2 33 4 5
# Please input number list b:
# 33 2 5 6 7
# And set: 33 2 5.
# Dissident set: 4 6 1 7.


a = (raw_input('Please input number list a:')).split(' ')
set1 = set(a)
print set1

b = (raw_input('Please input number list b:')).split(' ')
set2 = set(b)
print set2
 
Aset = set1&set2  #取交集
print "the AND set:",' '.join(Aset)

Dset =  set1^set2  #取外集
print "the Dissident set:",' '.join(Dset)
