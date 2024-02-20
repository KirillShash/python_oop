from range import Range


def print_functions_result(range_1: Range, range_2: Range):
    print(f'''range_1: {range_1} with range_2: {range_2}
intersection: {range_1.get_intersection(range_2)}
union: {range_1.get_union(range_2)}
''')


print_functions_result(Range(1.1, 2.2), Range(0.9, 3.3))
print_functions_result(Range(1.1, 2.2), Range(1.1, 2.2))
print_functions_result(Range(1.1, 2.2), Range(1.2, 2.1))
print_functions_result(Range(1.1, 2.2), Range(1.1, 2.1))
