from vector import Vector

vector_1 = Vector(5)
vector_2 = Vector(3, [1, 2, 3, 4])
vector_3 = Vector(vector_1)

print(f'Vector_1: {vector_1}')
print(f'Vector_2: {vector_2}')
print(f'Vector_3: {vector_3}')

vector_4 = Vector([1, 2, 3, 4, 5])
vector_5 = Vector([1.1, 2.3, 3.4, 4.5, 5.6, 6])

print(f'Vector_4: {vector_4}')
print(f'Vector_5: {vector_5}')

print()

print(f'vector_4 + vector_5: {vector_4 + vector_5}')
print(f'vector_4 - vector_5: {vector_4 - vector_5}')

print()

vector_4 += vector_5
print(f'vector_4 += vector_5: {vector_4}')

vector_4 -= vector_5
print(f'vector_4 -= vector_5: {vector_4}')

print()

print(f'Vector_4: {vector_4}')

vector_4 *= 2
print(f'vector_4 *= 2: {vector_4}')

vector_4.reverse()
print(f'vector_4.reverse(): {vector_4}')

print()

print(f'Vector_4: {vector_4}')
print(f'vector_4[4]: {vector_4[4]}')
print(f'vector_4[-6]: {vector_4[-6]}')
print(f'vector_4[1:4]: {vector_4[1:4]}')

vector_4[4] = 22
print(f'vector_4[4] = 22: vector_4: {vector_4}')

print()

print(f'Vector_4: {vector_4}')
print(f'Vector_5: {vector_5}')
print(f'vector_4.get_scalar_product(vector_5): {vector_4.get_scalar_product(vector_5)}')
