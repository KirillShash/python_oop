import math
from typing import override
from shape import Shape


class Triangle(Shape):
    def __init__(self, x_1: float, y_1: float, x_2: float, y_2: float, x_3: float, y_3: float):
        self.__x_1 = x_1
        self.__x_2 = x_2
        self.__x_3 = x_3
        self.__y_1 = y_1
        self.__y_2 = y_2
        self.__y_3 = y_3

    @property
    def x_1(self) -> float:
        return self.__x_1

    @x_1.setter
    def x_1(self, x_1: float):
        self.__x_1 = x_1

    @property
    def x_2(self) -> float:
        return self.__x_2

    @x_2.setter
    def x_2(self, x_2: float):
        self.__x_2 = x_2

    @property
    def x_3(self) -> float:
        return self.__x_3

    @x_3.setter
    def x_3(self, x_3: float):
        self.__x_3 = x_3

    @property
    def y_1(self) -> float:
        return self.__y_1

    @y_1.setter
    def y_1(self, y_1: float):
        self.__y_1 = y_1

    @property
    def y_2(self) -> float:
        return self.__y_2

    @y_2.setter
    def y_2(self, y_2: float):
        self.__y_2 = y_2

    @property
    def y_3(self) -> float:
        return self.__y_3

    @y_3.setter
    def y_3(self, y_3: float):
        self.__y_3 = y_3

    @override
    def get_width(self) -> float:
        return max(self.__x_1, self.__x_2, self.__x_3) - min(self.__x_1, self.__x_2, self.__x_3)

    @override
    def get_height(self) -> float:
        return max(self.__y_1, self.__y_2, self.__y_3) - min(self.__y_1, self.__y_2, self.__y_3)

    @override
    def get_area(self) -> float:
        pass

    @override
    def get_perimeter(self) -> float:
        pass

    @override
    def __repr__(self):
        return (f'Triangle with vertices ({self.__x_1}; {self.__y_1}) ({self.__x_2};'
                f' {self.__y_2}) ({self.__x_3}; {self.__y_3})')

    @override
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return (self.__x_1 == other.__x_1
                and self.__y_1 == other.__y_1
                and self.__x_2 == other.__x_2
                and self.__y_2 == other.__y_2
                and self.__x_3 == other.__x_3
                and self.__y_3 == other.__y_3)

    @override
    def __hash__(self):
        return hash((self.__x_1, self.__y_1, self.__x_2, self.__y_2, self.__x_3, self.__y_3))


def get_side_length(x_1: float, y_1: float, x_2: float, y_2: float):
    return math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
