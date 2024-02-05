from typing import override
from shape import Shape


class Triangle(Shape):
    @override
    def get_width(self) -> float:
        pass

    @override
    def get_height(self) -> float:
        pass

    @override
    def get_area(self) -> float:
        pass

    @override
    def get_perimeter(self) -> float:
        pass