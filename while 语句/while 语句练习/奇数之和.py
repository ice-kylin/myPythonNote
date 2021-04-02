#!/usr/bin/python

max = int(input('请输入想要计算多少以内奇数之和：'))

separator = '-' * 10
print(f'{separator}>8{separator}')

a = 1
summation = 0

while not (a >= max):
    summation += a
    a += 2
else:
    print(f'{max} 以内奇数之和为 {summation}')
