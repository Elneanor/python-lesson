import doctest

'''Fibonacci Module '''

def fib(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

def fiblist(n):
    fib = [0,1]
    for i in range(1,n):
        fib += [fib[-1] + fib[-2]]
    return fib


# 测试函数
if __name__ == "__main__":
    doctest.testmod(verbose=True)
