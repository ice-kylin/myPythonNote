class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> str:
        return self.__age


p_1 = Person('Issac', 19)

p_1.__name = 'Acker'
print(f'p_1.get_name() = {p_1.get_name()}')

p_1.__age = 20
print(f'p_1.get_age() = {p_1.get_age()}')
