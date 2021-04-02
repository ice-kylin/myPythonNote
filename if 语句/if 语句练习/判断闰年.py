#!/usr/bin/python

year = int(input("请输入一个年份："))

if year % 400 == 0:
    print(f'{year} 年是闰年')
elif year % 4 == 0 and year % 100 != 0:
    print(f'{year} 年是闰年')
else:
    print(f'{year} 年不是闰年')
