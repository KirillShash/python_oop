from __future__ import annotations
from typing import override, Union, List
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

        self.__components = [0.0 for _ in range(dimension)]

    @multimethod
    def __init__(self, dimension: int, components: List[int | float]):
        if dimension <= 0:
            raise ValueError(f'Dimension = {dimension}. The dimension of vector must be greater than 0.')

        max_dimension = max(dimension, len(components))

        self.__components = [0.0 for _ in range(max_dimension)]

        for i, component in enumerate(components):
            self.__components[i] = component

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
        summa = 0

        for component in self.__components:
            summa += component * component

        return math.sqrt(summa)

    @override
    def __repr__(self) -> str:
        return '{' + ", ".join(map(str, [round(component, 2) for component in self.__components])) + '}'

    @override
    def __eq__(self, other: Vector) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__components == other.__components

    @override
    def __hash__(self) -> int:
        return hash(tuple(self.__components))

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, type(self)):
            return NotImplemented

        return Vector([i + j for i, j in zip_longest(self.__components, other.__components, fillvalue=0.0)])

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, type(self)):
            return NotImplemented

        return Vector([i - j for i, j in zip_longest(self.__components, other.__components, fillvalue=0.0)])

    def __iadd__(self, other: Vector) -> Vector:
        if not isinstance(other, type(self)):
            return NotImplemented

        self.__components = list((self + other).__components)

        return self

    def __isub__(self, other: Vector):
        if not isinstance(other, type(self)):
            return NotImplemented

        self.__components = list((self - other).__components)

        return self

    def __mul__(self, scalar: float | int) -> Vector:
        if type(scalar) is not (int or float):
            raise TypeError('The scalar must be integer or float')

        return Vector([component * scalar for component in self.__components])

    def __check_index(self, index: int):
        if type(index) is not int:
            raise TypeError(f'The index must be integer')

        if index < 0 or index >= self.dimension:
            raise ValueError(f'The index must be equal to or greater than 0 and less than {self.dimension}')

    def __getitem__(self, item):
        if isinstance(item, slice):
            return self.__components[item.start:item.stop:item.step]

        self.__check_index(item)

        return self.__components[item]

    def __setitem__(self, index: int, value: int | float):
        if type(value) is not (int or float):
            raise TypeError('The component must be integer or float')

        self.__check_index(index)

        self.__components[index] = value

    def reverse(self):
        return self * -1

    def get_scalar_product(self, other: Vector) -> float:
        if not isinstance(other, type(self)):
            return NotImplemented

        min_size = min(len(self.__components), len(other.__components))
        product = 0

        for i in range(min_size):
            product += self.__components[i] * other.__components[i]

        return product
