from range import Range

range_1 = Range(1.1, 2.2)

print(range_1.is_inside(0))
print(range_1.is_inside(1.5))
print(range_1.get_length())

print(f'range_1: {range_1}', end='\n\n')

range_2 = Range(0.9, 3.3)

print(f'''range_1: {range_1} with range_3: {range_2}
intersection: {range_1.get_intersection_interval(range_2)}
union: {range_1.get_union(range_2)}
difference: {range_1.get_difference(range_2)}
''')

range_3 = Range(1.1, 2.2)

print(f'''range_1: {range_1} with range_3: {range_3}
intersection: {range_1.get_intersection_interval(range_3)}
union: {range_1.get_union(range_3)}
difference: {range_1.get_difference(range_3)}
''')

range_4 = Range(1.2, 2.1)

print(f'''range_1: {range_1} with range_4: {range_4}
intersection: {range_1.get_intersection_interval(range_4)}
union: {range_1.get_union(range_4)}
difference: {range_1.get_difference(range_4)}
''')

range_5 = Range(1.1, 2.1)

print(f'''range_1: {range_1} with range_5: {range_5}
intersection: {range_1.get_intersection_interval(range_5)}
union: {range_1.get_union(range_5)}
difference: {range_1.get_difference(range_5)}
''')
