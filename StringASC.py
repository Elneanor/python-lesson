# -*- coding: utf-8 -*-

#3 输入字符串，输出各字符的ASC码

str1 = raw_input("请输入要转换为ASC码的字符串：")
list1=list(str1)

print "转换此字符串为ASC码："
list2 = map(ord,list1)
list3 = zip(list1,list2)

#print list1
#print list2
#print list3

i=0
while i<=(len(list3)-1):
    print list3[i]
    i=i+1


    