from range import Range

range_1 = Range(1.1, 2.2)

print(range_1.is_inside(0))
print(range_1.is_inside(1.5))
print(range_1.get_length())

print(f'range_1: {range_1}', end='\n\n')

range_2 = Range(0.9, 3.3)

print(f'intersection, union, difference range_1: {range_1} with range_2: {range_2}')
print(range_1.get_intersection_interval(range_2))
print(range_1.get_union(range_2))
print(range_1.get_difference(range_2), end='\n\n')

range_3 = Range(1.1, 2.2)

print(f'intersection, union, difference range_1: {range_1} with range_3: {range_3}')
print(range_1.get_intersection_interval(range_3))
print(range_1.get_union(range_3))
print(range_1.get_difference(range_3), end='\n\n')

range_4 = Range(1.2, 2.1)

print(f'intersection, union, difference range_1: {range_1} with range_4: {range_4}')
print(range_1.get_intersection_interval(range_4))
print(range_1.get_union(range_4))
print(range_1.get_difference(range_4), end='\n\n')

range_5 = Range(1.1, 2.1)

print(f'intersection, union, difference range_1: {range_1} with range_5: {range_5}')
print(range_1.get_intersection_interval(range_5))
print(range_1.get_union(range_5))
print(range_1.get_difference(range_5))
