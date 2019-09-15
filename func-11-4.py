
def fact(num):
    '''
    用于定义阶乘的递归调用
    :param num:
    :return:
    '''
    if num == 1:
        return 1
    return num * fact(num - 1)

print(fact(5))

def sum(a):
    '''
    用于求和的递归调用
    :param a:
    :return:
    '''
    if a == 1:
        return 1
    return a + sum(a - 1)
print(sum(100))

