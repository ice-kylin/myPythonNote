a = 233
b = 666


def test() -> None:
    print('test')


def test2() -> None:
    print('test2')


class Person():
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name


if __name__ == '__main__':
    print(a)
    test()
    test2()
