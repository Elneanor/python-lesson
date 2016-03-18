# -*- coding: utf-8 -*-

# 5.    让用户输入超过3个数字，去掉最大和最小的数，计算并输出平均数。
# a)    运行python calAverage.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# Please input number list:
# 1 2
# The length of number list should be bigger than 3!
# b)    运行python calAverage.py
# 输出：（蓝色部分为程序输出，红色部分为用户输入）
# Please input number list:
# 11 22 33 44
# The average of the number list is: 27.50.

test1 = raw_input('Please input number list:')
list1 = map(int,test1.strip().split(' '))
print list1
  
if len(list1)<3: 
    print "The length of number list should be bigger than 3!"
else:
    print sorted(list1)
    list1.pop(0),list1.pop(-1) #去掉最小的数，去掉最大的数
    #print list1
    print "The average of the number list is: %.2f"%(float(sum(list1))/(len(list1)))
