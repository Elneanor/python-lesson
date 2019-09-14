import doctest


def fib(n):
    """
    calculate the n-th fibonacci bumber iteratively

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(10)
    56
    >>> fib(15)
    610

    """
    a, b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

if __name__ == "__main__":
    print("测试开始了")
    doctest.testmod(verbose=True) #调用这个方法。
