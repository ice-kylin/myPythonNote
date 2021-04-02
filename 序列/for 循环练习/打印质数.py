#!/usr/bin/python

from time import *

max_num = int(input('请输入想要计算多少以内所有的质数：'))

separator = '-' * 10
print(f'{separator}>8{separator}')

begin_time = time()

for num in range(2, max_num + 1):
    flag = True
    for i in range(2, int(num**0.5 + 1)):
        if num % i == 0:
            flag = False
    if flag:
        print(num, end=' ')

end_time = time()

print()

separator = '-' * 10
print(f'{separator}>8{separator}')

print(f'{end_time - begin_time}s')
