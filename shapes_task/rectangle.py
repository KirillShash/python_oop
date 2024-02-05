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

    def get_width(self) -> float:
        return self.__width

    def get_height(self) -> float:
        return self.height

    def get_area(self) -> float:
        return self.__width * self.__height

    def get_perimeter(self) -> float:
        return (self.__width + self.__height) * 2
