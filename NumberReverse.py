# -*- coding: utf-8 -*-

#5 输入数字串，输出倒序数字串

lis1 = (raw_input("请输入数字串：")).strip().split(' ')
lis1.reverse()
print ' '.join(lis1)    #按输入顺序倒序


lis1 = map(int,(raw_input("请输入数字串:")).strip().split(' '))
lis1.sort(reverse=True)   #按数字大小倒序
#print lis1  
lis2 = map(str,lis1)
print ' '.join(lis2) 

