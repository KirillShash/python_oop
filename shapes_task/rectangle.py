from typing import override
from shape import Shape


class Rectangle(Shape):
    def __init__(self, height: float, width: float):
        self.__height = height
        self.__width = width

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @override
    def get_width(self) -> float:
        return self.__width

    @override
    def get_height(self) -> float:
        return self.height

    @override
    def get_area(self) -> float:
        return self.__width * self.__height

    @override
    def get_perimeter(self) -> float:
        return (self.__width + self.__height) * 2

    @override
    def __repr__(self):
        return f'rectangle with sides lengths = [{self.__height}; {self.width}]'

    @override
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__height == other.__height and self.__width == other.__width

    @override
    def __hash__(self):
        return hash((self.__height, self.__width))
