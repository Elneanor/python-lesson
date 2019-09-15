
#函数的定义
def hello_world():
    '''
    要写注释，这是一个定义信息输出的函数。
    :return: 无返回，None .有return语句，则返回给调用处对应显示的内容。
    '''
    print("this is the first function written by me")

print(hello_world())
return_date = hello_world()    #没有return语句，接收的变量就是none.
print(return_date)
print(type(return_date))  #函数返回的值，给变量后，类型为字符串，<class 'str'>
print(type(hello_world))  #定义的函数的类型叫做 function  <class 'function'>
print(type(hello_world())) #注意写法，这个仍然是<classe 'str'>,不是function函数的类型。
print(type(input))   # <class 'builtin_function_or_method'>   这个是内建函数


#函数的互相调用
def get_info():
    '''
    这是一个用于函数之间互相调用的函数练习。
    :return:
    '''
    hello_world()
    return "this information come from get_info function"

print(get_info())