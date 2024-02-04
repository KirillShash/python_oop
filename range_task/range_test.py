from range import Range

range_1 = Range(1.1, 2.2)

print(range_1.is_inside(0))
print(range_1.is_inside(1.5))

print(range_1.get_length())

range_2 = Range(0.9, 3.3)

print(range_1.get_intersection_interval(range_2))
