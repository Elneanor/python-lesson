# -*- coding: utf-8 -*- 

# 2.    让用户从键盘依次输入两个实数，以及两者的和，判断用户计算是否正确。
# a)    运行python sum2Float.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# Please input a float number:
# 2.3
# Please input another float number:
# 2.4
# Please input sum number:
# 4.7
# The sum was Right !
# b)    运行python sum2Float.py
# Please input a float number:
# 2.3
# Please input another float number:
# 2.4
# Please input sum number:
# 5.7
# The sum was Wrong !

num2 = float(raw_input("Please input a float number:"))
num3 = float(raw_input("Please input another float number:"))
num4 =  float(raw_input("Please input sum number:"))
sum1 = num2 +num3

if  num4 == sum1:
    print "The sum was Right !"
else:
    print " The sum was Wrong !"



