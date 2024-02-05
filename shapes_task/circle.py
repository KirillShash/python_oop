import math

from typing import override
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

    @override
    def get_width(self) -> float:
        return self.__radius * 2

    @override
    def get_height(self) -> float:
        return self.__radius * 2

    @override
    def get_area(self) -> float:
        return math.pi * math.pow(self.__radius, 2)

    @override
    def get_perimeter(self) -> float:
        return 2 * math.pi * self.__radius

    @override
    def __repr__(self):
        return f'circle with radius = {self.__radius}'

    @override
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__radius == other.__radius

    @override
    def __hash__(self):
        return hash(self.__radius)
