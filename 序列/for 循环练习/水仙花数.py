#!/usr/bin/python

max_num = int(input('请输入想要计算多少以内所有的水仙花数：'))

separator = '-' * 10
print(f'{separator}>8{separator}')

for num in range(1, max_num + 1):
    total_digit = len(str(num))

    summation = 0
    independent_num = 0
    for digit in range(1, total_digit + 1):
        # 获取每个位上的数字
        independent_num = num % (10**digit) // 10**(digit - 1)

        # 获取每个位上的数字的 n 次幂
        power = independent_num**total_digit

        summation += power

    # 判断是否为水仙花数并打印
    if summation == num:
        print(num, end=' ')

print()
