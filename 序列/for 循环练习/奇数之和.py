#!/usr/bin/python

max_num = int(input('请输入想要计算多少以内奇数之和：'))

separator = '-' * 10
print(f'{separator}>8{separator}')

summation = 0

for i in range(1, max_num, 2):
    summation += i

print(f'{max_num} 以内奇数之和为 {summation}')
