from __future__ import annotations
from typing import override
from multipledispatch import dispatch
from itertools import zip_longest

import math


class Vector:
    @dispatch(int)
    def __init__(self, dimension: int):
        if dimension <= 0:
            raise ValueError(f'Dimension = {dimension}. The dimension of vector must be greater than 0.')

        self.__dimension = dimension
        self.__components = [0. for _ in range(dimension)]

    @dispatch(int, list)
    def __init__(self, dimension: int, components: list[float]):
        if dimension <= 0:
            raise ValueError(f'Dimension = {dimension}. The dimension of vector must be greater than 0.')

        self.__dimension = dimension
        self.__components = [0. for _ in range(dimension)]

        for i, component in enumerate(components):
            self.__components[i] = component

    @dispatch(list)
    def __init__(self, components: list[float]):
        if len(components) == 0:
            raise ValueError(f'Dimension = {len(components)}. The dimension of vector must be greater than 0.')

        self.__dimension = len(components)
        self.__components = list(components)

    @dispatch(object)
    def __init__(self, vector: Vector):
        self.__dimension = len(vector.__components)
        self.__components = list(vector.__components)

    @property
    def dimension(self) -> int:
        return self.__dimension

    @property
    def length(self) -> float:
        components_sum = 0

        for component in self.__components:
            components_sum += component * component

        return math.sqrt(components_sum)

    @override
    def __repr__(self) -> str:
        string = '{'

        for component in self.__components:
            string += str(component) + ', '

        return string[:-2] + '}'

    @override
    def __eq__(self, other: Vector) -> bool:
        if isinstance(other, type(self)):
            return NotImplemented

        return self.__dimension == other.__dimension and self.__components == other.__components

    @override
    def __hash__(self) -> int:
        return hash((self.__dimension, self.__components))

    def __add__(self, other: Vector) -> Vector:
        return Vector([round(i + j, 2) for i, j in zip_longest(self.__components, other.__components, fillvalue=0.)])

    def __sub__(self, other: Vector) -> Vector:
        return Vector([round(i - j, 2) for i, j in zip_longest(self.__components, other.__components, fillvalue=0.)])

    def __check_index(self, index: int):
        if index < 0 or index >= self.__dimension:
            raise ValueError(f'index = {index}, but must be greater than 0 and less than {self.dimension - 1}')

    def get_component(self, index: int) -> float:
        self.__check_index(index)

        return self.__components[index]

    def set_component(self, component: float, index: int):
        self.__check_index(index)

        self.__components[index] = component

    def add(self, other: Vector):
        self.__components = [round(i + j, 2) for i, j in zip_longest(self.__components, other.__components,
                                                                     fillvalue=0.)]

    def sub(self, other: Vector):
        self.__components = [round(i - j, 2) for i, j in zip_longest(self.__components, other.__components,
                                                                     fillvalue=0.)]

    def multiply_by_scalar(self, scalar: float):
        for i, component in enumerate(self.__components):
            self.__components[i] *= scalar

    def reverse(self):
        self.multiply_by_scalar(-1)

    def get_scalar_product(self, other: Vector) -> float:
        min_size = min(self.__dimension, other.__dimension)
        product = 0

        for i in range(min_size):
            product += self.__components[i] * other.__components[i]

        return round(product, 2)
