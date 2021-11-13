class A:
    def __init__(self, name: str) -> None:
        self._name = name

    def __del__(self) -> None:
        print(f'{self.name} 对象被删除了 QAQ')

    @property
    def name(self) -> str:
        return self._name


a = A('Issac')

print(a.name)

# b = a

# a = None # 将 a 设置为了 None，此时没有任何的变量对 A() 对象进行引用，它就变成了垃圾

input('按任意键退出...')