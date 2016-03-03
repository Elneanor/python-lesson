# -*- coding: utf-8 -*- 

# 1.    让用户从键盘输入一个二进制数，在键盘上显示其十进制，16进制，8进制格式。
# a)    运行python transBin2Other.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# Please input a number:
# 1100
# base 2 number in dec mode: 12
# base 2 number in oct mode: 014
# base 2 number in hex mode: 0xC
# eclipse ctrl +/ 可以注释多行

num1 = int(raw_input("Please input a number:"),base=2)
print "base 2 number in dec mode:%d"%(num1)
print "base 2 number in oct mode:%s"%(oct(num1))  #%o
print "base 2 number in hex mode:%s"%(hex(num1))  #%X
