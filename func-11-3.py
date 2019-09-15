def math1(cmd,*numbers):
    '''
    :param cmd:
    :param numbers:
    :return:
    '''
    print("可变参数numbers类型：%s,参数数量：%d" % (type(numbers),len(numbers)))
    sum = 0
    if cmd == "+":
        for num in numbers:
            sum = sum + num
    elif cmd == "-":
        for num in numbers:
            sum = sum - num
    return sum
print("执行累加操作:%d" % math1("+",1,2,3,4,5,9,10))
print("执行累减操作:%d" % math1("-",5,6,7,3,0,9,3,4,5,6,))

print("\t")
print("##############我是分隔线#####################")
print("\t")


def print_info(name,**urls):
    '''
    这是一个用来定义函数时，有必选参数和固定参数。
    :param name: 要输入的姓名
    :param urls: 一组的key=values的组合
    :return:
    '''
    print("用户姓名：%s" % name)
    print("喜欢的网站:")
    for key,value in urls.items():
        print("\t |- %s :%s" %(key,value))

print_info("jenny",yoo="www.baidu.com",mldn="test.baidu.com")

