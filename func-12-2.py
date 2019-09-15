
def out_oa(n1):
    '''
    闭包的概念。 nonlocal 用来访问外部的局部变量。
    :param n1:
    :return:
    '''
    def inner_oa(n2):
        nonlocal n1  #如果要调用inner_oa这个函数体内没有的变量n2,就得先用nonlocal关键字来访问外层非全局的变量n1
        n1 = n1 + 1  #有了上面的nonlocal语句的定义，才能对n1进行操作。
        return n1 + n2
    return inner_oa

oa = out_oa(100)  #n1=100,并且返回inner_oa
print(oa(20))   #返回inner_oa后，将20赋值给n2
print(oa(50))   #返回inner_oa后，将50赋值给n2，得出n1+n2=100+50=150
