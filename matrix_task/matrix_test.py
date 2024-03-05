from matrix import Matrix
from vector_task.vector import Vector

matrix_1 = Matrix(2, 2)
matrix_2 = Matrix([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]])
matrix_3 = Matrix(matrix_2)

vector = Vector(3, [1.1, 2.2, 3.3])
matrix_4 = Matrix([vector, vector, vector])

print(f'matrix_1: {matrix_1}')
print(f'matrix_2: {matrix_2}')
print(f'matrix_3: {matrix_3}')
print(f'matrix_4: {matrix_4}')

print(hash(matrix_2))
print(matrix_2 == matrix_4)
print(matrix_2 == matrix_2)
