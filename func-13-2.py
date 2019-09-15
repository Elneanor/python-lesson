
def hello():
    return "hello world"

print(callable(hello))
print(callable(input))

a = 9
print(callable(a))

'''
以上的例子主要判断函数是否可以调用。calllable
'''

'''
下面是例子是用来展示如何使用eval函数，它主要执行在字符串的计算。
'''

a = 10
sum = "a * 8"
print(sum)  # 原样输出字符串 a*8
# 如果加了eval，则会执行字符串的计算
sum1 = eval("a * 3")
print(sum1)  #30

statement = "for i in range(5):"\
            "   print(i)    "
result = exec(statement)   # exec用来执行字符串的中的单行或者多行语句。而eval只能执行单行的语句。
print(result)











