# -*- coding: utf-8 -*-

# PPT作业
# 请将字符串"aa$bb$cc$dd$ee$ff$"变成"aa bb cc dd ee ff",请注意变完后的字符串左右两边都没有空格。
# 请将字符串"hello world"的首字母变成大写。
# 请将字符串"hello world"中每个单词的首字母都变成大写。
# 请判断"cd"是否存在于字符串"aabbccddeeff"之中？如果存在,请输出"cd"最先出现的位置。
# 请反向输出字符串"hello, world!"。
# 请输出ASCII码表中,空格(" ")的后面一个字符是什么？
# 请判断"abcdcba"是否回文？
# 请将字符串"apple pear banana"中的每个单词反序输出,结果应为："elppa raep ananab"


print '请将字符串"aa$bb$cc$dd$ee$ff$"变成"aa bb cc dd ee ff",请注意变完后的字符串左右两边都没有空格。'
str1 = "aa$bb$cc$dd$ee$ff$"
str1_1 = str1.split('$')    #转成列表
str1_2 =  ' '.join(str1_1)  #将列表转成字符串
#print str1_1
#print str1_2
print str1_2.strip()  #将字符串末尾的空格去掉 lstrip, rstrip
print '------------------------------------------------------'

print '请将字符串"hello world"的首字母变成大写。每个单词的首字母都变成大写。'
str2 = 'hello world'
print str2.capitalize()  #首字母大写
print str2.title()   #每个单词的首字母大写
print '------------------------------------------------------'

print '请判断"cd"是否存在于字符串"aabbccddeeff"之中？如果存在,请输出"cd"最先出现的位置。'
str3 = "aabbccddeeff"
if str3.find('cd') >= 0:
    print " 'cd' is IN %s"%(str3)
    print "cd 出现的位置:%d"%(str3.find('cd'))
else:
    print "'cd' is NOT in %s"%(str3)
print '------------------------------------------------------'

print '请反向输出字符串"hello, world!"。'
str4 = "hello, world!"
print str4[::-1]
print '------------------------------------------------------'

print'请输出ASCII码表中,空格(" ")的后面一个字符是什么？'
print chr(ord(" ")+1)
print '------------------------------------------------------'

print '请判断"abcdcba"是否回文?'
str5 = "abcdcba"
if str5 == str5[::-1]:
    print "回文"
else:
    print "不是回文"
print '------------------------------------------------------'

print '# 请将字符串"apple pear banana"中的每个单词反序输出,结果应为："elppa raep ananab"'
str6 = "apple pear banana"
str7 = str6.split()
str8 =  ' '.join(str7[::-1])
print str8[::-1]

