#!/usr/bin/python

dog_age = float(input('请输入您家🐕的年龄：'))

if dog_age > 0:
    if dog_age > 2:
        people_age = 2 * 10.5 + (dog_age - 2) * 4
    else:
        people_age = dog_age * 10.5
    print(f'您家的🐕的年龄相当于人的 {people_age} 岁')
else:
    print('您家的🐕还没出生呢')
