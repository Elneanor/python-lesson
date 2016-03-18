# -*- coding: utf-8 -*-

# 3.    让用户输入若干个数字，从大到小排序，然后输出。
# a)    运行python sortNumList.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# Please input number list:
# 11 44 22 55
# Sort number list: 55 44 22 11.

num_l = raw_input('Please input number list:')
nn = map(int,num_l.strip().split(' '))
#print nn
tt = nn.sort(reverse=True)
#print nn
print ' '.join(map(str,nn)) 