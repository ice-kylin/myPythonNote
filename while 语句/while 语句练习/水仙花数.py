#!/usr/bin/python

max = int(input('请输入想要计算多少以内所有的水仙花数：'))

separator = '-' * 10
print(f'{separator}>8{separator}')

i = 1

while i <= max:
    # 获取位数
    n = 10
    total_digit = 1
    while i % n != i:
        total_digit += 1
        n *= 10

    # print(f'total_digit = {total_digit}')

    # 获取每个位上的数字的 n 次幂之和
    summation = 0
    digit = 1
    independent_num = 0
    power = 0
    while digit != (total_digit + 1):
        # 获取每个位上的数字
        independent_num = i % (10**digit) // (10**(digit - 1))

        # print(f'independent_num = {independent_num}')

        # 获取每个位上的数字的 n 次幂
        power = independent_num**total_digit

        summation += power
        digit += 1

    # print(f'i = {i}, summation = {summation}')

    # 判断是否为水仙花数并打印
    if summation == i:
        print(i, end=' ')

    i += 1

print()
