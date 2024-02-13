from __future__ import annotations

import math
from typing import override
from multipledispatch import dispatch


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
    def __repr__(self):
        string = '{'

        for i in self.__components:
            string += str(i) + ', '

        return string[:-2] + '}'
