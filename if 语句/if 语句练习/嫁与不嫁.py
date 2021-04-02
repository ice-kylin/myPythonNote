#!/usr/bin/python

height = float(input('请输入身高（厘米）：'))
wealth = float(input('请输入财富（万）：'))
appearance = float(input('请输入颜值：'))

if height >= 180 and wealth >= 1000 and appearance >= 500:
    print('我一定要嫁给他')
elif height >= 180 or wealth >= 1000 or appearance >= 500:
    print('嫁吧，比上不足，比下有余')
else:
    print('不嫁！')
