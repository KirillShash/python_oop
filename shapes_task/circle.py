import math

from shape import Shape


class Circle(Shape):
    def __init__(self, radius: float):
        self.__radius = radius

    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, radius: float):
        self.__radius = radius

    def get_width(self) -> float:
        return self.__radius * 2

    def get_height(self) -> float:
        return self.__radius * 2

    def get_area(self) -> float:
        return math.pi * math.pow(self.__radius, 2)

    def get_perimeter(self) -> float:
        return 2 * math.pi * self.__radius

    def __repr__(self):
        return f'circle with radius = {self.__radius}'
