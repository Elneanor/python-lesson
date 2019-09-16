from random import *
'''
用随机数函数来实现36选一的彩票抽奖
'''
numbers = []
while len(numbers) != 7:
    num = randint(1,36)
    if num not in numbers:
        numbers.append(num)
numbers.sort()
print("选出的数字为 %s" % numbers)

#生成一个序列
list1 = [item * 2 for item in range(10)]
print(list1)

for item in range(10):
    print(choice(list1),end=",")  #用choice实现随机抽取的功能。
