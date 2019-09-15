

def sum(x,y):
    '''
    两数之和的正常定义
    :param x: 加数
    :param y: 被加数
    :return: 两数之和
    '''
    return x + y

print(sum(30,20))

# 用lambda 函数实现这个两数之和的功能。

sum1 = lambda x,y : x + y
print(sum1(10,20))


print(__name__)