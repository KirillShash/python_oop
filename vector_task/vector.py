from __future__ import annotations
from typing import override, List
from itertools import zip_longest
from multimethod import multimethod

import math


class Vector:
    """
    Class can use constructors:
        1. Vector(n: int) – dimension n, all components are equal to 0
        2. Vector(vector: Vector) – copy constructor
        3. Vector(components: List[int | float]) – filling vector values from a list of numbers
        4. Vector(n: int, components: List[int | float]) – filling with vector values from the list.
    """

    @multimethod
    def __init__(self, dimension: int):
        if dimension <= 0:
            raise ValueError(f'Dimension = {dimension}. The dimension of vector must be greater than 0.')

        self.__components = [0.0] * dimension

    @multimethod
    def __init__(self, dimension: int, components: List[int | float]):
        if dimension <= 0:
            raise ValueError(f'Dimension = {dimension}. The dimension of vector must be greater than 0.')

        self.__components = [0.0] * dimension

        for i in range(min(dimension, len(components))):
            self.__components[i] = components[i]

    @multimethod
    def __init__(self, components: List[int | float]):
        if len(components) == 0:
            raise ValueError(f'Dimension = {len(components)}. The dimension of vector must be greater than 0.')

        self.__components = list(components)

    @multimethod
    def __init__(self, vector: Vector):
        self.__components = list(vector.__components)

    @property
    def dimension(self) -> int:
        return len(self.__components)

    @property
    def length(self) -> float:
        components_squares_sum = 0

        for component in self.__components:
            components_squares_sum += component * component

        return math.sqrt(components_squares_sum)

    @override
    def __repr__(self) -> str:
        return '{' + ', '.join([str(round(component, 2)) for component in self.__components]) + '}'

    @override
    def __eq__(self, other: Vector) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__components == other.__components

    @override
    def __hash__(self) -> int:
        return hash(tuple(self.__components))

    def __iadd__(self, other: Vector) -> Vector:
        if not isinstance(other, type(self)):
            return NotImplemented

        self.__components = [i + j for i, j in zip_longest(self.__components, other.__components, fillvalue=0.0)]

        return self

    def __isub__(self, other: Vector) -> Vector:
        if not isinstance(other, type(self)):
            return NotImplemented

        self.__components = [i - j for i, j in zip_longest(self.__components, other.__components, fillvalue=0.0)]

        return self

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, type(self)):
            return NotImplemented

        return Vector(self).__iadd__(other)

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, type(self)):
            return NotImplemented

        return Vector(self).__isub__(other)

    def __imul__(self, scalar: float | int) -> Vector:
        if type(scalar) is not (int or float):
            raise TypeError('The scalar must be integer or float')

        self.__components = [component * scalar for component in self.__components]

        return self

    def __mul__(self, scalar: float | int) -> Vector:
        if type(scalar) is not (int or float):
            raise TypeError('The scalar must be integer or float')

        return Vector(self).__imul__(scalar)

    def __check_index(self, index: int):
        if type(index) is not int:
            raise TypeError(f'Entered index type: {type(index)}, but the index must be integer')

        if index >= self.dimension or index <= -self.dimension - 1:
            raise IndexError(
                f'Entered index = {index}. The index must be less than {self.dimension} or greater than '
                f'{-self.dimension - 1}.')

    def __getitem__(self, item):
        if isinstance(item, slice):
            return self.__components[item.start:item.stop:item.step]

        self.__check_index(item)

        return self.__components[item]

    def __setitem__(self, index: int, value: int | float):
        if type(value) is not (int or float):
            raise TypeError(f'Entered value type: {type(value)}, but the component must be integer or float')

        self.__check_index(index)

        self.__components[index] = value

    def reverse(self):
        return self.__imul__(-1)

    def get_scalar_product(self, other: Vector) -> float:
        if type(other) is not Vector:
            raise TypeError(f'Entered object type: {type(other)}, but the object must be Vector')

        min_dimension = min(self.dimension, other.dimension)
        product = 0

        for i in range(min_dimension):
            product += self.__components[i] * other.__components[i]

        return product
