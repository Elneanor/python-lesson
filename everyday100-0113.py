# -*- coding:utf-8 -*-
#@Time : 2020/1/13 20:52
#@Author: Runner Yuan
#@File : everyday100-0113.py

'''每天写100行Python代码'''

tuple_one = (3,5,4)  #元组是只读列表
x,y,z = tuple_one
print('x:%d,y:%d,z:%d' % (x,y,z))

list_data = ["ace",20,11,89.4,(2020,1,13)]  #列表
name,one,two,three,(year,month,day) = list_data
print("name:%s \n"
      "one:%s \n"
      "two:%s \n"
      "three:%s \n"
      "year:%s \n"
      "month:%s \n"
      "day:%s \n"
      %
      (name,one,two,three,year,month,day))

str_data = "stupid"
a,b,c,d,e,f = str_data
print("a:%s,b:%s,c:%s,d:%s,e:%s,f:%s"%(a,b,c,d,e,f))

list_data2 = [3,4,5,6]
_,se,th,_ = list_data2  #用占位符丢弃不需要的值。
print('se:%s,th:%s' %(se,th))


