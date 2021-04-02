#!/usr/bin/python

height = 9
width = 1
h = 1
while h <= height:
    w = 1
    while w <= width:
        product = w * h
        print(f'{w}*{h}={product} ', end='')

        w += 1

    print('')

    h += 1
    width += 1
