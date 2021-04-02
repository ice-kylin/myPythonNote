#!/usr/bin/python

num = int(input('请输入一个数：'))

remainder = num % 2

if remainder == 0:
    print(f'{num} 是偶数')
else:
    print(f'{num} 是奇数')
