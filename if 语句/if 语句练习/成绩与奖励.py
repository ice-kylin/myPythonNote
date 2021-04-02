#!/usr/bin/python

result = float(input('请输入小明的成绩：'))

if 0 <= result <= 100:
    if result == 100:
        print('奖励一辆 BMW')
    elif result >= 80:
        print('奖励一台 Iphone')
    elif result >= 60:
        print('奖励一本参考书')
    else:
        print('什么奖励也没有')
else:
    print('请输入合理的成绩')
