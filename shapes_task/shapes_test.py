from circle import Circle
from triangle import Triangle
from square import Square
from rectangle import Rectangle
from shape import Shape
from typing import List


def get_shape_with_max_area(shapes: List[Shape]) -> Shape:
    if len(shapes) == 0:
        raise ValueError('List is empty.')

    shapes.sort(key=lambda shape: shape.get_area())

    return shapes[len(shapes) - 1]


def get_shape_with_second_max_perimeter(shapes: List[Shape]) -> Shape:
    if len(shapes) < 1:
        raise ValueError(f'The list must contain at least two shapes. The current list contains {len(shapes)} shapes.')

    shapes.sort(key=lambda shape: shape.get_perimeter())

    return shapes[len(shapes) - 2]


circle_1 = Circle(1)
circle_2 = Circle(2)
circle_3 = Circle(0.5)
circle_4 = Circle(4)

shapes_list = list()

shapes_list.append(circle_1)
shapes_list.append(circle_2)
shapes_list.append(circle_3)
shapes_list.append(circle_4)

triangle_1 = Triangle(0, 0, 2, 3, 11, 15)
triangle_2 = Triangle(0, 0, 2, 3, 11, 15)
triangle_3 = Triangle(4, 13, 2, 3, 11, 15)

shapes_list.append(triangle_1)
shapes_list.append(triangle_2)
shapes_list.append(triangle_3)

square_1 = Square(10)
square_2 = Square(5)
square_3 = Square(20)

shapes_list.append(square_1)
shapes_list.append(square_2)
shapes_list.append(square_3)

rectangle_1 = Rectangle(2, 4)
rectangle_2 = Rectangle(6, 4)
rectangle_3 = Rectangle(20, 8)

shapes_list.append(rectangle_1)
shapes_list.append(rectangle_2)
shapes_list.append(rectangle_3)

print(shapes_list)

shape_with_max_area = get_shape_with_max_area(shapes_list)
shape_with_second_max_perimeter = get_shape_with_second_max_perimeter(shapes_list)

print()

print(f'Shape with max area: {shape_with_max_area} Area = {shape_with_max_area.get_area()}')
print(f'Shape with second max perimeter: {shape_with_second_max_perimeter} Perimeter = '
      f'{shape_with_second_max_perimeter.get_perimeter()}')
