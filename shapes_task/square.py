import math

from shape import Shape


class Square(Shape):
    def __init__(self, side_length: float):
        self.__side_length = side_length

    @property
    def side_length(self) -> float:
        return self.__side_length

    @side_length.setter
    def side_length(self, side_length: float):
        self.__side_length = side_length

    def get_width(self) -> float:
        return self.__side_length

    def get_height(self) -> float:
        return self.__side_length

    def get_area(self) -> float:
        return math.pow(self.__side_length, 2)

    def get_perimeter(self) -> float:
        return self.__side_length * 4
