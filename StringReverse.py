# -*- coding: utf-8 -*-

#2 将字符串按字母倒序输出

str_list1 = list(raw_input("请输入字符串："))
str_list1.sort(reverse=True)
print ''.join(str_list1)


