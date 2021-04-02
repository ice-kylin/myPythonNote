#!/usr/bin/python

num = int(input('请输入一个要检验是否是质数的数：'))

separator = '-' * 10
print(f'{separator}>8{separator}')

if num <= 1:
    print(f'{num} 不是质数')
else:
    # 检验是否能被除 1 和它自身的数整除
    flag = True
    i = 2
    while i < num:
        if num % i == 0:
            flag = False
        i += 1

    if flag:
        print(f'{num} 是质数')
    else:
        print(f'{num} 不是质数')
