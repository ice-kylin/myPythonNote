#!/usr/bin/python

max_num = int(input('请输入想要计算多少以内 7 的倍数之和与个数：'))

summation = 0
i = 0

for a in range(7, max_num + 1, 7):
    summation += a
    i += 1

print(f'{max_num} 以内 7 的倍数之和为 {summation}')
print(f'个数为 {i}')
