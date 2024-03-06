from __future__ import annotations
from vector_task.vector import Vector
from multimethod import multimethod
from typing import override, List


class Matrix:
    """
        You can use constructors:
            1. Matrix(rows_count: int, columns_count: int) – matrix of zeros of size rows_count x columns_count
            2. Matrix(matrix: Matrix) – copy constructor
            3. Matrix(elements: list[list[float]]) – from a two-dimensional list of numbers
            4. Matrix(vectors: list[Vector]) – from a list of row vectors
    """

    @multimethod
    def __init__(self, matrix: Matrix):
        self.__vectors = list(matrix.__vectors)

    @multimethod
    def __init__(self, vectors: List[Vector]):
        if len(vectors) == 0:
            raise ValueError(f'List (vectors) is empty.')

        max_columns_count = vectors[0].dimension

        for row in vectors[1:]:
            if row.dimension > max_columns_count:
                max_columns_count = row.dimension

        self.__vectors = [Vector(max_columns_count) + vector for vector in vectors]

    @multimethod
    def __init__(self, elements: List[List[float | int]]):
        if len(elements) == 0:
            raise ValueError(
                f'List length = {len(elements)} (row count), but number of rows must be greater than 0.')

        max_columns_count = 0

        for row in elements:
            if len(row) > max_columns_count:
                max_columns_count = len(row)

        if max_columns_count == 0:
            raise ValueError(f'Nested array length = {max_columns_count} (column count), but number of columns must '
                             f'be greater than 0.')

        self.__vectors = [Vector(max_columns_count, row) for row in elements]

    @multimethod
    def __init__(self, rows_count: int, columns_count: int):
        if rows_count <= 0:
            raise ValueError(f'Rows count = {rows_count}, but the number of rows must be greater than 0.')

        if columns_count <= 0:
            raise ValueError(f'Columns count = {columns_count}, but the number of columns must be greater than 0.')

        self.__vectors = [Vector(columns_count) for _ in range(rows_count)]

    @property
    def rows_count(self) -> int:
        return len(self.__vectors)

    @property
    def columns_count(self) -> int:
        return self.__vectors[0].dimension

    @override
    def __repr__(self) -> str:
        return '{' + ', '.join([str(vector) for vector in self.__vectors]) + '}'

    @override
    def __eq__(self, other: Matrix) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__vectors == other.__vectors

    @override
    def __hash__(self) -> int:
        return hash(tuple(self.__vectors))

    def __check_index(self, index: int):
        if type(index) is not int:
            raise TypeError(f'Entered index type: {type(index)}, but the index must be integer')

        if index >= self.rows_count:
            raise IndexError(f'Entered index: {index}. The index must be less than {self.columns_count}')

    def __getitem__(self, item):
        if isinstance(item, slice):
            return self.__vectors[item.start:item.stop:item.step]

        self.__check_index(item)

        return self.__vectors[item]

    def __setitem__(self, index: int, value: Vector):
        if type(value) is not Vector:
            raise TypeError(f'Entered value type: {type(value)}. The value must be Vector type')

        self.__check_index(index)

        self.__vectors[index] = value

    def __check_matrices_sizes(self, other: Matrix):
        if self.rows_count != other.rows_count or self.columns_count != other.columns_count:
            raise ValueError(f'First matrix size = {self.rows_count}x{self.columns_count}, second matrix size = '
                             f'{other.rows_count}x{other.columns_count}. Matrices must have the same dimensions.')

    def __add__(self, other: Matrix) -> Matrix:
        if not isinstance(other, type(self)):
            return NotImplemented

        self.__check_matrices_sizes(other)

        return Matrix([vector_1 + vector_2 for vector_1, vector_2 in zip(self.__vectors, other.__vectors)])

    def __sub__(self, other: Matrix) -> Matrix:
        if not isinstance(other, type(self)):
            return NotImplemented

        return Matrix([vector_1 - vector_2 for vector_1, vector_2 in zip(self.__vectors, other.__vectors)])

    def __iadd__(self, other: Matrix) -> Matrix:
        if not isinstance(other, type(self)):
            return NotImplemented

        self.__vectors = [vector_1 + vector_2 for vector_1, vector_2 in zip(self.__vectors, other.__vectors)]

        return self

    def __isub__(self, other: Matrix) -> Matrix:
        if not isinstance(other, type(self)):
            return NotImplemented

        self.__vectors = [vector_1 - vector_2 for vector_1, vector_2 in zip(self.__vectors, other.__vectors)]

        return self
