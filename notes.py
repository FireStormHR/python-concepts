from typing import Callable


class car():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class volkswagen(car):
    """This is a nice car."""

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def race(self, onSuccess: Callable[[int], str]) -> None:
        print('racing')
        x = onSuccess(5)
