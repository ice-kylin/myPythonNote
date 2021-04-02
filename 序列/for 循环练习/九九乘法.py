#!/usr/bin/python

for height in range(1, 10):
    for width in range(1, height + 1):
        product = width * height
        print(f'{width}*{height}={product}', end=' ')
    print('')
