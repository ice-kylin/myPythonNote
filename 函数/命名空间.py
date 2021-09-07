#!/usr/bin/python


def func1() -> dict:
    a = 1
    func1_scope = locals()
    func1_scope['b'] = 2
    # print(f'b = {b}') # 可能报错
    return func1_scope


print(f'type(func1()) = {type(func1())}')
print(f'func1() = {func1()}')
