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

    @override
    def __repr__(self) -> str:
        return '{' + ', '.join(map(str, self.__vectors)) + '}'
