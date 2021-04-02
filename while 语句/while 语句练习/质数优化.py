#!/usr/bin/python

from time import *

max = int(input('请输入想要计算多少以内所有的质数：'))

separator = '-' * 10
print(f'{separator}>8{separator}')

begin_time = time()

num = 2

while num <= max:
    # 检验是否能被除 1 和它自身的数整除
    flag = True
    i = 2
    while i <= num**0.5:
        if num % i == 0:
            flag = False
            break
        i += 1

    if flag:
        print(num, end=' ')
        # pass

    num += 1

end_time = time()

print()

separator = '-' * 10
print(f'{separator}>8{separator}')

print(f'{end_time - begin_time}s')
