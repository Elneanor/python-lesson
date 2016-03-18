# -*- coding: utf-8 -*-

# 2.    让用户输入若干个数字，计算并输出这些数字的平方数。
# a)    输入python calNumListSquare.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# Please input number list:
# 2 3 4 6
# Square list: 4 9 16 36.

def Sq(x):
    s = x*x
    return s

l1 = map(int,raw_input('Please input number list:').split())
#l2 = map(Sq,l1)   #顺序执行代码，如果放在方法前，会不认得方法Sq
print 'Square list: ',' '.join(map(str,map(Sq,l1)))


# for x in l2:
#     print "Square list:", x*x
#     x=x+1   #输出样式不合要求

# for x in range(len(l2)-1):
#     print  x*x
#     x=x+1    输入index的平方数，不对

    