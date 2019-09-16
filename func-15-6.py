
from functools import reduce
'''
filter 过滤
map  处理
reduce 做计算统计
'''

numbers = [item * 2 for item in range(1,11)]  #生成一个数组，包括左边的数0，不包括右边的值11.
#print(numbers)

filter_result = list(filter(lambda item : item % 2 == 0 , numbers))  #取出偶数。
map_result = list(map(lambda item : item * 3 , filter_result))  #对取出的偶数数组进行mutiply 3
reduce_result = reduce(lambda x,y:x + y , map_result)   #对处理的数据进行统计，进行了求和。
print(filter_result)
print(map_result)
print(reduce_result)