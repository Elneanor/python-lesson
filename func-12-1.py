
num = 100
#如果要定义全局变量，用global的关键字。
#GLOBAL_VAR_URL = "www.baidu.com"

def change_num():
    '''
    修改全局变量,这是doc文件里会显示的内容。
    尽可能不要定义全局变量，全局变量尽可能是常量。如果真的要定义，注意使用global大写的字母来做区分。
    :return:
    '''
    #global num  #使用访语句后，表示调用的是全局变量num = 100
    num = 2
    print("change_num函数中的变量num:%d" % num)

print(change_num())
print("全局变量中的num %d" % num)
print(globals())
print(locals())
print(change_num.__doc__)
