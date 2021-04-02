#!/usr/bin/python

max = int(input('请输入想要计算多少以内 7 的倍数之和与个数：'))

a = 7
i = 0
summation = 0

while a <= max:
    summation += a
    i += 1
    a += 7
else:
    print(f'{max} 以内 7 的倍数之和为 {summation}')
    print(f'个数为 {i}')
