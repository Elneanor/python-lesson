from functools import partial

def add(a,b,c=2):  # c有默认值 2
    '''
    用来定义一个加法函数
    :param a: 加数一
    :param b: 加数二
    :param c: 加数三
    :return: 返回三个数的和
    '''
    return a + b + c

p = partial(add,100,200) # 用偏函数给 a,b 赋值。
print(p())   # 100+200+2 = 302  c为默认值2
print(p(30)) #100+200+30 = 330  c为新赋值30

