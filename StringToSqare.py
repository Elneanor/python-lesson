# -*- coding: utf-8 -*-

#4 输入数字列，输出个数字的平方列（字符串）

def pf(x):
    return x*x
 

num_list = range(10)
print num_list
print map(pf,num_list)