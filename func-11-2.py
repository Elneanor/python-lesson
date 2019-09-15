'''
练习函数传参的方式
'''

def out_info(name, age, title, homepage):
    print("名字:%s,年龄:%d,title:%s,homepage:%s" % (name,age,title,homepage))

print("first",30,"teacher","www.douban.com")  #按顺序
print(out_info(homepage="www.baidu.com",name = "Jenny", age=19,title="test",))  #用指定参数的方式

#函数里的列表的数据会被改变。

def change_data(list):
    list.append("hello")

infos = ["mldn"]
print(infos) # ['mldn']
print(id(infos))  #地址
change_data(infos  #调用函数
print(infos)    #infos内容被改变了
print(id(infos))
'''
['mldn', 'hello']
'''


