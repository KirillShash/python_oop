from __future__ import annotations
from vector_task.vector import Vector
from multipledispatch import dispatch
from typing import override


class Matrix:
    @dispatch(int, int)
    def __init__(self, rows_count: int, columns_count: int):
        if rows_count <= 0:
            raise ValueError(f'Rows count = {rows_count}, but the number of rows must be greater than 0.')

        if columns_count <= 0:
            raise ValueError(f'Columns count = {columns_count}, but the number of columns must be greater than 0.')

        self.__vectors = [Vector(columns_count) for _ in range(rows_count)]

    @dispatch(object)
    def __init__(self, matrix: Matrix):
        self.__vectors = list(matrix.__vectors)

    @dispatch(list)
    def __init__(self, elements: list[list[float]]):
        if len(elements) == 0:
            raise ValueError(f'List length = {len(elements)} (row count), but number of rows must be greater than 0.')

        max_columns_count = 0

        for row in elements:
            if len(row) > max_columns_count:
                max_columns_count = len(row)

        if max_columns_count == 0:
            raise ValueError(f'Nested array length = {max_columns_count} (column count), but number of columns must be '
                             f'greater than 0.')

        self.__vectors = [Vector(max_columns_count, row) for row in elements]

    @dispatch(list)
    def __init__(self, vectors: list[Vector]):
        if len(vectors) == 0:
            raise ValueError(f'List is empty.')

        max_columns_count = vectors[0].dimension

        for row in vectors[1:]:
            if row.dimension > max_columns_count:
                max_columns_count = row.dimension

        self.__vectors = [Vector(max_columns_count).add(vector) for vector in vectors]

    @override
    def __repr__(self) -> str:
        result = '{'

        for vector in self.__vectors:
            result += str(vector) + ', '

        return result[:-2] + '}'
